def bfs(graph, start, end):
    #store the paths and visited users
    queue = []
    visited = set()
    queue.append([start])

    # Loop until queue is empty
    while queue:
        # Dequeue the first path in the queue
        path = queue.pop(0)
        # Get the last user in the path
        user = path[-1]

        # If user is the end user
        if user == end:
            # Exclude start and end users from mutual friends
            mfs = set(graph[start]) & set(graph[end])
            mfs.discard(start)
            mfs.discard(end)
            return mfs

        # user is not visited, mark it as visited
        if user not in visited:
            visited.add(user)

        #enqueue a new path with the friend added
        for friend in graph[user]:
            queue.append(path + [friend])

    # no mutual friends found, return empty set
    return set()


graph = {
    "Alala": {"Ned", "Atwiine", "Diana"},
    "Ned": {"Alala", "Atwiine", "Ian"},
    "Atwiine": {"Alala", "Ned", "Diana"},
    "Diana": {"Alala", "Atwiine", "Ian"},
    "Ian": {"Ned", "Diana"},
}

mfs = bfs(graph, "Alala", "Ian")

print(f"Mutual friends between 'Alala' and 'Ian': {mfs}")
