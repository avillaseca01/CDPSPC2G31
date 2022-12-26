import os
from lxml import etree 
ngrupoenviron = str(os.environ["GROUP_NUMBER"])
ngrupogetenv = str(os.getenv("GROUP_NUMBER"))
try:

    parser = etree.HTMLParser()
    doc = etree.parse("./templates/productpage.html", parser)
    etiqueta = doc.find(".//a[@class='navbar-brand']")
    etiqueta.text = "Grupo "+ngrupoenviron+" "+ngrupogetenv

    with open("./templates/productpage.html", "w") as f:
        f.write(etree.tostring(doc, encoding='unicode', pretty_print=True))

except OSError as err:
    print("Error al leer el archivo:", err)
