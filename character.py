class Character():
    def __init__(self) -> None:
        self.currenthp = int()
        self.maxhp = int()
        self.name = ""
        self.strength = int()
        self.inventory = []
    def set_stats(self,currenthp,maxhp,name,strength):
        self.currenthp = currenthp
        self.maxhp = maxhp
        self.name = name
        self.strength = strength
    def add_inv(self,item):
        self.inventory.append(item)
    def rem_inv(self,item):
        self.inventory.remove(item)
    def dmg_tkn(self,dmg):
        self.currenthp = self.currenthp - dmg
    
