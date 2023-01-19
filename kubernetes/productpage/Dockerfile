FROM python:3.8
COPY ./productpage /opt/microservices 
WORKDIR /opt/microservices  
ENV GROUP_NUMBER=""
RUN pip install -r requirements.txt
EXPOSE 9080
CMD [ "python3", "productpage.py", "9080" ]
