FROM python:3.11-slim

WORKDIR /app

COPY . .

# Set PYTHONPATH to current folder so imports like 'from app.crud import ...' work
ENV PYTHONPATH=/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
