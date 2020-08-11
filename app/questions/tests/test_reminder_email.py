from django.utils import timezone
from django.conf import settings

from unittest import mock
import pytest

from questions.services.mailchimp import remind_incomplete, find_clients
from questions.tests.factories import SubmissionFactory
from questions.models import Submission


# Sample answers for testing
answers_with_email = [
    {"name": "CLIENT_NAME", "answer": "Michael Jordan"},
    {"name": "CLIENT_RENTAL_ADDRESS", "answer": "Chicago Bulls"},
    {"name": "CLIENT_DOB", "answer": "1963-02-17"},
    {"name": "CLIENT_EMAIL", "answer": "michael@jordan.com"},
    {"name": "CLIENT_PHONE", "answer": "4458 4858"},
]

answers_no_email = [
    {"name": "CLIENT_NAME", "answer": "Paul Scholes"},
    {"name": "CLIENT_RENTAL_ADDRESS", "answer": "Manchester United"},
    {"name": "CLIENT_DOB", "answer": "1974-11-16"},
    {"name": "CLIENT_PHONE", "answer": "4567 4756"},
]

# Sample dates for testing
three_weeks_ago = timezone.now() - timezone.timedelta(days=21)
three_days_ago = timezone.now() - timezone.timedelta(days=3)
one_day_ago = timezone.now() - timezone.timedelta(days=1)


@pytest.mark.django_db
def test_find_clients_no_emails():
    sub1 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="COVID",
        created_at=three_days_ago,
        answers=answers_no_email,
    )
    results = find_clients("COVID")
    assert results == []


@pytest.mark.django_db
def test_find_clients_with_emails():
    sub1 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="REPAIRS",
        created_at=three_days_ago,
        answers=answers_no_email,
    )
    sub2 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="REPAIRS",
        created_at=three_days_ago,
        answers=answers_with_email,
    )
    results = find_clients("REPAIRS")
    assert results == [(sub2, "michael@jordan.com")]


@pytest.mark.django_db
def test_find_clients_irrelevant_dates():
    sub1 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="COVID",
        created_at=three_weeks_ago,
        answers=answers_with_email,
    )
    sub2 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="COVID",
        created_at=one_day_ago,
        answers=answers_with_email,
    )
    results = find_clients("COVID")
    assert results == []


@pytest.mark.django_db
def test_find_clients_relevant_dates():
    sub1 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="REPAIRS",
        created_at=three_weeks_ago,
        answers=answers_with_email,
    )
    sub2 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="REPAIRS",
        created_at=three_days_ago,
        answers=answers_with_email,
    )
    results = find_clients("REPAIRS")
    assert results == [(sub2, "michael@jordan.com")]


@mock.patch("questions.services.mailchimp.MailChimp")
@pytest.mark.django_db
def test_remind_incomplete_sent(mock_API):
    sub1 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="COVID",
        created_at=three_days_ago,
        answers=answers_with_email,
    )
    remind_incomplete()
    sub1.refresh_from_db()
    assert sub1.is_reminder_sent == True


@mock.patch("questions.services.mailchimp.MailChimp")
@pytest.mark.django_db
def test_remind_incomplete_api(mock_API):
    mock_mailchimp = mock.Mock()
    mock_API.return_value = mock_mailchimp
    sub1 = SubmissionFactory(
        complete=False,
        is_reminder_sent=False,
        topic="REPAIRS",
        created_at=three_days_ago,
        answers=answers_with_email,
    )
    person = {"email_address": "michael@jordan.com", "status": "subscribed"}
    remind_incomplete()
    mock_API.assert_called_with(settings.MAILCHIMP_API_KEY)
    mock_mailchimp.lists.members.create.assert_called_with(
        list_id=settings.MAILCHIMP_REPAIRS_LIST_ID, data=person
    )
    mock_mailchimp.automations.emails.queues.create.assert_called_with(
        workflow_id=settings.MAILCHIMP_REPAIRS_WORKFLOW_ID,
        email_id=settings.MAILCHIMP_REPAIRS_EMAIL_ID,
        data=person,
    )