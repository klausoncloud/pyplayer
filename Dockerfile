From python:3

WORKDIR /usr/src/app
EXPOSE 80

COPY player.py ./
COPY playerinterface.py ./
COPY playerservice.py ./

RUN pip install --no-cache-dir Flask
RUN pip install --no-cache-dir Flask-API

ENV FLASK_APP playerservice.py
CMD ["python",  "playerservice.py"]