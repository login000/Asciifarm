


class Food:
    
    
    def __init__(self, health):
        self.healing = health
    
    def attach(self, obj, roomData):
        self.owner = obj
    
    
    def use(self, user):
        fighter = user.getComponent("fighter")
        if fighter:
            fighter.heal(self.healing, self.owner)
            self.owner.trigger("drop")
    