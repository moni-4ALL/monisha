# Import Django settings
import os
import django

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

# Import Django models
from bus_reservation.models import Bus, Passenger, Reservation

# Your script logic goes here


