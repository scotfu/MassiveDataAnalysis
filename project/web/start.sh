#! /bin/bash
uwsgi --socket 127.0.0.1:8000 --wsgi-file wsgi.py --callable app --master --processes 4 --threads 2 

