import discord
from discord import app_commands

# config.py is expected to exist at the root level
# should provide 2 variables: TOKEN and GUILD_ID
import config

TEST_GUILD = discord.Object(id=config.GUILD_ID)

class TruthNuke(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=TEST_GUILD)
        await self.tree.sync(guild=TEST_GUILD)

intents = discord.Intents.default()
intents.message_content = True

client = TruthNuke(intents=intents)

@client.tree.command()
async def grab_latest_truth(interaction: discord.Interaction):
    await interaction.response.send_message('test')

async def on_ready(self):
    print(f'Logged on as {self.user}!')

client.run(config.TOKEN)
