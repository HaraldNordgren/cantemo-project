#!/usr/bin/env bash

im=spagett.gif
stored_im=stored-images/$im

mv $stored_im $im
mv $im $stored_im
