FROM python:latest
COPY nettest .
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 main.py