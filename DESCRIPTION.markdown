#Descpription
I used Python and Django with the SQLite database, together with watchdog to monitor to image/video folder.

The imagebank index page shows a list of all files and two textboxes allow you to do substring search for filenames or metadata. Each listed file links to the file presentation area. Here you can edit the metadata, delete the file by click the red X, and go back to the previous screen.

The watch-folder script keeps track of files entering and leaving the watched directory. It updates the database and also performs conversion of non-mp4 videos which are then displayed instead of the original format in the web UI. Deleting the main file will also remove the converted file.

The different parts of the web UI communicate through GET and POST requests. Searching, entering meta-data or deleting a file is triggered from the html template (mysite/image_bank/templates/image_bank/index.html, mysite/image_bank/templates/image_bank/show_image.html) that send the data to the views (mysite/image_bank/views.py) that then communicates with the database and sends information back to render the new page.

I didn't see the need for three seprate database models, so the BankImage type contains all the information for a database file: path of the file, filetype, metadata and possible converted file

The watched folder is mysite/image_bank/static/stored-images. For some reason, downloading directly into that folder malfunctions, download files to another folder first, then move them to the watched folder.

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
