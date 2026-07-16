# Test Cases

## User APIs

### TC-01: Create User

**Endpoint:** `POST /users`

**Request Body**

```json
{
  "name": "Adarsh",
  "email": "Adarsh@example.com",
  "phone": "9000200020",
  "city": "Greater Noida"
}
```

**Result**

```json
{
  "message": "User created successfully",
  "user_id": "6a587fbd3f16cfde6eab3bf5"
}
```

---

### TC-02: Get All Users

**Endpoint:** `GET /users`

**Result**

```json
[
  {
    "_id": "6a587505324197059a06519e",
    "name": "Tanya Mishra",
    "email": "tanya@gmail.com",
    "phone": "9876543210",
    "city": "Noida",
    "created_at": "2026-07-16T06:07:01.402000"
  },
  {
    "_id": "6a587505324197059a06519f",
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "phone": "9876543211",
    "city": "Delhi",
    "created_at": "2026-07-16T06:07:01.402000"
  },
  {
    "_id": "6a587505324197059a0651a0",
    "name": "Anjali Verma",
    "email": "anjali@gmail.com",
    "phone": "9876543212",
    "city": "Lucknow",
    "created_at": "2026-07-16T06:07:01.402000"
  },
  {
    "_id": "6a5879c81dabd87341f5139e",
    "name": "Tanya",
    "email": "tanya@example.com",
    "phone": "232223",
    "city": "Indirapuram",
    "created_at": "2026-07-16T06:27:20.865000"
  },
  {
    "_id": "6a587fbd3f16cfde6eab3bf5",
    "name": "Adarsh",
    "email": "Adarsh@example.com",
    "phone": "9000200020",
    "city": "Greater Noida",
    "created_at": "2026-07-16T06:52:45.704000"
  }
]
```

---

## Category APIs

### TC-03: Create Category

**Endpoint:** `POST /categories`

**Request Body**

```json
{
  "name": "Skates",
  "description": "stylish roller skates"
}
```

**Result**

```json
{
  "category_id": "6a5880263f16cfde6eab3bf6"
}
```


---

### TC-04: Get All Categories

**Endpoint:** `GET /categories`

**Result**

```json
[
  {
    "_id": "6a587505324197059a065198",
    "name": "Electronics",
    "description": "Electronic gadgets"
  },
  {
    "_id": "6a587505324197059a065199",
    "name": "Fashion",
    "description": "Clothing and accessories"
  },
  {
    "_id": "6a587505324197059a06519a",
    "name": "Books",
    "description": "Books and stationery"
  },
  {
    "_id": "6a5879eb1dabd87341f5139f",
    "name": "Books",
    "description": "a new book"
  },
  {
    "_id": "6a5879eb1dabd87341f513a0",
    "name": "Books",
    "description": "a new book"
  },
  {
    "_id": "6a5880263f16cfde6eab3bf6",
    "name": "Skates",
    "description": "stylish roller skates"
  }
]
```

---

## Product APIs

### TC-05: Create Product

**Endpoint:** `POST /products`

**Request Body**

```json
{
  "name": "Roller Skates",
  "brand": "TamSkates",
  "price": 2000,
  "stock": 10,
  "category_id": "6a5880263f16cfde6eab3bf6"
}
```

**Result**

```json
{
  "message": "Product created successfully",
  "product_id": "6a5881333f16cfde6eab3bf7"
}
```

---

### TC-06: Get All Products

**Endpoint:** `GET /products`

**Result**

```json
[
  {
    "_id": "6a587505324197059a06519b",
    "name": "MacBook Air M2",
    "brand": "Apple",
    "price": 95000,
    "stock": 15,
    "category_id": "6a587505324197059a065198"
  },
  {
    "_id": "6a587505324197059a06519c",
    "name": "Nike Shoes",
    "brand": "Nike",
    "price": 6000,
    "stock": 30,
    "category_id": "6a587505324197059a065199"
  },
  {
    "_id": "6a587505324197059a06519d",
    "name": "Atomic Habits",
    "brand": "Penguin",
    "price": 550,
    "stock": 100,
    "category_id": "6a587505324197059a06519a"
  },
  {
    "_id": "6a5881333f16cfde6eab3bf7",
    "name": "Roller Skates",
    "brand": "TamSkates",
    "price": 2000,
    "stock": 10,
    "category_id": "6a5880263f16cfde6eab3bf6"
  }
]
```
---

## Order APIs

### TC-07: Create Order

**Endpoint:** `POST /orders`

**Request Body**

```json
{
  "user_id": "6a5879c81dabd87341f5139e",
  "product_id": "6a5881333f16cfde6eab3bf7",
  "quantity": 1,
  "total_amount": 2000,
  "status": "Delivered"
}
```

**Result**

```json
{
  "message": "Order created successfully",
  "order_id": "6a58824c3f16cfde6eab3bf8"
}
```

---

### TC-08: Get All Orders

**Endpoint:** `GET /orders`

**Expected Result**

```json
[
  {
    "_id": "6a587505324197059a0651a1",
    "user_id": "6a587505324197059a06519e",
    "product_id": "6a587505324197059a06519b",
    "quantity": 1,
    "total_amount": 95000,
    "status": "Delivered",
    "order_date": "2026-07-16T06:07:01.419000"
  },
  {
    "_id": "6a587505324197059a0651a2",
    "user_id": "6a587505324197059a06519e",
    "product_id": "6a587505324197059a06519d",
    "quantity": 2,
    "total_amount": 1100,
    "status": "Delivered",
    "order_date": "2026-07-16T06:07:01.419000"
  },
  {
    "_id": "6a587505324197059a0651a3",
    "user_id": "6a587505324197059a06519f",
    "product_id": "6a587505324197059a06519c",
    "quantity": 1,
    "total_amount": 6000,
    "status": "Processing",
    "order_date": "2026-07-16T06:07:01.419000"
  },
  {
    "_id": "6a587505324197059a0651a4",
    "user_id": "6a587505324197059a0651a0",
    "product_id": "6a587505324197059a06519d",
    "quantity": 3,
    "total_amount": 1650,
    "status": "Delivered",
    "order_date": "2026-07-16T06:07:01.419000"
  },
  {
    "_id": "6a58824c3f16cfde6eab3bf8",
    "user_id": "6a5879c81dabd87341f5139e",
    "product_id": "6a5881333f16cfde6eab3bf7",
    "quantity": 1,
    "total_amount": 2000,
    "status": "Delivered"
  }
]
```

---

# Aggregation APIs

### TC-09: User Order History

**Endpoint:** `GET /aggregation/user-orders`

**Result**
```json
[
  {
    "name": "Tanya Mishra",
    "email": "tanya@gmail.com",
    "city": "Noida",
    "orders": [
      {
        "quantity": 1,
        "total_amount": 95000,
        "status": "Delivered"
      },
      {
        "quantity": 2,
        "total_amount": 1100,
        "status": "Delivered"
      }
    ]
  },
  {
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "city": "Delhi",
    "orders": [
      {
        "quantity": 1,
        "total_amount": 6000,
        "status": "Processing"
      }
    ]
  },
  {
    "name": "Anjali Verma",
    "email": "anjali@gmail.com",
    "city": "Lucknow",
    "orders": [
      {
        "quantity": 3,
        "total_amount": 1650,
        "status": "Delivered"
      }
    ]
  },
  {
    "name": "Tanya",
    "email": "tanya@example.com",
    "city": "Indirapuram",
    "orders": [
      {
        "quantity": 1,
        "total_amount": 2000,
        "status": "Delivered"
      }
    ]
  },
  {
    "name": "Adarsh",
    "email": "Adarsh@example.com",
    "city": "Greater Noida",
    "orders": []
  }
]
```

---

### TC-10: Product Category Details

**Endpoint:** `GET /aggregation/product-category`

**Result**
```json
[
  {
    "brand": "Apple",
    "price": 95000,
    "stock": 15,
    "product_name": "MacBook Air M2",
    "category_name": "Electronics",
    "category_description": "Electronic gadgets"
  },
  {
    "brand": "Nike",
    "price": 6000,
    "stock": 30,
    "product_name": "Nike Shoes",
    "category_name": "Fashion",
    "category_description": "Clothing and accessories"
  },
  {
    "brand": "Penguin",
    "price": 550,
    "stock": 100,
    "product_name": "Atomic Habits",
    "category_name": "Books",
    "category_description": "Books and stationery"
  },
  {
    "brand": "TamSkates",
    "price": 2000,
    "stock": 10,
    "product_name": "Roller Skates",
    "category_name": "Skates",
    "category_description": "stylish roller skates"
  }
]
```
---

### TC-11: User Purchase Summary

**Endpoint:** `GET /aggregation/user-purchase-summary`

**Result**

```json
[
  {
    "name": "Tanya Mishra",
    "email": "tanya@gmail.com",
    "total_orders": 2,
    "total_spent": 96100
  },
  {
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "total_orders": 1,
    "total_spent": 6000
  },
  {
    "name": "Anjali Verma",
    "email": "anjali@gmail.com",
    "total_orders": 1,
    "total_spent": 1650
  },
  {
    "name": "Tanya",
    "email": "tanya@example.com",
    "total_orders": 1,
    "total_spent": 2000
  },
  {
    "name": "Adarsh",
    "email": "Adarsh@example.com",
    "total_orders": 0,
    "total_spent": 0
  }
]
```

---