import array
from random import *
import array
#import numpy

class kromoson:
    def __init__(self):
        self.arrayBinary =  []
        ##perulangan dengan rentang 8 menggunakan library random binary. 
        # #untuk memperoleh biner
        for i in range(8) :
            self.arrayBinary.append(randint(0, 1))
        ##0 dan 1 digunakan sebagai bilangan binernya
        self.populasi = 0
        self.obj = 0 #digunakan untuk menampung objek
        self.probabilitas =0
        self.nilaiFitnes = 0
##men decode batas x1 x2 ke biner
def decodeToBinary(kromoson):
    x1 = -3+((3+3)/((2**-1)+(2**-2)+(2**-3)+(2**-4)))*((kromoson.arrayBinary[0]*(2**-1))+(kromoson.arrayBinary[1]*(2**-2))+(kromoson.arrayBinary[2]*(2**-3))+(kromoson.arrayBinary[3]*(2**-4))) 
    x2 = -2+((2+2)/((2**-1)+(2**-2)+(2**-3)+(2**-4)))*((kromoson.arrayBinary[4]*(2**-1))+(kromoson.arrayBinary[5]*(2**-2))+(kromoson.arrayBinary[6]*(2**-3))+(kromoson.arrayBinary[7]*(2**-4)))
    # ##rumus diatas digunakan untuk men decode ke biner x2 yaitu -2 <= x2 ,= -2
    #  x1 = round(x1, 2)
    #  x2 = round(x2, 2)
    return x1, x2

def nilaiFitnes(kromoson) : 
    return (1/( kromoson.obj + 0.00001))
    ##perhitungan nilai fitnes menggunakan f= (1/(hta))

def hitungPopulasi(kromoson) :
    populasi = []
    for i in range(8):
        populasi.append(kromoson())
    return populasi
    #dalam kasus ini populasi yang digunakan sebanyak 8

def nilaiObj(kromoson):
    y = decodeToBinary(kromoson)
    x1 = y[0]
    x2 = y[1]
    return round(((4 -(2 * (x1**2)) + ((x1**4)/3)) * (x1 ** 2)) + (x1*x2) + ((-4 + (4 * x2**2))* (x2**2)))
    ##fungsi ini digunakan untuk menghitung nilai h untuk mencari fitness

def probabilitas(populasi):
    nilaiFitnes = 0
    for i in populasi:
        nilaiFitnes += populasi.fitnes
    for i in populasi:
        populasi.probabilitas = populasi.fitnes/nilaiFitnes
    return populasi.probabilitas
    ##fungsi ini digunakan untuk mencari probabilitas nilai total nilai fitnes

def seleksiOrtu(populasi):
    best = 0
    for i in populasi :
        best += populasi.nilaiFitnes
    r = randonuniform()
    return
    #fungsi seleksi ortu menggunakan metode roulette wheel selecton

def crossOver(kromoson, a, b):
    c = a[0:4] + b[4:8]
    d = b[0:4] + a[4:8]
    return (c, d)
    #digunakan untuk mengcrossover dari parent dengan nilai fitness terbaik
    
def mutasi(parent):
    persentasiMutasi = 0.6
    for i in range(len(kromoson)):
        r = uniform(0, 1)
        if (r < persentasiMutasi) :
            y = uniform(0, 1)
            parent.kromoson = float(y)
    #persentasi mutasi menggunakan probabilitas 60%


def gantiGenerasi(kromoson):
    populasi = newpopulasi(i)
    nilaiFitnes = evaluate(populasi)
    a, b = parentselection(populasi)
    offspring = crossOver(kromoson, a, b)
    offspring = mutasi(offspring, pm)
    populasi = gammavariate(offspring, offspring)
    #ganti generasi menggunakan metode steady state



kromoson = kromoson()
kromoson.obj = nilaiObj(kromoson)
kromoson.nilaiFitnes = nilaiFitnes(kromoson)
# kromoson.populasi = hitungPopulasi(kromoson) di command karena tidak untuk ditampilkan

print('x1, x2   : ',  decodeToBinary(kromoson))
print('Objektif : ', kromoson.obj)
print('Fitness  : ', kromoson.nilaiFitnes )
# print('Populasi : ', kromoson.populasi)
  




