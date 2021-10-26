import xml.etree.ElementTree as ET
arbol = ET.parse('ejemplo_country_data.xml')
raiz = arbol.getroot()

for child in raiz:
  print(child.tag, child.attrib)

print((raiz[0][1].text))