import lib.logic as wiki_logic
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}

@app.get("/search/{name}")
async def search(name: str):
    """Term to search in wikipedia"""
    return {"result": wiki_logic.search_wiki(name)}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Search wiki"""
    return {"result": wiki_logic.wiki(name)}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')