from weather_data_frame import get_df_rain
from twilio_config import TWILIO_PHONE_NUMBER, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, MY_PHONE_NUMBER, TWILIO_WHATSAPP_NUMBER, MY_WHATSAPP_NUMBER, QUERY
from twilio.rest import Client
import time

date, df_rain = get_df_rain()
sms_template = '\nHola! \n\n\n El pronostico del tiempo hoy '+ date +' en ' + QUERY +' es : \n\n\n ' + str(df_rain)
twilio_number=''
my_number=''

def build_sms(twilio_number, my_number):
    time.sleep(2)
    # setting client credentials
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    
    #making client msg
    msg = client.messages.create(
        from_ = twilio_number,
        body = sms_template,
        to =  my_number
    )
    print('Mensaje enviado! ', msg.sid)

# Function that send direct sms/whatsapp deppending of parameter
def send_weather_pronostic(pSmsWay):
    if pSmsWay == 'sms':
        twilio_number = TWILIO_PHONE_NUMBER
        my_number = MY_PHONE_NUMBER
    elif pSmsWay == 'whatsapp':
        twilio_number = TWILIO_WHATSAPP_NUMBER
        my_number = MY_WHATSAPP_NUMBER
    build_sms(twilio_number, my_number)
