FROM python:3.12-alpine

#update linux distribution
RUN apk add --no-cache gcc musl-dev linux-headers

#create working directory
WORKDIR /home/docker_tutorial/

#copy code from your machine (host) to the container youre creating
COPY ./ /home/docker_tutorial/

#make sure code can be executed with permissions
RUN chmod -R +x /home/docker_tutorial/

#run the webapp
CMD python -m http.server 6060

