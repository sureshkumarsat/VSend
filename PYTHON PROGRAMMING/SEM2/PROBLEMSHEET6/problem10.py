def distance(p1, p2):
    dist = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2)
    return dist


n = int(input("ENTER NUMBER OF POINTS : "))
Points_List = []
for i in range(0, n):
    coordinates = eval(input(f"ENTER COARDINATES FOR POINT {i+1}(x, y) : "))
    Points_List.append(coordinates)

min_dist = distance(Points_List[0], Points_List[1])
Point1 = Points_List[0]
Point2 = Points_List[1]

for i in range(0, len(Points_List)):
    for j in range(0, len(Points_List)):
        if i != j and distance(Points_List[i], Points_List[j]) < min_dist:
            min_dist = distance(Points_List[i], Points_List[j])
            Point1 = Points_List[i]
            Point2 = Points_List[j]

print(
    f"THE SHORTEST DISTANCE IS BETWEEN {Point1} AND {Point2} WITH DISTANCE {min_dist}"
)
