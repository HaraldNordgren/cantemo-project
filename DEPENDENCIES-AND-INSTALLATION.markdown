#Dependencies

Install python3 and pip3

sudo -H pip3 install django
sudo -H pip3 install watchdog

compile/install ffmpeg
install google chrome

#Preparation
python3 manage.py migrate

#Run (Go to mysite, then run both in different terminals)
python3 manage.py runserver
python3 watch-folder.py

run.sh does all of this, but starts watch-folder.py as a background process that will have to be manually killed later.
