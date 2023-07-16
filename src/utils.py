class House():
    def __init__(self,mc, i ,j,k,pos_x,pos_y,pos_z , material, roof):
        x,y,z = mc.player.getPos()
        self.roof = roof
        self.x = x
        self.y = y
        self.z = z
        self.i = i
        self.j = j
        self.k = k
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.material = material
        self.mc = mc

    def spawn(self):
        for a in range (self.i):
            for b in range (self.j):
                for c in range (self.k):
                    if a==0 or c==0 or b==0 or a==self.i-1 or c==self.k-1:
                        self.mc.setBlock(self.x+a+self.pos_x, self.y+b+self.pos_y , self.z+c+self.pos_z, self.material)
        for a in range (self.i):
            for c in range(self.k):
                self.mc.setBlock(self.x+a+self.pos_x, self.y+b-1+ self.pos_y, self.z+c+ self.pos_z, self.roof)


