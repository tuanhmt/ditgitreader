from python:3.10.12-slim

WORKDIR /app

COPY ./ .

RUN pip install numpy fastapi "uvicorn[standard]"

EXPOSE 8081
CMD [ "python3","api.py" ]