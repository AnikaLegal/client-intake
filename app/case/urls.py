from django.urls import include, path

from . import views

urlpatterns = [
    path("robots.txt", views.robots_view),
    # Auth
    path("oauth/", include("social_django.urls", namespace="social")),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # Cases
    path("cases/", views.case_list_view, name="case-list"),
    path("cases/<uuid:pk>/", views.case_details_view, name="case-detail"),
    path("", views.root_view, name="root"),
]
