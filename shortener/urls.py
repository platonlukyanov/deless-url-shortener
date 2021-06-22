from django.urls import path
from .views import *


urlpatterns = [
    path('', CreateLinkView.as_view(), name="create_link"),
    path('<str:code>/', ShortLinkRedirect.as_view(), name="short_link_redirect"),
    path('created/<int:pk>/<code>/', LinkCreatedView.as_view(), name="link_created"),
]