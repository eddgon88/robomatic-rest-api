# Dockerfile
FROM python:3.8.10
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
EXPOSE 5002
CMD ["run.py"]