FROM python:3.6.1

# set working directory
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
# ADD ./requirements.txt /usr/src/app
ADD . /usr/src/app


# install requirements
RUN pip install -r requirements.txt

RUN yum update
RUN yum install -y netcat

# run server
CMD ["./entrypoint.sh"]
# CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]
# CMD ["ping", "www.google.com"]