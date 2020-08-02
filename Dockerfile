FROM python:3.8.5

MAINTAINER WESLEI VARJAO <weslei.varjao@gmail.com>
ENV FLASK_APP=health.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app /app
COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
