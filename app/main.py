from fastapi import FastAPI
from urls.views import router as url_router

app = FastAPI(title="Scalable URL Shortener")

app.include_router(url_router)

@app.get("/")
def root():
    return {"message": "🚀 URL Shortener is up and running!"}

@app.get("/my-urls")
def get_all():
    return {"message": "List of the urls which I have created"}

@app.get("/create-new-shortened-url")
def create_new():
    return {"message": "shortened the url and returned the shortened one"}

