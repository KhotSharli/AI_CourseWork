from queue import PriorityQueue

# Heuristic function to estimate the cost of reaching the goal state from the current state
def heuristic(state):
    m_left, c_left, b_pos, m_right, c_right = state
    # Calculate the total number of missionaries and cannibals that need to move to the right bank
    return m_left + c_left

# Function to check if a state is valid
def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3:
        return False
    if (c_left > m_left > 0) or (c_right > m_right > 0):
        return False
    return True

# Function to generate the next valid states from the current state
def next_states(state):
    m_left, c_left, b_pos, m_right, c_right = state
    valid_moves = [
        (2, 0), (0, 2), (1, 1), (1, 0), (0, 1)  # Different possible combinations of missionaries and cannibals in the boat
    ]
    
    if b_pos == 'left':
        next_states = [(m_left - m, c_left - c, 'right', m_right + m, c_right + c) for m, c in valid_moves]
    else:
        next_states = [(m_left + m, c_left + c, 'left', m_right - m, c_right - c) for m, c in valid_moves]
    
    return [state for state in next_states if is_valid(state)]

# A* Search algorithm
def a_star(start_state):
    frontier = PriorityQueue()
    frontier.put((0, [start_state]))  # (cost, path_to_current_state)
    explored = set()
    
    while not frontier.empty():
        _, path = frontier.get()
        current_state = path[-1]
        
        if current_state == (0, 0, 'right', 3, 3):
            return path
        
        explored.add(current_state)
        
        for next_state in next_states(current_state):
            if next_state not in explored:
                new_cost = len(path)  # Each move has a cost of 1
                new_path = path + [next_state]
                frontier.put((new_cost + heuristic(next_state), new_path))
                explored.add(next_state)
    
    return None

# Testing the algorithm with the initial state (3, 3, 'left', 0, 0)
initial_state = (3, 3, 'left', 0, 0)
path = a_star(initial_state)

# Printing the path from the initial state to the goal state
if path:
    for state in path:
        print(state)
else:
    print("No valid path found.")
