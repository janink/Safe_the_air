import openpyxl

excelFile = 'LondonStreetData.xlsx'
data = openpyxl.load_workbook(excelFile)
london = data.get_sheet_by_name('london')

dictionary = {}
dictionary['Islington'] = 2
dictionary['Redbridge'] = 2
dictionary['Kensington and Chelsea'] = 2
dictionary['Greenwich'] = 2
dictionary['Sutton'] = 2
dictionary['Lewisham'] = 1
dictionary['Lambeth'] = 2
dictionary['Barnet'] = 1
dictionary['Hammersmith and Fulham'] = 2
dictionary['Richmond upon Thames'] = 2
dictionary['Barking and Dagenham'] =	1
dictionary['Southwark'] = 2
dictionary['Enfield'] = 1
dictionary['City of London'] =	2
dictionary['Wandsworth'] = 2
dictionary['Merton'] = 1
dictionary['Haringey'] = 2
dictionary['Harrow'] = 1
dictionary['Hackney'] = 2
dictionary['Hounslow'] = 2
dictionary['Westminster'] = 3
dictionary['Havering'] = 1
dictionary['Waltham Forest'] = 2
dictionary['Hillingdon'] = 2
dictionary['Bexley'] = 2
dictionary['Ealing'] = 2
dictionary['Bromley'] = 2
dictionary['Kingston upon Thames'] = 1
dictionary['Newham'] = 1
dictionary['Croydon'] = 1
dictionary['Tower Hamlets'] = 2
dictionary['Camden'] = 2
dictionary['Brent'] = 2


for i in range(2, london.max_row+1):
    if london['G'+str(i)].value == None:
        london['G'+str(i)] = 'Hillingdon'
    london['H'+str(i)] = dictionary[london['G'+str(i)].value]


data.save(excelFile)