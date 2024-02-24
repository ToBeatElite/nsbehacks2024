FROM python:3.8

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /backend

# Install app dependencies
COPY requirements.txt .

# Bundle app source
COPY . .

RUN pip install -r requirements.txt; \
    python3 setup.py install; \
    python3 manage.py makemigrations; \
    python3 manage.py migrate; 

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
# CHANGE Debug = True for production manually