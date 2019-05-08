import flask
import os
from command import Command

app = flask.Flask(__name__)

#COMMAND = ['/bin/sh', './deploy.sh', 'site.yml', 'dev']
# detect win/linux: https://stackoverflow.com/questions/4719063/can-python-detect-which-os-is-it-running-under
COMMAND = 'ping -n 10 www.google.de' if os.name == 'nt' else 'ping -c 10 www.google.de'
WORKING_DIR = '/ansible'


@app.route('/playbook')
def index():
    # text/html is required for most browsers to show th$
    return flask.Response(Command.run(COMMAND), mimetype='text/html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
