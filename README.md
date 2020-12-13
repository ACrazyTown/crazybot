# crazyBot

A Discord bot made using the Discord.py Library who doe nothing useful.

Originally named "Crazy's Awesome Discord Bot" it was really messy and bad so I've decided to rewrite it from scratch, hopefully making it better.

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
