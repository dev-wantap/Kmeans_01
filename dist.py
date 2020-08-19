def euclidean_distance(Vec1, Vec2):
    sum = 0
    for i in len(Vec1):
        sum += (Vec1[i][1]-Vec2[i][1])**2
    sum = math.sqrt(sum)
    return sum
