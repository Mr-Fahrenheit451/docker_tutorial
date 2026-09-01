FROM python:3.12-alpine

#update linux distribution
RUN apk add --no-cache gcc musl-dev linux-headers

#create working directory
WORKDIR /home/example_python_app/

#copy code from your machine (host) to the container youre creating
COPY ./ /home/example_python_app/

#make sure code can be executed with permissions
RUN chmod -R +x /home/example_python_app/

#install any python dependencies
RUN pip install -r requirements.txt 

#run your code
CMD python ./hello-world.py

