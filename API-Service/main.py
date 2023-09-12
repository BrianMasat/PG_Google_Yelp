from typing import Union
from fastapi import FastAPI, Response
from functions import get_recommendations

app = FastAPI(title='Google & Yelp API',
              description='Proyecto Grupal',
              version='1.0.0')

# Test request
@app.get('/')
async def root():
    return Response(content='<h2 style="text-align: center">Respuesta de API Google & Yelp exitosa</h2>', media_type='text/html')

app = FastAPI()

@app.get("/recommendations/{user_id}")
def get_recs(user_id: int):
    try:
        result = get_recommendations(user_id)
        return result
    except Exception as e:
        return {"error": str(e)}