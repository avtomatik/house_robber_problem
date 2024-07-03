def get_max_snatch(houses):
    if not houses:
        return

    if len(houses) == 1:
        return houses[-1]

    snatch = [max(houses[:_]) for _ in range(1, 3)]

    for house in houses[2:]:
        snatch.append(max((snatch[-1], house + snatch[-2])))

    return snatch[-1]


if __name__ == '__main__':
    houses = [4, 11, 10, 1, 2, 8, 5]
    print(get_max_snatch(houses))
