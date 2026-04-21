from flask import Flask, abort

cars = [
    { "id":0, "make":"Toyota", "model":"Corolla", "trim":"Hybrid XLE", "price":28440 },
    { "id":1, "make":"Hyundai", "model":"Elantra", "trim":"Limited", "price":28420 },
    { "id":2, "make":"Honda", "model":"Civic", "trim":"Hybrid Sport", "price":29395 }
]

app = Flask(__name__)

@app.get("/health")
def healthcheck():
    return {
        "status": "healthy",
        "service": "cars-ms",
        "version": "v1.0.0"
    }

@app.get("/api/v1/cars")
def get_all_cars():
    return cars

@app.get("/api/v1/cars/<int:id>")
def get_car_by_id(id):
    for c in cars:
        if c["id"] == id:
            return c
    abort(404)