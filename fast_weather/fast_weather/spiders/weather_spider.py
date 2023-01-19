import scrapy

class WeatherSpider(scrapy.Spider):
    name = "weather"

    def scrape(self):
        api_key = '4968e589f443bde5a7ebc60af5cb1da0'
        lat = 55.752
        lon = 37.615
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        yield scrapy.Request(url=url, callback=self.parse)
        # fetch('https://api.openweathermap.org/data/2.5/weather?lat=55.752&lon=37.615&appid=4968e589f443bde5a7ebc60af5cb1da0'