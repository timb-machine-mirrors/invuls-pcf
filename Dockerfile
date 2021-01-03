FROM python:3.8
ADD . /code
WORKDIR /code
RUN pip install -r requirements_unix.txt
CMD python app.py