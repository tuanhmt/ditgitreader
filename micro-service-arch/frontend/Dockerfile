FROM python:3.10.12-slim

WORKDIR /app

COPY api/api.py .
COPY api/handwriting.keras .
COPY index.html .

RUN pip install tensorflow numpy mnist keras fastapi "uvicorn[standard]" Pillow

EXPOSE 8081
CMD [ "python3","api.py"]