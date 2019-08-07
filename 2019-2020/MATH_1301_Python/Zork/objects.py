class trophy_case:
    def __init__(self):
        self.is_open = False
        
    
    def __str__(self):
        if self.is_open:
            s = "opened"
        else:
            s = "closed"
            
        return f"You see a large trophy case. Its doors are currently {s}."
        
    def open(self):
        if self.is_open:
            return "The doors are already opened."
        else:
            self.is_open = True
            return "You opened the doors to the trophy case."
            
    def close(self):
        if not self.is_open:
            return "The doors are already closed."
        else:
            self.is_open = False
            return "You closed the trophy case."
            
          
          
class treasure_chest:
    def __init__(self):
        self.is_open = False
        self.is_locked = True
        
    def __str__(self):
        if not self.is_open and self.is_locked: # Closed and locked.
            return "You see a treasure chest. Its lid is closed and locked tightly."
        elif not self.is_open and not self.is_locked:   # Closed and unlocked.
            return "You see a treasure chest that has been unlocked."
        elif not self.is_locked: # Opened and unlocked.
            return "You see a treasure chest with its lid open."
        else:   # Opened and locked.
            return "You see a treasure chest with its lid open. Its latch appears locked."
            
    def open(self):
        if self.is_open:    # Open (either locked or unlocked).
            return "The lid is already opened."
        elif self.is_locked:    # Closed and locked.
            return "The lid is locked. You cannot budge it."
        else:   # Closed and unlocked.
            self.is_open = True
            return "With great effort, you heave open the heavy lid to the treasure chest."
            
    def close(self):
        if not self.is_open:    # Closed (either locked or unlocked).
            return "The lid of the treasure chest is already closed."
        elif self.is_locked:    # Open and locked.
            return "You try to close the lid of the treasure chest, but its latch prevents it from closing."
        else:   # Open and unlocked.
            self.is_open = False
            return "The lid of the treasure chest slams shut."
            
    def unlock(self):
        if not self.is_locked:   # Unlocked (either opened or closed).
            return "You cannot unlock a chest that is already unlocked."
        else:   # Locked (either opened or closed).
            self.is_locked = False
            return "You hear the heavy latch of the chest open with a clang."
                 
    def lock(self):
        if self.is_locked:  # Locked (either opened or closed).
            return "The chest is already locked."
        else:
            self.is_locked = True
            return "You locked the treasure chest."