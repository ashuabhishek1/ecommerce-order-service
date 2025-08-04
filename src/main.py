from fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from typing import List

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///order.db"
engine = sa.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Pydantic models
class OrderItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    order_id: str
    customer_id: str
    total: float
    status: str
    created_at: str

# API endpoints
@app.post("/order")
async def place_order(customer_id: str):
    with SessionLocal() as session:
        order_id = "some_order_id"  # Generate UUID in production
        session.execute(
            sa.text("INSERT INTO orders (order_id, customer_id, total, status) VALUES (:order_id, :customer_id, 0, 'Pending')"),
            {"order_id": order_id, "customer_id": customer_id}
        )
        session.commit()
    return {"order_id": order_id}

@app.post("/order/{order_id}/tax")
async def apply_tax(order_id: str):
    return {"tax": 10.0}  # Placeholder

# Event publishing
def publish_order_placed(order_id: str, customer_id: str):
    pass