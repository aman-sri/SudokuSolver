from tkinter import *
from tkinter import messagebox
import tkinter.font as font

root = Tk()

global sudoku_data

def check_in_col(num, col):
    for i in range(1, 10):
        if(int(list_of_textboxes[i][col].get())==int(num)):
            return 1
        else:
            continue
    return 0

def check_in_row(num, row):
    for j in range(1, 10):
        if(int(list_of_textboxes[row][j].get())==int(num)):
            return 1
        else:
            continue
    return 0

def check_in_box1(num, j, i):
    box_x = (i // 3) + 1
    box_y = (j // 3) + 1

    if i % 3 == 0:
        box_x = box_x - 1

    if j % 3 == 0:
        box_y = box_y - 1

    box_dic = {1:[1, 2, 3], 2:[4, 5, 6], 3:[7, 8, 9]}

    for i in box_dic[box_y]:
        for j in box_dic[box_x]:
            if(int(list_of_textboxes[i][j].get())==int(num)):
                return 1
            else:
                continue
    return 0

def check_if_full():
    for i in range(1, 10):
        for j in range(1, 10):
            if(int(list_of_textboxes[i][j].get())==int(0)):
                return 0
            else:
                continue
    return 1

def read_sudoku():
    for i in range(1, 10):
        for j in range(1, 10):
            if(len(list_of_textboxes[i][j].get())==0):
                list_of_textboxes[i][j].delete(0, END)
                list_of_textboxes[i][j].insert(0, 0)
            else:
                list_of_textboxes[i][j].config(state=DISABLED)
                sudoku_data[i][j]=int(list_of_textboxes[i][j].get())

def read_sudoku_state():
    for i in range(1, 10):
        for j in range(1, 10):
            sudoku_data[i][j]=int(list_of_textboxes[i][j].get())

def clear_sudoku():
    sudoku_data = []
    for i in range(1, 10):
        for j in range(1, 10):
            list_of_textboxes[i][j].config(state=NORMAL)
            list_of_textboxes[i][j].delete(0, END)
            list_of_textboxes[i][j].insert(0, "")

def back_track_solve():
    #print("In back_track_solve")
    read_sudoku_state()
    solve_bt(sudoku_data)
    for i in range(1, 10):
        for j in range(1, 10):
            list_of_textboxes[i][j].delete(0, END)
            list_of_textboxes[i][j].insert(0, sudoku_data[i][j])

def solve_bt(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve_bt(bo):
                return True

            bo[row][col] = 0

    return False

def find_empty(bo):
    for i in range(1, len(bo)):
        for j in range(1, len(bo[1])):
            if int(bo[i][j]) == 0:
                return (i, j)  # row, col

    return None

def valid(bo, num, pos):
    # Check row
    for i in range(1, len(bo[1])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(1, len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = (pos[1] // 3) + 1
    box_y = (pos[0] // 3) + 1

    if pos[1] % 3 == 0:
        box_x = box_x - 1

    if pos[0] % 3 == 0:
        box_y = box_y - 1

    box_dic = {1:[1, 2, 3], 2:[4, 5, 6], 3:[7, 8, 9]}

    for i in box_dic[box_y]:
        for j in box_dic[box_x]:
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve_sudoku():
    full_flag = check_if_full()

    while(full_flag==0):
        print("Searching in each place")
        for i in range(1, 10):
            same_flag = 0
            for j in range(1, 10):
                if(int(list_of_textboxes[i][j].get())!=0):
                    continue
                else:
                    occurence = 0

                    for number in range(1,10):
                        col_flag = 0
                        row_flag = 0
                        box_flag = 0

                        col_flag = check_in_col(number, j)
                        row_flag = check_in_row(number, i)
                        box_flag = check_in_box1(number, i, j)
                        if(col_flag==1 or row_flag==1 or box_flag==1):
                            continue
                        elif(col_flag==0 and row_flag==0 and box_flag==0):
                            num1 = number
                            occurence += 1
                            continue
                    if(occurence==1):
                        msg = "Number fixed - " + str(num1) + "\nAt - " + str(i) + "," + str(j)
                        list_of_textboxes[i][j].delete(0,END)
                        list_of_textboxes[i][j].insert(0, num1)
                        same_flag = 1
                        messagebox.showinfo("Message",msg)
        if(same_flag == 0):
            print("Searching in rows...")
            nums_in_row = []
            for row in range(1, 10):
                same_flag = 0
                for col in range(1, 10):
                    if(int(list_of_textboxes[row][col].get())!=0):
                        nums_in_row.append(int(list_of_textboxes[row][col].get()))
                for col in range(1, 10):
                    if(int(list_of_textboxes[row][col].get())!=0):
                        continue
                    else:
                        for number in range(1,10):
                            if number in nums_in_row:
                                continue
                            col_flag = 0
                            row_flag = 0
                            box_flag = 0

                            col_flag = check_in_col(number, col)
                            row_flag = check_in_row(number, row)
                            box_flag = check_in_box1(number, row, col)
                            if(col_flag==1 or row_flag==1 or box_flag==1):
                                continue
                            elif(col_flag==0 and row_flag==0 and box_flag==0):
                                num1 = number
                                occurence += 1
                                continue
                        if(occurence==1):
                            msg = "Number fixed - " + str(num1) + "\nAt - " + str(row) + "," + str(col)
                            list_of_textboxes[row][col].delete(0,END)
                            list_of_textboxes[row][col].insert(0, num1)
                            same_flag = 1
                            messagebox.showinfo("Message",msg)
        if(same_flag == 0):
            print("Searching in columns...")
            nums_in_col = []
            for col in range(1, 10):
                same_flag = 0
                for row in range(1, 10):
                    if(int(list_of_textboxes[row][col].get())!=0):
                        nums_in_col.append(int(list_of_textboxes[row][col].get()))
                for row in range(1, 10):
                    if(int(list_of_textboxes[row][col].get())!=0):
                        continue
                    else:
                        for number in range(1,10):
                            if number in nums_in_col:
                                continue
                            col_flag = 0
                            row_flag = 0
                            box_flag = 0

                            col_flag = check_in_col(number, col)
                            row_flag = check_in_row(number, row)
                            box_flag = check_in_box1(number, row, col)
                            if(col_flag==1 or row_flag==1 or box_flag==1):
                                continue
                            elif(col_flag==0 and row_flag==0 and box_flag==0):
                                num1 = number
                                occurence += 1
                                continue
                        if(occurence==1):
                            msg = "Number fixed - " + str(num1) + "\nAt - " + str(row) + "," + str(col)
                            list_of_textboxes[row][col].delete(0,END)
                            list_of_textboxes[row][col].insert(0, num1)
                            same_flag = 1
                            messagebox.showinfo("Message",msg)

        if(same_flag == 0):
            messagebox.showinfo("Message","No more direct numbers, from here we use complex algorithm. To continue, click on 'OK'.")
            back_track_solve()
        full_flag = check_if_full()
    print("\n\nSudoku solved\n\n")
    messagebox.showinfo("Message","Sudoku solved")

list_of_textboxes = []
list_of_textbox_rows = []

sudoku_data = []
sudoku_data_rows = []

list_of_textboxes.append(0)
list_of_textbox_rows.append(0)

sudoku_data.append(0)
sudoku_data_rows.append(0)

Font_Size = font.Font(family="Calibri", size=20)

for i in range(1, 10):
    list_of_textbox_rows = []
    sudoku_data_rows = []
    list_of_textbox_rows.append(0)
    sudoku_data_rows.append(0)
    for j in range(1, 10):
        sudoku_data_rows.append(0)
        list_of_textbox_rows.append(Entry(root, font=Font_Size, width=5))
    list_of_textboxes.append(list_of_textbox_rows)
    sudoku_data.append(sudoku_data_rows)

for i in range(1, 10):
    for j in range(1, 10):
        list_of_textboxes[i][j].grid(row=i-1, column=j-1)

b1 = Button(root, font=Font_Size, text="Read", command=read_sudoku)
b1.grid(row=10, column=0, columnspan=9, pady=10)

b2 = Button(root, font=Font_Size, text="Solve", command=solve_sudoku)
b2.grid(row=11, column=0, columnspan=9, pady=10)

b3 = Button(root, font=Font_Size, text="Clear", command=clear_sudoku)
b3.grid(row=12, column=0, columnspan=9, pady=10)

root.mainloop()