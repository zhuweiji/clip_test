FROM python:3.10.0-slim

WORKDIR /app

RUN pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu117
RUN pip install clip-interrogator==0.5.4
RUN pip install fastapi[all]
RUN pip install python-multipart

COPY . .

ENTRYPOINT uvicorn clip_test.main:app --port 8000 --host 0.0.0.0
