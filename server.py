from fastapi import FastAPI, HTTPException
import sqlite3
import time  # For the 10-second delay
from pydantic import BaseModel
import bpy
app = FastAPI()


class TransformData(BaseModel):
    position: list[float]
    rotation: list[float]
    scale: list[float]

# ✅ API Endpoints

@app.post("/transform")
async def receive_transform(data: TransformData):
    time.sleep(10)  # ⏳ Simulate a 10-second delay
    print(f"Received Transform Data: {data}")
    return {"status": "success", "received": data}

# ✅ Position Only
@app.post("/translation")
async def receive_translation(position: list[float]):
    time.sleep(10)
    print(f"Received Position Data: {position}")
    return {"status": "success", "position": position}

# ✅ Rotation Only
@app.post("/rotation")
async def receive_rotation(rotation: list[float]):
    time.sleep(10)
    print(f"Received Rotation Data: {rotation}")
    return {"status": "success", "rotation": rotation}

# ✅ Scale Only
@app.post("/scale")
async def receive_scale(scale: list[float]):
    time.sleep(10)
    print(f"Received Scale Data: {scale}")
    return {"status": "success", "scale": scale}

@app.get("/file-path")
async def get_file_path(projectpath: bool = False):
    blend_file_path = bpy.data.filepath.strip()  # Get the current file path

    if not blend_file_path:
        return {
            "error": "No file is currently saved. Please save the Blender file first.",
            "debug": "bpy.data.filepath is empty."
        }

    try:
        bpy.ops.wm.save_mainfile()  # Now safe to save
    except RuntimeError as e:
        return {"error": f"Failed to save file: {str(e)}"}

    if projectpath:
        project_path = "/".join(blend_file_path.replace("\\", "/").split("/")[:-1])
        return {"project_path": project_path}

    return {"file_path": blend_file_path.replace("\\", "/")}

# Simulate 10-second delay
def delayed_response():
    time.sleep(10)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect("inventory.db")
    conn.row_factory = sqlite3.Row
    return conn

# Add an item to the inventory
@app.post("/add-item")
def add_item(name: str, quantity: int):
    delayed_response()
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, quantity))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Item already exists")
    conn.close()
    return {"message": "Item added", "name": name, "quantity": quantity}

# Remove an item from inventory
@app.delete("/remove-item")
def remove_item(name: str):
    delayed_response()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE name = ?", (name,))
    conn.commit()
    conn.close()
    return {"message": "Item removed", "name": name}

# Update item quantity
@app.put("/update-quantity")
def update_quantity(name: str, new_quantity: int):
    delayed_response()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET quantity = ? WHERE name = ?", (new_quantity, name))
    conn.commit()
    conn.close()
    return {"message": "Quantity updated", "name": name, "new_quantity": new_quantity}

# Get all inventory items
@app.get("/inventory")
def get_inventory():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    conn.close()
    return {"inventory": [dict(item) for item in items]}
