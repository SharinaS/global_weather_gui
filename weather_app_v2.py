'''
@author: Sharina Stubbs
Title: Weather GUI
Version: 1.2
Last Updated: June 29, 2018
Description: An international and USA Weather GUI that accesses live data from NOAA, Open Weather Map and Weather Underground. 
Scrapes XML and JSON data from respective websites. Location emphasis is on a specific region of Washington State, 
but nation-wide and international weather is easily accessed with this GUI.
'''


import tkinter as tk
from tkinter import Menu
from tkinter import ttk #themed tk (has other widgets than regular tk module

################################################################
# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

################################################################
# create instance
win = tk.Tk()

# GUI title
win.title("World and Local Weather")

################################################################
# Menu Bar
menuBar = Menu()
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)   #command callback
menuBar.add_cascade (label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

################################################################

# Tab Control / Notebook 
tabControl = ttk.Notebook(win)      # Create Tab Control

tab1 = ttk.Frame(tabControl)        # Create a tab
tabControl.add(tab1, text= "NOAA Weather") # Add the tab

tab2 = ttk.Frame(tabControl)       
tabControl.add(tab2, text= "Station IDs") 

tab4 = ttk.Frame(tabControl)        
tabControl.add(tab4, text= "Open Weather Map") 

tab5 = ttk.Frame(tabControl)        
tabControl.add(tab5, text= "Weather Underground") 

tabControl.pack(expand=1, fill="both")  # pack to make visible

################################################################
# TAB 1
################################################################

# Container frames to hold all other widgets -- Using grid manager
weather_conditions_frame = ttk.LabelFrame(tab1, text=' Current Weather Conditions ')
weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)

#===========================
ENTRY_WIDTH = 25
#===========================

#Adding Label & Texbox Entry widgets
#-------------------------------------
ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')
#-------------------------------------
ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='E')
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')  
#-------------------------------------   
ttk.Label(weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='E')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row=3, sticky='W')  
#-------------------------------------   
ttk.Label(weather_conditions_frame, text="Dewpoint:").grid(column=0, row=4, sticky='E')
dew = tk.StringVar()
dewEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=dew, state='readonly')
dewEntry.grid(column=1, row=4, sticky='W')  
#------------------------------------- 
ttk.Label(weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='E')
rel_humi = tk.StringVar()
rel_humiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=rel_humi, state='readonly')
rel_humiEntry.grid(column=1, row=5, sticky='W')    
#------------------------------------- 
ttk.Label(weather_conditions_frame, text="Wind:").grid(column=0, row=6, sticky='E')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=6, sticky='W')    
#------------------------------------- 
ttk.Label(weather_conditions_frame, text="Visibility:").grid(column=0, row=6, sticky='E')
visi = tk.StringVar()
visiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=visi, state='readonly')
visiEntry.grid(column=1, row=6, sticky='W') 
#------------------------------------- 
ttk.Label(weather_conditions_frame, text="MSL Pressure:").grid(column=0, row=7, sticky='E')
pressure = tk.StringVar()
pressureEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=pressure, state='readonly')
pressureEntry.grid(column=1, row=7, sticky='W') 
#------------------------------------- 
ttk.Label(weather_conditions_frame, text="Altimeter:").grid(column=0, row=8, sticky='E')
alti = tk.StringVar()
altiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=alti, state='readonly')
altiEntry.grid(column=1, row=8, sticky='W') 
#------------------------------------- 
ttk.Label(weather_conditions_frame, text="Wind").grid(column=0, row=9, sticky='E')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=9, sticky='W')
#-------------------------------------

# Add some space around each widget
for child in weather_conditions_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)        # adjust per visual taste of spacing around widgets   
   
#------------------------------------------------------------

# Container frame for choosing city to get weather data for
weather_cities_frame = ttk.LabelFrame(tab1, text=' Latest Observation for ')
weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

#----------------------------------------------------------
ttk.Label(weather_cities_frame, text="Weather Station ID: ").grid(column=0, row=0)

#----------------------------------------------------------
station_id = tk.StringVar()
station_id_combo = ttk.Combobox(weather_cities_frame, width=6, textvariable=station_id)
station_id_combo['values'] = ('KSEA', 'KBFI', 'KBLI', 'KBFI', 'KBVS', 'KELN')
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0)

#----------------------------------------------------------
def _get_station():
    station = station_id_combo.get()
    get_weather_data(station)
    populate_gui_from_dict()
    
get_weather_btn = ttk.Button(weather_cities_frame,text="Get Weather", command=_get_station).grid(column=2, row=0)

# Station City Label
location = tk.StringVar()
ttk.Label(weather_cities_frame, textvariable=location).grid(column=0, row=1, columnspan=3)      #full location printed under combobox
#----------------------------------------------------------
for child in weather_cities_frame.winfo_children():
    child.grid_configure(padx=5, pady=4)
    
#===============================================================================
# NOAA Data directly from live web search

# Retrieve the tags we are interested in
weather_data_tags_dict = {
    'observation_time': '',
    'weather': '',
    'temp_f': '',
    'temp_c': '',
    'dewpoint_f': '',
    'dewpoint_c': '',
    'relative_humidity': '',
    'wind_string': '',
    'visibility_mi': '',
    'pressure_string': '',
    'pressure_in': '',
    'location': ''
    }

#----------------------------------------------------------
import urllib.request

def get_weather_data(station_id='KSEA'):
    url_general = 'http://w1.weather.gov/xml/current_obs/{}.xml' # {} in this allows station id to be passed into address.
    url = url_general.format(station_id)
    print(url)
    request = urllib.request.urlopen( url )         # This pulls XML data
    content = request.read().decode()   #this decodes the data into a string
    #print(content)
    
    #Using ElementTree to retrieve specific tags from the xml
    import xml.etree.ElementTree as ET
    xml_root = ET.fromstring(content)
    print('xml_root: {}\n'.format(xml_root.tag))
    
    for data_point in weather_data_tags_dict.keys():
        weather_data_tags_dict[data_point] = xml_root.find(data_point).text #finds data point (the dict key) and retrieve text.
        #ie, in the xml format, <temp_f> is the key and value is the temperature that is next to it.
    
#----------------------------------------------------------

def populate_gui_from_dict():       
    location.set(weather_data_tags_dict['location']) #This prints out the full name of the location just below id combobox
    updated.set(weather_data_tags_dict['observation_time'].replace('Last Updated on ', ''))
    weather.set(weather_data_tags_dict['weather'])
    temp.set('{} \xb0F  ({} \xb0C)'.format(weather_data_tags_dict['temp_f'], weather_data_tags_dict['temp_c']))
    dew.set('{} \xb0F  ({} \xb0C)'.format(weather_data_tags_dict['dewpoint_f'], weather_data_tags_dict['dewpoint_c']))
    rel_humi.set(weather_data_tags_dict['relative_humidity'] + ' %')
    wind.set(weather_data_tags_dict['wind_string'])
    visi.set(weather_data_tags_dict['visibility_mi'] + ' miles')
    pressure.set(weather_data_tags_dict['pressure_string'])
    alti.set(weather_data_tags_dict['pressure_in'] + ' in Hg')  
    
################################################################
# TAB 2
################################################################

#container frame
weather_states_frame = ttk.LabelFrame(tab2, text=' Weather Station IDs ')
weather_states_frame.grid(column=0, row=0, padx=8, pady=4)

#--------------------------------------------------
#Label
ttk.Label(weather_states_frame, text="Select a State: ").grid(column=0, row=0)
    
#--------------------------------------------------
state = tk.StringVar()
state_combo = ttk.Combobox(weather_states_frame, width=5, textvariable=state)
state_combo['values'] = ('AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI',
                         'ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI',
                         'MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC',
                         'ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
                         'VT','VA','WA','WV','WI','WY'
                        )
state_combo.grid(column=1, row=0)
state_combo.current(0)      #highlight first
#--------------------------------------------------

def _get_cities():
    state=state_combo.get()
    get_city_station_ids(state)
    
get_weather_btn = ttk.Button(weather_states_frame, text='Get Cities', command=_get_cities).grid(column=2, row=0)

from tkinter import scrolledtext
scr = scrolledtext.ScrolledText(weather_states_frame, width=30, height=17, wrap=tk.WORD)
scr.grid(column=0, row=1, columnspan=3)

for child in weather_states_frame.winfo_children():
    child.grid_configure(padx=6, pady=6)

#--------------------------------------------------
def get_city_station_ids(state='wa'):   
    url_general = 'http://w1.weather.gov/xml/current_obs/seek.php?state={}&Find=Find' #default==> http://w1.weather.gov/xml/current_obs/seek.php?state=wa&Find=Find
    state = state.lower()       #has to be lower case
    url= url_general.format(state)
    request = urllib.request.urlopen ( url )
    content = request.read().decode()           # This returns *****HTML****** data
    print(content)    
    
    # Must now create an HTML parcer in order to get to the data we want in the HTML from the website -- the station name and the city name
    parser = WeatherHTMLParser()
    parser.feed(content)
     
    #verify we have as many stations as cities
    print(len(parser.stations) == len(parser.cities))
     
    scr.delete('1.0', tk.END) #clear scrolledText widget for next btn click
     
    for idx in range(len(parser.stations)):
        city_station = parser.cities[idx] + ' (' + parser.stations[idx] + ')'
        print(city_station)
        scr.insert(tk.INSERT, city_station + '\n')
         
 
from html.parser import HTMLParser
  
class WeatherHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stations= []
        self.cities = []
        self.grab_data = False
          
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if "display.php?stid=" in str(attr):
                cleaned_attr= str(attr).replace("('href', 'display.php?stid=", '').replace("')", '')
                self.stations.append(cleaned_attr)
                self.grab_data = True
                  
    def handle_data(self, data):
        if self.grab_data:
            self.cities.append(data)
            self.grab_data = False
            
################################################################
# TAB 3 was removed
################################################################


################################################################
# TAB 4 Open Weather Map
################################################################

# Create a container frame
open_weather_cities_frame = ttk.LabelFrame(tab4, text=' Latest Observation for ')
open_weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

# Station City label
open_location = tk.StringVar()
ttk.Label(open_weather_cities_frame, textvariable=open_location).grid(column=0, row=1, columnspan=3)
ttk.Label(open_weather_cities_frame, text="City: ").grid(column=0, row=0)

# ComboBox
open_city = tk.StringVar()
open_city_combo = ttk.Combobox(open_weather_cities_frame, width=16, textvariable=open_city)
open_city_combo['values'] = ('Seattle, US', 'London, UK', 'Paris, FR', 'Mumbai, IN', 'Beijing, CN')
open_city_combo.grid(column=1, row=0)
open_city_combo.current(1)

# Callback function
def _get_station_open():
    city = open_city_combo.get()
    get_open_weather_data(city)

# Button
get_weather_btn = ttk.Button(open_weather_cities_frame, text='Get Weather', command=_get_station_open).grid(column=2, row=0)

# Spacing
for child in open_weather_cities_frame.winfo_children():
    child.grid_configure(padx=5, pady=2)
#--------------------------------------------------

# container frame
open_weather_conditions_frame = ttk.LabelFrame(tab4, text=' Current Weather Conditions ')
open_weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)

# Label & Textbox Entry widgets
ENTRY_WIDTH = 25

ttk.Label(open_weather_conditions_frame, text = "Last Updated:").grid(column=0, row=1, sticky='E')
open_updated = tk.StringVar()
open_updatedEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_updated, state='readonly')
open_updatedEntry.grid(column=1, row=1, sticky='W')

ttk.Label(open_weather_conditions_frame, text = "Weather:").grid(column=0, row=2, sticky='E')
open_weather = tk.StringVar()
open_updatedEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_weather, state='readonly')
open_updatedEntry.grid(column=1, row=2, sticky='W')

ttk.Label(open_weather_conditions_frame, text = "Temperature:").grid(column=0, row=3, sticky='E')
open_temp = tk.StringVar()
open_tempEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_temp, state='readonly')
open_tempEntry.grid(column=1, row=3, sticky='W')

ttk.Label(open_weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='E')
open_rel_humi = tk.StringVar()
open_rel_humiEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_rel_humi, state='readonly')
open_rel_humiEntry.grid(column=1, row=5, sticky='W')

ttk.Label(open_weather_conditions_frame, text="Wind:").grid(column=0, row=6, sticky='E')
open_wind = tk.StringVar()
open_windEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_wind, state='readonly')
open_windEntry.grid(column=1, row=6, sticky='W')

ttk.Label(open_weather_conditions_frame, text="Visibility:").grid(column=0, row=7, sticky='E')
open_visi = tk.StringVar()
open_visiEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_visi, state='readonly')
open_visiEntry.grid(column=1, row=7, sticky='W')

ttk.Label(open_weather_conditions_frame, text="Pressure:").grid(column=0, row=8, sticky='E')
open_msl = tk.StringVar()
open_mslEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=open_msl, state='readonly')
open_mslEntry.grid(column=1, row=8, sticky='W')

ttk.Label(open_weather_conditions_frame, text="Sunrise:").grid(column=0, row=9, sticky='E')
sunrise = tk.StringVar()
sunriseEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=sunrise, state='readonly')
sunriseEntry.grid(column=1, row=9, sticky='E')

ttk.Label(open_weather_conditions_frame, text="Sunset:").grid(column=0, row=10, sticky='E')
sunset = tk.StringVar()
sunsetEntry = ttk.Entry(open_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=sunset, state='readonly')
sunsetEntry.grid(column=1, row=10, sticky='E')

for child in open_weather_conditions_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)
    
################################################################
# OpenWeatherMap Data Collection ==> In JSON format, which is very easily parsed and turned into a dictionary.

from API_key import OWN_API_KEY_
from urllib.request import urlopen
import json

def get_open_weather_data(city='London,uk'):
    city = city.replace(' ', '%20')  #replaces empty spaces in city name with %20 so url can read it
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, OWN_API_KEY_) 
    response = urlopen(url)
    data = response.read().decode()
    json_data = json.loads(data)
    
    from pprint import pprint
    pprint(json_data)
    # temp in Kelvin
    # dt is the time the weather information was last updated... in unix time stamp format
   
    #--------------------------------------------------
    #collect all the information we're interested in, and save it in local variables:
    # sometimes there is no visibility available, so we do a try and except so no error is thrown.
    lat_long = json_data['coord']
    lastupdate_unix = json_data['dt']
    city_id = json_data['id']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    temp_kelvin = json_data['main']['temp']
    city_name = json_data['name']
    city_country = json_data['sys']['country']
    
    sunrise_unix = json_data['sys']['sunrise']
    sunset_unix = json_data['sys']['sunset']
    
    try: visibility_meter = json_data['visibility']
    except: visibility_meter = 'N/A'
    owm_weather = json_data['weather'][0]['description']
    weather_icon = json_data['weather'][0]['icon']
    try: wind_deg = json_data['wind']['deg']
    except: wind_deg = 'N/A'
    wind_speed_meter_sec = json_data['wind']['speed']
    
    # helper functions to translate units to something more familiar:
    def kelvin_to_celsius(temp_k):
        return "{:.1f}".format(temp_k - 273.15)
    
    def kelvin_to_fahrenheit(temp_k):
        return "{:.1f}".format((temp_k - 273.15)* 1.8000 + 32.00)
    
    from datetime import datetime
    def unix_to_datetime(unix_time):
        return datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')
    
    def meter_to_miles(meter):
        return "{:.2f}".format((meter * 0.00062137))
    
    if visibility_meter is 'N/A':
        visibility_miles = 'N/A'
    else: visibility_miles = meter_to_miles(visibility_meter)
    
    def mps_to_mph(meter_second):
        return "{:.1f}".format((meter_second * (2.23693629)))

    #--------------------------------------------------
    # Update GUI entry widgets with live data
    open_location.set('{}, {}'.format(city_name, city_country))
    lastupdate = unix_to_datetime(lastupdate_unix)
    open_updated.set(lastupdate)
    open_weather.set(owm_weather)
    temp_fahr = kelvin_to_fahrenheit(temp_kelvin)
    temp_cels = kelvin_to_celsius(temp_kelvin)
    open_temp.set('{} \xb0F  ({} \xb0C)'.format(temp_fahr, temp_cels))
    open_rel_humi.set('{}%'.format(humidity))
    wind_speed_mph = mps_to_mph(wind_speed_meter_sec)
    open_wind.set('{} degrees at {} MPH'.format(wind_deg, wind_speed_mph))
    open_visi.set('{} miles'.format(visibility_miles))
    open_msl.set('{} hPa'.format(pressure))
    
    sunrise_dt = unix_to_datetime(sunrise_unix)
    sunrise.set(sunrise_dt)
    sunset_dt = unix_to_datetime(sunset_unix)
    sunset.set(sunset_dt)
    
    # NOT WORKING:
    #===========================================================================
    # print(weather_icon)
    # url_icon = "http://openweathermap.org/img/w/{}.png".format(weather_icon)
    # ico = urlopen(url_icon)
    # open_im = PIL.Image.open(ico)
    # open_photo = PIL.ImageTk.PhotoImage(open_im)
    # ttk.Label(open_weather_cities_frame, image=open_photo).grid(column=0, row=1)
    # win.update()
    #===========================================================================
    
    

################################################################
#Tab 5: WEATHER UNDERGROUND
################################################################

# Create a container frame
wu_cities_frame = ttk.LabelFrame(tab5, text=' Latest Observation for ')
wu_cities_frame.grid(column=0, row=0, padx=8, pady=4)

# Station City label
wu_location = tk.StringVar()
ttk.Label(wu_cities_frame, text="City: ").grid(column=0, row=0)
ttk.Label(wu_cities_frame, textvariable=wu_location).grid(column=0, row=1, columnspan=3)


# ComboBox
wu_city = tk.StringVar()
wu_state = tk.StringVar()

wu_city_combo = ttk.Combobox(wu_cities_frame, width=16, textvariable=wu_city)
wu_state_combo = ttk.Combobox(wu_cities_frame, width=6, textvariable=wu_state)
wu_city_combo['values'] = ('Renton', 'Seattle', 'North Bend', 'Redmond', 'San Francisco', 'Portland')
wu_state_combo['values'] = ('WA', 'CA', 'OR')
wu_city_combo.grid(column=1, row=0)
wu_state_combo.grid(column=3, row=0)
wu_city_combo.current(2)
wu_state_combo.current(0)

# Callback function
def _get_station_wu():
    city = wu_city_combo.get()
    state = wu_state_combo.get()
    get_wu_data(city, state)

# Button
get_weather_btn = ttk.Button(wu_cities_frame, text='Get Weather', command=_get_station_wu).grid(column=4, row=0)

# Spacing
for child in wu_cities_frame.winfo_children():
    child.grid_configure(padx=5, pady=2)
#--------------------------------------------------

# container frame
wu_weather_conditions_frame = ttk.LabelFrame(tab5, text=' Current Weather Conditions ')
wu_weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)

# Label & Textbox Entry widgets
ENTRY_WIDTH = 25

ttk.Label(wu_weather_conditions_frame, text = "Last Updated:").grid(column=0, row=1, sticky='E')
wu_updated = tk.StringVar()
wu_updatedEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_updated, state='readonly')
wu_updatedEntry.grid(column=1, row=1, sticky='W')

ttk.Label(wu_weather_conditions_frame, text = "Weather:").grid(column=0, row=2, sticky='E')
wu_weather = tk.StringVar()
wu_updatedEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_weather, state='readonly')
wu_updatedEntry.grid(column=1, row=2, sticky='W')

ttk.Label(wu_weather_conditions_frame, text = "Temperature:").grid(column=0, row=3, sticky='E')
wu_temp = tk.StringVar()
wu_tempEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_temp, state='readonly')
wu_tempEntry.grid(column=1, row=3, sticky='W')

ttk.Label(wu_weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='E')
wu_rel_humi = tk.StringVar()
wu_rel_humiEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_rel_humi, state='readonly')
wu_rel_humiEntry.grid(column=1, row=5, sticky='W')

ttk.Label(wu_weather_conditions_frame, text="Wind Direction:").grid(column=0, row=6, sticky='E')
wu_wind = tk.StringVar()
wu_windEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_wind, state='readonly')
wu_windEntry.grid(column=1, row=6, sticky='W')

ttk.Label(wu_weather_conditions_frame, text="Wind Speed:").grid(column=0, row=7, sticky='E')
wu_wind_spd = tk.StringVar()
wu_wind_spdEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_wind_spd, state='readonly')
wu_wind_spdEntry.grid(column=1, row=7, sticky='W')

ttk.Label(wu_weather_conditions_frame, text="Visibility:").grid(column=0, row=8, sticky='E')
wu_visi = tk.StringVar()
wu_visiEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_visi, state='readonly')
wu_visiEntry.grid(column=1, row=8, sticky='W')

ttk.Label(wu_weather_conditions_frame, text="Pressure:").grid(column=0, row=9, sticky='E')
wu_pres = tk.StringVar()
wu_presEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_pres, state='readonly')
wu_presEntry.grid(column=1, row=9, sticky='W')

ttk.Label(wu_weather_conditions_frame, text="Elevation:").grid(column=0, row=10, sticky='E')
wu_elev = tk.StringVar()
wu_elevEntry = ttk.Entry(wu_weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wu_elev, state='readonly')
wu_elevEntry.grid(column=1, row=10, sticky='W')


for child in wu_weather_conditions_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)
    
# GET WEATHER FROM wunderground.com:

from API_key_WU import OWM_API_KEY_WU

def get_wu_data(city = 'Seattle', state = 'WA'):
    city = city.replace(' ', '%20')
    #state = state.replace(' ', '%20')
    
    url = "http://api.wunderground.com/api/{}/conditions/q/{}/{}.json".format(OWM_API_KEY_WU, state, city)
    
    response = urlopen(url)
    data = response.read().decode()
    json_data = json.loads(data)
    
    from pprint import pprint
    pprint(json_data)
    
#get_wu_data()

    #local variables to pull desired info from json 
    last_update = json_data['current_observation']['observation_time_rfc822']
    clouds = json_data['current_observation']['weather']
    temp_wu = json_data['current_observation']['temperature_string']
    humidity = json_data['current_observation']['relative_humidity']
    wind_dir = json_data['current_observation']['wind_dir']
    wind_spd = json_data['current_observation']['wind_mph']
    try: visibility = json_data['current_observation']['visibility_mi']
    except: visibility = "NA"
    pressure_wu = json_data['current_observation']['pressure_in']
    elevation = json_data['current_observation']['display_location']['elevation']
    city_name = json_data['current_observation']['display_location']['full']
      
     
    #set the json data in the GUI
    wu_location.set(city_name)
    wu_updated.set(last_update)
    wu_weather.set(clouds)
    wu_temp.set(temp_wu)
    wu_rel_humi.set(humidity)
    wu_wind.set(wind_dir)
    wu_wind_spd.set(wind_spd)
    wu_visi.set(visibility)
    wu_pres.set(pressure_wu)
    wu_elev.set(elevation)
    
    
################################################################
################################################################

def get_current_window_size():
    win.update()                    # to get runtime size
    print('width = ', win.winfo_width())
    print('height = ', win.winfo_height())
    
def increase_window_width():
    win.minsize(width=300, height=1)    # 1 - default
    
    # disable resizing the GUI
    win.resizable(0,0)
    
#-------------------------
# start GUI
#-------------------------
#get_current_window_size()
#increase_window_width()
#print()
#get_current_window_size()

win.mainloop()