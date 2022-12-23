class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    def setdata(self, x, y):
        self.x = x
        self.y = y

class Rect:
    def __init__(self, top_left=Point(0,0), bottom_right=Point(0,0)) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right

def intersects(self, other):    
    return not (self.top_left.x > other.top_left.x or self.bottom_right.x < other.bottom_right.x or self.top_left.y > other.top_left.y or self.bottom_right.y < other.bottom_right.y)
    # return not (self.top_right.x < other.bottom_left.x or self.bottom_left.x > other.top_right.x or self.top_right.y < other.bottom_left.y or self.bottom_left.y > other.top_right.y)

# test code
standardRect = Rect()
standardRect.top_left = Point(0, 0)
standardRect.bottom_right = Point(4, 4)

myRect = Rect()
myRect.top_left = Point(1, 2)
myRect.bottom_right = Point(3, 3)

result = intersects(standardRect, myRect)
print(result)