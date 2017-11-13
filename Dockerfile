FROM python:3.6.1

# set working directory
WORKDIR /app

# add requirements (to leverage Docker cache)
ADD . /app

# install requirements
RUN pip install -r requirements.txt

EXPOSE 80

# run server
CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]