# crazyBot

A Discord bot made using the [discord.js](https://discord.js.org/) library who does nothing useful.

Originally named "Crazy's Awesome Discord Bot" it was really messy and bad so I've decided to rewrite it from scratch, hopefully making it better.

## Move to JavaScript
You may (or may not have) noticed that there is now a new branch called "pre-js". 
This is due to me deciding to move crazyBot to the discord.js library instead of discord.py

There are multiple reasons to this but the main one is that the discord.js library is more up-to-date and stronger.

I will update the pre-js branch to the last update I was working on with my friend, and then it's officially no longer supported.

## How to run?
Although this repository is more meant to make it easier for my friends to work on the bot with me, you can run the bot. (You will have to remove or change some specific stuff though.)

To run it, the bot needs a **data.json** file. 
I haven't included it because the Update feature in the Overseer will overwrite it.

Structure:
(**NEW; Upcoming in Release 1.0**)

```json
{
 "TOKEN":"MyToken",
 "PREFIX":"Prefix",
 "VERSION":"Version",
 "ICON_URL":"BotPFPUrl"
}
```
  
(**OLD**)

```json
{
 "TOKEN":"MyToken"
}
```
After specifying the JSON file, edit any specific values in **bot.py** and **crazycommands.py** to your wish.
Then run the start.sh file and voila!
