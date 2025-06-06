FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

RUN python -m grpc_tools.protoc -I=src --python_out=src --grpc_python_out=src src/sentiment_analysis.proto

EXPOSE 50051

CMD ["python", "./src/server.py"]