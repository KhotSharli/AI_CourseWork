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

# Depth-First Search (DFS) algorithm
def dfs(current_state, path, explored):
    # Check if we have reached the goal state
    if current_state == (0, 0, 'right', 3, 3):
        return path
    
    explored.add(current_state)
    
    # Explore all valid next states
    for next_state in next_states(current_state):
        if next_state not in explored:
            new_path = path + [next_state]
            result = dfs(next_state, new_path, explored)
            if result:
                return result
    
    explored.remove(current_state)
    return None

# Testing the algorithm with the initial state (3, 3, 'left', 0, 0)
initial_state = (3, 3, 'left', 0, 0)
explored = set()
path = dfs(initial_state, [initial_state], explored)

# Printing the path from the initial state to the goal state
if path:
    for state in path:
        print(state)
else:
    print("No valid path found.")
