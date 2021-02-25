const Discord = require("discord.js")
const config = require("../data.json")

module.exports = {
    execute(client, message, title, description, args) {
        embed = new Discord.MessageEmbed()
            .setColor(config.crazyBot.settings.accent_color)
            .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
            .setTitle(title)
            .setDescription(description);

        message.channel.send(embed);
    },

    errorMsg(client, message) {
        const errorMsgTitle = [
            "Uh oh!",
            "Oops!",
            "Yikes!",
            "Error!",
            "ERROR 4040 BREAK EVERYHINTG AHHHHHHHHHHHHHHH",
            ":("
        ];

        let randomErrMsg = errorMsgTitle[Math.floor(Math.random() * errorMsgTitle.length)];
        embed = new Discord.MessageEmbed()
            .setColor(config.crazyBot.settings.accent_color)
            .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
            .setTitle(randomErrMsg)
            .setDescription("Something happened and I failed to execute that command. Try again later or report a bug.");

        message.channel.send(embed);
    }
}