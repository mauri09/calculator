import tkinter as tk

calcuation = ""
#creating the events for when a button is pressed 
 
def add_to_calculation(symbol):
    global calcuation
    calcuation += str(symbol)
    text_results.delete(1.0, "end")
    text_results.insert(1.0 , calcuation)

def evaluate_calculation():
    global calcuation
    try:
        calcuation = str(eval(calcuation))
        
        text_results.delete(1.0, "end")
        text_results.insert(1.0,  calcuation)
    except:
        clear_field()
        text_results.delete(1.0, 'end')
        text_results.insert(1.0, "Error")
        
def clear_field():
    global calcuation
    calcuation = ""
    text_results.delete(1.0, "end")

#creating the basic frame and tittle
root = tk.Tk()
root.geometry("300x290")
root.title("Calculator")

#creating the screen for the calclation to be done in
text_results = tk.Text(root, height=2, width=16, font=("Arial" ,24))
text_results.grid(columnspan=5)

#creating the buttons
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=8, height=2)
btn_1.grid(row=2,column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2),width=8, height=2)
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3),width=8, height=2)
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4),width=8, height=2)
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5),width=8, height=2)
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6),width=8, height=2)
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7),width=8, height=2)
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8),width=8, height=2)
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9),width=8, height=2)
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0),width=8, height=2)
btn_0.grid(row=5,column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"),width=8, height=2)
btn_plus.grid(row=2,column=4)

btn_min = tk.Button(root, text="-", command=lambda: add_to_calculation("-"),width=8, height=2)
btn_min.grid(row=3,column=4)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"),width=8, height=2)
btn_mul.grid(row=4,column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"),width=8, height=2)
btn_div.grid(row=5,column=4)

btn_openPer = tk.Button(root, text="(", command=lambda: add_to_calculation("("),width=8, height=2)
btn_openPer.grid(row=5,column=1)

btn_closePer = tk.Button(root, text=")", command=lambda: add_to_calculation(")"),width=8, height=2)
btn_closePer.grid(row=5,column=3)

btn_clear = tk.Button(root, text="Clear", command=clear_field,width=17, height=2)
btn_clear.grid(row=6,column=1, columnspan=2)

btn_equals = tk.Button(root, text="=",command=evaluate_calculation,width=17, height=2)
btn_equals.grid(row=6,column=3, columnspan=2)


root.mainloop()