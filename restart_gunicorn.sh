#!/usr/bin/env bash

(
    flock -n 200 || exit 1
    gunicorn_status=$(supervisorctl status  gunicorn_workers | awk '{print($2)}')

    if [ $gunicorn_status == 'RUNNING' ]; then
        supervisorctl restart gunicorn_workers
    elif [ $gunicorn_status != 'RESTARTING']; then
        supervisorctl start gunicorn_workers
    fi
) 200>.gunicorn_reload.lock
