#Dependencies

sudo -H pip3 install django
sudo -H pip3 install watchdog

compile/install ffmpeg
install google chrome

#Preparation
python3 manage.py migrate

#Run
##Go to mysite, then run both in different terminals
python3 manage.py runserver
./watch-folder.py
