FROM python:3.13.5



RUN pip install fastapi uvicorn

COPY app.py .

CMD ["python3", "app.py"]

