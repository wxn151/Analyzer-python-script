from rutine import Rutine

calculator = Rutine()
quake = ['a', 'b', 'c', 'nyan']
opt = ['a)Exponential', 'b)Logarithm', 'c)Exit', '']
    
while True:    
    x = input("Introduce an operation:\n" + "\n".join(opt))
    x = x.lower()
    
    try:
        non_valid = x in quake 
        if (non_valid is False):
            raise ValueError("banned")
        else:
            if(x == 'b'):
                calculator.logarithm()
            elif(x == 'nyan'):
                calculator.conttribution = 'Nyan'
                calculator.easter_egg()
            elif(x == "a"):
                calculator.xponent()
            ###########################
            else: 
                print("bye.")
                break
    except ValueError:
        print("Not allow input.\n")
        pass
    
    

    
