import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGODB_URL, DATABASE_NAME

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]
games = db["games"]

seed_data = [
    {
        "name": "Hollow Knight",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/367520/header.jpg",
        "price": 14.99,
        "discount": 50.0,
        "description": "Juego de aventura y plataformas con mundo interconectado y un bello estilo dibujado a mano.",
    },
    {
        "name": "Stardew Valley",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg",
        "price": 9.99,
        "discount": 33.0,
        "description": "RPG agrícola donde cultivas, crías animales, minas y creas relaciones con los vecinos.",
    },
    {
        "name": "Cyberpunk 2077",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1091500/header.jpg",
        "price": 29.99,
        "discount": 70.0,
        "description": "RPG futurista de mundo abierto ambientado en Night City.",
    },
    {
        "name": "The Witcher 3: Wild Hunt",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/292030/header.jpg",
        "price": 19.99,
        "discount": 80.0,
        "description": "Gigantesca aventura de rol con monstruos, decisiones morales y una narrativa profunda.",
    },
    {
        "name": "Among Us",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/945360/header.jpg",
        "price": 3.99,
        "discount": 60.0,
        "description": "Juego multijugador de deducción social donde debes encontrar al impostor.",
    },
    {
        "name": "Portal 2",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/620/header.jpg",
        "price": 4.99,
        "discount": 75.0,
        "description": "Juego de puzzles con portales, humor absurdo y física divertida.",
    },
    {
        "name": "Dead Cells",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/588650/header.jpg",
        "price": 8.99,
        "discount": 70.0,
        "description": "Roguelike de acción con combates rápidos y permadeath parcial.",
    },
    {
        "name": "Celeste",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/504230/header.jpg",
        "price": 4.99,
        "discount": 80.0,
        "description": "Plataformas desafiantes con historia emocional sobre superar dificultades.",
    },
    {
        "name": "Terraria",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg",
        "price": 2.99,
        "discount": 90.0,
        "description": "Sandbox en 2D con construcción, exploración, combate y crafting.",
    },
    {
        "name": "Rust",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/252490/header.jpg",
        "price": 14.99,
        "discount": 40.0,
        "description": "Survival multijugador donde tienes que recolectar recursos, construir y sobrevivir frente a otros jugadores.",
    },
    {
        "name": "Subnautica",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/264710/header.jpg",
        "price": 11.99,
        "discount": 70.0,
        "description": "Exploración submarina en un planeta alienígena con peligros y maravillas.",
    },
    {
        "name": "Hades",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1145360/header.jpg",
        "price": 13.99,
        "discount": 50.0,
        "description": "Roguelike de acción mitológica donde intentas escapar del inframundo.",
    },
    {
        "name": "Sekiro: Shadows Die Twice",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/814380/header.jpg",
        "price": 24.99,
        "discount": 75.0,
        "description": "Juego de acción y sigilo ambientado en un Japón feudal fantástico.",
    },
    {
        "name": "Red Dead Redemption 2",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1174180/header.jpg",
        "price": 24.99,
        "discount": 80.0,
        "description": "Épica de western con mundo abierto, narrativa profunda y muchos detalles.",
    },
    {
        "name": "Control",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/870780/header.jpg",
        "price": 9.99,
        "discount": 85.0,
        "description": "Acción y aventuras paranormales dentro de una oficina misteriosa llamada The Oldest House.",
    },
    {
        "name": "DOOM Eternal",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/782330/header.jpg",
        "price": 14.99,
        "discount": 70.0,
        "description": "FPS frenético lleno de demonios, armas poderosas y un ritmo brutal.",
    },
    {
        "name": "Slay the Spire",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/646570/header.jpg",
        "price": 7.99,
        "discount": 60.0,
        "description": "Juego de construcción de mazos y roguelike donde subes una torre cambiante.",
    },
    {
        "name": "Disco Elysium",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/632470/header.jpg",
        "price": 11.99,
        "discount": 75.0,
        "description": "RPG narrativo profundo con diálogo, decisiones morales y un sistema de pensamiento muy original.",
    },
    {
        "name": "Cities: Skylines",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/255710/header.jpg",
        "price": 4.99,
        "discount": 85.0,
        "description": "Simulación de construcción de ciudades con gran profundidad en gestión.",
    },
    {
        "name": "Rocket League",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/252950/header.jpg",
        "price": 0.0,
        "discount": None,
        "description": "Juego deportivo donde coches juegan fútbol — free to play.",
    },
]

async def seed():
    await games.delete_many({})
    result = await games.insert_many(seed_data)
    print(f"✓ Insertados {len(result.inserted_ids)} juegos.")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed())