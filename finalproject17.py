class Character(object):
    """character template"""
    def __init__(self, name):
        self.name = name
        self.gp = 100 #gp stands for "grade points"
        self.sp = 100 #sp stands for "self-esteem points"

    def bang_head_against_wall(self,
