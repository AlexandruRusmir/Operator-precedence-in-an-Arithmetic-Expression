class Stack():
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


#Arithmetic operators priorities
priority = {
    "#" : 0,
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2
}


def annoyance(s1, s2):
    print("Operators: ", end = " ")
    print(s1.get_stack(), end = " ")
    print(" The last operator is bothered by " + el, end = " ; ")
    print("Operands: ", end = " ")
    print(s2.get_stack())
    aux = s2.peek()
    s2.pop()
    if not s2.is_empty() and not s1.is_empty():
        new_operand = ""
        if(s1.peek()[1] >= 10):
            new_operand += "("
        new_operand += s2.peek() + s1.peek()[0]
        new_operand += aux
        if(s1.peek()[1] >= 10):
            new_operand += ")"
        s2.pop()
        s2.push(new_operand)
        s1.pop()
        s1.push([el, priority[el] + brackets * 10])
    


s1 = Stack() #Operators stack
s2 = Stack() #Operands stack
expression = input()
expression = "#" + expression + "#"

brackets = 0
for el in expression:
    
    if el not in priority and el != "(" and el != ")":
        s2.push(el)

        
    elif el in priority:

        if s1.is_empty():
            s1.push([el, priority[el]+ brackets * 10])

        elif s1.peek()[1] < priority[el] + brackets * 10:
            s1.push([el, priority[el] + 10 * brackets])
        
        else:
            annoyance(s1, s2)
            while True:
                
                aux = s1.peek()
                s1.pop()
                if  s1.peek()[0] != "#":
                    if not s1.peek()[1] < aux[1]:
                        annoyance(s1, s2)
                
                    else:
                        s1.push(aux)
                        break
                else:
                    s1.push(aux)
                    break

    elif el == "(":
            brackets += 1

    elif el == ")":
        brackets -=1
        

        
print(s1.get_stack(), end = " ")
print("The end: ", end = " ")
print(s2.get_stack())
