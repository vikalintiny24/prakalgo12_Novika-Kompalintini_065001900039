# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 18:40:30 2022

@author: vikal
"""

def elkom1():
    print("LINEAR SEARCH")
    panjang = int(input("Masukkan Jumlah Angka Pada List : "))
    list_linear = []
    for i in range(panjang):
        list_linear.append(int(input("Angka Ke-{}: ".format(i + 1))))
    print("\nList Angka -> ", list_linear)

    def linearsearch(list_linear, x):
        for i in range(len(list_linear)):
            if list_linear[i] == x:
                return "Ditemukan\n"
        return "Tidak Ditemukan\n"

    x = int(input("Masukkan angka yang dicari : "))
    print("Hasil Linear Search -> " + str(linearsearch(list_linear, x)))


def elkom2():
    print("BINARY SEARCH")
    panjang = int(input("Masukkan Jumlah Angka Pada List: "))
    list_binary = []
    for i in range(panjang):
        list_binary.append(int(input("Angka Ke-{}: ".format(i + 1))))
    print("\nList Angka -> ", list_binary)

    list_binary = sorted(list_binary)
    print("\nList Angka Terurut -> {}\n".format(list_binary))

    def binary_search(list_binary, x, kiri, kanan):
        if kanan >= kiri:
            tengah = kiri + (kanan - kiri) // 2
            if list_binary[tengah] == x:
                return tengah
            elif list_binary[tengah] > x:
                return binary_search(list_binary, x, kiri, tengah - 1)
            else:
                return binary_search(list_binary, x, tengah + 1, kanan)
        else:
            return False

    dicari = int(input("Masukkan angka yang dicari: "))

    result = binary_search(list_binary, dicari, 0, len(list_binary) - 1)

    if result:
        print("Ditemukan di indeks: {}\n".format(str(result)))
    else:
        print("Tidak ditemukan\n")


def elkom3():
    print("BUBBLE SORT")
    panjang = int(input("Masukkan Jumlah Angka Pada List: "))
    list_bubble = []
    for i in range(panjang):
        list_bubble.append(int(input("Angka Ke-{}: ".format(i + 1))))
    print("\nList Angka -> ", list_bubble)

    def bubble_sort(list_bubble):
        for i in range(0, len(list_bubble) - 1):
            for j in range(len(list_bubble) - 1):
                if (list_bubble[j] > list_bubble[j + 1]):
                    temp = list_bubble[j]
                    list_bubble[j] = list_bubble[j + 1]
                    list_bubble[j + 1] = temp
        return list_bubble

    print("Hasil Bubble Sort -> " + str(bubble_sort(list_bubble)))
    print("")


def elkom4():
    print("SELECTION SORT")
    panjang = int(input("Masukkan Jumlah Angka Pada List: "))
    list_selection = []
    for i in range(panjang):
        list_selection.append(int(input("Angka Ke-{}: ".format(i + 1))))
    print("\nList Angka -> ", list_selection)

    def selection_sort(list_selection, panjang):
        for langkah in range(panjang):
            indeks_terkecil = langkah
            for i in range(langkah + 1, panjang):
                if list_selection[i] < list_selection[indeks_terkecil]:
                    indeks_terkecil = i
            (list_selection[langkah], list_selection[indeks_terkecil]) = (
            list_selection[indeks_terkecil], list_selection[langkah])
        return list_selection

    print("Hasil Selection Sort -> " + str(selection_sort(list_selection, panjang)))
    print("")

def mulai():
    while True:
        pilihan = input("Elkom?: ")
        print("")
        if pilihan == "1":
            elkom1()

        elif pilihan == "2":
            elkom2()

        elif pilihan == "3":
            elkom3()

        elif pilihan == "4":
            elkom4()

        elif pilihan == "e":
            break
        else:
            print("Pilih 1, 2, 3, 4 atau e untuk keluar\n")


if __name__ == "__main__":
    mulai()