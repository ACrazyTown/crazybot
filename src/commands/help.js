const Discord = require("discord.js");
const config = require("../data.json");

module.exports = {
    name: "help",
    title: "Help",
    description: "A help command. Lists all the commands and other functionalities.",
    execute(client, message, args) {       
        embed = new Discord.MessageEmbed()
        .setColor(config.crazyBot.settings.accent_color)
        .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
        .setTitle(this.title)
        .setDescription(this.description)
        .setFooter(`Command issued by: ${message.author.tag}  |  Thanks for using crazyBot!`)
        // .attachFiles("./assets/vibecheck.png")
        // .setImage("attachment://vibecheck.png");

        message.channel.send(embed); // just testing move along
    }
}