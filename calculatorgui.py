from calculator import *
import customtkinter

root = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root.geometry('722x768')    
frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=20, padx=10, fill="both", expand=True)
root.title("Calculator")
def calculator():
    
    calculator = output.get('0.0', 'end')
    result = formatNumber(solve(modifyInput(calculator))[0])
    output.delete('0.0', 'end')
    output.insert('0.0', result)

output = customtkinter.CTkTextbox(master=frame, width=640, height=70, corner_radius=10, border_width=5, border_color='#000000', font=(('Arial', 50)))
output.grid(row=0, column=0, columnspan=5, padx=8, pady=8)

btncount = 1
for i in range(2,5):
    for j in range(0,3):
        btn = customtkinter.CTkButton(master=frame,text=str(btncount), command= lambda btncount=btncount:output.insert('end', btncount), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
        btn.grid(row=i, column=j, padx=8, pady=8)
        btncount = btncount + 1
btncount = 0

btn_clear = customtkinter.CTkButton(master=frame,text='CE', command=lambda:output.delete('0.0', 'end'), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_clear.grid(row=1, column=3, padx=8, pady=8)

btn_equals = customtkinter.CTkButton(master=frame,text='=', command=calculator, width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_equals.grid(row=5, column=2, padx=8, pady=8)
                                                                                                
btn_add = customtkinter.CTkButton(master=frame,text=Add().operator, command=lambda:output.insert('end', Add().operator), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_add.grid(row=2, column=3, padx=8, pady=8)

btn_subtract = customtkinter.CTkButton(master=frame,text=Subtract().operator, command=lambda:output.insert('end', Subtract().operator), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_subtract.grid(row=3, column=3, padx=8, pady=8)

btn_multiply = customtkinter.CTkButton(master=frame,text=Multiply().operator, command=lambda:output.insert('end', Multiply().operator), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_multiply.grid(row=4, column=3, padx=8, pady=8)

btn_divide = customtkinter.CTkButton(master=frame,text=Divide().operator, command=lambda:output.insert('end', Divide().operator), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_divide.grid(row=5, column=3, padx=8, pady=8)

btn_bracketopen = customtkinter.CTkButton(master=frame,text=Brackets().operator, command=lambda:output.insert('end', Brackets().operator), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_bracketopen.grid(row=1, column=0, padx=8, pady=8)

btn_bracketclose = customtkinter.CTkButton(master=frame,text=Brackets().closeoperator, command=lambda:output.insert('end', Brackets().closeoperator), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_bracketclose.grid(row=1, column=1, padx=8, pady=8)

btn_dot = customtkinter.CTkButton(master=frame,text='.', command=lambda:output.insert('end', '.'), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn_dot.grid(row=5, column=1, padx=8, pady=8)

btn0 = customtkinter.CTkButton(master=frame, text='0', command= lambda:output.insert('end', 0), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btn0.grid(row=5, column=0, padx=8, pady=8)

btnaddmultiply = customtkinter.CTkButton(master=frame, text=AddMultiply().operator, command= lambda:output.insert('end', AddMultiply().operator), width=160, height=110, corner_radius=30, font=(('Arial', 60)))
btnaddmultiply.grid(row=1, column=2, padx=8, pady=8)

root.mainloop()
