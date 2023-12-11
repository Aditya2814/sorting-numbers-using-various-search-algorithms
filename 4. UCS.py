'''
In this scenario, all successor states generated from a given state have the same 
path cost, as determined by the given successor function. Since all of these successor 
states have identical path costs, they will all be explored. Therefore, the exploration 
technique is similar to Breadth-First Search, with the only difference being that a 
Priority Queue is used instead of a regular Queue.
'''

import heapq

def sort_numbers(numbers):
    goal_state = sorted(numbers)

    initial_state = tuple(numbers)

    priority_queue = [(0, initial_state)]

    visited = set()
    visited.add(initial_state)

    path = []

    while priority_queue:
        path_cost, current_state = heapq.heappop(priority_queue)

        path.append(current_state)

        if list(current_state) == goal_state:
            return path
        
        for i in range(len(current_state)-1):
            successor_state = list(current_state)
            successor_state[i], successor_state[i+1] = successor_state[i+1], successor_state[i]
            successor_state = tuple(successor_state)

            if successor_state not in visited:
                heapq.heappush(priority_queue, (path_cost+1, successor_state))
                visited.add(successor_state)

    return None


input_str = input('Enter input: ')
input_list = input_str.split()
n = input_list[0]
numbers = input_list[1:]

path = sort_numbers(numbers)

print("Path:", path)
print('Total Number of nodes explored:', len(path))