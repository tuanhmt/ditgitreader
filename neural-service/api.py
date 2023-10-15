from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import uvicorn
from numpy import exp, array, random, dot
import json

app = FastAPI()


@app.get('/')
async def getHome():
    return FileResponse('index.html')

synaptic_weights = 2 * random.random((3, 1)) - 1

# Sigmoid (activation function)
def sigmoid(x):
    return 1 / (1 + exp(-x))

# Tinking: multiply inputs with weights
def think(inputs):
    return sigmoid(dot(inputs, synaptic_weights))

# Training data (we'll use these in a bit)
#train_inputs = array([[0.9, 0.1, 0.1], [0.1, 0.6, 0.2], [0.4, 0.1, 0.1], [0.6, 0.8, 0.1]])
#train_outputs = array([[1, 0, 1, 0]]).T

synaptic_weights = [10, -10, -10]

@app.post('/neural-notrain')
async def apiThink(req: Request):
    # get value
    rgb = await req.body()
    data  = json.loads(rgb)

    
    result = think(array(data))
    
    return result

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8081)