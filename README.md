# docker-image-build
Using an AI to generate a py code for an app, and installing the dependencies, upload it to the docker hub repo and pull it on my local machine.

prompt AI to build a simple app that runs on localhost  "build a simple hello world flask app that runs on the local host by adding 0.0.0.0"



install the dependecies require which is flask in this case 
command on the terminal is
# pip install flask
 run the command below on the terminal and th simple app will open a port and start running and i used app.py because that's the name of the file my app code is in.
 # python app.py

 
 
 
 Our main goal here is to dockerlized the whole ap, requirements, and make it available for people to use.

 Now, Let's work on the Dockerfile
 Dockerfile comprises of the following
 1. Baseimage( could be alpine or small size image)
 2. the app code
 3. dependecies (flask)
 4. Run the code

 The docker file combined the whole mentioned above into a file and also set the variables too.

 and we are using the official Python runtime as base image because we need a smaller size for the simple appilication 

 we run the command below to build the app && docker images to show the built image
 # docker build -t nameyouwant:1.0 .
# docker images 

Now we have to do port-binding for the image
# docker run -td -p 5000:5000 sh
this command will open a port that will display the webpage

Now that we are done building the image, lets push it to the docker hub, search docker.com and sign up
After signing up, click on the profile and find the create repository

To push the image, you have to modify the name of the app to the name of the repository, use this command
# docker tag nameoftheimage:tagname nameoftheimage:tagnamegiventoyouinthedocker
# docker tag adeyinkapp:1.0 adeyinka12/adeyinkafirstapp:tagname

the tagname could be 1.0 or latest. you can use the docker images command to check for the tagname

pushing it to the dockerhub
I have to be authenticated 
so I run the command
# docker login
I open the link provided as an output on the terminal and I used the pincode provided as an ouput too
It might not show at first use the command docker logout and run the docker login again
After authentication then run the push command (the one given in the dockerhub)
#  docker push adeyinka12/adeyinkafirstapp:1.0

Now Lets remove all the images on the system and try using the images I created

docker rm -f $(docker ps -a)
docker rmi -f $(docker images)
docker rmi ContainerID