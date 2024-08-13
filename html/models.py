from django.db import models

class Bus(models.py):
    name = models.CharField(max_length=200)
    number_of_seats = models.IntegerField()

    def __str__(self):
        return self.name

class Route(models.py):
    name = models.CharField(max_length=200)
    start_point = models.CharField(max_length=200)
    end_point = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Stop(models.py):
    name = models.CharField(max_length=200)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reservation(models.py):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    passenger_name = models.CharField(max_length=200)
    passenger_email = models.EmailField()

    def __str__(self):
        return f"{self.passenger_name} - {self.bus.name} - {self.stop.name}"