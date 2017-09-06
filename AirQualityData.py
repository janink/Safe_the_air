
import json
import urllib2

class QualityData:
    def __init__(self, city):
        self.city = city


    def curl_data(self):
        data_json = json.load(urllib2.urlopen("http://api.erg.kcl.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/GroupName=London/Json"))
        #print data_json
        export_data= {}

        for authority in data_json['DailyAirQualityIndex']['LocalAuthority']:
            if 'Site' in authority.keys():
                #print (authority[u'@LocalAuthorityName'])
                max_list = []
                if type(authority['Site']) == list:
                    for site in authority['Site']:
                        if type(site['Species'])==list:
                            for el in site['Species']:
                                max_list.append(el['@AirQualityIndex'])
                                #print(el['@AirQualityIndex'])
                        elif type(site['Species'])== dict:
                            max_list.append(site['Species']['@AirQualityIndex'])
                            #print(site['Species']['@AirQualityIndex'])
                        else:
                            print "1", authority
                else:
                    if type(authority['Site']['Species']) == list:
                        for el in authority['Site']['Species']:
                            max_list.append(el['@AirQualityIndex'])
                            #print(el['@AirQualityIndex'])
                    elif type(authority['Site']['Species']) == dict:
                        max_list.append(authority['Site']['Species']['@AirQualityIndex'])
                        #print(authority['Site']['Species']['@AirQualityIndex'])

                    else:
                        print "2", authority

            else:
                max_list.append(1)
                print "3", authority

            export_data[authority[u'@LocalAuthorityName']] = max(max_list)
        write(export_data
        print len(export_data)