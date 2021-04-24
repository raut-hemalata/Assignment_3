FROM python:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PORT 8080
CMD ["main.py"]
ENTRYPOINT ["python"]
