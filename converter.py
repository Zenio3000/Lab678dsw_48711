#importy
import json 
import xml.etree.cElementTree as ET
import yaml
import xmltodict
from yaml import SafeLoader
import os.path
plik_json = "przyklad.json"
plik_xml = "przyklad.xml"
plik_yaml = "test.yaml"
file_type = ["json","xml","yaml"]
i = 0
while i != 7:
    print("""
    1 - konwersje json na xml
    2 - konwersje json na yaml
    3 - konwersja xml na json
    4 - konwersja xml na yaml
    5 - konwersja yaml na json
    6 - konwersja yaml na xml
    7 - zakonczenie programu
    """)

    i = int(input("Wybierz opcje"))

    if (i == 1 & os.path.isfile(plik_json) ):
    #json na xml
        with open(plik_json, "r") as json_file:
                data = json.load(json_file)
                with open(input(f'podaj nazwe nowego pliku '), "w") as  xml_file:
                    xmltodict.unparse(data, output=xml_file)
                    xml_file.close()
    elif (i == 2 & os.path.isfile(plik_json)):
    #json na yaml
        with open(plik_json, "r") as json_file:
            data = json.load(json_file)
            with open(input("podaj nazwe nowego pliku "), "w") as yaml_file:
                yaml.dump(data, yaml_file)
                yaml_file.close()
    elif (i == 3 & os.path.isfile(plik_xml)):
    #xml na json
        with open(plik_xml,"r") as xml_file:
                data = xmltodict.parse(xml_file.read())
                json = json.dumps(data)
                with open(input("podaj nazwe nowego pliku "), "w") as json_file:
                    json_file.write(json)
    elif (i == 4 & os.path.isfile(plik_xml)):                
    #xml na yaml
        with open(plik_xml,"r") as xml_file:
            data = xmltodict.parse(xml_file.read())
            with open(input("podaj nazwe nowego pliku "), "w") as yaml_file:
                    yaml.dump(data, yaml_file)
                    yaml_file.close()
    elif (i == 5 & os.path.isfile(plik_yaml)):
    #yaml na json
        with open(plik_yaml, "r") as yaml_file:
            data = yaml.load(yaml_file, Loader=SafeLoader)
            with open(input("podaj nazwe nowego pliku "), "w") as json_file:
                json.dump(data, json_file)
                json_file.close()
    elif (i == 6 & os.path.isfile(plik_yaml)):
    #yaml na xml
        with open(plik_yaml, "r") as yaml_file:
            data = yaml.load(yaml_file, Loader=SafeLoader)
            with open(input("podaj nazwe nowego pliku "), "w") as  xml_file:
                xmltodict.unparse(data, output=xml_file)
                xml_file.close()
    elif (i == 7):
        print("zakonczyles program")
    else:
         print("podales zly numer lub plik nie istnieje")