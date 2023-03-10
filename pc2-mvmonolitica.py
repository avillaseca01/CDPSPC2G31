import os
from subprocess import call
import logging

os.system('sudo apt-get update')
os.environ ["GROUP_NUMBER"]="31"
os.system('sudo apt-get install pip -y')
os.system('sudo pip install -r ./bookinfo/src/productpage/requirements.txt')
from lxml import etree
import re
ngrupo = os.environ.get("GROUP_NUMBER")

try:

    parser = etree.HTMLParser()
    doc = etree.parse("./bookinfo/src/productpage/templates/productpage.html", parser)
    etiqueta = doc.find(".//a[@class='navbar-brand']")
    etiqueta.text = "Grupo"+ngrupo

    with open("./bookinfo/src/productpage/templates/productpage.html", "w") as f:
        f.write(etree.tostring(doc, encoding='unicode', pretty_print=True))

except OSError as err:
    print("Error al leer el archivo:", err)

with open("./bookinfo/src/productpage/templates/productpage.html", "r") as f:
	filedata = f.read()

filedata = re.sub("{% block title %}Simple Bookstore App{% endblock %}", "{% block title %}Grupo "+ngrupo+" {% endblock %}", filedata)
with open("./bookinfo/src/productpage/templates/productpage.html", "w") as f:
	f.write(filedata)
os.system('python3 ./bookinfo/src/productpage/productpage_monolith.py 9080')
