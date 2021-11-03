 
 ​from​ ​pyrogram​ ​import​ ​Client​, ​Filters 
  
  
 ​@​Client​.​on_message​(​Filters​.​command​([​"info"​])) 
 ​async​ ​def​ ​start​(​client​, ​message​): 
 ​    ​helptxt​ ​=​ ​f"Atualmente aceito apenas links do Youtube (sem playlist) use /m + link" 
 ​    ​await​ ​message​.​reply_text​(​helptxt​)
