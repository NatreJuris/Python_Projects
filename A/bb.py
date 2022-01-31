class River:                #create parent class River
    substance = 'water'
    current_flow = 'downstream'
    destination = 'ocean'
    source = 'clouds'

class Columbia(River):
    location = 'Oregon'     #create child class
    size = 'large'

class Nile(River):
    location = 'Egypt'       #create child class
    size = 'large'
