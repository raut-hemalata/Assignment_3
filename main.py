import pendulum
import socket
from geopy.geocoders import Nominatim
ist = pendulum.timezone('Asia/Calcutta')
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
geolocator = Nominatim(user_agent="geoapiExercises")
Latitude = "18.5204"
Longitude = "73.8567"
location = geolocator.reverse(Latitude+","+Longitude)
address = location.raw['address']
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
print("Current Time in IST : ",pendulum.now(ist))
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)
print("City :" ,city)
print("Region :",state)
print("Country :",country)
