#!/usr/bin/env bash

cd mysite

python3 watch-folder.py &
python3 manage.py runserver
