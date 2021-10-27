FROM python:bullseye

WORKDIR /Upload

RUN pip freeze > requirements.txt
RUN pip install flask
RUN pip install -r requirements.txt

COPY . /Upload/

EXPOSE 5050

ENTRYPOINT [ "python3" ]

CMD ["server.py"]
