import time

from plyer import notification

while True : # infinite loop 
    print('Please sip some water!')
    notification.notify(title = "Please drink some water",
                        message = "You need to drink some water ",)
    time.sleep(60*60) #It will run ill here in this terminal only 
    # lets make it for entire notification:
    # for that pip install plyer
    ## > https://plyer.readthedocs.io/en/latest/?__cf_chl_f_tk=ViH3KW1fbYk5vpYwPUJosOxXeHBpQaI_2bRyPnCXII8-1782814107-1.0.1.1-eyzIvGP4rfKoNMHLMdKQ4q_yxShMTtCyHjnYPD4rP9c#



