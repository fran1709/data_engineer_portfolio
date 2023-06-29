from queryng_api import get_json, get_forecast 
from tqdm import tqdm
import pandas as pd

" ---------- GLOBAL VARIABLES ---------- "
data = []
col = ['Date', 'Hour', 'Condition', 'Temperature', 'Will it Rain', 'Probability of Rain']

" ---------- FUNCTIONS ----------"
def upload_data():
    # request the json from the api
    json_response = get_json()

    # scraping the relevant information
    for hour in tqdm(range(len(json_response['forecast']['forecastday'][0]['hour']))):
        data.append(get_forecast(json_response, hour))

def make_data_frame():
    # making data frame with it
    data_frame = pd.DataFrame(data, columns=col)
    return data_frame

def data_frame_rain():
    df = make_data_frame()
    date = df['Date'][0]

    # reducing the columns based on the active hours of the person and when it is going to rain.
    df_rain = df[(df['Will it Rain']==1) & (df['Hour']>6) & (df['Hour']<22)] #setting filter rules
    df_rain = df_rain[['Hour','Condition','Temperature']] #setting wich columns
    df_rain.set_index('Hour', inplace=True)
    return date, df_rain

def get_df_rain():
    upload_data()
    date, df_rain = data_frame_rain()
    return date, df_rain

" ---------- Prints ---------- " 
#print(data_frame)
#print(df_rain)