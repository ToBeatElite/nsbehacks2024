FROM python:3.8

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /frontend

# Install app dependencies
COPY requirements.txt .

# Bundle app source
COPY . .

RUN pip install -r requirements.txt;

EXPOSE 5000

CMD [ "python3", "app.py"]
# CHANGE Debug = True for production manually