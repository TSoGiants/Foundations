#####################
### Base classes. ###
#####################

class item:
    description = "A basic item."
    
    def __init__(self):
        print("Use only in testing. Base classes should not be instantiated.")
        
    def __str__(self):
        return self.description
        
######################
### Child classes. ###
######################

class trophy(item):
    description = "A shiny trophy."
    
    def __init__(self):
        pass
        
class key(item):
    description = "A simple metal key."
 
    def __init__(self, id=0):
        self.id = id
        
