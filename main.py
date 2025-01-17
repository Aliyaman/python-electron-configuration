from get_elem import get_electron
orbitals = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
electron_listesi = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
super_scripts = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', '¹⁰', '¹¹', '¹²', '¹³', '¹⁴']
result = []

print("Electron Configuration by element symbol or Electron value")

choice = input("1)Element \n2)Electron value: ")

if choice == "1":
    element = input("Enter element symbol(Upper-Lowercase sensitive): ")
    electron = get_electron(element) 
elif choice == "2":
    electron = int(input("Electron value: "))

i = 0

while True:
    if electron - electron_listesi[i] >= 0:
        electron -= electron_listesi[i]
        result.append(orbitals[i])
        result.append(electron_listesi[i])
        i+=1
    elif electron - electron_listesi[i] < 0:
        result.append(orbitals[i])
        result.append(electron)
        break

print("Without superscipt: ",end="")
for i in range(0,len(result),2):
    print("".join(str(result[i])+str(result[i+1])),end=" ")

print("\n")
print("With superscipt: ",end="")

for i in result:
    index_ = result.index(i)
    if type(i) == int:
        result[index_] = super_scripts[i-1]

for i in range(0,len(result),2):
    print("".join(str(result[i])+str(result[i+1])),end=" ")

