import tkinter as tk
import sympy

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()

        # Creating window
        self.title('Calculator')
        self.resizable(0, 0)
        self.geometry('290x380')
        self['bg'] = 'darkgrey'

        self.input = ''

        # Label for input
        self.labelInput = tk.Label(self, font=('Digital-7', 13), width='30', height='3', text=self.get_Input())

        # Labels for numbers
        self.labelNum0 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_0(), width='8', height='4', text='0')
        self.labelNum1 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_1(), width='8', height='4', text='1')
        self.labelNum2 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_2(), width='8', height='4', text='2')
        self.labelNum3 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_3(), width='8', height='4', text='3')
        self.labelNum4 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_4(), width='8', height='4', text='4')
        self.labelNum5 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_5(), width='8', height='4', text='5')
        self.labelNum6 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_6(), width='8', height='4', text='6')
        self.labelNum7 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_7(), width='8', height='4', text='7')
        self.labelNum8 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_8(), width='8', height='4', text='8')
        self.labelNum9 = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_9(), width='8', height='4', text='9')

        # Labels for operators
        self.labelPlus = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_Plus(), background='grey', width='8', height='4', text='+')
        self.labelMinus = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_Minus(), background='grey', width='8', height='4', text='-')
        self.labelMult = tk.Button(self, font=('Digital-7', 9), command=lambda:self.add_Mult(), background='grey', width='8', height='4', text='*')
        self.labelEqual = tk.Button(self, font=('Digital-7', 9), command=lambda:self.calculate_Result(), background='grey', width='8', height='4', text='=')

        # Labels for removing from input
        self.labelRemoveLast = tk.Button(self, font=('Digital-7', 9), command=lambda:self.remove_Last(), background='grey', width='8', height='4', text='Del')
        self.labelRemoveAll = tk.Button(self, font=('Digital-7', 9), command=lambda:self.remove_All(), background='grey', width='8', height='4', text='CE')

        # Placement for input
        self.labelInput.place(x=8, y=10)

        # Placements for numbers
        self.labelNum0.place(x=78, y=305)
        self.labelNum1.place(x=8, y=230)
        self.labelNum2.place(x=78, y=230)
        self.labelNum3.place(x=148, y=230)
        self.labelNum4.place(x=8, y=155)
        self.labelNum5.place(x=78, y=155)
        self.labelNum6.place(x=148, y=155)
        self.labelNum7.place(x=8, y=80)
        self.labelNum8.place(x=78, y=80)
        self.labelNum9.place(x=148, y=80)

        # Placements for operatives
        self.labelPlus.place(x=218, y=230)
        self.labelMinus.place(x=218, y=155)
        self.labelMult.place(x=218, y=80)
        self.labelEqual.place(x=218, y=305)

        # Placements for removing from input
        self.labelRemoveLast.place(x=148, y=305)
        self.labelRemoveAll.place(x=8, y=305)

    def get_Input(self):
        return self.input

    def update(self):
        self.labelInput.configure(text=self.get_Input()) # Updating label

    def add_0(self):
        num0 = '0'
        self.input += num0
        self.update()

    def add_1(self):
        num1 = '1'
        self.input += num1
        self.update()
    
    def add_2(self): 
        num2 = '2'
        self.input += num2
        self.update()
    
    def add_3(self):
        num3 = '3'
        self.input += num3
        self.update()

    def add_4(self):
        num4 = '4'
        self.input += num4
        self.update()

    def add_5(self):
        num5 = '5'
        self.input += num5
        self.update()

    def add_6(self):
        num6 = '6'
        self.input += num6
        self.update()

    def add_7(self):
        num7 = '7'
        self.input += num7
        self.update()
    
    def add_8(self):
        num8 = '8'
        self.input += num8
        self.update()

    def add_9(self):
        num9 = '9'
        self.input += num9
        self.update()

    def add_Plus(self):
        plus = ' + '
        self.input += plus
        self.update()

    def add_Minus(self):
        minus = ' - '
        self.input += minus
        self.update()

    def add_Mult(self):
        mult = ' * '
        self.input += mult
        self.update()

    def calculate_Result(self):
        result = str(sympy.sympify(self.input)) # Using sympy to get result from string
        self.input = result

        self.update()

    def remove_Last(self):
        splitStr = self.input.split() # Splitting string into list
        splitStr.pop() # Removing last element from list
        self.input = ' '.join(splitStr) # Joining list into string
        self.update()

    def remove_All(self):
        self.input = ''
        self.update()

if __name__ == "__main__":
    window = Calculator()
    window.mainloop()