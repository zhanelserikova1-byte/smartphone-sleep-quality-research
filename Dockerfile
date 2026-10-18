FROM python:3.12.3-slim
WORKDIR /app
COPY configs/ ./configs/
COPY data/sample/ ./data/sample/
COPY src/ ./src/
RUN mkdir -p results
CMD ["python", "src/benchmark.py"]
