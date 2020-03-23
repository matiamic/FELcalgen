#! /bin/bash
pip3 install virtualenv
virtualenv calgen_env
if [ ! -d calgen_env ]
then
    echo 'PROBLEM PRI INSTALACI virtualenv'
    exit 1
fi
source calgen_env/bin/activate
pip install ics requests
deactivate

