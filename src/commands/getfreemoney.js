const Discord = require("discord.js")
const config = require("../data.json")

module.exports = {
    name: "getsomefreemoney",
    title: "Get some free money!",
    description: "A command that tells you a TRUE, STILL WORKING method to get free money!",
    execute(client, message, args) {
      const embed = new Discord.MessageEmbed()
        .setColor(config.crazyBot.settings.accent_color)
        .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
        .setTitle(this.title)
        .setDescription(":wave:Hey!:wave: You are qualified to reedeem :money_mouth:thousands:money_mouth: of :moneybag:dollars:moneybag:. Just click this link and get your :moneybag:money:moneybag:!:point_right: <https://bit.ly/getsumfreemoneys>");
      message.channel.send(embed);
    }
}