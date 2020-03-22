pip3 install virtualenv
virtualenv calgen_env
cd calgen_env
cd Scripts
activate.bat
cd ..
cd ..
pip install ics requests
cls
python3 calgen.py
deactivate

