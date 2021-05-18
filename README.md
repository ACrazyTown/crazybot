# crazyBot

A Discord Bot made using the [discord.js](https://discord.js.org/) library that does literally nothing useful.

Originally named "Crazy's Awesome Discord Bot", it was really messy and bad so I've decided to rewrite it from scratch, hopefully making it better (plot twist: i didnt).

**you're allowed to do whatever you want with the bot AS LONG as you open source it**

## How to run?

Even though I DON'T recommend you run this (cuz a lot of values and shit are hardcoded to my server) you can do it.

You're gonna need [Python 3.7+](https://www.python.org/downloads/) and [Node.JS](https://nodejs.org/en/).
Once you installed Python & Node.JS you're gonna have to install some modules with `pip` and `npm` respectively.

Python stuff:
```
logging
```

Node.JS stuff:
```
discord.js
node-fetch
request
canvas
https
```

After installing all that crap you're almost ready to go!
Then, make a file called `data.json` in `src/` and copy paste the following (of course, you're gonna have to replace the placeholder text with ACTUAL stuff so the bot can run):
```
{
  "crazyBot": {
    "settings": {
      "token": "Your Discord Prefix",
      "prefix": "The prefix you want (default is crazy )",
      "version": "Bot version",
      "icon_url": "a url with the image for the bot's profile picture",
      "accent_color": "embed accent color"
    },
    "temp": {
      "on_reboot": false,
      "return_message_channel": ""
    },
    "api": {
      "yt-api-key": "youtube api key"
    }
  }
}
```

and after that, run overseer.py and it should work! (if it doesnt, i dont care figure it out yourself)
