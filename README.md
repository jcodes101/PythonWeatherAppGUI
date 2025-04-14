# 🌦️ Python Weather App

This is a Python-based desktop weather app built with Tkinter. It uses the **OpenWeatherMap API**, **Geopy**, and **TimezoneFinder** to display real-time weather details for any city you search.

---

## 🚀 Features

- Live weather updates for any city
- Real-time local time display
- Temperature (°C), Wind Speed, Humidity, Pressure, and Description
- Beautiful GUI built with `Tkinter`
- Uses icons and visual layout for clean presentation

---

## 📦 Dependencies

Before running, make sure to install the following Python packages:

```bash
pip install geopy timezonefinder pytz requests python-dotenv

🧪 How to Use
Clone or Download this repository.

Create a free OpenWeatherMap account:

👉 https://openweathermap.org/

Get your API key and endpoint structure:

Visit: https://openweathermap.org/current

Learn how to structure your API requests. Example format:
  http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

Go to your OpenWeatherMap profile and copy your unique API key.

Create a .env file in the project folder and add your API key like this:
  OWM_API_KEY=your_api_key_here

Make sure the following image files are in the same directory as your Python script:

search.png

search_icon.png

weather_logo.png

bottom_box.png

Run the app:

bash
Copy
Edit

🛠️ Built With
Python 3 | PyCharm

Tkinter

OpenWeatherMap API

Geopy

TimezoneFinder

pytz

dotenv
