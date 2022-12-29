FROM node:12.18.1-slim
COPY /ratings/package.json /opt/microservices/
COPY /ratings/ratings.js /opt/microservices/
ENV SERVICE_VERSION=v1
WORKDIR /opt/microservices
RUN npm install httpdispatcher@1.0.0
RUN npm install mongodb@3.6.0
RUN npm install mysql@2.15.0
EXPOSE 9080
CMD ["node", "ratings.js", "9080"]
