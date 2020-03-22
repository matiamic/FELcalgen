#! /bin/bash
if [ ! -d calgen_env ]
then
    ./install_env.sh
fi

if [ ! -d calgen_env ]
then
    exit 1
fi
source calgen_env/bin/activate
source calgen_env/bin/activate
clear
python3 calgen.py
deactivate

