#!/bin/bash

export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_11
export ORACLE_HOME=/opt/oracle/instantclient_21_11
export PATH=$PATH:$ORACLE_HOME

# Nos vamos a la ruta donde se encuentra nuestro proyecto
cd /app
/usr/local/bin/python main.py >> /var/log/cron.log 2>&1