import random
from list_text import list_text
import time
import copy

source_file_puzzle = "./puzzle.txt"
list_puzzle = []
list_puzzle_color = None
word_choice = list_text
list_true_puzzle = []
list_color = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']
dict_puzzle_komparasi = {}


def count_column(source_file_puzzle):
    puzzle = open(source_file_puzzle, "r")
    column = int(len(puzzle.readline())/2)
    return column
    

def count_row(source_file_puzzle):
    puzzle = open(source_file_puzzle, "r")
    row = 0
    for l in puzzle:
        if l != "\n" and l != " ":
            row += 1
    
    return row

def convert_text_to_list(source_file_puzzle):
    for letter in open(source_file_puzzle, "r"):
        temp_list_puzzle = []
        for l in letter:
            if l != "\n" and l != " ":
                temp_list_puzzle.append(l)
        list_puzzle.append(temp_list_puzzle)
    return list_puzzle


def check_top():
    print("\n---------------Hasil dari atas ke bawah---------------")
    list_true_text = []
    list_true_row = []
    list_true_column = []
    for i in range(len(list_puzzle[0])):        
        temp_list_puzzle_top = []
        for j in range(row):
            temp_list_puzzle_top.append(list_puzzle[j][i])
        for iword, vword in enumerate(word_choice):
            if vword[0].lower() in temp_list_puzzle_top or vword[0] in temp_list_puzzle_top:
                letterv = vword[0]
                lenv = len(vword)
                lenp = len(temp_list_puzzle_top)
                if lenv <= lenp:
                    for it, iv in enumerate(temp_list_puzzle_top):
                        list_true = []
                        list_row = []
                        list_column = []
                        if letterv.lower() == iv.lower():
                            jumlah = dict_puzzle_komparasi.get(vword)
                            jumlah += 1
                            dict_puzzle_komparasi[vword] = jumlah
                            if (len(vword)) <= len(temp_list_puzzle_top):
                                m = 0
                                for l in range(it, len(temp_list_puzzle_top)):
                                    if m >= len(vword):
                                        break
                                    if vword[m] == temp_list_puzzle_top[l]:
                                        list_true.append(temp_list_puzzle_top[l])
                                        list_row.append(l)
                                        list_column.append(i)
                                    m += 1
                                if len(list_true) == len(vword) and ''.join(list_true).lower() == ''.join(vword).lower():
                                    list_true_text.append(list_true)
                                    list_true_column.append(list_column)
                                    list_true_row.append(list_row)
    k = 0
    while True:
        if k >= len(list_true_text):
            break
        print(' '.join(list_true_text[k]), ":")
        i = 0
        ii = 0
        jj = 0
        color = random.choice(list_color)
        while True:
            if i >= row or ii >= row:
                break
            j = 0
            jjj = 0
            while True:
                if jjj > len(list_true_text):
                    jjj = 0
                if j >= column or jj >= column:
                    break
                if i == list_true_row[k][ii] and j == list_true_column[k][jj]:
                    print(list_puzzle[i][j], end=" ")
                    value = list_puzzle_color[i][j]
                    list_puzzle_color[i][j] = f"{color}{value}"
                    ii += 1
                    jj += 1
                    if jj >= len(list_true_column[k]) or ii >= len(list_true_row[k]):
                        ii -= 1
                        jj -= 1
                else:
                    print("-", end=" ")
                j += 1
                jjj += 1
            print("\n")
            i += 1
        k += 1


def check_bottom():
    print("\n---------------Hasil dari bawah ke atas---------------")
    list_true_text = []
    list_true_row = []
    list_true_column = []
    for i in range(len(list_puzzle[0])):        
        temp_list_puzzle_top = []
        for j in range(row):
            temp_list_puzzle_top.append(list_puzzle[-j+-1][i])
        for iword, vword in enumerate(word_choice):
            if vword[0].lower() in temp_list_puzzle_top or vword[0] in temp_list_puzzle_top:
                letterv = vword[0]
                lenv = len(vword)
                lenp = len(temp_list_puzzle_top)
                if lenv <= lenp:
                    for it, iv in enumerate(temp_list_puzzle_top):
                        list_true = []
                        list_row = []
                        list_column = []
                        if letterv.lower() == iv.lower():
                            jumlah = dict_puzzle_komparasi.get(vword)
                            jumlah += 1
                            dict_puzzle_komparasi[vword] = jumlah
                            if (len(vword)) <= len(temp_list_puzzle_top):
                                m = 0
                                for l in range(it, len(temp_list_puzzle_top)):
                                    if m >= len(vword):
                                        break
                                    if vword[m] == temp_list_puzzle_top[l]:
                                        list_true.append(temp_list_puzzle_top[l])
                                        list_row.append(len(temp_list_puzzle_top)-l-1)
                                        list_column.append(i)
                                    m += 1
                                if len(list_true) == len(vword) and ''.join(list_true).lower() == ''.join(vword).lower():
                                    list_true_text.append(list_true)
                                    list_true_column.append(list_column)
                                    list_true_row.append(list_row)
    k = 0
    while True:
        if k >= len(list_true_text):
            break
        print(' '.join(list_true_text[k]), ":")
        list_true_row[k].sort()
        list_true_column[k].sort()
        i = 0
        ii = 0
        jj = 0
        color = random.choice(list_color)
        while True:
            if i >= row or ii >= row:
                break
            j = 0
            jjj = 0
            while True:
                if jjj > len(list_true_text):
                    jjj = 0
                if j >= column or jj >= column:
                    break
                if i == list_true_row[k][ii] and j == list_true_column[k][jj]:
                    print(list_puzzle[i][j], end=" ")
                    value = list_puzzle_color[i][j]
                    list_puzzle_color[i][j] = f"{color}{value}"
                    ii += 1
                    jj += 1
                    if jj >= len(list_true_column[k]) or ii >= len(list_true_row[k]):
                        ii -= 1
                        jj -= 1
                else:
                    print("-", end=" ")
                j += 1
                jjj += 1
            print("\n")
            i += 1
        k += 1


def check_left(list_puzzle_to_resolve):
    print("\n---------------Hasil dari kiri ke kanan---------------")
    list_true_text = []
    list_true_row = []
    list_true_column = []
    baris = 0
    for p in list_puzzle_to_resolve:
        for _, v in enumerate(word_choice):
            if v[0].lower() in p or v[0].upper() in p:
                letter = v[0]
                len_v = len(v)
                for i, vp in enumerate(p):
                    if vp.lower() == letter.lower() and ((i+1) - (len_v)) >= 0:
                        jumlah = dict_puzzle_komparasi.get(v)
                        jumlah += 1
                        dict_puzzle_komparasi[v] = jumlah
                        count_true = 0
                        list_true = []
                        list_column = []
                        list_row = []
                        false = False
                        for j in range(i, i-(len_v-1)-1, -1):
                            for idxv in range(count_true, count_true-1, -1):
                                if p[j].lower() == v[idxv].lower():
                                    count_true += 1
                                    list_true.append(p[j])
                                    list_column.append(str(j))
                                    list_row.append(str(baris))
                                else:
                                    false = True
                                break
                            if false:
                                break
                        if count_true == len_v:
                            if list_true not in list_true_puzzle:
                                list_true_puzzle.append(list_true)
                            list_true_text.append(list_true)
                            list_true_column.append(list_column)
                            list_true_row.append(list_row)
        baris += 1
    k = 0
    while True:
        color = random.choice(list_color)
        if k >= len(list_true_text):
            break
        print(' '.join(list_true_text[k]), ":")
        i = 0
        while True:
            if i >= row:
                break
            j = 0
            while True:
                if j >= column:
                    break
                if str(i) in list_true_row[k] and str(j) in list_true_column[k]:
                    print(list_puzzle[i][j], end=" ")
                    value = list_puzzle_color[i][j]
                    list_puzzle_color[i][j] = f"{color}{value}"
                else:
                    print("-", end=" ")
                j += 1
            print("\n")
            i += 1
        k += 1

    
def check_right(list_puzzle_to_resolve):
    print("\n---------------Hasil dari kanan ke kiri---------------")
    list_true_text = []
    list_true_row = []
    list_true_column = []
    baris = 0
    for p in list_puzzle_to_resolve:
        for _, v in enumerate(word_choice):
            if v[0].lower() in p or v[0].upper() in p:
                letter = v[0]
                len_v = len(v)
                for i, vp in enumerate(p):
                    if vp.lower() == letter.lower() and ((i) + (len_v)) <= len(p):
                        jumlah = dict_puzzle_komparasi.get(v)
                        jumlah += 1
                        dict_puzzle_komparasi[v] = jumlah
                        count_true = 0
                        list_true = []
                        list_column = []
                        list_row = []
                        false = False
                        for k in range(i, i+(len_v)):
                            for idxv in range(count_true, count_true-1, -1):
                                if idxv < len(v):
                                    if p[k].lower() == v[idxv].lower():
                                        count_true += 1
                                        list_true.append(p[k])
                                        list_column.append(str(k))
                                        list_row.append(str(baris))
                                    else:
                                        false = True
                                    break
                            if false:
                                break
                        if count_true == len_v:
                            if list_true not in list_true_puzzle:
                                list_true_puzzle.append(list_true)
                            list_true_text.append(list_true)
                            list_true_column.append(list_column)
                            list_true_row.append(list_row[0])
        baris += 1
    k = 0
    while True:
        if k >= len(list_true_text):
            break
        print(' '.join(list_true_text[k]), ":")
        i = 0
        color = random.choice(list_color)
        while True:
            if i >= row:
                break
            j = 0
            while True:
                if j >= column:
                    break
                if str(i) in list_true_row[k] and str(j) in list_true_column[k]:
                    print(list_puzzle[i][j], end=" ")
                    value = list_puzzle_color[i][j]
                    list_puzzle_color[i][j] = f"{color}{value}"
                else:
                    print("-", end=" ")
                j += 1
            print("\n")
            i += 1
        k += 1


def check_top_left(list_puzzle_to_resolve):
    print("\n---------------Hasil dari atas ke samping kiri---------------")
    list_true_text = []
    list_true_column = []
    list_true_row = []
    baris = 0
    for ipp, p in enumerate(list_puzzle_to_resolve):
        for _, v in enumerate(word_choice):
            if v[0].lower() in p or v[0].upper() in p:
                letter = v[0]
                len_v = len(v)
                for i, vp in enumerate(p):
                    if vp.lower() == letter.lower():
                        jumlah = dict_puzzle_komparasi.get(v)
                        jumlah += 1
                        dict_puzzle_komparasi[v] = jumlah
                        list_letter_true = []
                        list_letter_true.append(vp.lower) 
                        ib = i
                        vi = 0
                        baris_p = ipp
                        count_true = 0
                        list_true = []
                        list_kolom = []
                        list_baris = []
                        while(True):
                            if v[vi].lower() == list_puzzle_to_resolve[baris_p][ib].lower():
                                list_true.append(v[vi])
                                list_kolom.append(ib)
                                list_baris.append(baris_p)
                                ib-=1
                                vi+=1
                                baris_p+=1
                                count_true+=1
                            else:
                                break
                            if baris_p+1 > row or ib == column or vi > len_v-1 or ib < 0:
                                break
                        if count_true == len_v:
                            if list_true not in list_true_puzzle:
                                list_true_puzzle.append(list_true)
                            list_true_text.append(list_true)
                            list_true_column.append(list_kolom)
                            list_true_row.append(list_baris)
        baris += 1
    k = 0
    while True:
        if k >= len(list_true_text):
            break
        print(' '.join(list_true_text[k]), ":")
        i = 0
        ii = 0
        jj = 0
        color = random.choice(list_color)
        while True:
            if i >= row or ii >= row:
                break
            j = 0
            jjj = 0
            while True:
                if jjj > len(list_true_text):
                    jjj = 0
                if j >= column or jj >= column:
                    break
                if i == list_true_row[k][ii] and j == list_true_column[k][jj]:
                    print(list_puzzle[i][j], end=" ")
                    value = list_puzzle_color[i][j]
                    list_puzzle_color[i][j] = f"{color}{value}"
                    ii += 1
                    jj += 1
                    if jj >= len(list_true_column[k]) or ii >= len(list_true_row[k]):
                        ii -= 1
                        jj -= 1
                else:
                    print("-", end=" ")
                j += 1
                jjj += 1
            print("\n")
            i += 1
        k += 1


def check_top_right(list_puzzle_to_resolve):
    print("\n---------------Hasil dari atas ke samping kanan---------------")
    list_true_text = []
    list_true_column = []
    list_true_row = []
    baris = 0
    for ipp, p in enumerate(list_puzzle_to_resolve):
        for _, v in enumerate(word_choice):
            if v[0].lower() in p or v[0].upper() in p:
                letter = v[0]
                len_v = len(v)
                for i, vp in enumerate(p):
                    if vp.lower() == letter.lower():
                        jumlah = dict_puzzle_komparasi.get(v)
                        jumlah += 1
                        dict_puzzle_komparasi[v] = jumlah
                        list_letter_true = []
                        list_letter_true.append(vp.lower) 
                        ib = i
                        vi = 0
                        baris_p = ipp
                        count_true = 0
                        list_true = []
                        list_kolom = []
                        list_baris = []
                        while(True):
                            if v[vi].lower() == list_puzzle_to_resolve[baris_p][ib].lower():
                                list_true.append(v[vi])
                                list_kolom.append(ib)
                                list_baris.append(baris_p)
                                ib+=1
                                vi+=1
                                baris_p+=1
                                count_true+=1
                            else:
                                break
                            if baris_p+1 > row or ib == column or vi > len_v-1:
                                break
                        if count_true == len_v:
                            if list_true not in list_true_puzzle:
                                list_true_puzzle.append(list_true)
                            list_true_text.append(list_true)
                            list_true_column.append(list_kolom)
                            list_true_row.append(list_baris)
        baris += 1
    k = 0
    while True:
        if k >= len(list_true_text):
            break
        print(' '.join(list_true_text[k]), ":")
        i = 0
        ii = 0
        jj = 0
        color = random.choice(list_color)
        while True:
            if i >= row or ii >= row:
                break
            j = 0
            jjj = 0
            while True:
                if jjj > len(list_true_text):
                    jjj = 0
                if j >= column or jj >= column:
                    break
                if i == list_true_row[k][ii] and j == list_true_column[k][jj]:
                    print(list_puzzle[i][j], end=" ")
                    value = list_puzzle_color[i][j]
                    list_puzzle_color[i][j] = f"{color}{value}"
                    ii += 1
                    jj += 1
                    if jj >= len(list_true_column[k]) or ii >= len(list_true_row[k]):
                        ii -= 1
                        jj -= 1
                else:
                    print("-", end=" ")
                j += 1
                jjj += 1
            print("\n")
            i += 1
        k += 1


def check_bottom_left(list_puzzle_to_resolve):
    print("\n---------------Hasil dari bawah ke samping kiri---------------")
    list_true_text = []
    list_true_column = []
    list_true_row = []
    baris = 0
    for ipp, p in enumerate(list_puzzle_to_resolve):
        for _, v in enumerate(word_choice):
            v = v[::-1]
            if v[0].lower() in p or v[0].upper() in p:
                letter = v[0]
                len_v = len(v)
                for i, vp in enumerate(p):
                    if vp.lower() == letter.lower():
                        vvv = v[::-1]
                        jumlah = dict_puzzle_komparasi.get(vvv)
                        jumlah += 1
                        dict_puzzle_komparasi[vvv] = jumlah
                        list_letter_true = []
                        list_letter_true.append(vp.lower) 
                        ib = i
                        vi = 0
                        baris_p = ipp
                        count_true = 0
                        list_true = []
                        list_kolom = []
                        list_baris = []
                        while(True):
                            if v[vi].lower() == list_puzzle_to_resolve[baris_p][ib].lower():
                                list_true.append(v[vi])
                                list_kolom.append(ib)
                                list_baris.append(baris_p)
                                ib+=1
                                vi+=1
                                baris_p+=1
                                count_true+=1
                            else:
                                break
                            if baris_p+1 > row or ib == column or vi > len_v-1:
                                break
                        if count_true == len_v:
                            if list_true not in list_true_puzzle:
                                list_true_puzzle.append(list_true)
                            list_true_text.append(list_true)
                            list_true_column.append(list_kolom)
                            list_true_row.append(list_baris)
        baris += 1
    k = 0
    while True:
        if k >= len(list_true_text):
            break
        list_true_text[k].reverse()
        print(' '.join(list_true_text[k]), ":")
        i = 0
        ii = 0
        jj = 0
        color = random.choice(list_color)
        while True:
            if i >= row or ii >= row:
                break
            j = 0
            jjj = 0
            while True:
                if jjj > len(list_true_text):
                    jjj = 0
                if j >= column or jj >= column:
                    break
                if i == list_true_row[k][ii] and j == list_true_column[k][jj]:
                    print(list_puzzle[i][j], end=" ")
                    value = list_puzzle_color[i][j]
                    list_puzzle_color[i][j] = f"{color}{value}"
                    ii += 1
                    jj += 1
                    if jj >= len(list_true_column[k]) or ii >= len(list_true_row[k]):
                        ii -= 1
                        jj -= 1
                else:
                    print("-", end=" ")
                j += 1
                jjj += 1
            print("\n")
            i += 1
        k += 1


def check_bottom_right(list_puzzle_to_resolve):
    print("\n---------------Hasil dari bawah ke samping kanan---------------")
    list_true_text = []
    list_true_column = []
    list_true_row = []
    baris = 0
    for ipp, p in enumerate(list_puzzle_to_resolve):
        for _, v in enumerate(word_choice):
            v = v[::-1]
            if v[0].lower() in p or v[0].upper() in p:
                letter = v[0]
                len_v = len(v)
                for i, vp in enumerate(p):
                    if vp.lower() == letter.lower():
                        vvv = v[::-1]
                        jumlah = dict_puzzle_komparasi.get(vvv)
                        jumlah += 1
                        dict_puzzle_komparasi[vvv] = jumlah
                        list_letter_true = []
                        list_letter_true.append(vp.lower) 
                        ib = i
                        vi = 0
                        baris_p = ipp
                        count_true = 0
                        list_true = []
                        list_kolom = []
                        list_baris = []
                        while(True):
                            if v[vi].lower() == list_puzzle_to_resolve[baris_p][ib].lower():
                                list_true.append(v[vi])
                                list_kolom.append(ib)
                                list_baris.append(baris_p)
                                ib-=1
                                vi+=1
                                baris_p+=1
                                count_true+=1
                            else:
                                break
                            if baris_p+1 > row or ib == column or vi > len_v-1 or ib < 0:
                                break
                        if count_true == len_v:
                            if list_true not in list_true_puzzle:
                                list_true_puzzle.append(list_true)
                            list_true_text.append(list_true)
                            list_true_column.append(list_kolom)
                            list_true_row.append(list_baris)
        baris += 1
    k = 0
    while True:
        if k >= len(list_true_text):
            break
        list_true_text[k].reverse()
        print(' '.join(list_true_text[k]), ":")
        i = 0
        ii = 0
        jj = 0
        color = random.choice(list_color)
        while True:
            if i >= row or ii >= row:
                break
            j = 0
            jjj = 0
            while True:
                if jjj > len(list_true_text):
                    jjj = 0
                if j >= column or jj >= column:
                    break
                if i == list_true_row[k][ii] and j == list_true_column[k][jj]:
                    print(list_puzzle[i][j], end=" ")
                    value = list_puzzle_color[i][j]
                    list_puzzle_color[i][j] = f"{color}{value}"
                    ii += 1
                    jj += 1
                    if jj >= len(list_true_column[k]) or ii >= len(list_true_row[k]):
                        ii -= 1
                        jj -= 1
                else:
                    print("-", end=" ")
                j += 1
                jjj += 1
            print("\n")
            i += 1
        k += 1


list_temp = convert_text_to_list(source_file_puzzle)
list_puzzle_color = copy.deepcopy(list_temp)
start_time = time.time()
column = count_column(source_file_puzzle)
row = count_row(source_file_puzzle)

for word in word_choice:
    dict_puzzle_komparasi.update({f"{word}": 0})

print("----------------Hasil pencarian satu per satu------------------\n")
check_left(list_puzzle)
check_right(list_puzzle)
check_top_right(list_puzzle)
check_top_left(list_puzzle)
check_top()
check_bottom()
check_bottom_left(list_puzzle)
check_bottom_right(list_puzzle)
print("\n----------------Batas akhir hasil pencarian satu per satu------------------\n\n")


print("\nPuzzle")
for i in list_puzzle:
    print(" ".join(i))

print("\nHasil Pencarian Berwarna")
for i in list_puzzle_color:
    for j in i:
        print(j, end=" ")
        if '[' in j:
            print('\33[0m', end="")
            
    print("\n")

total = 0
for key, value in dict_puzzle_komparasi.items():
    total += value
    print(f"{key} = {value}")
print(f"Total komparasi = {total}")
print("\nWaktu eksekusi program =  %s detik" % (time.time() - start_time))