FROM python:3.8
RUN pip3 install -r requirements.txt
RUN python3 db_init.py
RUN python3 app.py --port 5000

EXPOSE 5000