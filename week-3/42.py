def inside_circle(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 < r**2

a, b, r = map(float, input("Enter circle center (a, b) and radius r (separated by spaces): ").split())
n = int(input("Enter the number of points: "))
points = []
for i in range(n):
    x, y = map(float, input("Enter point: ").split())
    points.append((x, y))

count = 0
for x, y in points:
    if inside_circle(x, y, a, b, r):
        count += 1

print("Points inside:", count)