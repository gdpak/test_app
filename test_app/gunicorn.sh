#!/bin/bash

NAME="test_app"
USER=nginx
GROUP=nginx
LOG_LEVEL=debug
NUM_WORKERS=4

DJANGO_WSGI_MODULE=test_app.wsgi
DJANGO_SETTINGS_MODULE=test_app.settings
DJANGODIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))
PROJECTDIR=$(readlink -f $(dirname ${DJANGODIR}))

TLS_CRT=$PROJECTDIR/ssl/server.crt
TLS_KEY=$PROJECTDIR/ssl/server.key
PIDFILE=$PROJECTDIR/run/gunicorn.pid
SOCKFILE=$PROJECTDIR/run/gunicorn.sock
ERRORLOG=$PROJECTDIR/logs/gunicorn-error.log
ACCESSLOG=$PROJECTDIR/logs/gunicorn-access.log

echo "Starting $NAME"
cd $DJANGODIR
source $PROJECTDIR/virtualenv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --pid            $PIDFILE       \
  --bind           unix:$SOCKFILE \
  --name           $NAME          \
  --user           $USER          \
  --group          $GROUP         \
  --workers        $NUM_WORKERS   \
  --log-file       $ERRORLOG      \
  --log-level      $LOG_LEVEL     \
  --access-logfile $ACCESSLOG     \
  --timeout        6000
