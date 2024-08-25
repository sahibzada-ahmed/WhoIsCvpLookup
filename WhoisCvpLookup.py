import whois
import socket
import random
from termcolor import colored

def display_banner():
    banner = """
     ██████╗██╗   ██╗██████╗  █████╗ ███████╗ █████╗  ██████╗██╗   ██╗
    ██╔════╝██║   ██║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗██╔════╝╚██╗ ██╔╝
    ██║     ██║   ██║██████╔╝███████║  ███╔╝ ███████║██║  ███╗╚████╔╝ 
    ██║     ██║   ██║██╔══██╗██╔══██║ ███╔╝  ██╔══██║██║   ██║ ╚██╔╝  
    ╚██████╗╚██████╔╝██║  ██║██║  ██║███████╗██║  ██║╚██████╔╝  ██║   
     ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═════╝   ╚═╝   
                                                                      
    """
    creator_info = "Made by Faraz Ahmed | Cyber Vigilance PK"
    
    # Display banner and creator information in random colors
    print(colored(banner, random_color()))
    print(colored(creator_info, random_color()))

def random_color():
    # Randomly select a color for the text
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    return random.choice(colors)

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Error: {str(e)}"

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "IP address not found."

def display_whois_info(w, ip_address):
    print(colored(f"\n{'-'*50}", random_color()))
    print(colored(f"WHOIS Information for {w.domain_name}", random_color()))
    print(colored(f"{'-'*50}\n", random_color()))
    
    print(colored(f"Domain Name: {w.domain_name}", random_color()))
    print(colored(f"IP Address: {ip_address}", random_color()))
    print(colored(f"Registrar: {w.registrar}", random_color()))
    print(colored(f"Creation Date: {w.creation_date}", random_color()))
    print(colored(f"Expiration Date: {w.expiration_date}", random_color()))
    print(colored(f"Updated Date: {w.updated_date}", random_color()))
    print(colored(f"Name Servers: {', '.join(w.name_servers)}", random_color()))
    print(colored(f"Status: {w.status}\n", random_color()))
    
    if w.org:
        print(colored(f"Organization: {w.org}", random_color()))
    if w.country:
        print(colored(f"Country: {w.country}", random_color()))
    if w.city:
        print(colored(f"City: {w.city}", random_color()))
    if w.address:
        print(colored(f"Address: {w.address}", random_color()))
    if w.emails:
        print(colored(f"Emails: {', '.join(w.emails)}", random_color()))
    print(colored(f"{'-'*50}\n", random_color()))

if __name__ == "__main__":
    display_banner()
    
    # Prompt user for the domain name
    domain = input(colored("Enter the domain name to lookup WHOIS information: ", random_color()))
    
    whois_data = whois_lookup(domain)
    ip_address = get_ip_address(domain)
    
    if isinstance(whois_data, str):
        print(colored(whois_data, 'red'))
    else:
        display_whois_info(whois_data, ip_address)
