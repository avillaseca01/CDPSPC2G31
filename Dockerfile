FROM python:3.8

COPY /bookinfo/src/productpage/productpage_monolith.py ./app
RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
EXPOSE 9080
CMD [ "python3", "productpage_monolith.py 9080" ]
