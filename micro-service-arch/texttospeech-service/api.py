from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import uvicorn
import boto3
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set your AWS credentials and region
aws_access_key_id = 'AKIAX3X6M7S6IQPDTIYF'
aws_secret_access_key = 'GUHRFPiPp5iTum+WSAdnq/Ks/aOqwIRtRMFCWG4w'
aws_region = 'us-east-1'  # Specify your AWS region

def readAudio(fileName):
    return FileResponse(fileName, media_type="audio/mpeg")

def textToSpeechTask(data):
    string_data = data.decode('utf-8')
    # Text to be converted to speech
    text = "Hello, this is a test of Amazon Polly text-to-speech service."

    # Initialize a Boto3 Polly client with credentials and region
    client = boto3.client('polly', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Request speech synthesis
    response = client.synthesize_speech(
        OutputFormat='mp3',  # Format of the output audio (other options include 'ogg_vorbis', 'pcm')
        Text=string_data,           # The text you want to convert
        VoiceId='Joanna'     # Voice to use (you can choose from various voices)
    )

    # Get the audio stream
    audio_stream = response['AudioStream'].read()
    
    randomdata = random.randint(1, 100)
    # Save the audio to a file or do further processing
    with open(str(randomdata)+"-output"+".mp3", 'wb') as f:
        f.write(audio_stream)
    
    fileName=str(randomdata)+"-output"+".mp3"
    return readAudio(fileName)






@app.post('/text-to-speech')
async def textToSpeech(req: Request):
    # save uploaded file
    content = await req.body()
    return textToSpeechTask(content)

   

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)