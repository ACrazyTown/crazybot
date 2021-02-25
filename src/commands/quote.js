const Discord = require("discord.js");
const config = require("../data.json")
const simpleEmbed = require("../templates/simpleEmbed")

module.exports = {
    name: "quote",
    title: "Quote",
    description: "Makes a quote. That wasn't obvious at all was it now?",
    execute(client, message, args) {
        if (args.length == 0) {
            simpleEmbed.execute(client, message, this.title, "I can't quote nothing...", args)
        }

        if (args.length >= 1) {
            const quote = args.join(" ");
            const author = message.author.username;
            
            var d = new Date();
            const year = d.getFullYear();

            var toSend = `
            *"${quote}"*
            - ${message.author.username}, ${year}
            `

            const embed = new Discord.MessageEmbed()
                .setColor(config.crazyBot.settings.accent_color)
                .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
                .setTitle(this.title)
                .setDescription(toSend)

            message.channel.send(embed);
        }
    }
}