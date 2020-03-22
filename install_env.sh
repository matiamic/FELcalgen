#! /bin/bash
pip3 install virtualenv
virtualenv calgen_env
source calgen_env/bin/activate
pip install ics requests
deactivate

