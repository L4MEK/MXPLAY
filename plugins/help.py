 
 ​from​ ​pyrogram​ ​import​ ​Client​, ​Filters 
  
  
 ​@​Client​.​on_message​(​Filters​.​command​([​"info"​])) 
 ​async​ ​def​ ​start​(​client​, ​message​): 
 ​    ​helptxt​ ​=​ ​f"Currently Atualmente só aceito links do Youtube (sem playlist) use /m + link" 
 ​    ​await​ ​message​.​reply_text​(​helptxt​)
