#!/usr/bin/env python3

from urllib.parse import quote
import sopel
import subprocess
import sys


def wttr(location):
    c = "curl -s wttr.in/" + quote(location) + "?0TQ"
    r = subprocess.run(c, shell=True, stdout=subprocess.PIPE)
    l = r.stdout.decode("utf-8").split("\n")
    w = " ".join([s[16:].strip() for s in l])
    return w + " https://" + c[8:]


@sopel.module.commands("wttr", "weather")
def sopel_wttr(bot, trigger):
    l = trigger.group(2)
    if l is None:
        bot.reply("Specify a location: .wttr london")
    else:
        bot.reply(wttr(l))


def main():
    # print( wttr('brisbane') )
    l = " ".join(sys.argv[1:])
    print(wttr(l))


if __name__ == "__main__":
    main()
