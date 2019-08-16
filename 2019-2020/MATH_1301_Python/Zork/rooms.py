#####################
### Base classes. ###
#####################

class room:
    repr = "room"
    m_description = "You are in a simple room."
    
    
    def __init__(self, contents=[]):
        self.contents = contents
        
    def __str__(self):
        s = ""
        for object in self.contents:
            s += " " + str(object)
        return self.m_description + s
        
    def __repr__(self):
        return self.repr
    
        
######################
### Child classes. ###
######################

class blue_room(room):
    repr = "b. room"
    m_description = "You are in a blue room."
    
    
class red_room(room):
    repr = "r. room"
    m_description = "You are in a red room."
    
class green_room(room):
    repr = "g. room"
    m_description = "You are in a green room."
    
class final_room(room):
    repr = "goal"
    m_description = "You found the hidden room!"
    
    