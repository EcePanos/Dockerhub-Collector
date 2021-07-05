FROM python:3.9.6-buster

WORKDIR /usr/src/app
RUN mkdir data

COPY ./main.py ./counter.py ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]
