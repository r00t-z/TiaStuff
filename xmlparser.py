import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\Matheus\Documents\Codes\TIA_Addins\FC180_STATUS.xml')
root = tree.getroot()

#print(root.tag, root.attrib)
for stuff in root:
    for stuffs in stuff.iter():
        print(stuffs.attrib)