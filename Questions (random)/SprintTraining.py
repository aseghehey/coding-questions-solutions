"""

Pat is an ordinary kid who works hard to be a great runner. As part of training, Pat must run
sprints of different intervals on a straight trail. The trail has numbered markers that the coach uses as goals.
Pat's coach provides a list of goals to reach in order. Each time Pat starts at, stops at, or passes a marker,
it is considered a visit. Determine the lowest numbered marker that is visited the most times during Pat's day of training.

n = 5
sprints = [2, 4, 1, 3]

Pat has visited markers 2 and 3 a total of 3 times each. Since 2 < 3, the lowest numbered marker that is visited
the most times during Pat's day of training is 2.

"""

def getMostVisited(n, sprints):
    arr = [0] * (n + 1)
    for i in range(1, len(sprints)):
        lower, upper = min(sprints[i - 1], sprints[i]), max(sprints[i - 1], sprints[i])
        for j in range(lower, upper + 1):
            arr[j] += 1
    
    return arr.index(max(arr))

print(getMostVisited(5, [2,4,1,3]))