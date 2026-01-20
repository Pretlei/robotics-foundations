class point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def changeX(self, x):
        self.x = x
    
    def changeY(self, y):
        self.y = y

    def print(self):
        print("(%d, %d)" % (self.x, self.y))

        