#MIT License
#Copyright (c) 2023, ©NovaNetworks

from async_pymongo import AsyncClient

from MukeshRobot import MONGO_DB_URI

DBNAME = "MukeshRobot"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
