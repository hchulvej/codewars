"""
Situation

You have been hired by a company making electric garage doors. Accidents with the present product line have resulted in numerous damaged cars, broken limbs and several killed pets. Your mission is to write a safer version of their controller software.
Specification

We always start with a closed door. The remote control has exactly one button, with the following behaviour.

    If the door is closed, a push starts opening the door, and vice-versa
    It takes 5 seconds for the door to open or close completely
    While the door is moving, one push pauses movement, another push resumes movement in the same direction

In order to make the door safer, it has been equiped with resistance-based obstacle detection. When the door detects an obstacle, it must immediately reverse the direction of movement.
Input

A string where each character represents one second, with the following possible values.

    '.' No event
    'P' Button has been pressed
    'O' Obstacle has been detected (supersedes P)

As an example, '..P....' means that nothing happens for two seconds, then the button is pressed, then no further events.
Output

A string where each character represents one second and indicates the position of the door (0 if fully closed and 5 fully open). The door starts moving immediately, hence its position changes at the same second as the event.
Example

..P...O..... as input should yield 001234321000 as output
"""
def controller(events):
    
    class State:
        def __init__(self):
            self.position = 0
            self.dir = 1
            self.stopped = True
            self.time = 0
        
        def reverse_dir(self):
            self.dir = (self.dir + 1) % 2
        
        def stop_start(self):
            self.stopped = not self.stopped
        
        def move(self):
            self.time = self.time + 1
            if self.dir == 1:
                self.position = min(self.position + 1, 5)
                if self.position == 5:
                    self.reverse_dir()
            else:
                self.position = max(self.position - 1, 0)
                if self.position == 0:
                    self.reverse_dir()
        
        def get_position(self):
            return self.position
        
        
            
        
        
    
    st = new State()
        
