#input1 =input(str("what u want : "  )).lower()
#print(input1)

lines = []
while True : 
        l = input()
        if l:
            lines.append(l.upper())
        else:
            break;

for l in lines:
            print(l)
	