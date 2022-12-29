FROM python:3.8
COPY ./productpage /opt/microservices 
WORKDIR /opt/microservices  
RUN pip install -r requirements.txt
EXPOSE 9080
#RUN python3 cambianombre.py
CMD [ "python3", "productpage", "9080" ]
