FROM willhallonline/ansible:2.7-alpine-3.9

WORKDIR /ansible
COPY requirements.yml ./
RUN ansible-galaxy install -r requirements.yml
VOLUME [ "/root/.ansible/roles/" ]

COPY . .

CMD [ "./deploy.sh", "site.yml", "dev", "${PASSWORD}", "--check"]
