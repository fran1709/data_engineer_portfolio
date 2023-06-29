import requests
from twilio_config import * #credentials

" ---------- FUNCTIONS ---------- "
# Function that get the Json from the API with all the info.
def get_json():
    # Setting query info
    query = '10.4, -84.38'  # Location by latitude, longitude.  (Quesada, Alajuela, Costa Rica)
    api_key = API_KEY_WAPI
    url_clima = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'

    # Doing the request to API
    response = requests.get(url_clima).json()
    return response

# Function that get all the necesary info of weather.
# Specific Date, hour, condition, temperature, will it rain?, probability of rain.
def get_forecast(pResponse, pHour):
    date = pResponse['forecast']['forecastday'][0]['hour'][pHour]['time'].split()[0]  #str
    hour = int(pResponse['forecast']['forecastday'][0]['hour'][pHour]['time'].split()[1].split(':')[0]) #int
    condition = pResponse['forecast']['forecastday'][0]['hour'][pHour]['condition']['text'] #str
    temperature = pResponse['forecast']['forecastday'][0]['hour'][pHour]['temp_c'] #float
    will_rain = pResponse['forecast']['forecastday'][0]['hour'][pHour]['will_it_rain'] #bool
    probability_of_rain = pResponse['forecast']['forecastday'][0]['hour'][pHour]['chance_of_rain'] #int
    return date, hour, condition, temperature, will_rain, probability_of_rain


" ---------- Prints ---------- " 
#print(response.keys())
#print(response['location'])
#print(response['forecast']['forecastday'][0].keys())
#print(len(response['forecast']['forecastday'][0]['hour'][0]))
#print(response['forecast']['forecastday'][0]['hour'][13])
#print(date)
#print(hour)
#print(condition)
#print(temperature)
#print(will_rain)
#print(probability_of_rain)
#print(data)