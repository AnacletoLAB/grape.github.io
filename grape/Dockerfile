FROM python:3.7

ENV PORT 8000
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# RUN python -m manage test

# TODO: Implement container logging
# CMD touch /opt/microservices/microservice.log && \
#    tail -f /opt/microservices/microservice.log & \

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 wsgi:app