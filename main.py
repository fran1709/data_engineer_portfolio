from bs4  import BeautifulSoup
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
from building_sms import send_weather_pronostic

" ---------- MAIN FUNCTION ---------- " 
def main():
    send_weather_pronostic('whatsapp')

# call of the main function
main()