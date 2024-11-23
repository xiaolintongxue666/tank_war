from tank import Tank

class Player:
    def __init__(self, name, controls, tank_image, initial_position):
        super.__init__()
        self.name = name
        self.controls = controls
        self.tank = Tank(initial_position, tank_image, controls)
        self.score = 0

    def reset(self, position):
        self.tank.reset(position)
