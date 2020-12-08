import tkinter as tk
from tkinter import ttk
from tkinter import *
from math import *
import pprint

FONT = ("Times New Roman", 20, "bold")
FONTS = ("Times New Roman", 20)
font = ("Times New Roman", 18)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class spiralcipher:
    def __init__(self, master):
        master.title("Spiral Cipher")
        master.configure(background='rosybrown2')
        self.plaintext = tk.StringVar(master, value="")
        self.ciphertext = tk.StringVar(master, value="")
        self.gambar = PhotoImage(
            file="c:/Users/User/Documents/TI UNPAD/SEMESTER 5/Kriptografi/Praktikum/UAS/shift-spiral/crypto.png")
        w1 = Label(root, image=self.gambar).grid(
            row=1, column=1)
        self.plain_label = tk.Label(
            master, text="SPIRAL CIPHER", fg="black", font=FONT, bg='rosybrown2').grid(row=0, column=1, pady=40)

        # Plaintext controls
        self.plain_label = tk.Label(
            master, text="Plaintext", fg="black", font=FONT, bg='rosybrown2').grid(row=2, column=0, padx=90, pady=18)
        self.plain_entry = tk.Entry(master,
                                    textvariable=self.plaintext, width=50, font=FONTS)
        self.plain_entry.grid(row=2, column=1, padx=20)
        self.espiral_button = tk.Button(master, text="Encrypt",
                                        command=lambda: self.encrypt_callback(), font=font, bg='salmon4').grid(row=2, column=2)
        self.plain_clear = tk.Button(master, text="Clear",
                                     command=lambda: self.clear('plain'), font=font).grid(row=2, column=3)

        # Ciphertext controls
        self.cipher_label = tk.Label(
            master, text="Ciphertext", fg="black", font=FONT, bg='rosybrown2').grid(row=3, column=0)
        self.cipher_entry = tk.Entry(master,
                                     textvariable=self.ciphertext, width=50, font=FONTS)
        self.cipher_entry.grid(row=3, column=1, padx=20)
        self.dspiral_button = tk.Button(master, text="Decrypt",
                                        command=lambda: self.decrypt_callback(), font=font, bg='salmon4').grid(row=3, column=2)
        self.cipher_clear = tk.Button(master, text="Clear",
                                      command=lambda: self.clear('cipher'), font=font).grid(row=3, column=3)

    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        elif str_val == 'plain':
            self.plain_entry.delete(0, 'end')

    def encrypt_callback(self):
        x = encrypt(self.plain_entry.get())
        self.cipher_entry.delete(0, tk.END)
        self.cipher_entry.insert(0, x)

    def decrypt_callback(self):
        x = decrypt(self.cipher_entry.get())
        self.plain_entry.delete(0, tk.END)
        self.plain_entry.insert(0, x)


def store_spiral(array, plaintext, l):
    direction = 0
    dx = directions[direction][0]
    dy = directions[direction][1]
    x = 0
    y = 0
    for c in plaintext:
        array[x][y] = c
        x = x + dx
        y = y + dy
        if (x >= l) or (y >= l) or (x < 0) or (y < 0):
            x = x-dx
            y = y-dy
            direction = (direction + 1) % 4
            dx = directions[direction][0]
            dy = directions[direction][1]
            x = x+dx
            y = y+dy
        elif (array[x][y] != ''):
            x = x-dx
            y = y-dy
            direction = (direction + 1) % 4
            dx = directions[direction][0]
            dy = directions[direction][1]
            x = x+dx
            y = y+dy
            
def store_column(array, ciphertext):
    x = 0
    for j in range(len(array[0])):
        for i in range(len(array)):
            array[i][j] = ciphertext[x]
            x = x+1


def encrypt(plaintext):
    l = len(plaintext)
    sl = int(ceil(sqrt(l)))
    # make empty 2d array of [ ['','', ... ], .... ]
    ar2 = [['' for i in range(sl)] for j in range(sl)]
    store_spiral(ar2, plaintext, sl)

    for i in range(len(ar2)):
        for j in range(len(ar2[0])):
            if ar2[i][j] == '':
                ar2[i][j] = 'x'

    x = ''
    for j in range(len(ar2[0])):
        for i in range(len(ar2)):
            x += ar2[i][j]
    return(x)


def decrypt(ciphertext):
    l = len(ciphertext)
    sl = int(ceil(sqrt(l)))
    # make empty 2d array of [ ['','', ... ], .... ]
    ar2 = [['' for i in range(sl)] for j in range(sl)]
    store_column(ar2, ciphertext)

    k = 0
    l = 0
    m = sl
    n = sl
    x = ''
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            x += ar2[k][i]

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            x += ar2[i][n - 1]

        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                x += ar2[m - 1][i]

            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                x += ar2[i][l]

            l += 1

    return(x)


if __name__ == "__main__":
    root = tk.Tk()
    cipher = spiralcipher(root)
    root.mainloop()
