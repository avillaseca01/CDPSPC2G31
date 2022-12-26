import os
from lxml import etree 
ngrupo = str(os.environ.get("GROUP_NUMBER"))

try:

    parser = etree.HTMLParser()
    doc = etree.parse("./CDPSPC2G31/bookinfo/src/productpage/templates/productpage.html", parser)
    etiqueta = doc.find(".//a[@class='navbar-brand']")
    etiqueta.text = "Grupo"+ngrupo

    with open("./CDPSPC2G31/bookinfo/src/productpage/templates/productpage.html", "w") as f:
        f.write(etree.tostring(doc, encoding='unicode', pretty_print=True))

except OSError as err:
    print("Error al leer el archivo:", err)
