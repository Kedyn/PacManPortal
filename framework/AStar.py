class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return "(" + str(self.position[0]) + ", " + str(self.position[1]) + ")"

    def __repr__(self):
        return "(" + str(self.position[0]) + ", " + str(self.position[1]) + ")"


FULL_NEIGHBORS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
FOUR_NEIGHBORS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def astar(grid, start, end, diagonal=True):
    neighbors = []

    if diagonal:
        neighbors = FULL_NEIGHBORS
    else:
        neighbors = FOUR_NEIGHBORS

    total_rows = len(grid)
    total_cols = len(grid[0])

    open_list = []
    closed_list = []

    start_node = Node(position=start)
    end_node = Node(position=end)

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]

        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)

        closed_list.append(current_node)

        if current_node == end_node:
            path = []

            previous = current_node

            while previous is not None:
                path.append(previous)

                previous = previous.parent

            path.reverse()

            return path

        for neighbor in neighbors:
            neighbor_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if neighbor_position[0] > total_rows - 1 or neighbor_position[0] < 0 or \
                    neighbor_position[1] > total_cols - 1 or neighbor_position[1] < 0:
                continue

            if grid[neighbor_position[0]][neighbor_position[1]] != 0:
                continue

            neighbor_node = Node(current_node, neighbor_position)

            if neighbor_node not in closed_list:
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = abs(neighbor_node.position[0] - end_node.position[0]) + \
                    abs(neighbor_node.position[1] - end_node.position[1])
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if neighbor_node not in open_list:
                    open_list.append(neighbor_node)

    return []
