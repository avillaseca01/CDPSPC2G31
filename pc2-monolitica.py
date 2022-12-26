import os
from subprocess import call
import logging


os.system('sudo apt-get update')
os.environ ["GROUP_NUMBER"]="31"
os.system('sudo apt-get install pip -y')
os.system('sudo pip install -r ./CDPSPC2G31/bookinfo/src/productpage/requirements.txt')
from lxml import etree
arser = etree.XMLParser(recover=True)
ngrupo = os.environ.get("GROUP_NUMBER")

try:

    parser = etree.HTMLParser()
    doc = etree.parse("./CDPSPC2G31/bookinfo/src/productpage/templates/productpage.html", parser)
    etiqueta = doc.find(".//a[@class='navbar-brand']")
    etiqueta.text = "Grupo"+ngrupo

    with open("./CDPSPC2G31/bookinfo/src/productpage/templates/productpage.html", "w") as f:
        f.write(etree.tostring(doc, encoding='unicode', pretty_print=True))

except OSError as err:
    print("Error al leer el archivo:", err)

os.system('python3 ./CDPSPC2G31/bookinfo/src/productpage/productpage_monolith.py 9080')




