symbols = {
    "i": 0,
    '+': 1,
    '-': 2,
    '(': 3,
    ')': 4,
    '$': 5
}

grammar = {
    "E": 0,
    "E'": 1,
    "T": 2
}

table = [["E->TE'", "", "", "E->TE'", "", ""],
         ["", "E'->+TE'", "E'->-TE'", "", "E'->e", "E'->e"],
         ["T->i", "", "", "T->(E)", "", ""]]

space = 40


def getColumn(inputSymbol):
    return symbols[inputSymbol]


def getRow(noGrammar):
    return grammar[noGrammar]


class Pile:
    def __init__(self):
        self.items = list()

    def empty(self):
        return self.items == list()

    def insert(self, item):
        self.items.append(item)

    def extract(self):
        return self.items.pop()

    def check(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def contents(self):
        return self.items


def Parser(p, input0, numbers):
    input1 = input0.copy()
    add = True
    total = 0
    output = ''
    print(' A N A L I Z A D O R   S I N T A C T I C O')
    print('PILA' + ' ' * (space - 4) + 'ENTRADA' + ' ' * (space - 7) + 'SALIDA')
    print(str(p.contents()) + ' ' * (space - len(str(p.contents()))) + str(input1) + ' ' * (
                space - len(str(input1))) + str(output))

    for inputSymbol in input0:
        topPila = p.check()
        while topPila != inputSymbol:
            col = getColumn(inputSymbol)
            row = getRow(topPila)
            output = table[row][col]
            if output != "":
                p.extract()
                position = output.find(">")
                production = output[position + 1:]
                productionPile = list()
                for symbol in production:
                    if symbol != "'":
                        position2 = production.find(symbol)
                        if production[position2 + 1:position2 + 2] == "'":
                            productionPile.append(symbol + "'")
                        else:
                            productionPile.append(symbol)
                for symbol in reversed(productionPile):
                    if symbol != 'e':
                        p.insert(symbol)
            print(str(p.contents()) + ' ' * (space - len(str(p.contents()))) + str(input1) + ' ' * (
                        space - len(str(input1))) + str(output))
            topPila = p.check()
        if inputSymbol == '$' and p.check() == '$':
            print('Analisis finalizado')
        else:
            extrae = p.extract()
            if extrae == 'i':
                if add:
                    total += int(numbers.pop(0))
                else:
                    total -= int(numbers.pop(0))
            else:
                if extrae == '+':
                    add = True
                elif extrae == '-':
                    add = False
            input1.pop(0)
            print(str(p.contents()) + ' ' * (space - len(str(p.contents()))) + str(input1))
    return total


def syntacticTree(p, input0, output):
    input1 = input0.copy()
    print("\nARBOL SINTACTICO:\n")
    for inputSymbol in input0:
        topPila = p.check()
        while topPila != inputSymbol:
            col = getColumn(inputSymbol)
            row = getRow(topPila)
            output = table[row][col]
            if output != '':
                print(p.extract())
                position = output.find('>')
                production = output[position + 1: len(output)]
                productionPile = list()
                for symbol in production:
                    if symbol != "'":
                        position2 = production.find(symbol)
                        if production[position2 + 1: position2 + 2] == "'":
                            productionPile.append(symbol + "'")
                        else:
                            productionPile.append(symbol)
                for symbol in reversed(productionPile):
                    if symbol != 'e':
                        p.insert(symbol)
                    else:
                        print(symbol)
            topPila = p.check()
        if inputSymbol == '$' and p.check() == '$':
            print('Arbol finalizado')
        else:
            print(p.extract())
            input1.pop(0)


def calculate(input0):
    global x
    l = list()
    numbers = ''
    input1 = list()
    for x in input0:
        if x not in ['+', '-', '(', ')']:
            numbers += x
        else:
            if numbers != '':
                l.append(numbers)
                input1.append('i')
            input1.append(x)
            numbers = ''
    l.append(numbers)
    if x != ')':
        input1.append('i')
    input1.append('$')
    return input1, l


if __name__ == "__main__":
    analyzer = Pile()
    analyzer.insert('$')
    analyzer.insert('E')
    tree = Pile()
    tree.insert('$')
    tree.insert('E')
    entrada, numeros = calculate(input('Ingrese numero: '))
    result1 = Parser(analyzer, entrada, numeros)
    syntacticTree(tree, entrada, "")
    print(f' El resultado de la expresion es: {result1}')
