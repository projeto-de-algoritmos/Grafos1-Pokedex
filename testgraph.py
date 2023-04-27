from collections import defaultdict


class Pokedex:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_pokemon(self, name, evolution):
        self.graph[name].append(evolution)

    def show_pokedex(self):
        print("Pokedex:")
        for pokemon in self.graph.keys():
            evolutions = ", ".join(self.graph[pokemon])
            print(f"{pokemon}: {evolutions}")

f = open("testador.txt", "a")

def bfs(self, start, end):
    visited = set()
    queue = [start]
    prev = {start: None}

    while queue:
        node = queue.pop(0)

        if node == end:
            path = [end]
            while prev[path[-1]] is not None:
                path.append(prev[path[-1]])
            path.reverse()
            print(" -> ".join(path))
            return

        if node not in visited:
            visited.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    prev[neighbor] = node

    print(f"Nenhum caminho de {start} para {end} encontrado.")


'''def get_Data():
    i = 0
    a = input('pokemon name ')
    print('seu pokemon se chama :', a , 'esta correto?')
    confirm = input('1 para sim e 0 para não')
    if(not confirm):
        i = 0
    while i != 0:
        a = input('pokemon name ')
        print('seu pokemon se chama :', a , 'esta correto?')
        confirm = ('1 para sim e 0 para não')
        if(not confirm):
            i = 0
    b = input('Qual o nome da evolução dele?')
    c = "->"
    f.writelines([a, c, b, "\n"])'''

if __name__ == "__main__":
    pokedex = Pokedex()
    # Load pokedex from file
    try:
        with open("testador.txt", "r") as f:
            for line in f:
                name, *evolutions = line.strip().split()
                for evolution in evolutions:
                    pokedex.add_pokemon(name, evolution)
    except FileNotFoundError:
        pass

    while True:
        print("\nMenu:")
        print("1. Add pokemon")
        print("2. Show pokedex")
        print("3. Save pokedex")
        print("4. DFS search")
        print("5. BFS search")
        print("6. Quit")
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            name = input("Enter pokemon name: ")
            evolution = input("Enter evolution: ")
            pokedex.add_pokemon(name, evolution)
            print(f"{name} added to pokedex.")

        elif choice == "2":
            pokedex.show_pokedex()

        elif choice == "3":
            with open("pokedex.txt", "w") as f:
                for pokemon, evolutions in pokedex.graph.items():
                    f.write(f"{pokemon} {' '.join(evolutions)}\n")
            print("Pokedex saved to file.")

        elif choice == "4":
            print("function under construction!!!")

        elif choice == "5":
            name = input("Enter pokemon name to search: ")
            try:
                print(f"BFS search starting from {name}:")
                pokedex.bfs("Arceus", name)
            except KeyError:
                print(f"{name} not found in pokedex.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
