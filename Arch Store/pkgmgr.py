import os
import os.path

def Start():
    print(colorama.Style.BRIGHT+colorama.Fore.CYAN+"     _             _     "+colorama.Style.BRIGHT+colorama.Fore.BLUE+"      /\      "+colorama.Style.BRIGHT+colorama.Fore.CYAN+"     _                         "+colorama.Style.BRIGHT+colorama.Fore.WHITE+"                                                                 |")
    print(colorama.Style.BRIGHT+colorama.Fore.CYAN+"    / \   _ __ ___| |__  "+colorama.Style.BRIGHT+colorama.Fore.BLUE+"     /  \     "+colorama.Style.BRIGHT+colorama.Fore.CYAN+" ___| |_ ___  _ __ ___         "+colorama.Style.BRIGHT+colorama.Fore.WHITE+"                                                                 |") 
    print(colorama.Style.BRIGHT+colorama.Fore.CYAN+"   / _ \ | '__/ __| '_ \ "+colorama.Style.BRIGHT+colorama.Fore.BLUE+"    /    \    "+colorama.Style.BRIGHT+colorama.Fore.CYAN+"/ __| __/ _ \| '__/ _ \        "+colorama.Style.BRIGHT+colorama.Fore.WHITE+"                                                                 |")
    print(colorama.Style.BRIGHT+colorama.Fore.CYAN+"  / ___ \| | | (__| | | |"+colorama.Style.BRIGHT+colorama.Fore.BLUE+"   /  __  \   "+colorama.Style.BRIGHT+colorama.Fore.CYAN+"\__ \ || (_) | | |  __/        "+colorama.Style.BRIGHT+colorama.Fore.WHITE+"                                                                 /")
    print(colorama.Style.BRIGHT+colorama.Fore.CYAN+" /_/   \_\_|  \___|_| |_|"+colorama.Style.BRIGHT+colorama.Fore.BLUE+"  / _/  \_ \  "+colorama.Style.BRIGHT+colorama.Fore.CYAN+"|___/\__\___/|_|  \___|        "+colorama.Style.BRIGHT+colorama.Fore.WHITE+"                                                               /")
    print(colorama.Style.BRIGHT+colorama.Fore.CYAN+"                         "+colorama.Style.BRIGHT+colorama.Fore.BLUE+" //        \\\\            "+"                                                           "+colorama.Style.BRIGHT+colorama.Fore.WHITE+"                      /")
    print(colorama.Style.BRIGHT+colorama.Fore.CYAN+"                         "+colorama.Style.BRIGHT+colorama.Fore.BLUE+"/            \             "+"                                                           "+colorama.Style.BRIGHT+colorama.Fore.WHITE+"                  /")
    print(colorama.Style.BRIGHT+colorama.Fore.WHITE+'-------------------------------------------------------------------------------------------------------------------------------/ ')
    print(colorama.Style.BRIGHT+colorama.Fore.WHITE+'--------Created by Donny Moree----------------------------------------------------------------------------------------------- | ')
    print(colorama.Style.BRIGHT+colorama.Fore.WHITE+'------------------------------------------------------------------------------------------------------------------------------| ')
    print(colorama.Style.BRIGHT+colorama.Fore.WHITE+'If you need help type "help"')

    while True:
        print(colorama.Style.BRIGHT+colorama.Fore.CYAN+'user@archstore >>',end='')
        userinput = input('')
        if userinput.strip() == '':
            continue
        if userinput.startswith('help'):
            print('exit')
            print('autoremove')
            print('aur install [package name]')
            print('aur remove [package name]')
            print('aur search [package name]')
            print('snap install [package name]')
            print('snap remove [package name]')
            print(colorama.Style.BRIGHT+colorama.Fore.YELLOW+'if this is your first start type "FStart"')
        if userinput.lower().startswith('aur'):
            if userinput.lower().split()[1] == 'search':
                package = userinput[10:]
                os.system('yay -Ss ' + package)
            
            if userinput.lower().split()[1] == 'install':
                package = userinput[10:]
                os.system('yay -S ' + package)
            
            if userinput.lower().split()[1] == 'remove':
                package = userinput[10:]
                os.system('yay -R ' + package)
        
        if userinput.startswith('autoremove'):
            os.system('yay -c')
        
        if userinput.startswith('FStart'):
            first()
        
        if userinput.lower().startswith('snap'):
            os.system(userinput)
        
        if userinput=='exit':
            os.system('clear')
            break

        print('')
        print('')

        
        
def first():
    d=input('Is "yay" and "snap" installed (y/n)')
    os.chdir(os.path.expanduser('~'))
    bashfile = open(".bashrc", "a")
    bashfile.write('\n alias store="python3 ~/pkgmgr.py"')
    bashfile.close()
    if d == 'y':
        print('Installing...')
        os.system('sudo pacman -S base-devel')
        
        print('')
        print('')
        print('')
        print('')
        print('Done.')
        print('Use the global "Store" command to activate archstore')
    if d == 'n':
        print('Installing yay...')
        os.system('sudo pacman -S base-devel git')
        os.system('git clone https://aur.archlinux.org/yay.git')
        os.chdir('yay')
        os.system('makepkg -si')
        os.chdir('..')
        print('\n\nInstalling snap...')
        os.system('git clone https://aur.archlinux.org/snapd.git')
        os.chdir('snapd')
        os.system('makepkg -si')
        os.system('sudo systemctl enable --now snapd.socket')
        print('\n\n\n\nInstalling a graphical appstore...(snap store)')
        os.system('snap install snap-store')
        print('')
        print('')
        print('')
        print('')
        print('Done.')
        print('Use the global "Store" command to activate archstore. REBOOT HIGHLY RECOMMENDED!')

try:
    import colorama
    colorama.init(autoreset=True)
    os.system('clear')
    try:
        Start()
    except:
        quit()
except:
    x = input('Is pip for python3 installed? (y/n)> ')
    if x.strip().lower() == 'n':
        os.system('sudo pacman -S python-pip')
    os.system('pip install colorama')
    os.system('pip3 install colorama')
    import colorama
    colorama.init()
    os.system('clear')
    Start()
