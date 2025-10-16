import tkinter as tk

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.resizable(False, False)


expression = ""
input_text = tk.StringVar()


def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except ZeroDivisionError:
        input_text.set("Error (÷0)")
        expression = ""
    except:
        input_text.set("Error")
        expression = ""


input_frame = tk.Frame(root, bd=5, relief=tk.RIDGE)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('Arial', 18, 'bold'),
                       textvariable=input_text, width=25, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


btns_frame = tk.Frame(root)
btns_frame.pack()


tk.Button(btns_frame, text="C", width=10, height=3, command=btn_clear, bg="#ff6666").grid(row=0, column=0)
tk.Button(btns_frame, text="/", width=10, height=3, command=lambda: btn_click("/")).grid(row=0, column=1)
tk.Button(btns_frame, text="*", width=10, height=3, command=lambda: btn_click("*")).grid(row=0, column=2)
tk.Button(btns_frame, text="-", width=10, height=3, command=lambda: btn_click("-")).grid(row=0, column=3)


tk.Button(btns_frame, text="7", width=10, height=3, command=lambda: btn_click(7)).grid(row=1, column=0)
tk.Button(btns_frame, text="8", width=10, height=3, command=lambda: btn_click(8)).grid(row=1, column=1)
tk.Button(btns_frame, text="9", width=10, height=3, command=lambda: btn_click(9)).grid(row=1, column=2)
tk.Button(btns_frame, text="+", width=10, height=3, command=lambda: btn_click("+")).grid(row=1, column=3)


tk.Button(btns_frame, text="4", width=10, height=3, command=lambda: btn_click(4)).grid(row=2, column=0)
tk.Button(btns_frame, text="5", width=10, height=3, command=lambda: btn_click(5)).grid(row=2, column=1)
tk.Button(btns_frame, text="6", width=10, height=3, command=lambda: btn_click(6)).grid(row=2, column=2)
tk.Button(btns_frame, text="=", width=10, height=7, command=btn_equal, bg="#99ff99").grid(row=2, column=3, rowspan=2)


tk.Button(btns_frame, text="1", width=10, height=3, command=lambda: btn_click(1)).grid(row=3, column=0)
tk.Button(btns_frame, text="2", width=10, height=3, command=lambda: btn_click(2)).grid(row=3, column=1)
tk.Button(btns_frame, text="3", width=10, height=3, command=lambda: btn_click(3)).grid(row=3, column=2)


tk.Button(btns_frame, text="0", width=21, height=3, command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2)
tk.Button(btns_frame, text=".", width=10, height=3, command=lambda: btn_click(".")).grid(row=4, column=2)

root.mainloop()

