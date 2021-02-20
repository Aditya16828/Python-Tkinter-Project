from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.maxsize(785, 500)
root.minsize(785, 500)

frm = Frame(root)
frm.grid()


class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        self.result = False
        num1 = txtDisplay.get()
        num2 = str(num)
        if self.input_value:
            self.current = num2
            self.input_value = False
        else:
            if num2 == '.':
                if num2 in num1:
                    return
            self.current = num1 + num2
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.opt == "add":
            self.total += self.current
        if self.opt == "sub":
            self.total -= self.current
        if self.opt == "multiply":
            self.total *= self.current
        if self.opt == "divide":
            self.total /= self.current
        if self.opt == "remainder":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, opt):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.opt = opt
        self.result = False

    def ce(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def c(self):
        self.ce()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def sqrtt(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def ln(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)


objcal = Calculator()


txtDisplay = Entry(frm, font=('lucida', 32, 'bold'), bg='white', fg="red", justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=10, pady=0)
txtDisplay.insert(0, "")

numpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(
            Button(frm, width=6, height=2, bg='white', fg='black', font=('lucida', 20, 'bold'), text=numpad[i]))
        btn[i].grid(row=j, column=k, pady=0)
        btn[i]["command"] = lambda x=numpad[i]: objcal.numberEnter(x)
        i = i + 1

clear_btn = Button(frm, text="C", width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                   command=objcal.ce).grid(row=1, column=0, pady=0)

AllClear_btn = Button(frm, text="CE", width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                      command=objcal.c).grid(row=1, column=1, pady=0)

sq_btn = Button(frm, text="\u221A", width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                command=objcal.sqrtt).grid(row=1, column=2, pady=0)

add_btn = Button(frm, text="+", width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                 command=lambda: objcal.operation("add")).grid(row=1, column=3, pady=0)

sub_btn = Button(frm, text="-", width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                 command=lambda: objcal.operation("sub")).grid(row=2, column=3, pady=0)

mul_btn = Button(frm, text="x", width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                 command=lambda: objcal.operation("multiply")).grid(row=3, column=3, pady=0)

div_btn = Button(frm, text="/", width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                 command=lambda: objcal.operation("divide")).grid(row=4, column=3, pady=0)

zero_btn = Button(frm, text="0", width=6, height=2, bg='white', fg='black', font=('lucida', 20, 'bold'),
                  command=lambda: objcal.numberEnter(0)).grid(row=5, column=1, pady=0)

dot_btn = Button(frm, text=".", width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                 command=lambda: objcal.numberEnter(".")).grid(row=5, column=0, pady=0)

pm_btn = Button(frm, text=chr(177), width=6, height=2, bg='black', fg='white', font=('lucida', 20, 'bold'),
                command=objcal.mathPM).grid(row=5, column=2, pady=0)

equals_btn = Button(frm, text="=", width=6, height=2, bg='violet', fg='cyan', font=('lucida', 20, 'bold'),
                    command=objcal.sum_of_total).grid(row=5, column=3, pady=0)

pi_btn = Button(frm, text="\u03C0", width=6, height=2, fg='white', bg='green', font=('lucida', 20, 'bold'),
                command=objcal.pi).grid(row=5, column=6, pady=0)

cos_btn = Button(frm, text="cos", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                 command=objcal.cos).grid(row=1, column=5, pady=0)

tan_btn = Button(frm, text="tan", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                 command=objcal.tan).grid(row=1, column=6, pady=0)

sin_btn = Button(frm, text="sin", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                 command=objcal.sin).grid(row=1, column=4, pady=0)

cosh_btn = Button(frm, text="cosh", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                  command=objcal.cosh).grid(row=2, column=5, pady=0)

tanh_btn = Button(frm, text="tanh", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                  command=objcal.tanh).grid(row=2, column=6, pady=0)

sinh_btn = Button(frm, text="sinh", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                  command=objcal.sinh).grid(row=2, column=4, pady=0)

ln_btn = Button(frm, text="ln", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                command=objcal.ln).grid(row=3, column=4, pady=0)

exp_btn = Button(frm, text="exp", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                 command=objcal.exp).grid(row=3, column=5, pady=0)

mod_btn = Button(frm, text="mod", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                 command=lambda: objcal.operation("remainder")).grid(row=3, column=6, pady=0)

e_btn = Button(frm, text="e", width=6, height=2, fg='white', bg='green', font=('lucida', 20, 'bold'),
               command=objcal.e).grid(row=5, column=5, pady=0)

log_btn = Button(frm, text="log", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                 command=objcal.log).grid(row=4, column=4, pady=0)

deg_btn = Button(frm, text="deg", width=6, height=2, fg='white', bg='green', font=('lucida', 20, 'bold'),
                 command=objcal.degrees).grid(row=5, column=4, pady=0)

acosh_btn = Button(frm, text="acosh", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                   command=objcal.acosh).grid(row=4, column=6, pady=0)

asinh_btn = Button(frm, text="asinh", width=6, height=2, fg='white', bg='blue', font=('lucida', 20, 'bold'),
                   command=objcal.asinh).grid(row=4, column=5, pady=0)

root.mainloop()
