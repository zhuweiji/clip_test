from pathlib import Path

from clip_interrogator import Config, Interrogator
from PIL import Image

IMG_DIR = Path(__file__).parents[1] / 'data' / 'imgs'

assert IMG_DIR.is_dir()

files = [p for p in IMG_DIR.glob(r'*') if p.suffix in ('.jpg','.png') ]

ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))

results = {}

for file in files:
    image = Image.open(file).convert('RGB')
    image_text = ci.interrogate_fast(image)
    results[file] = image_text
    
print(results)