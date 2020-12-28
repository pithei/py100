import xml.etree.ElementTree as ET 

stream = open('1_data.xml', 'r')

xml = ET.parse(stream)

root = xml.getroot()


for element in root:
    print(ET.tostring(element))
    print("")

    print(element.get("food"))