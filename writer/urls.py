from django.urls import path
from .views import GigDescriptionView

urlpatterns = [
    path('write/', GigDescriptionView.as_view()),
]