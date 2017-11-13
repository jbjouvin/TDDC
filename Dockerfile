FROM python:3.6.1

# set working directory
RUN mkdir -p /usr/src/app

# add requirements (to leverage Docker cache)
ADD . /usr/src/app

WORKDIR /usr/src/app

# install requirements
RUN pip install -r requirements.txt

# run server
CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]
# CMD ["ping", "www.google.com"]