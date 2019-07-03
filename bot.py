#!/usr/bin/env python3

import argparse
import configparser
from discord.ext import commands
import random

def randomLink (linkListesi):
    return random.choice (linkListesi)

def main (args):
    config = configparser.ConfigParser ()
    config.read (args.config_file)
    BOT_TOKEN = config["BOT"]["Token"]
    BOT_PREFIX = config["BOT"]["Prefix"]

    with open (args.links) as dosya:
        icerik = dosya.read ().splitlines ()

    
    client = commands.Bot (command_prefix=BOT_PREFIX)
    @client.event
    async def on_message (message):
        if message.author == client.user:
            return
        await client.process_commands (message)

    @client.command ()
    async def hesapal (context):
        reply = "{0.message.author.mention}\nLink: {1}".format (context,
                                                                randomLink (icerik))
        await context.send (reply)

    client.run (BOT_TOKEN)

if __name__ == "__main__":
    parser = argparse.ArgumentParser ()
    parser.add_argument ("links", help="Linklerin bulunduğu dosyanın konumu.")
    parser.add_argument ("-c", "--config-file", help="config dosyasının konumu",
                         default="bot.config.cfg")
    args = parser.parse_args ()
    main (args)
