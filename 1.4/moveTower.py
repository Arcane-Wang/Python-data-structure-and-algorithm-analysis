def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    global count
    count += 1
    # print("moving disk from", fp, "to", tp)
    tp.insert(0, fp.pop(0))
    # print("Pole1: ", fromPole_init)
    # print("Pole2: ", withPole_init)
    # print("Pole3: ", toPole_init)


count = 0
h = int(input("Input the height of the tower: "))
fromPole_init = list(range(1, 1 + h))
toPole_init = []
withPole_init = []
moveTower(h, fromPole_init, toPole_init, withPole_init)
print("count = ", count)