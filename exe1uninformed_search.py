class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []
            print("Node added to graph")
            print("")
        else:
            print("Node already exists")
            print("")

    def delete_node(self, node):
        if node in self.adj:
            for i in self.adj:
                self.adj[i] = [x for x in self.adj[i] if x[0] != node]
            del self.adj[node]
            print("Node deleted from graph")
            print("")
        else:
            print("Node not found")
            print("")

    def add_edge(self, n1, n2, cost):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1].append((n2, cost))
            self.adj[n2].append((n1, cost))
            print("Edge added to graph")
            print("")
        else:
            print("Both nodes must exist")
            print("")

    def delete_edge(self, n1, n2):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1] = [x for x in self.adj[n1] if x[0] != n2]
            self.adj[n2] = [x for x in self.adj[n2] if x[0] != n1]
            print("Edge deleted from graph")
            print("")
        else:
            print("Nodes not found")
            print("")

    def display(self):
        print("\nAdjacency List:")
        for i in self.adj:
            print(i, "->", self.adj[i])

def bfs(graph, start, goal):
    if start not in graph.adj or goal not in graph.adj:
        print("Start or Goal node not found")
        return
    visited = []
    fringe = []
    print("\nBFS:")
    fringe.append(start)
    while fringe:
        current = fringe.pop(0)
        print("\nDequeue:", current)
        if current not in visited:
            visited.append(current)
            print("Visited:", visited)
            if current == goal:
                print("\nGoal node", goal, "found!")
                print("Final Visited Order:", visited)
                return
            for i, _ in graph.adj[current]:
                if i not in visited and i not in fringe:
                    fringe.append(i)
                    print("Enqueue:", i)
            print("Fringe:", fringe)
    print("\nGoal not found")
    print("Visited order:", visited)

def dfs(graph, start, goal):
    if start not in graph.adj or goal not in graph.adj:
        print("Start or Goal node not found")
        return
    visited = []
    stack = [start]
    print("\nDFS:")
    while stack:
        current = stack.pop()
        print("Pop:", current)
        if current not in visited:
            visited.append(current)
            print("Visited:", visited)
            if current == goal:
                print("\nGoal found")
                print("Visited order:", visited)
                return
            neighbors = []
            for i, _ in graph.adj[current]:
                if i not in visited:
                    neighbors.append(i)
            stack.extend(reversed(neighbors))
            print("Stack:", stack)
    print("\nGoal not found")
    print("Visited order:", visited)
def ucs(graph, start, goal):
    visited = []
    queue = [(start, 0, [start])]
    fringe = [start]
    print("Initial fringe:", fringe)

    while queue:
        min_index = 0
        for i in range(len(queue)):
            if queue[i][1] < queue[min_index][1]:
                min_index = i
        current, cost, path = queue.pop(min_index)
        print(current)
        if current == goal:
            print("Goal node found.")
            print("Visited nodes:", visited + [current])
            print("Final path:", path)
            print("Total cost:", cost)
            return
        if current not in visited:
            visited.append(current)
            for i, c in graph.adj[current]:
                if i not in visited:
                    queue.append((i, cost + c, path + [i]))
                    fringe.append(i)
        print("Fringe after processing node", current, ":", fringe)

    print("Goal node not found")
    print("Visited:", visited)

graph = Graph()

n = int(input("Enter no of nodes: "))
for _ in range(n):
    graph.add_node(input("Enter node to add: "))

e = int(input("Enter no of edges: "))
for _ in range(e):
    n1 = input("Enter 1st node: ")
    n2 = input("Enter 2nd node: ")
    cost = int(input("Enter cost: "))
    graph.add_edge(n1, n2, cost)

while True:
    print("\n1. Add Node")
    print("2. Delete Node")
    print("3. Add Edge")
    print("4. Delete Edge")
    print("5. Display Graph")
    print("6. BFS")
    print("7. DFS")
    print("8. UCS")
    print("9. Exit")
    ch = int(input("Enter choice: "))
    print("")
    if ch == 1:
        graph.add_node(input("Enter node to add: "))
        print("")
    elif ch == 2:
        graph.delete_node(input("Enter node to delete: "))
        print("")
    elif ch == 3:
        n1 = input("Enter 1st node: ")
        print("")
        n2 = input("Enter 2nd node: ")
        print("")
        cost = int(input("Enter cost: "))
        print("")
        graph.add_edge(n1, n2, cost)
    elif ch == 4:
        graph.delete_edge(input("Enter 1st node: "), input("Enter 2nd node: "))
    elif ch == 5:
        graph.display()
    elif ch == 6:
        bfs(graph, input("Start node: "), input("Goal node: "))
    elif ch == 7:
        dfs(graph, input("Start node: "), input("Goal node: "))
    elif ch == 8:
        ucs(graph, input("Start node: "), input("Goal node: "))
    elif ch == 9:
        print("Exiting")
        break
    else:
        print("Invalid choice")
