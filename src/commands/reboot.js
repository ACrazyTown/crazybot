const fileName = "../data.json";
const file = require(fileName);
const fs = require("fs");

module.exports = {
    name: "reboot",
    title: "Reboot",
    description: "Reboots the bot.",
    execute(client, message, args) {
        message.channel.send("Rebooting...");
       
        file.crazyBot.temp.on_reboot = true;
        file.crazyBot.temp.return_message_channel = message.channel.id;

        // Figure out better way, but for now, delete JSON file then write a new one.
        fs.unlink(fileName, (err) => {
            if (err) {
              console.log(err);
              return
            }
        });

        fs.writeFile("data.json", JSON.stringify(file, null, 2), function writeJSON(err) {
            if (err) return console.log(err);
            console.log(JSON.stringify(file));
            console.log("Wrote to " + fileName);
        });
        
        setTimeout(function() {
            process.exit(3);
        }, 5000);

    }
}