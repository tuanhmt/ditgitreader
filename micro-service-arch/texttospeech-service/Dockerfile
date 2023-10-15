FROM python:3.10-alpine


WORKDIR /app

COPY api.py .

RUN pip install boto3 fastapi "uvicorn[standard]" Pillow

EXPOSE 8080
CMD [ "python3","api.py"]