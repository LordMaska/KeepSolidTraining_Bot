import os
import aiosqlite as sq
from aiogram.types import Message
from aiogram import Router

import aiofiles

async def get_tren(column: str):
    async with sq.connect('Trening_bot/Data/BD.db') as connect:
        async with connect.cursor() as cursor:
            await cursor.execute(f"SELECT {column} FROM Trenings;")
            result=await cursor.fetchall()
            tren=[row[0] for row in result]
            return tren

async def into_record(data: list):
    async with sq.connect('Trening_bot/Data/BD.db') as connect:
        async with connect.cursor() as cursor:
            await cursor.execute('''INSERT INTO Record (Name,Surname,Age,Phine,Email,Trening,Shedule,Interesting)
                                 VALUES (?,?,?,?,?,?,?,?);''', (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            await connect.commit()