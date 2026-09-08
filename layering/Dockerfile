FROM pramanan3/home_example:latest

#create working directory
WORKDIR /home/python_app/

#copy code from your machine (host) to the container youre creating
COPY ./ /home/python_app/

#make sure code can be executed with permissions
RUN chmod -R +x /home/python_app/

#run your code
CMD python ./hello-world2.py

# CMD tail -f /dev/null