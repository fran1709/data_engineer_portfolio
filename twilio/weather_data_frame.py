from queryng_api import get_json, get_forecast 
from tqdm import tqdm
import pandas as pd

" ---------- GLOBAL VARIABLES ---------- "
data = []
col = ['Specific Date', 'Hour', 'Condition', 'Temperature', 'Will it Rain', 'Probability of Rain']

" ---------- Procedure ----------"
# request the json from the api
json_response = get_json()

# scraping the relevant information
for hour in tqdm(range(len(json_response['forecast']['forecastday'][0]['hour']))):
    data.append(get_forecast(json_response, hour))

# making data frame with it
data_frame = pd.DataFrame(data, columns=col)
print(data_frame)