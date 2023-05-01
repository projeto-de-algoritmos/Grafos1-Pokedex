from collections import defaultdict
import tkinter as tk
import tkinter.messagebox
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

        print(f"No path from {start} to {end} found.")

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

f = open("pokedex.txt", "a")

def Mostra_Lista():
    file = open("pokedex.txt", "r")
    root = tk.Tk()
    root.configure(bg='#F96F6F')
    listbox = tk.Listbox(root, height = 30,
                  width = 30,
                  bg = "#F96F6F",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "black")
    # Define the size of the window.
    root.geometry("600x600") 
    i = 0
    lines = iter(file.readlines())
    while True:
        try:
            line = next(lines)
            listbox.insert(i, line)
            i+=1
        except StopIteration:
            break

    # Define a label for the list. 
    label = tk.Label(root, text = "Listagem pokemon")
    label.pack()
    listbox.pack()
    listbox.configure(justify='center')
    root.mainloop()
class Passwordchecker(tk.Frame):
    def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.initialize_user_interface()

    def initialize_user_interface(self):
       self.parent.geometry("600x600")
       self.parent.title("Inserir Pokemon")
       self.entry=tk.Entry(self.parent)
       self.entry.pack()
       self.entry.place(anchor = 'center', relx = .5, rely = .1)
       self.label=tk.Label(self.parent,text="Digite o nome de um pokemon", bg='#B8B7B7', fg='black')
       texto.config(font=('Helvetica bold', 26))
       self.label.pack()
       self.label.place(anchor = 'center', relx = .5, rely = .2)
       self.entry2=tk.Entry(self.parent)
       self.entry2.pack()
       self.entry2.place(anchor = 'center', relx = .5, rely = .3)
       self.label=tk.Label(self.parent,text="Digite o nome de sua evolução", bg='#B8B7B7', fg='black')
       texto.config(font=('Helvetica bold', 26))
       self.label.pack()
       self.label.place(anchor = 'center', relx = .5, rely = .4)
       self.button=tk.Button(self.parent,text="Inserir", bg='#7CFF00', activebackground="#BC03FC", command=self.Namecheck)
       self.button.pack(pady=20)
       self.button.place(anchor = 'center', relx = .5, rely = .5)
       self.button=tk.Button(self.parent,text="voltar", bg='#FF0036', activebackground="#BC03FC", command=self.destroy)
       self.button.pack(pady=20)
       self.button.place(anchor = 'center', relx = .5, rely = .6)

    def Namecheck(self):
        try:
            name = self.entry.get()
            evolution = self.entry2.get()
        except:
            self.label.config(text="Falha na inserção")
        if((name and evolution) != None):
            pokedex.add_pokemon(name, evolution)
            print("consegui adicionar", name, evolution)
            tk.messagebox.showinfo("Aviso!!",  "Adicionados a lista, para salvar em arquivo clique em [salvar pokedex]")

def Insert_Name():
    root = tk.Tk()
    root.configure(bg='#F96F6F')
    run = Passwordchecker(root)
    root.mainloop()

class Buscapokemon(tk.Frame):

    def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.user_interface()

    def user_interface(self):
       self.parent.geometry("600x600")
       self.parent.title("Inserir Pokemon")
       self.entry=tk.Entry(self.parent)
       self.entry.pack()
       self.entry.place(anchor = 'center', relx = .5, rely = .1)
       self.label=tk.Label(self.parent,text="Digite o pokemon que deseja iniciar a buscar", bg='#B8B7B7', fg='black')
       texto.config(font=('Helvetica bold', 26))
       self.label.pack()
       self.label.place(anchor = 'center', relx = .5, rely = .3)
       self.entry2=tk.Entry(self.parent)
       self.entry2.pack()
       self.entry2.place(anchor = 'center', relx = .5, rely = .2)
       self.label=tk.Label(self.parent,text="Digite o pokemon que deseja finalizar a buscar", bg='#B8B7B7', fg='black')
       texto.config(font=('Helvetica bold', 26))
       self.label.pack()
       self.button=tk.Button(self.parent,text="Buscar", bg='#7CFF00', activebackground="#BC03FC", command=self.BuscaNome)
       self.button.pack(pady=20)
       self.button.place(anchor = 'center', relx = .5, rely = .5)

    def BuscaNome(self):
        try:
            inicio = self.entry.get()
            fim = self.entry2.get()
            text = pokedex.dfs(inicio, fim)
            print(text)
            if text == None:
                raise Exception(tk.messagebox.showinfo("Aviso!!",  f"não encontramos evoluções para: {name} (*∩*)."))
            tk.messagebox.showinfo("Linha evolutiva",  text)
        except KeyError:
            tk.messagebox.showinfo("Aviso!!",  f"não encontramos evoluções para: {name} (*∩*).")
            

def Buscador_pokemon():
    root = tk.Tk()
    root.configure(bg='#F96F6F')
    run = Buscapokemon(root)
    root.mainloop()

class Alargabusca(tk.Frame):

    def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.user_interface()

    def user_interface(self):
       self.parent.geometry("600x600")
       self.parent.title("Inserir Pokemon")
       self.entry=tk.Entry(self.parent)
       self.entry.pack()
       self.entry.place(anchor = 'center', relx = .5, rely = .1)
       self.label=tk.Label(self.parent,text="Digite o pokemon que deseja iniciar a buscar", bg='#B8B7B7', fg='black')
       texto.config(font=('Helvetica bold', 26))
       self.label.pack()
       self.label.place(anchor = 'center', relx = .5, rely = .3)
       self.entry2=tk.Entry(self.parent)
       self.entry2.pack()
       self.entry2.place(anchor = 'center', relx = .5, rely = .2)
       self.label=tk.Label(self.parent,text="Digite o pokemon que deseja finalizar a buscar", bg='#B8B7B7', fg='black')
       texto.config(font=('Helvetica bold', 26))
       self.label.pack()
       self.button=tk.Button(self.parent,text="Buscar", bg='#7CFF00', activebackground="#BC03FC", command=self.BuscaNome)
       self.button.pack(pady=20)
       self.button.place(anchor = 'center', relx = .5, rely = .5)

    def BuscaNome(self):
        try:
            inicio = self.entry.get()
            fim = self.entry2.get()
            text = pokedex.bfs(inicio, fim)
            print(text)
            if text == None:
                raise Exception(tk.messagebox.showinfo("Aviso!!",  f"não encontramos evoluções para: {name} (*∩*)."))
            tk.messagebox.showinfo("Linha evolutiva",  text)
        except KeyError:
            tk.messagebox.showinfo("Aviso!!",  f"não encontramos evoluções para: {name} (*∩*).")
            

def BuscaLarga():
    root = tk.Tk()
    root.configure(bg='#F96F6F')
    run = Alargabusca(root)
    root.mainloop()

def Save_Pokedex():
    with open("pokedex.txt", "w") as f:
            for pokemon, evolutions in pokedex.graph.items():
                f.write(f"{pokemon} {' '.join(evolutions)}\n")
    print("Pokedex armazenada!!")
    tk.messagebox.showinfo("Aviso!!",  "Pokedex armazenada")

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
    janela.geometry('600x600')
    janela.title("Pokedex customizada!")
    janela.configure(bg='#F96F6F')
    texto = tk.Label(janela, text="Bem vindo a pokedex customizada!!", bg='#B8B7B7', fg='black')
    texto.config(font=('Helvetica bold', 26))
    texto.place(anchor = 'center', relx = .5, rely = .1)
    #print("\nMenu:")
    #choice = input("Escolha uma opção entre (1-6): ")
    botao1 = tk.Button(janela, text="1. Adicionar pokemon", bg='#6FF9DE', activebackground="#BC03FC", command=Insert_Name)
    #botao1.grid(column=0, row=1, padx=50, pady=90)
    botao1.place(anchor = 'center', relx = .5, rely = .3)

    botao2 = tk.Button(janela, text="2. Mostrar pokedex", bg='#A1F968', activebackground="#BC03FC", command=Mostra_Lista)
    #botao2.grid(column=1, row=1, padx=50, pady=90)
    botao2.place(anchor = 'center', relx = .5, rely = .4)

    botao3 = tk.Button(janela, text="3. Salvar pokedex", bg='#689EF9', activebackground="#BC03FC", command=Save_Pokedex)
    #botao3.grid(column=0, row=3, padx=50, pady=90)
    botao3.place(anchor = 'center', relx = .5, rely = .5)

    botao4 = tk.Button(janela, text="4. Busca usando profundidade (DFS)", bg='#F9F068', activebackground="#BC03FC", command=Buscador_pokemon)
    #botao4.grid(column=1, row=3, padx=50, pady=90)
    botao4.place(anchor = 'center', relx = .5, rely = .6)

    botao5 = tk.Button(janela, text="5. Busca usando largura (BFS)", bg='#F9A968', activebackground="#BC03FC", command=BuscaLarga)
    #botao5.grid(column=0, row=6, padx=50, pady=90)
    botao5.place(anchor = 'center', relx = .5, rely = .7)

    botao6 = tk.Button(janela, text="6. SAIR", bg='#F96879',  activebackground="#BC03FC", command=exit)
    #botao6.grid(column=1, row=6, padx=50, pady=90)
    botao6.place(anchor = 'center', relx = .5, rely = .8)

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
        print("jonis")

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

    else:
        print("Escolha invalida. Por favor tente novamente!!")
        #print("dummy call dfs:", pokedex.dfs("Arceus"))
    janela.mainloop()