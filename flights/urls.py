from django.urls import path, include
from . import views



urlpatterns = [
    path('flights', views.FlightView.as_view()),
    path('tickets/<int:some_id>', views.TicketView.as_view()),
    path('tickets', views.TicketView.as_view()),
]
