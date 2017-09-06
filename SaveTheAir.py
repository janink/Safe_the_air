from AirQualityData import *


def collect_data(city):
    d = QualityData(city)
    d.curl_data()

if __name__ == "__main__":
    city = "London"
    collect_data(city)




