#!/usr/bin/env bash

gunicorn_status=$(supervisorctl status  gunicorn_workers | awk '{print($2)}')

if [ $gunicorn_status == 'RUNNING' ]; then
    supervisorctl restart gunicorn_workers
elif [ $gunicorn_status != 'RESTARTING']; then
    supervisorctl start gunicorn_workers
fi
