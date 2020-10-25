import requests
import json
import pandas as pd
from csv import writer

df = pd.read_csv("https://raw.githubusercontent.com/williamshammond/dont-burn-your-tv/main/or_data.csv")
df['Lat'] = ''
df['Long'] = ''

for i in range(1, len(df.index)):
    name = df.loc[i]['Name']
    addr = df.loc[i]['Street Address']
    city = df.loc[i]['City']
    state = df.loc[i]['State']

    api_key = 'AIzaSyBpzHrL-D9VewwuEby1ybkWIiBEYpaD_Pw'
    url='https://maps.googleapis.com/maps/api/geocode/json?'

    r = requests.get(url, params = {
        'key': api_key,
        'address': name + " " + addr + " " + city + " " + state
    })

    try:
        lat = r.json()['results'][0]['geometry']['location']['lat']
        lng = r.json()['results'][0]['geometry']['location']['lng']

        df.at[i, 'Lat'] = lat
        df.at[i, 'Long'] = lng
    except(IndexError):
        print('none found at col ', i)

df.to_csv("or_data.csv")
