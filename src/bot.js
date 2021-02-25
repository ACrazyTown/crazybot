const fs = require("fs");
const Discord = require("discord.js");
const client = new Discord.Client;
client.commands = new Discord.Collection();
const commandFiles = fs.readdirSync("./commands").filter(file => file.endsWith(".js"));

const config = require("./data.json");
const simpleEmbed = require("./templates/simpleEmbed.js");

const settings = config.crazyBot.settings, temp = config.crazyBot.temp;
const token = settings.token, prefix = settings.prefix, version = settings.version;

for (const file of commandFiles) {
    const command = require(`./commands/${file}`);

    console.log(`Loaded command ${command.name}`);
    client.commands.set(command.name, command);
}

client.once("ready", message => {
    client.user.setPresence({status: 'online',activity: {name: 'with JavaScript',type: 'PLAYING'}})
    console.log("/".repeat(25));
    console.log(`Name: ${client.user.tag}`);
    console.log(`Version: ${version}`);
    console.log("If you're seeing this, I'm up!");
    console.log("\\".repeat(25));

    if (config.crazyBot.temp.on_reboot) { 
        const returnScript = require("./commands/return.js");

        returnScript.execute(client, message);
    }
});

client.on("guildMemberAdd", (message) => {
    const msgChannel = client.channels.cache.get("769534876000845825");
    let memberRole = message.guild.roles.cache.find(role => role.name === "Citizens");

    if (msgChannel) {
        if (!memberRole) return;
        message.guild.members.cache.get(message.user.id).roles.add(memberRole);
        msgChannel.send(`:arrow_right: **<@${message.user.id}>** welcome to **${message.guild.name}**.`);
    }
});

client.on("guildMemberRemove", (message) => {
    const msgChannel = client.channels.cache.get("769534876000845825");

    if (msgChannel) {
        msgChannel.send(`:arrow_left: **${message.user.tag}** has escaped Braz- I mean has left **${message.guild.name}**.`);
    }
});

client.on("message", message => {
    if (!message.content.startsWith(prefix)) return;

    const args = message.content.slice(prefix.length).trim().split(/ +/);
    const commandName = args.shift().toLowerCase();

    const command = client.commands.get(commandName);

    if (!client.commands.has(commandName)) return;

    try {
        command.execute(client, message, args);
    } catch(error) {
        console.error(error);
        simpleEmbed.errorMsg(client, message);
    }
});

client.login(token);