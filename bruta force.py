import random
import pyautogui
keyword="01234567890"
lst=list(keyword)
key=pyautogui.password(text="hello! there type your password below",title="#fuck you")
guss=""
tried=[]

def generate(guss):
    for k in range(0,len(key)):
        guss=guss+random.choice(lst)
    print(">>"+guss+"<<")
    return guss
def brutal(key):
    guss=""
    tried = []
    while guss!=key:
        

        guss=generate(guss)
        
        tried.append(guss)
        
        if guss not in tried:
            
        if guss==key:
            print("password = ",key)
            print(tried)
            print("the possible trial+>",len(tried))
            break
        guss=""
        
    
    
brutal(key)
