FROM python:3

RUN curl -sSL https://github.com/openfaas/faas/releases/download/0.6.11/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog
WORKDIR /root/

COPY requirements.txt   .
RUN pip install -r requirements.txt
COPY *.py .
ENV write_debug=true
ENV read_debug=true

# Web UI info
# https://docs.locust.io/en/latest/running-locust-without-web-ui.html

# 100 total users (eventually)
# Add 10 users every second (10 secs until full speed)
# 1000 requests total.

ENV fprocess="xargs locust --no-web -c 100 -r 10 -n 1000 --host"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
