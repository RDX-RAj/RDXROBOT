#MIT License
#Copyright (c) 2024, ©RdxNetworks

from async_pymongo import AsyncClient

from RDXROBOT import MONGO_DB_URI

DBNAME = "RDXROBOT"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
