#!/usr/bin/env bash

(
    flock -n 300 || exit 1
    $XANADOU_PATH/$XANADOU_APP_NAME/manage.py collectstatic --noinput

    #Sometime the watchemedo generate zombies, cleaning it up
    kill -HUP $(ps -A -ostat,ppid |  awk '/[zZ]/{print $2}')
) 300>.collect_static.lock
