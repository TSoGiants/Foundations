#####################
### Base classes. ###
#####################

class room:
    m_description = "You are in a simple room."
    
    def __init__(self, contents=[]):
        self.contents = contents
        
    def __str__(self):
        s = ""
        for object in self.contents:
            s += " " + str(object)
        return self.m_description + s
    
        
######################
### Child classes. ###
######################

class blue_room(room):
    m_description = "You are in a blue room."
    
class red_room(room):
    m_description = "You are in a red room."
    
class green_room(room):
    m_description = "You are in a green room."
    
    