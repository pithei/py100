from lxml import etree as ET 

stream = open('1_data2.xml', 'r')

xml = ET.parse(stream)

root = xml.getroot()


for element in root:
    print(ET.tostring(element))
    print("")

    print(element.get("food"))