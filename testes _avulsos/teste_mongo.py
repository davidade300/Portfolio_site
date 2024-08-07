import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

"""
arquivo com um pequeno teste de conexão com o mongo
"""


async def test_connection():
    MONGO_DETAILS = "mongodb://davidade:aderaldo01@localhost:27017"
    client = AsyncIOMotorClient(MONGO_DETAILS)
    db = client.mydatabase

    try:
        info = await db.command("ping")
        print("Conexão bem-sucedida:", info)
    except Exception as e:
        print("Erro ao conectar ao MongoDB:", e)
    finally:
        client.close()


asyncio.run(test_connection())
