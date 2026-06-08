#!/bin/sh

echo "Aplicando migrations..."
python manage.py migrate

echo "Iniciando servidor..."
python manage.py runserver 0.0.0.0:8000