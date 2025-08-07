    FROM python:3.12.0-slim-bookworm

    ENV PYTHONBUFFERED=1
    ENV PYTHONWRITEBYTECODE=1

    ENV DJANGO_SUPERUSER_USERNAME=root
    ENV DJANGO_SUPERUSER_EMAIL=root@root.com
    ENV DJANGO_SUPERUSER_PASSWORD=root
    ENV APP=/app

    # Change the workdir.
    WORKDIR $APP

    # Install the requirements
    COPY requirements.txt $APP

    RUN pip3 install -r requirements.txt

    # Copy the rest of the files
    COPY . $APP

    # Copy sqlite database
    RUN python3 manage.py makemigrations
    RUN python3 manage.py migrate --run-syncdb
    RUN python3 manage.py createsuperuser --no-input

    EXPOSE 8000

    RUN chmod +x /app/entrypoint.sh

    ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

    CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]