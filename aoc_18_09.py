def day_1(players=9, max_marble=25):
    circle = [0]
    cur_marble = 0
    scores = [0 for _ in range(players)]
    cur_player = 0
    next_marble = 0
    while True:
        next_marble += 1
        if not next_marble % 23 == 0:
            location_next_marble = (cur_marble+2) % len(circle)
            circle.insert(location_next_marble+1, next_marble)
            cur_marble = location_next_marble
        else:
            location_next_marble = (cur_marble-6) % len(circle)
            print(cur_player, next_marble, circle[location_next_marble])
            scores[cur_player] += next_marble + circle.pop(location_next_marble)
            cur_marble = location_next_marble-1
            
        cur_player = (cur_player+1) % players
        if next_marble == max_marble:
            break
    return max(scores)

##print(day_1(9, 25))
##print(day_1(10, 1618))
##print(day_1(13, 7999))
##print(day_1(17, 1104))
##print(day_1(21, 6111))
##print(day_1(30, 5807))
##print(day_1(459, 71320))
print(day_1(459, 7132000))
