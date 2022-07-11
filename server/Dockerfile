FROM python:3.8
# Alternatively you can use different tags from https://hub.docker.com/r/nginx/unit
WORKDIR /backend

COPY ./backend/requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

# server/backend/requirements.txt
COPY . /backend/server

EXPOSE 8080
# 
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]