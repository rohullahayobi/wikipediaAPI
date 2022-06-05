# Sets the base image for subsequent instructions
FROM ubuntu:22.04
# Sets the working directory in the container  
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev-is-python3
# Copies the files to the working directory
COPY . /app
# Install dependencies
RUN pip install -r requirements.txt
# Command to run on container start
CMD ["flask", "run", "--host=0.0.0.0"] 
CMD [ "python3" , "./db.py" ]   
CMD [ "python3" , "./app.py" ]
EXPOSE 5000

