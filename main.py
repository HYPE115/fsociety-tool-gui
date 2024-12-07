import os
import sys
from colorama import Fore, Style, init

# Initialisation de Colorama
init(autoreset=True)

def clear_screen():
    """Efface l'écran pour une meilleure lisibilité."""
    os.system('cls' if os.name == 'nt' else 'clear')

ascii_art = r"""
  █████▒ ██████  ▒█████   ▄████▄   ██▓▓█████▄▄▄█████▓▓██   ██▓
▓██   ▒▒██    ▒ ▒██▒  ██▒▒██▀ ▀█  ▓██▒▓█   ▀▓  ██▒ ▓▒ ▒██  ██▒
▒████ ░░ ▓██▄   ▒██░  ██▒▒▓█    ▄ ▒██▒▒███  ▒ ▓██░ ▒░  ▒██ ██░
░▓█▒  ░  ▒   ██▒▒██   ██░▒▓▓▄ ▄██▒░██░▒▓█  ▄░ ▓██▓ ░   ░ ▐██▓░
░▒█░   ▒██████▒▒░ ████▓▒░▒ ▓███▀ ░░██░░▒████▒ ▒██▒ ░   ░ ██▒▓░
 ▒ ░   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓  ░░ ▒░ ░ ▒ ░░      ██▒▒▒ 
 ░     ░ ░▒  ░ ░  ░ ▒ ▒░   ░  ▒    ▒ ░ ░ ░  ░   ░     ▓██ ░▒░ 
 ░ ░   ░  ░  ░  ░ ░ ░ ▒  ░         ▒ ░   ░    ░       ▒ ▒ ░░  
             ░      ░ ░  ░ ░       ░     ░  ░         ░ ░     
                         ░                            ░ ░     
"""

menu_text = """
                1. Information Gathering
                2. Password Attacks
                3. Wireless Testing
                4. Exploitation Tools
                5. Sniffing & Spoofing
                6. Web Hacking
                7. Private Web Hacking
                8. Post Exploitation
                9. Install & Update
                0. Quitter
"""

menus = {
    "1": ("Information Gathering", [
        "Nmap", "Setoolkit", "Host To IP", "WPScan", 
        "CMS Scanner", "XSStrike", 
        "Dork - Google Dorks Passive Vulnerability Auditor",
        "Scan A server's Users", "Crips"
    ]),
    "2": ("Password Attacks", ["Cupp", "Ncrack"]),
    "3": ("Wireless Testing", ["Reaver", "Pixiewps", "Bluetooth Honeypot"]),
    "4": ("Exploitation Tools", [
        "ATSCAN", "sqlmap", "Shellnoob", "Commix", 
        "FTP Auto Bypass", "JBoss Autopwn"
    ]),
    "5": ("Sniffing & Spoofing", ["Setoolkit", "SSLtrip", "pyPISHER", "SMTP Mailer"]),
    "6": ("Web Hacking", [
        "Drupal Hacking", "Inurlbr", "Wordpress & Joomla Scanner", 
        "Gravity Form Scanner", "File Upload Checker", 
        "Wordpress Exploit Scanner", "Wordpress Plugins Scanner", 
        "Shell and Directory Finder", 
        "Joomla! 1.5 - 3.4.5 remote code execution",
        "Vbulletin 5.X remote code execution", 
        "BruteX", "Arachni"
    ]),
    "7": ("Private Web Hacking", [
        "Get all websites", "Get joomla websites", 
        "Get wordpress websites", "Control Panel Finder", 
        "Zip Files Finder", "Upload File Finder", 
        "Get server users", "SQli Scanner", 
        "Ports Scan (range of ports)", 
        "Ports Scan (common ports)", "Get server Info", 
        "Bypass Cloudflare"
    ]),
    "8": ("Post Exploitation", ["Shell Checker", "POET", "Weeman"]),
    "9": ("Install & Update", []),
    "0": ("Quitter", [])
}

def display_main_menu():
    """Affiche le menu principal."""
    clear_screen()
    print(Fore.RED + ascii_art)
    print(Fore.GREEN + "=" * 80)
    print(Fore.GREEN + menu_text)
    print(Fore.GREEN + "=" * 80)

    choice = input(Fore.GREEN + "Choisissez une option : ")
    return choice

def display_tools(tools):
    """Affiche une liste d'outils et permet de revenir au menu principal."""
    while True:
        clear_screen()
        for i, tool in enumerate(tools, start=1):
            print(f"{i}. {tool}")
        print("0. Retour au menu principal")
        choice = input(Fore.GREEN + "Choisissez une option ou tapez 0 pour revenir : ")
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(tools):
            print(Fore.GREEN + f"Vous avez choisi : {tools[int(choice)-1]}")
            input(Fore.GREEN + "Appuyez sur Entrée pour continuer...")
        else:
            print(Fore.RED + "Option invalide. Essayez à nouveau.")
            input(Fore.GREEN + "Appuyez sur Entrée pour continuer...")

def install_update():
    """Menu Install & Update."""
    clear_screen()
    print(Fore.CYAN + "Installation & Mise à jour")
    print("=" * 40)
    print("Utilisez le script d'installation pour configurer les outils requis.")
    print("Téléchargez les mises à jour depuis le dépôt GitHub officiel.")
    input(Fore.YELLOW + "Appuyez sur Entrée pour revenir au menu principal...")

def handle_choice(choice):
    """Gère le choix de l'utilisateur."""
    if choice in menus:
        title, tools = menus[choice]
        if tools:
            display_tools(tools)
        elif choice == "9":
            install_update()
        elif choice == "0":
            print(Fore.CYAN + "Au revoir!")
            sys.exit()
        else:
            print(Fore.RED + "Aucune option valide n'est associée à ce menu.")
            input(Fore.GREEN + "Appuyez sur Entrée pour continuer...")
    else:
        print(Fore.RED + "Option invalide. Essayez à nouveau.")
        input(Fore.YELLOW + "Appuyez sur Entrée pour continuer...")

def main():
    """Boucle principale pour afficher le menu et gérer les options."""
    while True:
        choice = display_main_menu()
        handle_choice(choice)

if __name__ == "__main__":
    main()