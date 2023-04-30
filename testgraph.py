from collections import defaultdict
import tkinter as tk
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

class Passwordchecker(tk.Frame):
    def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.initialize_user_interface()

    def initialize_user_interface(self):
       self.parent.geometry("400x400")
       self.parent.title("Inserir Pokemon")
       self.entry=tk.Entry(self.parent)
       self.entry.pack()
       self.label=tk.Label(self.parent,text="Digite o nome de um pokemon")
       self.label.pack()
       self.entry2=tk.Entry(self.parent)
       self.entry2.pack()
       self.label=tk.Label(self.parent,text="Digite o nome de sua evolução")
       self.label.pack()
       self.button=tk.Button(self.parent,text="Inserir", command=self.Namecheck)
       self.button.pack()

    def Namecheck(self):
        try:
            name = self.entry.get()
            evolution = self.entry2.get()
        except:
            self.label.config(text="Falha na inserção")
        pokedex.add_pokemon(name, evolution)

def Insert_Name():
    root = tk.Tk()
    run = Passwordchecker(root)
    root.mainloop()

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

def dfs(self, start, end, visited=None, prev=None):
        if visited is None:
            visited = set()
        if prev is None:
            prev = {start: None}

        visited.add(start)

        if start == end:
            path = [end]
            while prev[path[-1]] is not None:
                path.append(prev[path[-1]])
            path.reverse()
            print(" -> ".join(path))
            return

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                prev[neighbor] = start
                self.dfs(neighbor, end, visited, prev)

        if start == prev[start]:
            print(f"No path from {start} to {end} found.")

if __name__ == "__main__":
    pokedex = Pokedex()
    # Load pokedex from file

    try:
        with open("pokedex.txt", "r") as f:
            for line in f:
                name, *evolutions = line.strip().split()
                for evolution in evolutions:
                    pokedex.add_pokemon(name, evolution)
    except FileNotFoundError:
        pass

    choice=0

    janela = tk.Tk()
    janela.geometry('400x400')
    janela.title("Pokedex customizada!")
    texto = tk.Label(janela, text="Bem vindo a pokedex customizada!!")
    texto.grid(column=0, row=0, padx=10, pady=10)
    #print("\nMenu:")
    #choice = input("Escolha uma opção entre (1-6): ")
    botao1 = tk.Button(janela, text="1. Adicionar pokemon", command=Insert_Name)
    botao1.grid(column=0, row=1, padx=10, pady=10)

    botao2 = tk.Button(janela, text="2. Mostrar pokedex", command=2)
    botao2.grid(column=0, row=2, padx=10, pady=10)

    botao3 = tk.Button(janela, text="3. Salvar pokedex", command=3)
    botao3.grid(column=0, row=3, padx=10, pady=10)

    botao4 = tk.Button(janela, text="4. Busca usando profundidade (DFS)", command=4)
    botao4.grid(column=0, row=4, padx=10, pady=10)

    botao5 = tk.Button(janela, text="5. Busca usando largura (BFS)", command=5)
    botao5.grid(column=0, row=5, padx=10, pady=10)

    botao6 = tk.Button(janela, text="6. SAIR", command=exit)
    botao6.grid(column=0, row=6, padx=10, pady=10)

    while True:
        '''print("\nMenu:")
        choice = input("Escolha uma opção entre (1-6): ")
        print("1. Adicionar pokemon")
        print("2. Mostrar pokedex")
        print("3. Salvar pokedex")
        print("4. Busca usando profundidade (DFS)")
        print("5. Busca usando largura (BFS)")
        print("6. SAIR")'''
        

        if choice == "1":
            print("dummy print")

        elif choice == "2":
            pokedex.show_pokedex()

        elif choice == "3":
            with open("pokedex.txt", "w") as f:
                for pokemon, evolutions in pokedex.graph.items():
                    f.write(f"{pokemon} {' '.join(evolutions)}\n")
            print("Pokedex armazenada!!")

        elif choice == "4":
            name = input("Qual pokemon deseja buscar: ")
            try:
                print(f"DFS search starting from {name}:")
                pokedex.dfs("Arceus", name)
            except KeyError:
                print(f"{name} Pokemon não encontrado (*∩*).")

        elif choice == "5":
            name = input("Qual pokemon deseja buscar: ")
            try:
                print(f"BFS search starting from {name}:")
                pokedex.bfs("Arceus", name)
            except KeyError:
                print(f"{name} Pokemon não encontrado (*∩*).")

        elif choice == "6":
            print("Tchau Tchau!")
            break

        else:
            print("Escolha invalida. Por favor tente novamente!!")
        janela.mainloop()