# challenge1

Implement rest layer application in golang/python/nodeJS (any one of your choice) that should listen on port 9098 and should ask for name and upon submitting should return "Hello [entered name]" string
E.g. If you submit "Cognologix" the returning string will be "Hello Cognologix". In case no name is provided it should return "Hello stranger"
Dockerize the above implemented application.

# Answer - App - server.py 
Line 42 - we can use localhost instead of 0.0.0.0 if we are reunning it locally.

python3 server.py ----> Access over http://localhost:9098/


# Answer - Dockerize -  Dockerfile

docker build -t challenge1 .   ----> build image

Line 42 - you can change it to localhost if you are going to use host network

docker run -it --network host -p 9098:9098 challenge  --> using host network
            or
docker run -d --network host -p 9098:9098 challenge



docker run -it -p 9098:9098 challenge1 
            or
docker run -d -p 9098:9098 challenge1  --> using deafult network






