FROM python
COPY app/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 9090
#CMD waitress-serve --port=9090 --call app:app
CMD gunicorn -b 0.0.0.0:80 app.app:server
