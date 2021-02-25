const Discord = require("discord.js")
const config = require("../data.json")
const simpleEmbed = require("../templates/simpleEmbed")

module.exports = {
    name: "vibecheck",
    title: "Vibecheck",
    description: "A command that vibechecks people... Pretty self explanatory, isn't it?",
    execute(client, message, args) {
        const botId = 2679940978190319646;
        const messages = ["*You have passed the vibecheck.*", "*You have failed the vibecheck.*"];
        const randomMsg = messages[Math.floor(Math.random() * messages.length)];

        if (args.length >= 2) { 
            simpleEmbed.execute(message, this.title, `Proper usage is \`${config.crazyBot.settings.prefix}${this.name} <mention> (Optional)\``, args);
        }

        if ("yourself" === args[0] || message.mentions.has(client.user)) {
            simpleEmbed.execute(message, this.title, "Silly, my Vibe is just too powerful to be checked.", args);
            return;
        }
        
        if (args.length === 1) {
            let mention = message.mentions.members.first();
            const mentionMessages = [`*${mention} has passed the vibecheck.*`, `*${mention} has failed the vibecheck.*`]

            if (!mention) {
                simpleEmbed.execute(message, this.title, `Proper usage is \`${config.crazyBot.settings.prefix}${this.name} <mention> (Optional)\``, args);
            } else{

            embed = new Discord.MessageEmbed()
                .setColor(config.crazyBot.settings.accent_color)
                .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
                .setTitle(this.title)
                .setDescription(mentionMessages[Math.floor(Math.random() * mentionMessages.length)])
                .attachFiles("./assets/vibecheck.png")
                .setImage("attachment://vibecheck.png");

            message.channel.send(embed);
        }}
        
        if (args.length == 0) {
            embed = new Discord.MessageEmbed()
                .setColor(config.crazyBot.settings.accent_color)
                .setAuthor("crazyBot", config.crazyBot.settings.icon_url)
                .setTitle(this.title)
                .setDescription(randomMsg)
                .attachFiles("./assets/vibecheck.png")
                .setImage("attachment://vibecheck.png");

            message.channel.send(embed);   
        }
    }
}