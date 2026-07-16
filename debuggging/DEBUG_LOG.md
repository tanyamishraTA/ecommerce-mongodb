# Debug Log

## Issue 1: MongoDB Connection Error

**Problem**

The FastAPI application failed to connect to MongoDB during initial setup.

**Cause**

- Incorrect MongoDB connection string.
- MongoDB server was not running.

**Solution**

- Verified the MongoDB URI in the `.env` file.
- Started the MongoDB server.
- Confirmed successful database connection.

---

## Issue 2: PyMongo `bson` Import Conflict

**Problem**

```
ImportError: cannot import name 'SON' from 'bson'
```

**Cause**

A standalone `bson` package was installed, conflicting with the `bson` module bundled with PyMongo.

**Solution**

- Uninstalled the standalone `bson` package.
- Removed the corrupted PyMongo installation.
- Reinstalled PyMongo using:

```bash
pip uninstall bson
pip uninstall pymongo
pip install pymongo
```

---

## Issue 3: ObjectId Serialization Error

**Problem**

```
TypeError: 'ObjectId' object is not iterable
```

**Cause**

MongoDB `ObjectId` values cannot be directly serialized into JSON by FastAPI.

**Solution**

Implemented a custom serializer utility (utils/serializer.py) to recursively convert:

- `ObjectId` → String
- `datetime` → ISO formatted string

This utility was reused across all CRUD and aggregation APIs.

---

## Issue 4: Aggregation Response Contained Unnecessary Fields

**Problem**

The initial aggregation response returned internal fields such as:

- `_id`
- `user_id`
- `product_id`
- `created_at`

**Cause**

Only `$lookup` was used in the aggregation pipeline.

**Solution**

Added a `$project` stage to return only the required fields and used `$map` to format nested order data.

---

## Issue 5: User Without Orders

**Problem**

A newly created user returned:

```json
{
    "orders": []
}
```

**Cause**

The user had not placed any orders.

**Solution**

No code changes were required. This is the expected behavior of MongoDB's `$lookup`, which functions similarly to a SQL LEFT JOIN by returning the user document with an empty array when no matching orders exist.

---

## Summary

The following issues were identified and resolved during development:

- MongoDB connection configuration
- PyMongo and `bson` dependency conflict
- MongoDB `ObjectId` serialization
- Seed script execution
- Aggregation pipeline refinement
- ObjectId reference validation
- Response formatting using `$project`