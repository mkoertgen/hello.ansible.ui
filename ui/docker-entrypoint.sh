#!/bin/sh
set -e

if [ $# -eq 0 ]; then
    # TODO: docker login with secrets so we can pull/update an image (e.g. updater, might have been pruned), cf.:
    # - https://docs.docker.com/engine/swarm/secrets/#defining-and-using-secrets-in-compose-files

    # TODO: DB
    # mkdir -p ${DATA_DIR}
    # flask db upgrade

    # Start gunicorn
    gunicorn --workers=1 --threads=8 --worker-class=gthread --bind 0.0.0.0:5000 app:app
fi

exec "$@"
