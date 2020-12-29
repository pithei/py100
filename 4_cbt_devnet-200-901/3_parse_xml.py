import xmltodict

stream = open("1_data2.xml", "r")

xml = xmltodict.parse(stream.read())

for e in xml["breakfast_menu"]["food"]:
    print(e)