# RSS-To-Discord-PM-Notification-Bot-for-iPhone
This bot is intended to check the provided RSS feed every defined seconds and send a PM on discord to one user. This was made for iPhone users who have issues with their browsers' push notifications.

This bot uses 3 packages in Python and they are listed below.
* Discord
* Feedparser
* Asyncio

To install these packages, you will have to run the following commands one by one:
* pip install discord
* pip install feedparser
* pip install asyncio

After you install the packages, all you need to do is edit the file and make following changes in the code:
* Line 5: Replace DISCORD-TOKEN-HERE with your discord bot token.
* Line 6: Replace USER-ID-HERE with the user ID of the discord user who you want the bot to send PM's to.
* Line 7: Replace RSS-FEED-HERE with link to the RSS feed of your choice. It can be a news website RSS feed or an RSS feed of any forum you want.
* Line 8: Replace the number 300 with your choice of how frequent the bot should check the RSS feed. This time is mentioned in seconds. 300 means 5 minutes. I recommend you to keep it at 300.

After making these changes, all you need to do is run the bot with this command: python notify.py
