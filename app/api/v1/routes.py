from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from app.schemas.game import GameCreate, GameRead
from app.db.session import get_database

router = APIRouter()
COLLECTION = "games"

def _doc_to_game(doc: dict) -> dict:
    return {
        "id": str(doc["_id"]),
        "name": doc.get("name"),
        "image": doc.get("image"),
        "price": doc.get("price"),
        "discount": doc.get("discount"),
        "description": doc.get("description"),
    }

@router.get("/games/", response_model=list[GameRead])
async def list_games():
    db = get_database()
    cursor = db[COLLECTION].find()
    docs = await cursor.to_list(length=200)
    return [_doc_to_game(d) for d in docs]

@router.get("/games/{game_id}", response_model=GameRead)
async def get_game(game_id: str):
    db = get_database()
    try:
        oid = ObjectId(game_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid id")
    doc = await db[COLLECTION].find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    return _doc_to_game(doc)

@router.post("/games/", response_model=GameRead, status_code=status.HTTP_201_CREATED)
async def create_game(game: GameCreate):
    db = get_database()
    payload = game.dict()
    result = await db[COLLECTION].insert_one(payload)
    new_doc = await db[COLLECTION].find_one({"_id": result.inserted_id})
    return _doc_to_game(new_doc)

@router.put("/games/{game_id}", response_model=GameRead)
async def update_game(game_id: str, game: GameCreate):
    db = get_database()
    try:
        oid = ObjectId(game_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid id")
    update_result = await db[COLLECTION].update_one({"_id": oid}, {"$set": game.dict()})
    if update_result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    doc = await db[COLLECTION].find_one({"_id": oid})
    return _doc_to_game(doc)

@router.delete("/games/{game_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: str):
    db = get_database()
    try:
        oid = ObjectId(game_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid id")
    delete_result = await db[COLLECTION].delete_one({"_id": oid})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    return None