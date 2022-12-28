FROM python:3.8
COPY /home/-----/CDPSPC2G31/bookinfo /app
WORKDIR /app/bookinfo/src/productpage 
RUN pip install -r requirements.txt
EXPOSE 9080
#RUN python3 cambianombre.py
CMD [ "python3", "productpage", "9080" ]
