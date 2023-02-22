import logging
from pathlib import Path
from typing import List

from clip_interrogator import Config, Interrogator
from PIL import Image

logging.basicConfig(format='%(name)s-%(levelname)s|%(lineno)d:  %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

import contextlib
import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Image to Text Service",
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
    app.state.interrogator = ci


@app.get('/')
def root():
    return {'message': "we're up!"}


@app.post('/')
async def convert_image_to_text(file: UploadFile= File()):
    file_suffix_is_img = (file.filename or "").split('.')[-1] in ('jpg','png')
    if not file_suffix_is_img:
        raise HTTPException(400, 'The file must be either a .jpg or .png file')
    
    file_obj = file.file
    try:
        image = Image.open(file_obj).convert('RGB')
        image_text = app.state.interrogator.interrogate_fast(image)
        return {file.filename: image_text}
    except:
        log.exception('Exception while trying to run CLIP on an image')
        raise HTTPException(500, 'An error occured while processing the file')
        
    
    
    

    
    
