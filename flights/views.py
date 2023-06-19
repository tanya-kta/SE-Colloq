from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from flights.models import Flights, Tickets
from rest_framework.views import APIView


class FlightView(APIView):
    def post(self, request):
        flight = Flights(where_from=request.data.get("where_from", None),
                         where_to=request.data.get("where_to", None),
                         arrival_time=request.data.get("arrival_time", None),
                         departure_time=request.data.get("departure_time", None))
        flight.save()
        return HttpResponse(flight)

    def get(self, request):
        return HttpResponse(f'{Flights.objects.get()}')


class TicketView(APIView):
    def post(self, request):
        ticket = Tickets(passenger_id=request.data.get("passenger_id", None),
                         flight_id=request.data.get("flight_id", None))
        ticket.save()
        return HttpResponse(f'{ticket}')

    def get(self, request, some_id):
        return HttpResponse(f'{Tickets.objects.filter(passenget_id=some_id)}')

    def delete(self, request, some_id):
        Tickets.objects.filter(id=some_id).delete()
        return HttpResponse(f"deleted id {some_id}")

