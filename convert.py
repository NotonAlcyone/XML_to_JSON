import xml.etree.ElementTree as ET
import json

def changer(n):
	try:
		int(n)
		return int(n)
	except:
		return n

data = {}
def convert(root, data):
	for child in root:
		name = child.attrib["name"]
		if "value" not in child.attrib:
			data[name] = convert(child,data = {})
		else:
			data[name] = changer(child.attrib["value"])
	else:
		return data

tree = ET.parse('FileName')
root = tree.getroot()
data = convert(root, data)
print(json.dumps(data, indent = 2))
