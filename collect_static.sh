#!/usr/bin/env bash

(
    flock -n 300 || exit 1
    $XANADOU_PATH/$XANADOU_APP_NAME/manage.py collectstatic --noinput
) 300>.collect_static.lock
