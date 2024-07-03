import discord
import feedparser
import asyncio

TOKEN = 'DISCORD-TOKEN-HERE'
USER_ID = USER-ID-HERE  # replace with the user's ID
RSS_FEED_URL = 'RSS-FEED-HERE'
CHECK_INTERVAL = 300  # Time in seconds to check the feed

intents = discord.Intents.default()
intents.messages = True

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, intents=intents)
        self.feed_url = RSS_FEED_URL
        self.user_id = USER_ID
        self.check_interval = CHECK_INTERVAL
        self.last_entry = None

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        self.target_user = await self.fetch_user(self.user_id)
        if self.target_user is None:
            print(f'Error: Could not find user with ID {self.user_id}')
        else:
            self.loop.create_task(self.check_feed())

    async def check_feed(self):
        while True:
            feed = feedparser.parse(self.feed_url)
            if feed.entries:
                latest_entry = feed.entries[0]
                if self.last_entry is None or latest_entry.link != self.last_entry.link:
                    self.last_entry = latest_entry
                    await self.send_update(latest_entry)
            await asyncio.sleep(self.check_interval)

    async def send_update(self, entry):
        if self.target_user is not None:
            description = entry.summary
            if len(description) > 4096:
                description = description[:4093] + '...'  # truncate to 4096 characters
            embed = discord.Embed(title=entry.title, url=entry.link)
            await self.target_user.send(embed=embed)
        else:
            print(f'Error: User is None, cannot send message')

client = MyClient()
client.run(TOKEN)