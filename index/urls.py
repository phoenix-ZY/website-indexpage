from django.urls import path
from index import views

urlpatterns = [
    path("", views.index, name="index"),
]

from django.views.generic.base import RedirectView

urlpatterns += [
    path(
        "to_third/<str:param>",
        RedirectView.as_view(url="{}", permanent=False),
        name="to_third",
    ),
]
