import os
from subprocess import call
import logging


os.system('sudo apt-get update')
os.system('sudo apt-get install pip -y')
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')
os.system('sudo pip install -r ./practica_creativa2/bookinfo/src/productpage/requirements.txt')
os.system('sudo pip install urllib3==1.21.1')
os.system('sudo pip install testresources')
os.system('sudo pip install lxml')
from lxml import etree
arser = etree.XMLParser(recover=True)

try:

    parser = etree.HTMLParser()
    doc = etree.parse("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", parser)
    etiqueta = doc.find(".//a[@class='navbar-brand']")
    etiqueta.text = "Grupo 31"

    with open("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "w") as f:
        f.write(etree.tostring(doc, encoding='unicode', pretty_print=True))

except OSError as err:
    print("Error al leer el archivo:", err)

os.system('python3 ./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080')




