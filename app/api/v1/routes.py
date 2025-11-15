from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from app.schemas.item import ItemCreate, ItemRead
from app.db.session import db

router = APIRouter()

COLLECTION_NAME = "items"

def _doc_to_item(doc: dict) -> dict:
    return {"id": str(doc["_id"]), "name": doc.get("name"), "description": doc.get("description")}

@router.get("/items/", response_model=list[ItemRead])
async def read_items():
    if db is None:
        raise HTTPException(status_code=500, detail="Database not initialized")
    cursor = db[COLLECTION_NAME].find()
    docs = await cursor.to_list(length=100)
    return [_doc_to_item(d) for d in docs]

@router.get("/items/{item_id}", response_model=ItemRead)
async def read_item(item_id: str):
    if db is None:
        raise HTTPException(status_code=500, detail="Database not initialized")
    try:
        oid = ObjectId(item_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid id")
    doc = await db[COLLECTION_NAME].find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return _doc_to_item(doc)

@router.post("/items/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    if db is None:
        raise HTTPException(status_code=500, detail="Database not initialized")
    payload = item.dict()
    result = await db[COLLECTION_NAME].insert_one(payload)
    new_doc = await db[COLLECTION_NAME].find_one({"_id": result.inserted_id})
    return _doc_to_item(new_doc)