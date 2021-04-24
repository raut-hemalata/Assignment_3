FROM python:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["main.py"]
ENTRYPOINT ["python"]
