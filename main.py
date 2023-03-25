import check_weather 


city = "galle"
api_key = "a4cd98b4856ea84f52ad5b45a741cd41"
delay = 0.5





if __name__ == "__main__":
    weather_generate = check_weather.CheckWeather(city,api_key,delay)
    weather_generate.start()
    weather_generate.join()


    
    
    