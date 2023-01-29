import os
os.system('cp ./dockermonolitica/Dockerfile .')
os.system('sudo apt-get update')
os.system('sudo apt-get install docker.io -y')
os.system('sudo docker build -t g31/product-page .')
os.system('sudo docker run --name g31-product-page -p 9080:9080 -e GROUP_NUMBER=31 -d g31/product-page')
