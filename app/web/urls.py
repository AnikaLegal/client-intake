from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from . import views


def template(name):
    return TemplateView.as_view(template_name=name)


urlpatterns = [
    # Jobs
    path("openings/", template("web/openings.html"), name="openings"),
    # About
    path("about/", template("web/about/about.html"), name="about"),
    path("about/annual-reports/", template("web/about/reports.html"), name="reports"),
    path("about/team/", views.team_view, name="team"),
    path("about/impact/", template("web/about/impact.html"), name="impact"),
    # Services
    path(
        "services/rental-repairs/",
        template("web/services/repairs.html"),
        name="repairs",
    ),
    path(
        "services/eviction-support/",
        template("web/services/evictions.html"),
        name="evictions",
    ),
    path(
        "services/refer-someone/",
        template("web/services/refer-someone.html"),
        name="refer",
    ),
    # Wagtail
    path("cms/admin/", include(wagtailadmin_urls)),
    path("cms/documents/", include(wagtaildocs_urls)),
    path("cms/", include(wagtail_urls)),
    path("blog/search/", views.blog_search_view, name="blog-search"),
    # Robots.txt
    path("robots.txt", views.robots_view),
    # Landing page
    path("landing/contact/", views.landing_contact_form_view, name="landing-contact"),
    path("", views.landing_view, name="landing"),
]
