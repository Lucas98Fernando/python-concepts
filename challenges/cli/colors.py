from colorama import Fore, Style

def cliColor(color, text):
    return (f'{getattr(Fore, color)}{text}{Style.RESET_ALL}')
