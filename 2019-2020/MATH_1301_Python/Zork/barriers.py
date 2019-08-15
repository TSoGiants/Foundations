#####################
### Base classes. ###
#####################

class barrier:
    synonyms = ["wall"]
    m_description = "There is a barrier in the way."
    
    def __init__(self, passable=False):
        self.passable = passable
        
    def __str__(self):
        return self.m_description
        
    def __repr__(self):
        return self.synonyms[0]
        
class passage(barrier):
    synonyms = ["clearing"]
    m_description = "There is a clearing ahead."
    
    def __init__(self, passable=True):
        self.passable = passable
        
class door(barrier):
    synonyms = ["door"]
    m_description = "There is door ahead."
    m_already_open = "The door is already opened."
    m_on_open = "You opened the door."
    m_already_closed = "The door is already closed."
    m_on_close = "You closed the door."
    
    def open(self):
        if self.passable:
            return self.m_already_open
        else:
            self.passable = True
            return self.m_on_open
            
    def close(self):
        if not self.passable:
            return self.m_already_closed
        else:
            self.passable = False
            return self.m_on_close
    
    def __str__(self):
        if self.passable:
            s = "opened"
        else:
            s = "closed"
            
        s = f"{self.m_description} It is currently {s}."
        return s
    
        
######################
### Child classes. ###
######################