FROM ruby:2.7.1-slim
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true
EXPOSE 9080
COPY ./details/details.rb /opt/microservices/details.rb
WORKDIR /opt/microservices
CMD ["ruby", "details.rb", "9080"]
