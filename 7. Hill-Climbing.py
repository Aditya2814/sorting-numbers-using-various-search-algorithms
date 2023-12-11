import heapq

def heuristic_function(state, goal_state):
    misplaced_count = 0
    
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            misplaced_count += 1

    return misplaced_count


def sort_numbers(numbers):
    goal_state = sorted(numbers)

    initial_state = tuple(numbers)

    visited = set()
    visited.add(initial_state)

    path = []

    priority_queue = [(heuristic_function(initial_state, goal_state), initial_state)]

    while True:
        current_state = heapq.heappop(priority_queue)[1]
        priority_queue = []

        path.append(current_state)

        if list(current_state) == goal_state:
            return path

        for i in range(len(current_state)-1):
            successor_state = list(current_state)
            successor_state[i], successor_state[i+1] = successor_state[i+1], successor_state[i]
            successor_state = tuple(successor_state)

            if successor_state not in visited:
                visited.add(successor_state)
                heapq.heappush(priority_queue, (heuristic_function(successor_state, goal_state), successor_state))

    return None
        

input_str = input('Enter input: ')
input_list = input_str.split()
n = input_list[0]
numbers = input_list[1:]

path = sort_numbers(numbers)

print('Final State:', path[len(path)-1])
print('Total Number of nodes explored:', len(path))