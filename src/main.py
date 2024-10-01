""" FastAPI Boilerplate Library """
import logging

import uvicorn
from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get('/hello')
async def hello() -> dict:
    """ hello world """
    return {'message': 'Hello World'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)
