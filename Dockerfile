FROM python:2.7.14
COPY app /app
RUN pip install --no-cache-dir boto3 flask
CMD ["python", "/app/app.py"]