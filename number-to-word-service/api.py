from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import uvicorn
import inflect

app = FastAPI()


@app.get('/')
async def getHome():
    return FileResponse('index.html')

@app.post('/number-to-words')
async def apiNumberToWord(req: Request):
    inflector = inflect.engine()
    # get value
    number = await req.body()
    # Convert to words
    words = inflector.number_to_words(number)
    
    return words

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8082)