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


def get_Data():
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
    f.writelines([a, c, b, "\n"])

get_Data()
with open('testador.txt') as f:
    lines = f.readlines()
print(lines)
f.close()
