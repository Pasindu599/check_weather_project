from threading import Thread
import time
import requests
import json
class CheckWeather(Thread):
    def __init__(self,city,api_key,delay = 5) -> None:
        super().__init__()
        self.city = city
        self.api_key = api_key
        self.delay = delay



    def run(self):
        while True:
            weather = self.get_wether(self.city,self.api_key)
            print(weather)
            # to wait 
            time.sleep(self.delay * 60)



            


    def get_wether(self,city,api_key):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            json_content = json.loads(response.content)
            weather = json_content["weather"]
            if weather:
                return weather[0]
        