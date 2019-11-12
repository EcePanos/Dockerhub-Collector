FROM python:3.7.5-buster

WORKDIR /usr/src/app
RUN mkdir data

COPY ./main.py ./counter.py ./requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
