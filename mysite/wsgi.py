"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the Python path
project_home = '/home/yourusername/mysite'  # change to your path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate your virtual environment
activate_env = '/home/yourusername/.virtualenvs/myenv/bin/activate_this.py'  # change to your venv path
with open(activate_env) as file_:
    exec(file_.read(), dict(__file__=activate_env))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()