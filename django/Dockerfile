FROM python:3.12-alpine AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile --system

# Copy project
COPY . /app/


FROM base AS development

# Install development dependencies
RUN pipenv install --deploy --ignore-pipfile --dev --system


FROM base AS production

WORKDIR /app

ENV ENV prod

# Install production dependencies
COPY ./prod-requirements.txt /app/prod-requirements.txt
RUN pip install -r prod-requirements.txt

RUN chmod +x ./entrypoint.sh

# Run entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM base AS static

# Collect static files
RUN python manage.py collectstatic --noinput


FROM nginx:1.21-alpine AS nginx

# Copy nginx configuration
COPY ./nginx/templates/ /etc/nginx/templates/

# Copy static files
COPY --from=static /app/static /app/static
