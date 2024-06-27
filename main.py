from fastapi import FastAPI
import uvicorn
from views.views import router as router_view

app = FastAPI()
app.include_router(router_view)


@app.get("/")
def root():
    return {"message": "Hello World", "Available sections": "/api"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
