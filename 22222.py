n=int(input('Dati numarul de elemente din vector='))
z=[]
# if n<10:
# print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(n):
    x=int(input('Dati elementul='))
    z.append(x)
print(z)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
for i in range(0, len(z), 5):
    print(z[i])

print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
print(z[::-1])

print('c)  sortează componentele tabloului în ordine descrescătoare;')
c=sorted(z)
c.sort(reverse=True)
print(c)

print('d)  afişează pe ecran doar componentele pare;')
d=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        d.append(z[i])
print(d)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')

media = 0
for i in d:
   media += i
print('media este: ', media/len(d) )

print('f)  afişează pe ecran doar componentele impare;')
numere_impare = []
for i in range(0,len(z)):
    if z[i]%2!=0:
        numere_impare.append(z[i])
print(numere_impare)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x= int(input('introdu x: '))
y= int(input('introdu y: '))
for n in z:
    if x < n and n % y != 0:
        print(n)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x= int(input('introdu x: '))
y= int(input('introdu y: '))
for n in z:
    if x < n < y:
        print(n)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
for i, n in enumerate(z):
    if n < 0:
        print(i)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
for n in z:
    if 9 < n < 100:
        print(n)
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
z[0] = min(z)
print(z)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
n=int(input('Dati numarul de elemente din vector='))
nr_pare = []
for i in range(n):
    x = int(input('introdu elementul: '))
    if x % 2 == 0:
        nr_pare.append(x)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=int(input('Dati numarul de elemente din vector='))
arr = []
for i in range(n):
    x = int(input('introdu elementul: '))
    if x % 3 == 0:
        arr.append(x)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')