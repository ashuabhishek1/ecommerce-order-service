# Ecommerce Order Service

Manages order creation and processing.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Initialize database:
   ```bash
   sqlite3 order.db < config/schema.sql
   ```
3. Run the service:
   ```bash
   uvicorn src.main:app --reload
   ```

## Endpoints
- `POST /order`: Create a new order
- `POST /order/{order_id}/tax`: Apply tax to an order

## Dependencies
- Database: SQLite (replace with production DB)
- Event Bus: For OrderPlaced events
- User Service: For customer_id validation
- Product Service: For product_id validation

## Entities
- **Order**: `{order_id: Guid, customer_id: Guid, total: decimal, status: string, created_at: datetime}`
- **OrderItem**: `{product_id: Guid, quantity: int}`
