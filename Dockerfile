FROM python:3.11-slim-buster

RUN \
    apt-get update && \
    apt-get install -y supervisor && \
    apt clean && \
    pip install -U pip && \
    rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    PYTHONPATH=/app/src:$PYTHONPATH

RUN ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo "Europe/Moscow" > /etc/timezone


RUN useradd -m -d /app -s /bin/bash -U user_app
    

WORKDIR /app

COPY ./requirements.txt .
COPY ./supervisord.conf /etc/supervisor/

RUN pip3 install -r requirements.txt

COPY . .

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
