from django.core.wsgi import get_wsgi_application

__import__('os').environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
application = get_wsgi_application()
