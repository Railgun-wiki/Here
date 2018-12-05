# -*- coding: utf-8 -*-

import re

here_user = 0

def onServerStartup(server):
  global here_user
  here_user = 0

def onServerInfo(server, info):
  global here_user
  WAYPOINT_SUPPORT = False
  HIGHLIGHT_ENABLE = True
  dimension_convert = {"0":"主世界","-1":"地狱","1":"末地"}
  if (info.isPlayer == 0):
    if("following entity data" in info.content and here_user>0):
      name = info.content.split(" ")[0]
      dimension = re.search("(?<=Dimension: )-?\d",info.content).group()
      position_str = re.search("(?<=Pos: )\[.*?\]",info.content).group()
      position = re.findall("\[(-?\d*).*?, (-?\d*).*?, (-?\d*).*?\]",position_str)[0]
      position_show = "["+str(position[0])+","+str(position[1])+","+str(position[2])+"]"
      if(WAYPOINT_SUPPORT):
        pass
      else:
        server.say("§e" + name + "§r 在 §2" + dimension_convert[dimension] + position_show + "§r 向各位打招呼")
      if(HIGHLIGHT_ENABLE):
        server.execute("effect give "+ name + " minecraft:glowing 15 1 true")
        server.tell(name,"您将会被高亮15秒")
      here_user-=1
  else:
    if info.content.startswith('!!here'):
      here_user+=1
      server.execute("data get entity "+info.player)
