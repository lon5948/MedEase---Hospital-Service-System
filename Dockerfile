# from the public docker repository
# FROM ubuntu:22.04
FROM python:3.10

RUN pip install --upgrade pip\
    && pip install flask\
    && pip install uwsgi\
    && pip install mysql-connector-python\
    && pip install geocoder\
    && pip install pytest
#    && pip install waitress\
    

# copy the requirements file into the image
# COPY ./requirements.txt /app/requirements.txt

# EXPOSE 5000

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
# RUN python -m pip install --upgrade pip\
#    && pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner

# run uwsgi ince the docker image is running
CMD ["uwsgi", "--ini", "wsgi.ini"]
# CMD ["python", "-m", "pytest"]
# CMD python app.py