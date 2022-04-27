
### LOCAL

git clone the project then cd into the directory
git clone url

create a virtual environment
python3 -m venv venv

active a virtual environment
source venv/bin/activate

upgrading version pip
python3 -m pip install --upgrade pip

installer dependency
pip install -r requirements.txt

run application local 
python main.py

the running app in a browser at the URL
http://127.0.0.1:1000


### DOCKER

build the docker image
docker build -t flaskapp:latest .

start the container
docker run -d -p 1000:1000 flaskapp
docker run --name flaskapp -d -p 1000:1000 --rm flaskapp:latest



#### Kubernates

tag images 
docker build --tag flaskapp:latest .

Deploying to Kubernetes
kubectl apply -f deployment.yaml

Ydaydevops1!