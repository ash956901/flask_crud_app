FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "run.py"]
EXPOSE 5002
EXPOSE 5000
