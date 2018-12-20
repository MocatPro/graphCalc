import math
segmentArea = []
points = [0]
totalArea = 0
c = "nope"

x = 0





def get_segment(a, b):
    sa = ((a + b) / 2) * 10
    return sa


while c != 'done':
    c = (input(": "))
    if c == "done":
        break
    
    points.append(int(c))
x = 0
for coord in points:
    x = x + 1
    if x >= len(points):
        break
    print(x)
    segmentArea.append(get_segment(points[x-1], points[x]))
    

for item in segmentArea:
    totalArea = totalArea + int(item)

print(totalArea)

