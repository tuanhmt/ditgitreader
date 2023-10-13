from python:3.10.12-slim

WORKDIR /app

COPY ./ .

RUN pip install tensorflow numpy mnist keras fastapi "uvicorn[standard]" Pillow

EXPOSE 8080
CMD [ "python3","api.py" ]