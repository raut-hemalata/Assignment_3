import pendulum
import socket
from geopy.geocoders import Nominatim
from flask import Flask, render_template,url_for
app = Flask(__name__)
ist = pendulum.timezone('Asia/Calcutta')
Time=pendulum.now(ist)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Current Time in IST : ",Time)
print("IP Address:",ip_address)
print("Hostname: ",hostname)
geolocator = Nominatim(user_agent="geoapiExercises")
Latitude = "18.5204"
Longitude = "73.8567"
location = geolocator.reverse(Latitude+","+Longitude)
address = location.raw['address']
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
print("City :" ,city)
print("Region :",state)
print("Country :",country)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/pucsdian")
def pucsd():
    return render_template("pucsdian.html",content1=Time,content2=hostname,content3=ip_address,content4=city,content5=state,content6=country)
if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=True)

