from pythonds.graphs import Graph


def knightGraph(bdsize):
    ktGraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = positionToId(row, col, bdsize)
            newPositions = genLegalPositions(row, col, bdsize)
            for ele in newPositions:
                nid = positionToId(ele[0], ele[1], bdsize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def positionToId(row, col, bdsize):
    return row * bdsize + col % bdsize


def genLegalPositions(row, col, bdsize):
    moves = [(2, 1), (2, -1), (1, 2), (1, -2),
             (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
    newPositions = []
    for dir1, dir2 in moves:
        if 0 <= dir1 + row < bdsize and 0 <= dir2 + col < bdsize:
            newPositions.append((dir1 + row, dir2 + col))
    return newPositions


def knightTour(n, in_path, u, limit):
    def orderByAvail(n):
        resList = []
        for v in n.getConnections():
            if v.getColor() == 'white':
                c = 0
                for w in v.getConnections():
                    if w.getColor() == 'white':
                        c += 1
                resList.append((c, v))
        resList.sort(key=lambda x: x[0])
        return [y[1] for y in resList]

    u.setColor('gray')
    in_path.append(u)
    if n < limit:
        # nbrList = list(u.getConnections())
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, in_path, nbrList[i], limit)
            i += 1
        if not done:
            in_path.pop()
            u.setColor('white')
    else:
        done = True
    return done


size = 5
g = knightGraph(size)
path = []
knightTour(1, path, g.getVertex(0), size * size)
idxs = [ele.getId() for ele in path]
instruction = [[0]*size for _ in range(size)]
i = 1
for ele in idxs:
    instruction[ele//size][ele%size] = i
    i += 1
for i in range(size):
    print(instruction[i])
