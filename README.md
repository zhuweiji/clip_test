A repository to run a web server to serve a CLIP Interrogator, a ML model that given an image, reverse engineers prompts to generate that image.
We use it to perform keyword generation for images as a proxy for the textual summarisation of the contents of an image.

Most of the code is from the clip-interrogator repo https://github.com/pharmapsychotic/clip-interrogator

This repository and the docker image it produces is used as a service by the textrank project.

When running either clip_test/main.py or the container, a webserver is provided on port 8000 that has two endpoints:
GET / : returns a message indicating the server is up
POST / : takes an image file called file and returns the text from the image


## For Developers:

### Using a Docker Container

For the easiest experience:

Pull and run the docker image. 

However, the image size is ~6GB because of the CLIP model size. The performance is also quite a bit (~5-10x?) slower running in the container.

The docker hub link: https://hub.docker.com/repository/docker/zhuweiji/clip-web-server/general


### Running locally

Since installing torch and torchvision is a PITA, run the following commands in your preferred python venv to install dependencies

1. pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu117
2. pip install clip-interrogator==0.5.4
3. pip install fastapi[all]
4. pip install python-multipart

Run `uvicorn clip_test.main:app --port 8000 --host 0.0.0.0` to serve on 0.0.0.0:8000