FROM python:3.8
#RUN apt-get update && apt-get install -y \
#    python3 \
#    python3-pip \
#    git
#RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
COPY . /app
COPY /bookinfo/src/productpage/productpage_monolith.py ./app
WORKDIR /app
RUN pip install -r requirements.txt 
CMD [ "python3", "productpage_monolith.py 9080" ]   
#RUN pip install lxml
