import xml.etree.ElementTree as ET
import shutil
#open xml file.
tree = ET.ElementTree(file="config.xml")
# file elements
out=tree.findall("./file")
for child in out:
    temp = []
    #check if source_path atribute exist
    if "source_path" in child.attrib:
        temp.append(child.attrib["source_path"])
    #check if destination_path atribute exist
    if "destination_path" in child.attrib:
        temp.append(child.attrib["destination_path"])
    #check if file_name atribute exist
    if "file_name" in child.attrib:
        temp.append(child.attrib["file_name"])
    #check if number of atribues == 3
    if(len(temp)>=3):
        #error handle, try catch exception OSError
        try:
            #copy file
            shutil.copy(temp[0]+"/"+temp[2],temp[1]+"/"+temp[2])
        except OSError as e:
            #error messages
            print(temp[2]+": System can't copy the file!" )
            print("Possible solution: Check destination in xml file. If it's Windows locations, try running script on Windows")


