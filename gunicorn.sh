#!/bin/sh
gunicorn --bind 0.0.0.0:5000 narcis_app:app