from fastapi import FastAPI

from app.routes.user_routes import router as user_router
from app.routes.category_routes import router as category_router
from app.routes.product_routes import router as product_router
from app.routes.order_routes import router as order_router
from app.routes.aggregation_routes import router as aggregation_router

app = FastAPI(title="E-Commerce MongoDB API")


app.include_router(user_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(aggregation_router)

@app.get("/")
def root():
    return {"message": "API Running Successfully 🚀"}