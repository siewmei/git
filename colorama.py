
# %%
# =============================================================================
# colorama - May 12, 2021
# =============================================================================

#import colorama
from colorama import Fore, Back, Style

print('\nwith Fore.RESET and Style.BRIGHT at every line.')
print(Fore.RED + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.GREEN + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.BLUE + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.CYAN + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.YELLOW + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.WHITE + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(f"{Style.BRIGHT}{Fore.RED}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O{Fore.RESET}")
print(f"{Style.BRIGHT}{Fore.RED}W{Fore.YELLOW}O{Fore.GREEN}R{Fore.BLUE}L{Fore.MAGENTA}D{Fore.RESET}")
print(f"{Style.BRIGHT}{Fore.BLACK}{Back.RED}H{Back.YELLOW}E{Back.GREEN}L{Back.BLUE}L{Back.MAGENTA}O{Fore.RESET}")
print(f"{Style.BRIGHT}{Fore.BLACK}{Back.RED}W{Back.YELLOW}O{Back.GREEN}R{Back.BLUE}L{Back.MAGENTA}D{Fore.RESET}")
print(Style.RESET_ALL) #reset, without this line, the Back.MAGENTA setting still there

print('set Style.BRIGHT once in the first line and Style.RESET_ALL at the last line.') #to set Style.BRIGHT to all below until the RESET_ALL code.
print(Style.BRIGHT + Fore.RED + 'Hello World')
print(Fore.GREEN + 'Hello World')
print(Fore.BLUE + 'Hello World')
print(Fore.CYAN + 'Hello World')
print(Fore.YELLOW + 'Hello World')
print(Fore.WHITE + 'Hello World')
print(f"{Fore.RED}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O")
print(f"{Fore.RED}W{Fore.YELLOW}O{Fore.GREEN}R{Fore.BLUE}L{Fore.MAGENTA}D")
print(f"{Fore.BLACK}{Back.RED}H{Back.YELLOW}E{Back.GREEN}L{Back.BLUE}L{Back.MAGENTA}O")
print(f"{Fore.BLACK}{Back.RED}W{Back.YELLOW}O{Back.GREEN}R{Back.BLUE}L{Back.MAGENTA}D")
print(Style.RESET_ALL)

#without Style.BRIGHT setting.
print('Without the Style.BRIGHT setting')
print(Fore.RED + 'Hello World')
print(Fore.GREEN + 'Hello World')
print(Fore.BLUE + 'Hello World')
print(Fore.CYAN + 'Hello World')
print(Fore.YELLOW + 'Hello World')
print(Fore.WHITE + 'Hello World')
print(f"{Fore.RED}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O")
print(f"{Fore.RED}W{Fore.YELLOW}O{Fore.GREEN}R{Fore.BLUE}L{Fore.MAGENTA}D")
print(f"{Fore.BLACK}{Back.RED}H{Back.YELLOW}E{Back.GREEN}L{Back.BLUE}L{Back.MAGENTA}O")
print(f"{Fore.BLACK}{Back.RED}W{Back.YELLOW}O{Back.GREEN}R{Back.BLUE}L{Back.MAGENTA}D")
print(Style.RESET_ALL)
















