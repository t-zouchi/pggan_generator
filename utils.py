import numpy as np
from PIL import Image

def save_image(img, filename):
    img = np.transpose(img, (1, 2, 0))
    img = img * 256
    img = img.astype(np.int32)
    img[img < 0] = 0
    img[img >= 256] = 255
    img = np.uint8(img)
    img = Image.fromarray(img)
    img.save(filename)

def save_imges_to_gif(images, filename, _duration):
    _images = []
    
    for img in images:
        img = np.transpose(img, (1, 2, 0))
        img = img * 256
        img = img.astype(np.int32)
        img[img < 0] = 0
        img[img >= 256] = 255
        img = np.uint8(img)
        img = Image.fromarray(img)
        _images.append(img)
        
    _images[0].save(filename,save_all=True, append_images=_images[1:], optimize=False, duration=_duration, loop=0)    
