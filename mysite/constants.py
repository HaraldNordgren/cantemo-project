from django.conf import settings

watched_folder = settings.STATIC_URL.lstrip("/") + "/stored-images"
