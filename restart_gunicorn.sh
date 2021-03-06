#!/usr/bin/env bash

(
    flock -n 200 || exit 1
    gunicorn_status=$(supervisorctl status  gunicorn_workers | awk '{print($2)}')

    if [ $gunicorn_status == 'RUNNING' ]; then
        supervisorctl restart gunicorn_workers
    elif [ $gunicorn_status != 'RESTARTING']; then
        supervisorctl start gunicorn_workers
    fi

    #Sometime the watchemedo generate zombies, cleaning it up
    kill -HUP $(ps -A -ostat,ppid |  awk '/[zZ]/{print $2}')
) 200>$XANADOU_PATH/.gunicorn_reload.lock
