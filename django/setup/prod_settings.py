import os

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-40qupekaydigi_y71x+6@5w-6aiov3vz^6=v_%60)$b!qq4^tv")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "localhost").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "postgres"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": int(os.getenv("DB_PORT", "5432")),
    }
}
