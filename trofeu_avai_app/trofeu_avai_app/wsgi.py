
import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(
    0, '/home/diegocosta/webapps/trofeu_avai/env/lib/python3.5/site-packages')
sys.path.append('/home/diegocosta/webapps/trofeu_avai')
sys.path.append('/home/diego_costa/webapps/trofeu_avai/trofeu_avai')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trofeu_avai_app.settings")

application = get_wsgi_application()
