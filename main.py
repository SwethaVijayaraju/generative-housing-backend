from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.layout_routes import router as layout_router

app = FastAPI()

app.include_router(layout_router)

@app.get("/")
def root():
    return JSONResponse(content={"status": "ok"}, status_code=200)
