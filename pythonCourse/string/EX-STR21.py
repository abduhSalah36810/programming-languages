# middle string exercise

input1 = input("a word please : ").strip()
input2 = input("another word please : ").strip()
y = int(len(input1)*0.5)
print(f"{input1[0:y]}{input2}{input1[y:int(len(input1))]}")


