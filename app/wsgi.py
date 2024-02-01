"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()


#Rodar Servidor 
# uwsgi --http :8000 --module app.wsgi --static-map /static=/var/www/study_project_cars/static/ --chmod-socket=666

#Rodar Servidor Nginx

# uwsgi --socket /var/www/study_project_cars/carros.sock --module app.wsgi --chmod-socket=666

# Rodar Servidor Nginx com o carros_uwsgi que criou no raiz
# uwsgi --ini carros_uwsgi.ini

# Reiniciar sudo systemctl restart nginx

# a configuração do nginx fica em  /etc/nginx/sites-available/


