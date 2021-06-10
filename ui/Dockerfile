FROM docker/compose:alpine-1.29.2 as base

ENV PYTHONUNBUFFERED=1
# hadolint ignore=DL3042,DL3018,DL3013
RUN echo "**** install Python ****" && \
  apk add --no-cache python3 && \
  if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
  \
  echo "**** install pip ****" && \
  python3 -m ensurepip && \
  rm -r /usr/lib/python*/ensurepip && \
  pip3 install --no-cache --upgrade pip setuptools wheel && \
  if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
ENTRYPOINT [ ]

#--- test ----------------------------------------------------------------------
FROM python:3.9.5-slim-buster as test
WORKDIR /usr/src/app
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt
COPY . .
RUN coverage run -m pytest && coverage report

#--- final ----------------------------------------------------------------------
FROM base as final
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# cf.: https://askubuntu.com/questions/117359/how-do-i-change-the-timezone-to-utc
ENV TZ UTC
ENV FLASK_DEBUG '0'

EXPOSE 5000
ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]
