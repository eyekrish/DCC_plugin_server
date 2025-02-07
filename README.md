# 🏗️ DCC Plugin with FastAPI Backend  

This project integrates **Blender** with a **FastAPI** backend, enabling seamless interaction between a **Digital Content Creation (DCC) tool** and an external API. It includes:  

- **📌 Blender UI Panel**: A custom panel inside Blender.  
- **⚡ FastAPI Backend**: Endpoints for object transformations & inventory.  
- **🎨 Advanced Inventory UI**: A modern UI for managing assets.  
- **📂 File Path Retrieval**: Fetches the current file & project path.  

---

## 🚀 Features  

### 🔹 Blender UI Panel  
- Controls **position, rotation, and scale** of selected objects.  
- **Submit Transform** button sends data to the FastAPI server.  

### 🔹 Inventory UI  
- **Styled layout** for better readability.  
- **Interactive buttons** for item management.  
- **Color-coded categories** for better organization.  

### 🔹 FastAPI Backend  
- Receives and processes **transform data**.  
- Provides **Blender file path** retrieval.  
- Handles **inventory management**.  

---
## 📡 API Endpoints  

### 🔹 Transform Data  

| Method | Endpoint         | Description                        |
|--------|----------------|------------------------------------|
| `POST` | `/transform`   | Sends position, rotation, and scale data. |
| `POST` | `/translation` | Sends only position data.         |
| `POST` | `/rotation`    | Sends only rotation data.         |
| `POST` | `/scale`       | Sends only scale data.            |

#### Example Request (POST `/transform`)
```json
{
  "position": [1.0, 2.0, 3.0],
  "rotation": [0.0, 90.0, 0.0],
  "scale": [1.0, 1.0, 1.0]
}
```
#### Response
```json
{
  "status": "success",
  "received": {
    "position": [1.0, 2.0, 3.0],
    "rotation": [0.0, 90.0, 0.0],
    "scale": [1.0, 1.0, 1.0]
  }
}
```
# 🏪 Inventory Management API  

This section covers the API endpoints for managing inventory items in the **DCC Plugin**.

---

## 📡 API Endpoints  

| Method   | Endpoint           | Description                         |
|----------|-------------------|-------------------------------------|
| `GET`    | `/inventory`      | Retrieves the list of inventory items. |
| `POST`   | `/inventory`      | Adds a new item to the inventory.  |
| `PUT`    | `/inventory/{id}` | Updates an existing inventory item. |
| `DELETE` | `/inventory/{id}` | Deletes an item from the inventory. |

---

## 📥 Retrieve Inventory (`GET /inventory`)  

### Example Response  
```json
{
  "inventory": [
    {"id": 1, "name": "Sword", "type": "Weapon", "quantity": 2},
    {"id": 2, "name": "Health Potion", "type": "Consumable", "quantity": 5}
  ]
}
```
# 📂 File Path API  

This section covers the API endpoints for retrieving file paths in the **DCC Plugin**.

---

## 📡 API Endpoints  

| Method  | Endpoint           | Description                                      |
|---------|-------------------|--------------------------------------------------|
| `GET`   | `/file-path`      | Returns the current DCC file's path.            |
| `GET`   | `/file-path?projectpath=true` | Returns the project folder path. |

---

## 📥 Retrieve File Path (`GET /file-path`)  

### Description  
Returns the path of the currently open DCC (Blender) file.

### Example Response  
```json
{
  "file_path": "C:/Users/Username/Documents/my_project.blend"
}


