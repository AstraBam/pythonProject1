stone_bunch1 = int(input())
stone_bunch2 = int(input())
stone_bunch3 = int(input())
while stone_bunch3 != 0 or stone_bunch2 != 0 or stone_bunch1 != 0:
    bunch = int(input())
    stone = int(input())
    if bunch == 1:
        stone_bunch1 -= stone
        print(stone_bunch1, stone_bunch2, stone_bunch3)
    elif bunch == 2:
        stone_bunch2 -= stone
        print(stone_bunch1, stone_bunch2, stone_bunch3)
    else:
        stone_bunch3 -= stone
        print(stone_bunch1, stone_bunch2, stone_bunch3)
