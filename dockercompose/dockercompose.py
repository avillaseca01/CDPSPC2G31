import os
os.system('sudo apt-get update')
os.system('sudo apt-get install -y docker.io')
os.system('sudo apt-get install docker-compose')
os.system('cd ./bookinfo/src/reviews/reviews-wlpcfg')
os.system('docker run --rm -u root -v "$(pwd)":/home/gradle/project -w/home/gradle/project gradle:4.8.1 gradle clean build')
