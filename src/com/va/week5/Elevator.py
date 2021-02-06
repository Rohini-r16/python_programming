class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current >= self.top:
            return self.top

        elif self.current < self.top:
            self.current = self.current + 1

            return self.current

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current <= self.bottom:
            return self.bottom
        else:
            self.current = self.current - 1
            return self.current

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor >= self.top:
            self.current = self.top
        elif floor <= self.bottom:
            self.current = self.bottom
        else:
            self.current = floor
        return self.current


#elevator = Elevator(-1, 10, 0)