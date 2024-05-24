FROM python:latest

WORKDIR /app

COPY requirments.txt ./
COPY ./src ./src

RUN pip install -r requirments.txt

EXPOSE 8000

CMD ["uvicorn", "src.server.main:app", "--host", "0.0.0.0", "--port", "8000"]