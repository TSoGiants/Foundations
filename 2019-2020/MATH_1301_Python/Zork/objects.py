import items

#####################
### Base classes. ###
#####################

class container:
    m_description = "A basic container."
    m_on_open = "You open the container."
    m_already_open = "The container is already opened."
    m_on_close = "You close the container."
    m_already_closed = "The container is already closed."
    m_add_item = "You put the item in the container."
    m_closed = "You can't do that while the container is closed."
    
    is_windowed = False
    
    def __init__(self, is_open=False, contents=[]):
        self.is_open = is_open
        self.contents = contents

        
    def __str__(self):
        if self.is_open:
            s = "opened"
        else:
            s = "closed"
            
        s = f"{self.m_description} It is currently {s}."
        
        if self.is_open or self.is_windowed:
            if self.contents:
                s += " It contains:"
                for item in self.contents:
                    s += "\n* " + str(item) 
            else:
                s += " There is nothing inside."
                
        return s
        
        
    def open(self):
        if self.is_open:
            return self.m_already_open
        else:
            self.is_open = True
            return self.m_on_open
            
    def close(self):
        if not self.is_open:
            return self.m_already_closed
        else:
            self.is_open = False
            return self.m_on_close
            
    def add(self, item):
        if self.is_open:
            self.contents.append(item)
            return self.m_add_item
        else:
            return self.m_closed
        
    def take(self, index):
        if self.is_open:
            contents_temp = []
            for i in range(len(self.contents)):
                if i != index:
                    contents_temp.append(self.contents[i])
            
            try:
                item = self.contents[index]
            except:
                item = None
            self.contents = contents_temp
            
            return item
        else:
            return self.m_closed
            
            
class locked_container(container):
    m_description = "A container with a lock."
    m_locked = "The container is locked and won't open."
    m_already_unlocked = "The container is already unlocked."
    m_on_unlock = "You unlocked the container."
    m_already_locked = "The container is already locked."
    m_on_lock = "You locked the container."
    
    m_bad_key = "That is not the right key for this container."
    m_no_key = "You need a key to open this container."
    
    def __init__(self, is_open=False, is_locked=True, contents=[], id=0):
        self.is_open = is_open
        self.is_locked = is_locked
        self.contents = contents
        self.id = id
        
    def open(self):
        if self.is_open:    # Open (either locked or unlocked).
            return self.m_already_open
        elif self.is_locked:    # Closed and locked.
            return self.m_locked
        else:   # Closed and unlocked.
            self.is_open = True
            return self.m_on_open
            
    def close(self):
        if not self.is_open:    # Closed (either locked or unlocked).
            return self.m_already_closed
        else: # Open (either locked or unlocked).
            self.is_open = False
            return self.m_on_close
        
    def unlock(self, key=None):
        if isinstance(key, items.key):
            if key.id == self.id or key.id == 0: # Allows for master keys (id = 0).
                if not self.is_locked:   # Unlocked (either opened or closed).
                    return self.m_already_unlocked
                else:   # Locked (either opened or closed).
                    self.is_locked = False
                    return self.m_on_unlock
            else:
                return self.m_bad_key
        else:
            return self.m_no_key
                 
    def lock(self):
        if self.is_locked:  # Locked (either opened or closed).
            return self.m_already_locked
        else:
            self.is_locked = True
            return self.m_on_lock   
            
######################
### Child classes. ###
######################
          
class trophy_case(container):
    m_description = "You see a large trophy case."
    
    m_on_open = "You opened the doors to the trophy case."
    m_already_open = "The doors are already opened."
    m_on_close = "You closed the doors to the trophy case."
    m_already_closed = "The doors are already shut."
    
    is_windowed = True
    
class treasure_chest(locked_container):
    m_description = "You see a treasure chest."
    
    m_on_open = "With great effort, you heave open the heavy lid to the treasure chest."
    m_already_open = "The lid is already opened."
    m_on_close = "The lid of the treasure chest slams shut."
    m_already_closed = "The lid is already shut."
    
    m_locked = "The lid is locked. You cannot budge it."
    m_already_unlocked = "You cannot unlock a chest that is already unlocked."
    m_on_unlock = "You hear the heavy latch of the chest open with a clang."
    m_already_locked = "The chest is already locked."
    m_on_lock = "You locked the treasure chest."
    
    m_bad_key = "You try the key in the treasure chest, but it doesn't fit the lock."
    m_no_key = "You can't unlock the chest without a key."
            
            
        