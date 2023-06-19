from django.db import models


class Flights(models.Model):
    id = models.AutoField(primary_key=True)
    where_from = models.TextField()
    where_to = models.TextField()
    arrival_time = models.DateTimeField(blank=True)
    departure_time = models.DateTimeField(blank=True)

    class Meta:
        app_label = 'flights'

    def __str__(self):
        return f'Flight #{self.id} [where_from: {self.where_from}; where_to: {self.where_to}; arrival_time: {self.arrival_time}; departure_time: {self.departure_time}]'


class Tickets(models.Model):
    id = models.AutoField(primary_key=True)
    passenger_id = models.IntegerField()
    flight_id = models.IntegerField()

    class Meta:
        app_label = 'tickets'

    def __str__(self):
        return f'Tickets #{self.id} of passerger {self.passenger_id} and flight {self.flight_id}'
