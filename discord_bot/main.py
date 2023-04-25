
import discord
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)



if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run("MTA3NDk5MTQ5NTMyMjU0NjE3Ng.GaHmCv.-J-HDactJUv-_nZ4e1pxz-qjCv5z5XaNUis3sI")
