
from .room import Room


class WorldTemplate:
    
    
    def __init__(self):
        
        self.prefabs = {}
    
    
    def addPrefabs(self, prefabs):
        for name, data in prefabs.items():
            self.addPrefab(name, data)
    
    def addPrefab(self, name, data):
        self.prefabs[name] = data
    
    
    def getTemplate(self, name):
        if name in self.prefabs:
            return self.prefabs[name]
        
        return None
    
    def getRoom(self, name):
        template = self.getTemplate(name)
        if not template:
            return None
        return Room(name, template)
