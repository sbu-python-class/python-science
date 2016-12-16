class Box(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


boxes = []
for n in range(1, 10):
    boxes.append(Box(2*n, 4*n))


for b in boxes:
    print(b.area())


big_boxes = [b for b in boxes if b.area() > 100.]
print big_boxes
