from fastapi import FastAPI
from .test import tr
# Create an instance of the FastAPI class
app = FastAPI()

# Define a route using a decorator, which specifies the HTTP method and endpoint path
@app.get("/")
def read_root():
    tr()
    return {"message": "Hello, FastAPI"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="127.0.0.1", port=8000)