FROM python:3.8

COPY . /app
WORKDIR /app/bookinfo/src/productpage 
RUN pip install -r requirements.txt
EXPOSE 9080
CMD [ "python3", "productpage_monolith.py", "9080" ]
