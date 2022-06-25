FROM python:3.6
COPY . /appdir
WORKDIR /appdir
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]