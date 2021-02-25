# crazyBot

A Discord bot made using the [discord.js](https://discord.js.org/) library that does nothing useful.

Originally named "Crazy's Awesome Discord Bot", it was really messy and bad so I've decided to rewrite it from scratch, hopefully making it better.

## Move to JavaScript
You may (or may not have) noticed that there is now a new branch called "pre-js". 
This is due to me deciding to port crazyBot to discord.js. (It was originally written in Python, using the [discord.py](https://discordpy.readthedocs.io/en/latest/) library.)

There are multiple reasons for this, but the main one is that the discord.js library is more up-to-date and stronger.

I will update the pre-js branch to the last update I was working on with my friend, and then it's officially no longer supported.

## How to run?
Even though this repository is meant to make it easier for me to work on the bot with my friends, you are allowed to run it yourself. (You will not receive any support though.)

The bot needs a **data.json** file to read settings. 
I don't include it in the repository because the Overseer's Update feature would overwrite it.

JSON Structure:
(**NEW (Release 1.0+)**)

```json
{"crazyBot":{
    "settings":{
        "token":"Token",
        "prefix":"Prefix",
        "version":"Version",
        "icon_url":"Profile Picture URL",
        "accent_color":"Embed Accent Color"
    },
    "temp":{
        "on_reboot":"false",
        "return_message_channel":""
    }
}}
```

(**OLD**)

```json
{
 "TOKEN":"MyToken"
}
```
After specifying the JSON file, edit any specific values in **bot.js** the commands folder to your wish.

When you do all that, just run the **start.sh** script and you're good to go!
