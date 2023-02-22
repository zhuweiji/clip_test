FROM python:3.10.0-slim

WORKDIR /app

RUN pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu117
RUN pip install clip-interrogator==0.5.4

COPY . .

ENTRYPOINT poetry run start
