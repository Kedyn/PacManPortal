def heuristic(a, b):
    return abs(a['i'] - b['i']) + abs(a['j'] - b['j'])


def AStar(grid, start, end):
    open_list = []
    close_list = []

    open_list.append(start)

    while open_list:
        current = open_list[0]

        for item in open_list:
            if item.f < current.f:
                current = item

        if current is end:
            curr = current
            path = []

            while curr.previous:
                path.append(curr)

                curr = curr.previous

            path.reverse()

            return path

        open_list.remove(current)
        close_list.append(current)

        neighbors = current.neighbors

        for neighbor in neighbors:
            if neighbor not in close_list:
                temp_g = current.g + 1

                if neighbor in open_list:
                    if temp_g < neighbor.g:
                        neighbor.g = temp_g
                else:
                    neighbor.g = temp_g
                    open_list.append(neighbor)

                neighbor.h = heuristic(neighbor, end)

                neighbor.f = neighbor.g + neighbor.h

                neighbor.previous = current

    return []
