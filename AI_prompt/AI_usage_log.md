# AI Usage Log

## Project: E-Commerce MongoDB Backend API (Week 9 Assignment)

### Prompt:
**"How should I design a MongoDB database schema for an e-commerce application that supports aggregation using `$lookup`?"**

**AI Assistance:**
Helped design the collections, relationships, and `ObjectId` references required for efficient aggregation queries.

---

### Prompt:
**"What is the recommended FastAPI project structure for a MongoDB backend application?"**

**AI Assistance:**
Suggested a clean layered architecture using Routes, Services, Repositories, Database, Schemas, and Utilities to improve code organization and maintainability.

---

### Prompt:
**"How can I connect MongoDB to a FastAPI application using `pymongo`?"**

**AI Assistance:**
Provided guidance on configuring the MongoDB connection, environment variables, and database initialization using PyMongo.

---

### Prompt:
**"How should I implement `ObjectId` references between MongoDB collections?"**

**AI Assistance:**
Explained how to store and use `ObjectId` references between Users, Categories, Products, and Orders collections to enable `$lookup` operations.

---

### Prompt:
**"Explain the MongoDB Aggregation Framework and the use of `$lookup`, `$group`, `$match`, and `$project`."**

**AI Assistance:**
Helped understand aggregation pipelines and how different stages work together to join, filter, group, and transform data.

---

### Prompt:
**"How do I organize repositories, services, and routes for a MongoDB FastAPI project?"**

**AI Assistance:**
Provided implementation guidance for creating modular repository, service, and route layers while following separation of concerns.

---

### Prompt:
**"Create a seed script to populate MongoDB with sample data?"**

**AI Assistance:**
Generated a seed script to populate Users, Categories, Products, and Orders collections while maintaining proper `ObjectId` relationships.

---

### Prompt:
**"How do I serialize MongoDB `ObjectId` values in FastAPI responses?"**

**AI Assistance:**
Suggested implementing a reusable serializer utility to recursively convert `ObjectId` and `datetime` objects into JSON-serializable formats for API responses.

---

### Prompt:
**"How can I implement MongoDB aggregation queries in FastAPI?"**

**AI Assistance:**
Provided guidance for implementing aggregation pipelines, including User Order History, Product Category Details, and User Purchase Summary using `$lookup`, `$project`, `$unwind`, `$map`, `$size`, and `$sum`.

---
