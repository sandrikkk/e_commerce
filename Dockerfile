FROM python:3.11

WORKDIR /app

COPY requirements/dev.txt /app/requirements/
RUN pip install -r requirements/dev.txt

COPY scripts/docker-entrypoint.sh /app/scripts/
COPY scripts/check_service.py /app/scripts/
RUN chmod +x /app/scripts/docker-entrypoint.sh


ENTRYPOINT ["sh","/app/scripts/docker-entrypoint.sh"]

EXPOSE 8000
