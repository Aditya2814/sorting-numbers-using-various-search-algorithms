import heapq

def heuristic_function(state, goal_state): # calculates number of misplaced values comparing with goal state.
    misplaced_count = 0
    
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            misplaced_count += 1

    return misplaced_count


def sort_numbers(numbers):
    goal_state = sorted(numbers)

    initial_state = tuple(numbers)

    priority_queue = [(0 + heuristic_function(initial_state, goal_state), 0, initial_state)]

    visited = set()
    visited.add(initial_state)

    path = []

    while priority_queue:
        f_cost, path_cost, current_state = heapq.heappop(priority_queue)

        path.append(current_state)

        if list(current_state) == goal_state:
            return path
        
        for i in range(len(current_state)-1):
            successor_state = list(current_state)
            successor_state[i], successor_state[i+1] = successor_state[i+1], successor_state[i]
            successor_state = tuple(successor_state)

            if successor_state not in visited:
                heapq.heappush(priority_queue, (path_cost+1+heuristic_function(successor_state, goal_state), path_cost+1, successor_state))
                visited.add(successor_state)

    return None


input_str = input('Enter input: ')
input_list = input_str.split()
n = input_list[0]
numbers = input_list[1:]

path = sort_numbers(numbers)

print("Path:", path)
print('Total Number of nodes explored:', len(path))