import discum     
bot = discum.Client(token='MTE0ODAwNjE2NDQyNTA4OTE5NQ.GYMQLu.qfbkvIhP0Ut6CkMe7Xbd7-jFp2Wu6qgqX_6HtE', log=False)

d = "-70"
e = "@Levelup"
onoff = True




    
@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp.event.message:
        m = resp.parsed.auto()
        guildID = m['guild_id'] if 'guild_id' in m else None #because DMs are technically channels too
        channelID = m['channel_id']
        username = m['author']['username']
        discriminator = m['author']['discriminator']
        content = m['content']
        print("> guild {} channel {} | {}#{}: {}".format(guildID, channelID, username, discriminator, content))


        global onoff

        if channelID == "1148190609060921374":
            if "spop" in content.lower():
                onoff = False
            elif "starp" in content.lower():
                onoff = True

        f1 = d in content
        f2 = e in content

        if f1 and f2 and onoff:
            bot.sendMessage("1148190609060921374", "Take2x")


bot.gateway.run(auto_reconnect=True)



       




