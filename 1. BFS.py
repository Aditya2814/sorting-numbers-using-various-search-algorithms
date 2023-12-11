def sort_numbers(numbers):
    goal_state = sorted(numbers)

    initial_state = tuple(numbers)

    queue = [initial_state]

    visited = set()
    visited.add(initial_state)

    path = []
    
    while queue:
        current_state = queue[0]
        queue.pop(0)

        path.append(current_state)

        if list(current_state) == goal_state:
            return path
        
        for i in range(len(current_state)-1):
            succesor_state = list(current_state)
            succesor_state[i], succesor_state[i+1] = succesor_state[i+1], succesor_state[i]
            succesor_state = tuple(succesor_state)
            
            if succesor_state not in visited:
                queue.append(succesor_state)
                visited.add(succesor_state)

    return None

input_str = input('Enter input: ')
input_list = input_str.split()
n = input_list[0]
numbers = input_list[1:]

path = sort_numbers(numbers)

print("Path:", path)
print('Total Number of nodes explored:', len(path))