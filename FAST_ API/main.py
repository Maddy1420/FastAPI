from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def show():
    return {"message": "Hello, World!"}

@app.get("/products")
def get_products():
    return {"products": ["Laptop", "mobile", "ipad", "tablet"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload = True)
