def dfs(initial_state, goal_state, visited, path, depth):
    if list(initial_state) == goal_state:
        return True
    
    if depth == 0:
        return False
    
    for i in range(len(initial_state)-1):
        successor_state = list(initial_state)
        successor_state[i], successor_state[i+1] = successor_state[i+1], successor_state[i]
        successor_state = tuple(successor_state)

        if successor_state not in visited:
            path.append(successor_state)
            visited.add(successor_state)

            if dfs(successor_state, goal_state, visited, path, depth-1):
                return True
    
    return False

def sort_numbers(numbers):
    goal_state = sorted(numbers)

    path = []
    depth = 0
    while(depth >= 0):
        initial_state = tuple(numbers)

        visited = set()
        visited.add(initial_state)

        path.append(initial_state)

        if dfs(initial_state, goal_state, visited, path, depth):
            return path
        else:
            depth += 1
            continue


input_str = input('Enter input: ')
input_list = input_str.split()
n = input_list[0]
numbers = input_list[1:]

path = sort_numbers(numbers)

print("Path:", path)
print('Total Number of nodes explored:', len(path))