# hell.ansible.ui

## Getting Started

```shell
docker compose up -d ui
```

Hit [http://localhost:5000/playbook] to see the Flask App (`ui`) run an Ansible container (`ansible`) executing a playbook on container `myhost` using `docker compose`.

```shell
$ curl http://localhost:5000/playbook
Starting work_myhost_1 ...
Starting work_myhost_1 ... done
Creating _work_ansible_run ...
Creating _work_ansible_run ... done
+ PLAYBOOK=site.yml
+ INVENTORY=dev
+ PASSWORD=password
+ shift
+ true
+ shift
+ true
+ shift
+ true
+ other_args=
+ ansible-galaxy install -r requirements.yml
Starting galaxy role install process
- robertdebock.bootstrap (master) is already installed, skipping.
+ sshpass -p password ansible-playbook -i inventories/dev site.yml --extra-vars 'ansible_become_pass=password' -k

PLAY [Prepare system to be managed by Ansible] *********************************
TASK [robertdebock.bootstrap : test if bootstrap_user is set correctly] ********
...
PLAY [Update application] ******************************************************
...
PLAY RECAP *********************************************************************
myhost : ok=15 changed=2 unreachable=0 failed=0 skipped=4 rescued=1 ignored=0
```

## Local Development

Install dependencies

```shell
cd ./ui
npm ci
pip install -r requirements.txt -r requirements-dev.txt
```

Update dependencies with [pip-update-requirements (pur)](https://github.com/alanhamlett/pip-update-requirements), i.e.

```shell
pur -r requirments.txt
pur -r requirements-dev.txt
```

Run the app in development mode

```console
python app.py
```

Run tests & coverage

```bash
python -m coverage run -m pytest
python -m coverage report
python -m coverage html
# See generated html report in ./htmlcov/index.html
```
