A repository to run CLIP Interrogator, a ML model that given an image, reverse engineers prompts to generate that image.
We use it to perform keyword generation for images as a proxy for the textual summarisation of the contents of an image.

Most of the code is from the clip-interrogator repo https://github.com/pharmapsychotic/clip-interrogator

This repository and the docker image it produces is used as a service by the textrank project.

### For Developers:
Since installing torch and torchvision is a PITA, run the following commands in your preferred python venv to install dependencies

1. pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu117
2. pip install clip-interrogator==0.5.4
