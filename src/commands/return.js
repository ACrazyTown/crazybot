const fs = require("fs");
const fileName = "../data.json";
const file = require(fileName);

module.exports = {
    execute(client, message) {
        const returnMessages = [
            "I have returned!",
            "I'm back!",
            "sup",
            "Huzzah! I have returned!",
            "I did whatever I was doing and I'm back!"
        ];
        
        if (!file.crazyBot.temp.on_reboot) return;

        var randomInt = Math.floor(Math.random() * returnMessages.length);

        client.channels.cache.get(file.crazyBot.temp.return_message_channel).send(returnMessages[randomInt]);

        file.crazyBot.temp.on_reboot = false;
        file.crazyBot.temp.return_message_channel = "";

        fs.unlink(fileName, (err) => {
            if (err) {
              console.log(err);
              return
            }
        });

        fs.writeFile("data.json", JSON.stringify(file, null, 2), function writeJSON(err) {
            if (err) return console.log(err);
            console.log(JSON.stringify(file));
            console.log("Writing to " + fileName);
        });
     }
}