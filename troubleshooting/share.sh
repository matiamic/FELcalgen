#! /bin/bash
# make a cute zip file with this
if [ -f share.zip ]
then
    rm share.zip
fi
> felcal.ics
> felcal_collabedit.in
zip share.zip -r ../README.md ../calgen.py ../felcal.ics ../felcal.in ../generate_calendar.sh ../generate_calendar.bat ../install_env.sh ../felcal_collabedit.in ../input_url.txt ../troubleshooting

