f = open("testador.txt", "a")

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