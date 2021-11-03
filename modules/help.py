
 ​ ​​@​​Client​​.​​on_message​​(​​Filters​​.​​command​​([​"​info​1"​]))​  
 ​ ​​async​​ ​​def​​ ​​start​​(​​client​​, ​​message​​):  
 ​ ​    ​​helptxt​​ ​​=​​ ​​f​"Clique nos 3 pontos na música e escolha a opção de salvar."

 
 ​ ​​@​​Client​​.​​on_message​​(​​Filters​​.​​command​​([​"​info2​"​]))​  
 ​ ​​async​​ ​​def​​ ​​start​​(​​client​​, ​​message​​):  
 ​ ​    ​​helptxt​​ ​​=​​ ​​f​"Atualmente aceito apenas links do Youtube (sem playlist) use /m + link"​  
 ​ ​    ​​await​​ ​​message​​.​​reply_text​​(​​helptxt​​)​  
 ​ ​    ​​await​​ ​​message​​.​​reply_text​​(​​helptxt​​)
