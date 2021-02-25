const Discord = require("discord.js");
const config = require("../data.json");

module.exports = {
    name: "yomama",
    title: "Yo Mama",
    description: "A command that insults your mother dearest.",
    execute(client, message, args) {
        const https = require('https');
        const url = "api.yomomma.info";
        var options = {
            host: url,
            port: 443,
            path: "/",
            headers: {"Accept":"application/json", "User-Agent":"crazyBot (https://github.com/acrazytown/crazybot)"}
        }

        var getData = function(options) {
            https.get(options, (resp) => {
            let data = '';
    
            resp.on('data', (chunk) => {
                data += chunk;
            });
    
            resp.on('end', () => {
                const embed = new Discord.MessageEmbed()
                    .setColor(config.crazyBot.settings.accent_color)
                    .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
                    .setTitle(this.title)
                    .setDescription(JSON.parse(data).joke)
                    .setFooter(`Powered by ${url}`);
                
                message.channel.send(embed);
            });
    
            }).on("error", (err) => {
            console.log("Error: " + err.message);
            });
        }.bind(this);

        getData(options);
    }
}  