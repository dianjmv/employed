from django.urls import path

from .views import PruebaView

urlpatterns = [
    path('', PruebaView.as_view())
]