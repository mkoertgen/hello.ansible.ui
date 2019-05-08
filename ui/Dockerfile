#FROM python:3.7.3-alpine3.9
FROM docker/compose:1.24.0

ENTRYPOINT [ ]

# Add python, cf.: https://github.com/frol/docker-alpine-python3/blob/master/Dockerfile
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Add app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

# cf.: https://stackoverflow.com/questions/55315103/oserror-errno-8-exec-format-error-when-trying-to-run-simple-flask-app-in-a
RUN chmod 644 app.py
CMD [ "python", "app.py" ]