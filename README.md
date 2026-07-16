# E-Commerce MongoDB Backend API

**Week 9 Assignment**

A FastAPI backend application integrated with MongoDB that demonstrates CRUD operations and MongoDB Aggregation Framework using `$lookup`. The project follows a layered architecture with separate Routes, Services, Repositories, and Database modules.

---

## Objectives

- Connect MongoDB with a FastAPI backend.
- Implement CRUD APIs for multiple collections.
- Demonstrate MongoDB Aggregation Framework.
- Use `$lookup` to perform joins between collections.

---

## Tech Stack

- FastAPI
- MongoDB
- PyMongo
- Pydantic
- Python
- Uvicorn

---

## Project Structure

```text
ecommerce-mongodb/
│
├── app/
│   ├── database/
│   │   └── connection.py
│   │
│   ├── repositories/
│   │   ├── aggregation_repository.py
│   │   ├── category_repository.py
│   │   ├── order_repository.py
│   │   ├── product_repository.py
│   │   └── user_repository.py
│   │
│   ├── routes/
│   │   ├── aggregation_routes.py
│   │   ├── category_routes.py
│   │   ├── order_routes.py
│   │   ├── product_routes.py
│   │   └── user_routes.py
│   │
│   ├── schemas/
│   │   ├── category_schema.py
│   │   ├── order_schema.py
│   │   ├── product_schema.py
│   │   └── user_schema.py
│   │
│   ├── services/
│   │   ├── aggregation_service.py
│   │   ├── category_service.py
│   │   ├── order_service.py
│   │   ├── product_service.py
│   │   └── user_service.py
│   │
│   ├── utils/
│   │   └── serializer.py
│   │
│   ├── database/
│   ├── seed.py
│   └── main.py
│
├── .env
├── requirements.txt
├── TEST_CASES.md
└── README.md
```

---

## Database Collections

The application uses four MongoDB collections:

- Users
- Categories
- Products
- Orders

### Collection Relationships

```text
Users
   │
   │ user_id
   ▼
Orders
   ▲
   │ product_id
Products
   ▲
   │ category_id
Categories
```

MongoDB references (`ObjectId`) are used to establish relationships between collections.

---

## API Endpoints

### Users

| Method | Endpoint |
|---------|----------|
| POST | `/users` |
| GET | `/users` |

### Categories

| Method | Endpoint |
|---------|----------|
| POST | `/categories` |
| GET | `/categories` |

### Products

| Method | Endpoint |
|---------|----------|
| POST | `/products` |
| GET | `/products` |

### Orders

| Method | Endpoint |
|---------|----------|
| POST | `/orders` |
| GET | `/orders` |

---

## Aggregation APIs

### 1. User Order History

**Endpoint**

```
GET /aggregation/user-orders
```

**Collections Used**

- Users
- Orders

**Aggregation Stages**

- `$lookup`
- `$project`
- `$map`

---

### 2. Product Category Details

**Endpoint**

```
GET /aggregation/product-category
```

**Collections Used**

- Products
- Categories

**Aggregation Stages**

- `$lookup`
- `$unwind`
- `$project`

---

### 3. User Purchase Summary

**Endpoint**

```
GET /aggregation/user-purchase-summary
```

**Collections Used**

- Users
- Orders

**Aggregation Stages**

- `$lookup`
- `$project`
- `$size`
- `$sum`

---

## Features

- MongoDB integration with FastAPI
- Layered project architecture
- CRUD operations
- MongoDB Aggregation Framework
- `$lookup` joins across collections
- Seed script for sample data
- JSON serialization for MongoDB ObjectIds
- Swagger API documentation

---

## Testing

Test cases are documented in:

```
TEST_CASES.md
```

The project includes:

- CRUD API test cases
- Aggregation API test cases
- Validation test cases
- Negative test cases

---

## Assignment Deliverables

- MongoDB connected with FastAPI
- CRUD APIs for all collections
- Three aggregation queries using `$lookup`
- Seed script
- Test cases
- Debug logging
- AI usage log
- Project documentation

---

## Author

**Tanya Mishra**

**Week 9 Assignment**