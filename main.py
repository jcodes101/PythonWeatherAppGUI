from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OWM_API_KEY")

root=Tk()
root.title("Python Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:

        # looks for user-input for getting the city
        city=textfield.get()

        # geopy is used to get the location (latitude & longitude) of the city
        geolocator = Nominatim(user_agent="jadin_python_weather_app ")
        location = geolocator.geocode(city)

        # get the timezone based on coordinates
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        # get the current local time in the city
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")

        # update clock and label for weather title
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # openweathermap api | fstring is needed for allowing proper searching
        # builds the OpenWeatherMap API URL (f-string allows variable injection)
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        # fetch weather data from the API
        json_data = requests.get(api).json()

        # extract necessary weather info from the JSON response
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        # converting the kelvin to the celcius
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        # update the UI labels with the retrieved data
        temperatureLabel.config(text=(temp,"°"))
        conditionLabel.config(text=(condition,"|", "FEELS", "LIKE", temp, "°"))

        windLabel.config(text=wind)
        humidityLabel.config(text=humidity)
        descriptionLabel.config(text=description)
        pressureLabel.config(text=pressure)

        # terminal printing
        print(result)

    # error message
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry")


# search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=70,y=40)
textfield.focus()

# search_icon button
Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400,y=34)

# weather logo
Logo_image=PhotoImage(file="weather_logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

# bottom weather info box
Frame_image=PhotoImage(file="bottom_box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# city time
name=Label(root,font=("arial", 15, "bold"))
name.place(x=30,y=100)
clock=Label(root, font=("Helvetica", 20))
clock.place(x=30,y=130)

# wind label
windHeader=Label(root, text= "WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
windHeader.place(x=120,y=400)

# humidity label
humidityHeader=Label(root, text= "HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
humidityHeader.place(x=250,y=400)

# description label
descriptionHeader=Label(root, text= "DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
descriptionHeader.place(x=430,y=400)

# pressure label
pressureHeader=Label(root, text= "PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
pressureHeader.place(x=650,y=400)

# temperature label
temperatureLabel=Label(font=("arial", 70, "bold"), fg="#ee776d")
temperatureLabel.place(x=400,y=150)

# condition label
conditionLabel=Label(font=("arial", 15, "bold"))
conditionLabel.place(x=400,y=250)

# wind label
windLabel=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
windLabel.place(x=120,y=430)

# humidity label
humidityLabel=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
humidityLabel.place(x=280,y=430)

# description label
descriptionLabel=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
descriptionLabel.place(x=450,y=430)

# pressure label
pressureLabel=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
pressureLabel.place(x=670,y=430)

root.mainloop()