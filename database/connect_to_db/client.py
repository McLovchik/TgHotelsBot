from motor import motor_asyncio
import motor.motor_asyncio

from config_data.config import MONGO_DB_USERNAME, MONGO_DB_PASSWORD

client = motor_asyncio.AsyncIOMotorClient(f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}'
                                          f'@cluster0.ekgiy0k.mongodb.net?retryWrites=true&w=majority')


def get_favorites_collection() -> motor.motor_asyncio.AsyncIOMotorCollection:
    """Returns async collection of favorite hotels from MongoDB"""

    db = client['Hotels']
    return db['Favorites']


def get_history_collection() -> motor.motor_asyncio.AsyncIOMotorCollection:
    """Returns async collection of user history from MongoDB"""

    db = client['Hotels']
    return db['History']
