import os
os.system('sudo apt-get update')
os.system('sudo apt-get install -y docker.io')
os.system('sudo apt-get install -y docker-compose')
os.system('cp ./dockercompose/productpage/Dockerfile ./bookinfo/src/productpage/')
os.system('cp ./dockercompose/details/Dockerfile ./bookinfo/src/details/')
os.system('cp ./dockercompose/ratings/Dockerfile ./bookinfo/src/ratings/')
os.system('cp ./dockercompose/docker-compose.yaml ./bookinfo/src/')
os.chdir(os.getcwd()+'/bookinfo/src/reviews/')
os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w/home/gradle/project gradle:4.8.1 gradle clean build')
os.system('cd ..')
os.system('sudo docker-compose up -d')
