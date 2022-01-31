from sre_constants import OP_LOCALE_IGNORE


class River:            #parent class
    substance = 'water'
    current_flow = 'downstream'
    destination = 'ocean'
    source = 'clouds'

    def getfishing(self):       #parent method
        pole = input("type of pole")
        hook = input("type of hook")
        bait = input("type of bait")
        if (hook == self.hook and bait == self.bait):
            print("Get your {} and lets go.".format(pole))
        else:
            print("Fish won't wait all day")

class Columbia(River):  #child class
    location = 'Oregon'
    size = 'large'
   
    def getfishing(self):       #child method
            pole = input("type of pole")
            hook = input("type of hook")
            lure = input("type of lure")
            if (hook == self.hook and lure == self.lure):
                print("Get your {} and lets go.".format(pole))
            else:
                print("Fish won't wait all day")

river = River()         #invokes parent and child methods
river.getfishing()

columbia = Columbia()
columbia.getfishing()