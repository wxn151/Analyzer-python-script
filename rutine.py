import math
import re
import os
import time

class Rutine():
    def __init__(self):
        self.pattern = r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$"
        self._conttribution = 'none' # previous
        
    @property
    def conttribution(self):
        return self.__conttribution
    
    @conttribution.setter
    def conttribution(self, override):
        self._conttribution = f'Made by {override}'
    
    def logarithm(self):
        while True:
            try:
                no = input("The number is:\n")
                # nøne
                banned = re.match(self.pattern, no)
                if(banned is None):
                    raise ValueError("press restart")
                else:
                    w = math.log(int(no))
                    print(w)
                    break
            except ValueError:
                print('Please; enter a numerical type\n')
                pass
        
        
    def xponent(self):
        intent = 0
        bias = False
        while True: 
            try:
                
                # recursion
                if (bias is False): 
                    bs = input("The base is:\n")
                    on = re.match(self.pattern, bs)
                    
                    # who knows how it gøt there
                    if (intent > 3 and on is None):
                        print('Error again, are you stupid or what.')
                        pass
                    elif(on is None):
                        raise ValueError("press restart")
                    else:
                        bias = True
                        pass
                    
                else:
                    xpn = input("and the exp:\n")
                    off = re.match(self.pattern, xpn)
                    if (off is None):
                        raise ValueError("press restart")
                    else:
                        print(int(bs) ** int(xpn))
                        break
            except ValueError:
                print('Please; enter a numerical type\n')
                intent += 1
                pass
        
    #able to linux
    def easter_egg(self):
        self.animate_text(self._conttribution)
        

    def animate_text(self, text):
        no_characters=1
        while True:
            print("\n")
            print(text[0:no_characters])
            no_characters += 1
            if no_characters > len(text):
                no_characters = 0
                print('''
        ⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠉⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠑⠢⠄⣀⠉⠓⠦⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂⠀⠀⠀
    ⠀⠂⠤⣀⠈⠑⠂⠤⣀⠈⠑⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡡⠀⠀⠀
    ⠂⢄⣀⠀⠉⠒⠤⣀⠀⠉⠒⠤⣀⠈⠑⠢⢄⡀⠀⣀⠤⠒⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠄⣀⠀⠉⠒⠤⢀⠀⠈⠑⠢⢀⡀⠉⠒⠤⣀⢨⠟⠛⠒⠦⢄⣀⠀⠈⠑⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣀⠀⠉⠒⠤⣀⠀⠉⠒⠠⢄⡀⠈⠑⠢⣄⣀⡉⠀⢀⣠⣄⡀⠈⠉⠒⠦⢄⣀⠀⠉⠓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⡀⠉⠒⠤⣀⠀⠉⠒⠢⢄⠀⠈⠑⠢⢼⠉⢻⠣⠀⢸⠀⠀⡉⠑⠲⠤⣀⠀⠈⠉⠒⠢⣄⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠈⠑⠢⢄⡀⠉⠑⠢⢄⡀⠈⠑⠢⢄⣸⠀⢸⣷⠀⢸⠀⠸⠟⠀⠀⠀⢠⡿⣷⣶⢤⡀⠀⢳⠀⠀⢱⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠑⠢⢄⣀⠈⠑⠢⠄⡀⠈⢧⡀⢻⠀⢸⣄⠀⠀⢀⣀⡀⠀⠘⡇⠈⠳⣿⠀⠀⡇⠀⢸⡤⠋⠀⡇⠀⠀⠀⠀⡠⠂
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⢤⡀⠈⠉⠒⠿⣿⠀⢸⠁⠀⠀⠘⠚⠁⣤⣄⣣⠀⠀⠘⠒⠚⠓⠒⠚⠁⠀⠀⣷⠀⠀⠀⢠⠁⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠲⠤⣀⢸⠀⠘⣄⠀⠿⠇⠀⢀⡉⢹⠃⠀⠀⣠⣄⠀⠀⠀⠀⠀⣠⣄⠸⡆⠀⣠⠃⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠣⡴⠈⡟⠢⢄⣀⠙⠃⢸⣀⠠⢄⠻⠋⠀⠀⣤⡄⠀⠛⢛⠅⢿⠀⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⢀⠿⠤⣀⠈⠙⠒⠼⣷⣄⠜⠀⢠⠀⠀⣸⠀⠀⡤⠘⣦⠏⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠉⠒⠦⣄⡀⠉⠒⢤⣌⣉⣉⣉⣉⣻⣥⠒⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⡎⠀⣴⡇⢀⣼⡂⠈⢣⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡦⠴⠋⠉⠉⠀⠈⠓⠊⠀⠀⠀⠀⠀⠀⠀''')
                break;
                
            time.sleep(0.3)
            os.system('clear')
            #os.system('cls')  
  

