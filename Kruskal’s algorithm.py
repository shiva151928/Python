def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller ranked tree under larger ranked tree
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot

    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal_mst(graph):

    result = []

    # Find number of vertices
    vertices = set()

    for edge in graph:
        vertices.add(edge[1])
        vertices.add(edge[2])

    v = len(vertices)

    # Sort edges according to weight
    graph.sort(key=lambda edge: edge[0])

    # Create parent and rank arrays
    parent = [i for i in range(v)]
    rank = [0] * v

    i = 0

    while len(result) < v - 1:

        weight, u, vertex = graph[i]
        i += 1

        # Find roots
        x = find(parent, u)
        y = find(parent, vertex)

        # If roots are different, no cycle is formed
        if x != y:
            result.append((weight, u, vertex))
            union(parent, rank, x, y)

    return result


def get_user_input():

    while True:
        try:

            # Get number of edges
            e = int(input("Enter the number of edges in the graph: "))

            if e <= 0:
                print("Please enter a positive integer.")
                continue

            graph = []

            print("Enter each edge in the format:")
            print("weight vertex1 vertex2")

            for _ in range(e):

                edge_input = input("Edge: ").strip()

                weight, u, v = map(int, edge_input.split())

                graph.append((weight, u, v))

            return graph

        except ValueError:
            print("Invalid input. Please enter integers only.")


# Main program
if __name__ == "__main__":

    graph = get_user_input()

    mst = kruskal_mst(graph)

    print("\nMinimum Cost Spanning Tree Edges:")

    total_cost = 0

    for edge in mst:
        print(edge)
        total_cost += edge[0]

    print("Minimum Cost =", total_cost)
