#importy
import json 
import xml.etree.cElementTree as ET
import yaml
import xmltodict
from yaml import SafeLoader
import os.path
plik_json = "przyklad.json"
plik_xml = "przyklad.xml"
plik_yaml = "przyklad.yaml"
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
    