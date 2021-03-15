# testing purposes to find real cost
from collections import deque
def bfs(puzzle):
    queue = deque()
    seen = set()
    
    queue.append(puzzle.get_state())
    queue.append(None)
    
    seen.add(puzzle.get_state())
    
    cost = 0
    while True:
        top = queue.popleft()
        if top is None:
            cost += 1
            queue.append(None)
            continue
        puzzle.set_state(top)
        if puzzle.is_current_state_goal():
            break
        for child in puzzle.get_current_state_children():
            if child in seen:
                continue
            seen.add(child)
            queue.append(child)
    return cost