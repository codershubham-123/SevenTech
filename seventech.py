from tkinter import *
from tkinter import ttk
import requests


def data_get(state, city):
    data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid=63cfe938a09ada9e27d7f5e19a230ba8&units=metric').json()

    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temperature = str(int(data["main"]["temp"]))
    pressure = data['main']['pressure']

    return weather, description, temperature, pressure

def show_weather():
    state = state_combobox.get()
    city = city_combobox.get()

    if not state or not city:
        w_label1.config(text='Please select a state and a city.')
    else:
        weather, description, temperature, pressure = data_get(state, city)
        w_label1.config(text=f'Weather: {weather}')
        wb_label1.config(text=f'Description: {description.capitalize()}')
        temp_label1.config(text=f'Temperature: {temperature}°C')
        pre_label1.config(text=f'Pressure: {pressure} hPa')

def on_state_selected(event):
    selected_state = state_combobox.get()
    cities = state_cities[selected_state]
    city_combobox.config(values=cities)


state_cities = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Thane"],
    "Manipur": ["Imphal", "Thoubal", "Bishnupur", "Ukhrul", "Churachandpur"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru", "Belagavi"],
    "Mizoram": ["Aizawl", "Lunglei", "Champhai", "Serchhip", "Kolasib"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Tuensang", "Wokha"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur"],
    "Punjab": ["Chandigarh", "Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer"],
    "Sikkim": ["Gangtok", "Namchi", "Gyalshing", "Mangan", "Ravangla"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam"],
    "Tripura": ["Agartala", "Udaipur", "Belonia", "Dharmanagar", "Kailasahar"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Allahabad"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Roorkee", "Nainital", "Almora"],
    "West Bengal": ["Kolkata", "Asansol", "Siliguri", "Durgapur", "Howrah"],
    
}

# GUI setup
win = Tk()
win.title("Temp Research")
win.config(bg="orange")
win.geometry("500x700")

name_lable = Label(win, text="Cloud Point", font=("Time New Roman", 38, "bold"))
name_lable.place(x=25, y=50, height=50, width=450)

state_label = Label(win, text="Select State:", font=("Time New Roman", 28, "bold"))
state_label.place(x=40, y=120, height=50, width=420)

state_combobox = ttk.Combobox(win, values=list(state_cities.keys()), state="readonly")
state_combobox.place(x=40, y=190, height=50, width=420)

state_combobox.bind("<<ComboboxSelected>>", on_state_selected)


city_label = Label(win, text="Select City:", font=("Time New Roman", 28, "bold"))
city_label.place(x=40, y=260, height=50, width=420)


city_combobox = ttk.Combobox(win, state="readonly")
city_combobox.place(x=40, y=330, height=50, width=420)


show_weather_button = Button(win, text="Submit", command=show_weather, font=("Time New Roman", 18, "bold"))
show_weather_button.place(x=40, y=400, height=50, width=420)

w_label = Label(win, text="Weather Climate", font=("Time New Roman", 12))
w_label.place(x=25, y=470, height=50, width=210)

w_label1 = Label(win, text="", font=("Time New Roman", 12))
w_label1.place(x=250, y=470, height=50, width=210)


wb_label = Label(win, text="Weather Description", font=("Time New Roman", 12))
wb_label.place(x=25, y=520, height=50, width=210)

wb_label1 = Label(win, text="", font=("Time New Roman", 12))
wb_label1.place(x=250, y=520, height=50, width=210)


temp_label = Label(win, text="Temperature", font=("Time New Roman", 12))
temp_label.place(x=25, y=570, height=50, width=210)

temp_label1 = Label(win, text="", font=("Time New Roman", 12))
temp_label1.place(x=250, y=570, height=50, width=210)


pre_label = Label(win, text="Pressure", font=("Time New Roman", 12))
pre_label.place(x=25, y=620, height=50, width=210)

pre_label1 = Label(win, text="", font=("Time New Roman", 12))
pre_label1.place(x=250, y=620, height=50, width=210)



win.mainloop()