#####################
### Base classes. ###
#####################

class item:
    description = "A basic item."
    synonyms = ["item"]
    
    def __init__(self):
        print("Use only in testing. Base classes should not be instantiated.")
        
    def __str__(self):
        return self.description
    
    def __repr__(self):
        return self.synonyms[0]
        
######################
### Child classes. ###
######################

class trophy(item):
    synonyms = ["trophy"]
    description = "A shiny trophy."
    
    def __init__(self):
        pass
        
class key(item):
    synonyms = ["key"]
    description = "A simple metal key."
 
    def __init__(self, id=0):
        self.id = id
        
