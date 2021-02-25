const Discord = require("discord.js")
const config = require("../data.json")
const simpleEmbed = require("../templates/simpleEmbed")

module.exports = {
    name: "say",
    title: "Say",
    description: "A command that makes me say what you say!",
    execute(client, message, args) {
        if (args.length == 0) {
            simpleEmbed.execute(client, message, this.title, "You have to tell me something to say...", args)
        }

        if (args.length == 1) {
            const embed = new Discord.MessageEmbed()
                .setColor(config.crazyBot.settings.accent_color)
                .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
                .setTitle(this.title)
                .setDescription(args.join(" "))
                .setFooter(`Requested by ${message.author.username}`);

            message.channel.send(embed)
        }

    }
}