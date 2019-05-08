import flask
import os
from command import Command

app = flask.Flask(__name__)

# detect win/linux: https://stackoverflow.com/questions/4719063/can-python-detect-which-os-is-it-running-under
if os.name == 'nt':
    COMMAND = 'ping -n 10 www.google.de' if os.name == 'nt' else 'ping -c 10 www.google.de'
    WORKING_DIR = '.'
else:
    COMMAND = 'docker-compose run --rm ansible ./deploy.sh'
    WORKING_DIR = '/_work'


@app.route('/playbook')
def index():
    # text/html is required for most browsers to show th$
    return flask.Response(Command.run(COMMAND, WORKING_DIR), mimetype='text/html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
