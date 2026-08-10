from fastapi import FastAPI, UploadFile, File
from PIL import Image
from predict import predict

app = FastAPI()

@app.get('/')
def welcome():
    return {'message':'Plant Disese Prediction Welcomes You....'}


@app.post("/predict")
async def predict_disease(file : UploadFile = File(...)):
    image = Image.open(file.file)
    disease,confidence = predict(image)

    return{
        "disease":disease,
        "confidence":confidence
    }



