'''
Script : PhoneSploit Pro
Author : Mohd Azeem (github.com/AzeemIdrisi)
'''

from modules import color
menu1 = f'''

    {color.WHITE}1. {color.GREEN}Connect a device             {color.WHITE}6. {color.GREEN}Get Screenshot                       {color.WHITE}11. {color.GREEN}Install an APK  
    {color.WHITE}2. {color.GREEN}List connected devices       {color.WHITE}7. {color.GREEN}Screen Record                        {color.WHITE}12. {color.GREEN}Uninstall an App
    {color.WHITE}3. {color.GREEN}Disconnect all devices       {color.WHITE}8. {color.GREEN}Download File/Folder from device     {color.WHITE}13. {color.GREEN}List installed Apps 
    {color.WHITE}4. {color.GREEN}Access device shell          {color.WHITE}9. {color.GREEN}Send File/Folder to device           {color.WHITE}14. {color.GREEN}Restart device
    {color.WHITE}5. {color.GREEN}Stop ADB server             {color.WHITE}10. {color.GREEN}Run an App                           {color.WHITE}15. {color.GREEN}Hack Device {color.RED}(Using Metasploit)


   {color.YELLOW} 
  N : Next Page                   (Page : 1 / 2)'''
menu2 = f'''

    {color.WHITE}16. {color.GREEN}List all Folders/Files      {color.WHITE}21. {color.GREEN}Anonymous Screenshot                {color.WHITE}26. {color.GREEN}Play a Video on device
    {color.WHITE}17. {color.GREEN}Advanced Reboot Options     {color.WHITE}22. {color.GREEN}Anonymous Screen Record
    {color.WHITE}18. {color.GREEN}Copy WhatsApp Data          {color.WHITE}23. {color.GREEN}Open a Link on device 
    {color.WHITE}19. {color.GREEN}Copy All Screenshots        {color.WHITE}24. {color.GREEN}Display a Photo on device
    {color.WHITE}20. {color.GREEN}Copy All Camera Photos      {color.WHITE}25. {color.GREEN}Play an Audio on device


   {color.YELLOW} 
  P : Previous Page               (Page : 2 / 2)'''

instruction = f'''

This attack will launch Metasploit-Framework    (msfconsole)

Use 'Ctrl + C' to stop at any point

1. Wait until you see:
    
    {color.GREEN}meterpreter >      {color.WHITE}

2. Then use 'help' command to see all meterpreter commands:

    {color.GREEN}meterpreter > {color.YELLOW}help       {color.WHITE}

3. To exit meterpreter enter 'exit' or To exit Metasploit enter 'exit -y':

    {color.GREEN}meterpreter > {color.YELLOW}exit       {color.WHITE}

    {color.GREEN}msf6 > {color.YELLOW}exit -y       {color.WHITE}
     
{color.RED}[PhoneSploit Pro]   {color.WHITE}Press 'Enter' to continue attack
    '''

banner2 = f'''

        ░█▀▀█ █──█ █▀▀█ █▀▀▄ █▀▀ ░█▀▀▀█ █▀▀█ █── █▀▀█ ─▀─ ▀▀█▀▀ 　 ░█▀▀█ █▀▀█ █▀▀█ 
        ░█▄▄█ █▀▀█ █──█ █──█ █▀▀ ─▀▀▀▄▄ █──█ █── █──█ ▀█▀ ──█── 　 ░█▄▄█ █▄▄▀ █──█ 
        ░█─── ▀──▀ ▀▀▀▀ ▀──▀ ▀▀▀ ░█▄▄▄█ █▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ──▀── 　 ░█─── ▀─▀▀ ▀▀▀▀


                                                 {color.WHITE}By github.com/AzeemIdrisi
'''

banner3 = f'''

        █▀█ █░█ █▀█ █▄░█ █▀▀ █▀ █▀█ █░░ █▀█ █ ▀█▀   █▀█ █▀█ █▀█
        █▀▀ █▀█ █▄█ █░▀█ ██▄ ▄█ █▀▀ █▄▄ █▄█ █ ░█░   █▀▀ █▀▄ █▄█


                                {color.WHITE}By github.com/AzeemIdrisi
'''

banner4 = f'''
    _________.__                           _________      .__         .__  __    __________                 
    \______   \  |__   ____   ____   ____  /   _____/_____ |  |   ____ |__|/  |_  \______   \_______  ____   
    |     ___/  |  \ /  _ \ /    \_/ __ \ \_____  \\\____ \|  |  /  _ \|  \   __\  |     ___/\_  __ \/  _ \  
    |    |   |   Y  (  <_> )   |  \  ___/ /        \  |_> >  |_(  <_> )  ||  |    |    |     |  | \(  <_> ) 
    |____|   |___|  /\____/|___|  /\___  >_______  /   __/|____/\____/|__||__|    |____|     |__|   \____/  
                \/            \/     \/        \/|__|                                                     


                                                                {color.WHITE}By github.com/AzeemIdrisi
'''
banner5 = f'''
       ___  __                 ____     __     _ __     ___         
      / _ \/ /  ___  ___  ___ / __/__  / /__  (_) /_   / _ \_______ 
     / ___/ _ \/ _ \/ _ \/ -_)\ \/ _ \/ / _ \/ / __/  / ___/ __/ _ \\
    /_/  /_//_/\___/_//_/\__/___/ .__/_/\___/_/\__/  /_/  /_/  \___/
                               /_/                                                                                                         


                                    {color.WHITE}By github.com/AzeemIdrisi
'''

banner6 = f'''
        ____  __                    _____       __      _ __       ____           
       / __ \/ /_  ____  ____  ___ / ___/____  / /___  (_) /_     / __ \_________ 
      / /_/ / __ \/ __ \/ __ \/ _ \\\__ \/ __ \/ / __ \/ / __/    / /_/ / ___/ __ \\
     / ____/ / / / /_/ / / / /  __/__/ / /_/ / / /_/ / / /_     / ____/ /  / /_/ /
    /_/   /_/ /_/\____/_/ /_/\___/____/ .___/_/\____/_/\__/    /_/   /_/   \____/ 
                                     /_/                                                                         
    
    
                                                  {color.WHITE}By github.com/AzeemIdrisi

'''

banner10 = f'''
     ____    __                              ____            ___               __        ____                        
    /\  _`\ /\ \                            /\  _`\         /\_ \           __/\ \__    /\  _`\                      
    \ \ \L\ \ \ \___     ___     ___      __\ \,\L\_\  _____\//\ \     ___ /\_\ \ ,_\   \ \ \L\ \_ __   ___          
     \ \ ,__/\ \  _ `\  / __`\ /' _ `\  /'__`\/_\__ \ /\ '__`\\\ \ \   / __`\/\ \ \ \/    \ \ ,__/\`'__\/ __`\        
      \ \ \/  \ \ \ \ \/\ \L\ \/\ \/\ \/\  __/ /\ \L\ \ \ \L\ \\\_\ \_/\ \L\ \ \ \ \ \_    \ \ \/\ \ \//\ \L\ \       
       \ \_\   \ \_\ \_\ \____/\ \_\ \_\ \____\\\ `\____\ \ ,__//\____\ \____/\ \_\ \__\    \ \_\ \ \_\\\ \____/       
        \/_/    \/_/\/_/\/___/  \/_/\/_/\/____/ \/_____/\ \ \/ \/____/\/___/  \/_/\/__/     \/_/  \/_/ \/___/        
                                                         \ \_\                                                       
                                                          \/_/                                                       


                                                                    {color.WHITE}By github.com/AzeemIdrisi

'''

banner11 = f'''
    _____________                   ________       ______     __________       ________              
    ___  __ \__  /_____________________  ___/__________  /________(_)_  /_      ___  __ \____________ 
    __  /_/ /_  __ \  __ \_  __ \  _ \____ \___  __ \_  /_  __ \_  /_  __/      __  /_/ /_  ___/  __ \\
    _  ____/_  / / / /_/ /  / / /  __/___/ /__  /_/ /  / / /_/ /  / / /_        _  ____/_  /   / /_/ /
    /_/     /_/ /_/\____//_/ /_/\___//____/ _  .___//_/  \____//_/  \__/        /_/     /_/    \____/ 
                                            /_/                                                       


                                                                {color.WHITE}By github.com/AzeemIdrisi

'''

banner12 = f'''

        ▒█▀▀█ █░░█ █▀▀█ █▀▀▄ █▀▀ ▒█▀▀▀█ █▀▀█ █░░ █▀▀█ ░▀░ ▀▀█▀▀ 　 ▒█▀▀█ █▀▀█ █▀▀█ 
        ▒█▄▄█ █▀▀█ █░░█ █░░█ █▀▀ ░▀▀▀▄▄ █░░█ █░░ █░░█ ▀█▀ ░░█░░ 　 ▒█▄▄█ █▄▄▀ █░░█ 
        ▒█░░░ ▀░░▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ▒█▄▄▄█ █▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ░░▀░░ 　 ▒█░░░ ▀░▀▀ ▀▀▀▀


                                                            {color.WHITE}By github.com/AzeemIdrisi

'''
banner_list = [banner2, banner3, banner4, banner5,
               banner6, banner10, banner11, banner12]

instructions_banner = f'''{color.CYAN}
        ____           __                  __  _                 
       /  _/___  _____/ /________  _______/ /_(_)___  ____  _____
       / // __ \/ ___/ __/ ___/ / / / ___/ __/ / __ \/ __ \/ ___/
     _/ // / / (__  ) /_/ /  / /_/ / /__/ /_/ / /_/ / / / (__  ) 
    /___/_/ /_/____/\__/_/   \__,_/\___/\__/_/\____/_/ /_/____/  
        {color.WHITE}                                                        
'''

hacking_banner = f'''{color.GREEN}
    
    █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀ ░ ░ ░
    █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█ ▄ ▄ ▄
    {color.WHITE}
'''

# for i in range(len(banner_list)):
#     print(f"{i+1}")
#     print(banner_list[i])
