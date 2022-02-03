FROM python:3.9-slim-buster
MAINTAINER Craig Harman <craig@craigharman.net>
LABEL Description="Image for running a Turkle interface"

RUN apt-get update && apt-get install -y --no-install-recommends \
    cron \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/turkle

COPY requirements.txt /opt/turkle/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt && \
    pip install --no-cache-dir gunicorn whitenoise

COPY turkle /opt/turkle/turkle
COPY manage.py /opt/turkle/manage.py
COPY scripts /opt/turkle/scripts
COPY turkle_site /opt/turkle/turkle_site
COPY docker-config/create_turkle_admin.sh /opt/turkle/create_turkle_admin.sh
COPY docker-config/entrypoint.sh /usr/local/bin/entrypoint.sh

COPY docker-config/turkle.crontab /etc/cron.d/turkle
RUN crontab /etc/cron.d/turkle

ENV TURKLE_DOCKER=1
RUN python manage.py collectstatic
RUN python manage.py migrate
RUN ./create_turkle_admin.sh

VOLUME /opt/turkle

EXPOSE 8080

CMD [ "/usr/local/bin/entrypoint.sh" ]
