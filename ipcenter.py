import weechat
import re
##Regiesters
weechat.register("ipcenter_python", "JerryGarcia", "1.0", "GPL3", "IPCenter Script", "", "")

##Loading message
weechat.prnt("", "%s[IPcenter]%s Script Loaded (by Jerry Garcia)" % (weechat.color("white,red"),weechat.color("reset")))
def modifier_cb(data, modifier, modifier_data, string):
        finals = string
        match = re.search('([0-9]{8})',string)
        if match:
            ipcenter = "https://ipcenter.ipsoft.com/IPim/Ticket/Display.html?id="+match.group()
            weechat.prnt(weechat.current_buffer(), "%s[IPCenter] %s%s" % (weechat.color("red") ,weechat.color("reset") , ipcenter))
            
        return "%s%s" % (string, "")

weechat.hook_modifier("irc_in_privmsg", "modifier_cb", "")