#!/usr/bin/env python3

from urllib.parse import quote
#import sopel
from sopel import module
import subprocess
import sys


def wttr(location):
    u = "wttr.in/" + quote(location) + "?0TQ"
    r = subprocess.run(['/usr/bin/env', 'curl', '-s', u], stdout=subprocess.PIPE)
    l = r.stdout.decode("utf-8").split("\n")
    w = " ".join([s[16:].strip() for s in l])
    return w + " https://" + u


@module.commands("wttr", "weather")
def sopel_wttr(bot, trigger):
    l = trigger.group(2)
    if l is None:
        l = bot.db.get_nick_value(trigger.nick, 'wttr_location')
        if not l:
            bot.reply("Specify a location: '.wttr london' or '.setlocation london'")
            return None

    bot.reply(wttr(l))

@module.commands("setlocation")
def sopel_wttr_setlocation(bot, trigger):
    l = trigger.group(2)
    if l is None:
        bot.reply("Specify a location: '.setlocation london'")
    else:
        bot.db.set_nick_value(trigger.nick, 'wttr_location', l)
        bot.reply("I now have you at: " + l)

def main():
    # print( wttr('brisbane') )
    l = " ".join(sys.argv[1:])
    print(wttr(l))


if __name__ == "__main__":
    main()
