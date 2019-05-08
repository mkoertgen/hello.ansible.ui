FROM python:3.7.3-alpine3.9

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python", "app.py" ]