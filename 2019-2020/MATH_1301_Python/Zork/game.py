import rooms
import barriers
import objects
import items
import player

class adventure:
    def __init__(self, y=1, x=1):
        self.x = x
        self.y = y
        
        self.map = []
        for i in range(2*y+1):
            self.map.append([])
            for j in range(2*x+1):
                self.map[i].append(None)

        
    def __str__(self):
        s = ""
        for row in self.map:
            for room in row:
                if room:
                    r = repr(room)
                else:
                    r = ""
                s += r
                spacing = len(r)
                while spacing < 20:
                    s += " "
                    spacing += 1
                    
            s += "\n"
        return s
        
    def add_room(self, room, y, x):
        if x < self.x and x >= 0 and y < self.y and y >= 0:
            self.map[2*y+1][2*x+1] = room
        else:
            print("Room coordinates out of bounds")
            
    def add_barrier(self, barrier, y, x, dir="N"):
        if x < self.x and x >= 0 and y < self.y and y >= 0:
            if dir.upper() == "N":
                y_offset = -1
                x_offset = 0
            elif dir.upper() == "S":
                y_offset = 1
                x_offset = 0
            elif dir.upper() == "W":
                y_offset = 0
                x_offset = -1
            elif dir.upper() == "E":
                y_offset = 0
                x_offset = 1
            else:
                y_offset = 0
                x_offset = 0
            
            if x_offset or y_offset:   # If a valid direction, dir, was given.
                self.map[2*y+1+y_offset][2*x+1+x_offset] = barrier
            else:
                print("Direction is not valid.")
        else:
            print("Coordinates out of bounds.")
            
if __name__ == "__main__":
    a = adventure(2,3)
    
    ### Rooms
    room = rooms.room()
    red_room = rooms.red_room()            
    blue_room = rooms.blue_room()
    green_room = rooms.green_room()
    goal = rooms.final_room()
    
    
    a.add_room(room, 1,1)
    a.add_room(red_room, 0,0)
    a.add_room(blue_room, 0,1)
    a.add_room(green_room, 0,2)
    a.add_room(goal, 1, 2)
    
    ### Barriers
    
    passage = barriers.passage()
    passage_2 = barriers.passage()
    passage_3 = barriers.passage()
    door = barriers.door()
    
    a.add_barrier(passage, 1,1, "N")
    a.add_barrier(passage_2, 0,1, "W")
    a.add_barrier(door, 0,1, "E")
    a.add_barrier(passage_3, 0,2, "S")
    
    print(a)
                
        