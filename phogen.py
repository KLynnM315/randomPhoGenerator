import csv
import numpy as np
import pandas as pd

def menu_order(order):
    
    for row in order:
        
        dfmenu = pd.read_csv('pho_cali.csv')
        
        if row == 'A':
            randno = np.random.randint(1,17)
        elif row == 'PH':
            randno = np.random.randint(18,40)
            
        newdf = dfmenu[(dfmenu.SectionLetter == row[0]) & (dfmenu.MenuItemNo == randno)]
        print(newdf)
       
if __name__ == '__main__':
     open_menu(('A', 'PH'))
