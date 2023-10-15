from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from keras import models
import uvicorn
import time
import numpy
from PIL import Image
import os

model = models.load_model('handwriting.keras')

app = FastAPI()


@app.get('/')
async def getHome():
    return FileResponse('../index.html')

def convertImage(dst):
    pic = numpy.asarray(Image.open(dst).convert('L').resize((28, 28)), float)
    return pic

@app.post('/read-image')
async def readImage(req: Request):
    # save uploaded file
    content = await req.body()
    dst = str(time.time())+'.png'
    fo = open(dst, 'wb')
    fo.write(content)
    fo.close()

    # convert image
    pic = convertImage(dst)

    # transform image
    pic = numpy.expand_dims(pic, axis=0)
    pic = (pic/255)-0.5
    pic = numpy.expand_dims(pic, axis=3)

    # predict image
    predictions = model.predict(pic)
    label = numpy.argmax(predictions)

    # delete image
    os.remove(dst)
    return str(label)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8081)