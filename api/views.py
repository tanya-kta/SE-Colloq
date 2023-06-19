from django.http import HttpResponse, QueryDict
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from api.models import Flights, Tickets
from rest_framework.views import APIView


@csrf_exempt
def tickets_view(request):
    print(request.content)


class FlightView(APIView):
    def post(self, request):
        flight = Flights(where_from=request.data.get("where_from", None),
                         where_to=request.data.get("where_to", None))
        flight.save()
        return HttpResponse(flight)

    def get(self):
        return HttpResponse(f'{Flights.objects.get()}')


class TicketView(APIView):
    def post(self, request):
        ticket = Tickets(passenger_id=request.data.get("passenger_id", None),
                         flight_id=request.data.get("flight_id", None))
        ticket.save()
        return HttpResponse(ticket)

    def get(self, request, some_id):
        return HttpResponse(f'{Tickets.objects.filter(passenget_id=some_id)}')

    def delete(self, request, some_id):
        Tickets.objects.filter(id=some_id).delete()
        return HttpResponse(f"deleted id {some_id}")

