
import json
import urllib2

class QualityData:
    def __init__(self, city):
        self.city = city


    def curl_data(self):
        token = "935d45824e3d1e4b01d3c3052464f0e7b72c5465"
        data_img = json.load(urllib2.urlopen("http://api.waqi.info/feed/"+self.city+"/?token="+token))
        print data_img