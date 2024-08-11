from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AnonXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="AnonXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="AnonXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="AnonXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="AnonXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Iniciando assistentes...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("Learningbots79")
                await self.one.join_chat("Learning_bots")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistente iniciado")
            except:
                LOGGER(__name__).error(
                    "A conta do assistente 1 não conseguiu acessar o grupo de logs. Certifique-se de ter adicionado seu assistente ao seu grupo de log e promovido como administrador!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistente 1 iniciado como {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("Learningbots79")
                await self.two.join_chat("Learning_bots")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistente iniciado")
            except:
                LOGGER(__name__).error(
                    "A conta do assistente 2 não conseguiu acessar o grupo de logs. Certifique-se de ter adicionado seu assistente ao seu grupo de log e promovido como administrador!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistente 2 começou como {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("Learningbots79")
                await self.three.join_chat("Learning_bots")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistente iniciado")
            except:
                LOGGER(__name__).error(
                    "A conta do assistente 3 não conseguiu acessar o grupo de logs. Certifique-se de ter adicionado seu assistente ao seu grupo de log e promovido como administrador!"
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistente 3 começou como {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("Learningbots79")
                await self.four.join_chat("Learning_bots")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistente iniciado")
            except:
                LOGGER(__name__).error(
                    "A conta do assistente 4 não conseguiu acessar o grupo de logs. Certifique-se de ter adicionado seu assistente ao seu grupo de log e promovido como administrador!"
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistente 4 começou como {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("Learningbots79")
                await self.five.join_chat("Learning_bots")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistente iniciado")
            except:
                LOGGER(__name__).error(
                    "A conta do assistente 5 não conseguiu acessar o grupo de logs. Certifique-se de ter adicionado seu assistente ao seu grupo de log e promovido como administrador!"
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistente 5 começou como {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Parando assistentes...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
