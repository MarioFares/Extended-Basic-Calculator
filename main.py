"""
Welcome to the Extended Basic Calculator.

This console was designed for you to be able to use all the functions of a simple fx-95 calculator and more.
A handy, efficient and fast tool to conduct numerous mathematical calculations with ease.

This application is a command line interpreter (CLI) built with python's standard library module cmd, and depends
on numerous modules from the python standard library such as math, statistics, and fractions.

It also makes use of the NumPy library for functions concerned with calculating the roots of higher degree polynomials
and solving systems of equations (linear algebra).

This application also features trigonometric, inverse trigonometric, and reciprocal trigonometric identities, as well
as functions to calculate the circumference or area of a circle.

There are conversion features as well that include degrees to radians and vice versa, as well as decimals to fractions.

This application has a very long list of commands and functions that aim to encompass both easy and higher mathematical
algorithms that any student might need.
"""

import calendar
import cmd
import datetime
import fractions
import math
import os
import statistics
import numpy


# noinspection PyUnusedLocal,PyUnresolvedReferences
class App(cmd.Cmd):
    intro = f"Welcome to the Extended Basic Calculator\t\tDate: {datetime.date.today()}\nTo learn more about the" \
            f" console and commands, type menu, about, help, or ?"
    prompt = ">>>"
    file = None
    ans_his = []
    history = []
    variables = {}

    # Trigonometric Functions
    def do_sin(self, arg):
        """
        Return the sine of an angles in degrees.

        Argument: angles in degrees
        """
        try:
            ans = math.sin(math.radians(float(arg)))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_cos(self, arg):
        """
        Return the cosine of an angle in degrees.

        Argument: angles in degrees
        """
        try:
            ans = math.cos(math.radians(float(arg)))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_tan(self, arg):
        """
        Return the tangent of an angle in degrees.

        Argument: angles in degrees
        """
        try:
            ans = math.tan(math.radians(float(arg)))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Inverse Trigonometric Functions
    def do_asin(self, arg):
        """
        Return measure of angles using inverse sine(arcsine) function.

        Argument: value
        """
        try:
            ans = math.degrees(math.asin(float(arg)))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_acos(self, arg):
        """
        Return measure of angles using inverse cosine(arccosine) function.

        Argument: value
        """
        try:
            ans = math.degrees(math.acos(float(arg)))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_atan(self, arg):
        """
        Return measure of angles using inverse tangent(arctangent) function.

        Argument: value
        """
        try:
            ans = math.degrees(math.atan(float(arg)))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Reciprocal Trigonometric Functions
    def do_sec(self, arg):
        """
        Return the secant of a given angle in degrees.

        Argument: angles in degrees
        """
        try:
            ans = (1 / math.cos(math.radians(float(arg))))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_csc(self, arg):
        """
        Return the cosecant of an angle in degrees.

        Argument: angles in degrees
        """
        try:
            ans = (1 / math.sin(math.radians(float(arg))))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_cot(self, arg):
        """
        Return the cotangent of an angle in degrees.

        Argument: angles in degrees
        """
        try:
            ans = (1 / math.tan(math.radians(float(arg))))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Logarithmic Functions
    def do_Log(self, arg):
        """
        Return the base 10 logarithm of input x.

        Argument: value
        """
        try:
            ans = math.log10(float(arg))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_ln(self, arg):
        """
        Return the value of the Natural Logarithm of a number (base e).

        Argument: value
        """
        try:
            ans = math.log(float(arg))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_log(self, arg):
        """
        Return the logarithm of number x base b.

        Argument 1: base
        Argument 2: x - value
        """
        try:
            array = parse(arg)
            ans = math.log(int(array[1]), int(array[0]))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Constants
    def do_pi(self, arg):
        """
        Number Pi raised to the argument.

        Argument: value
        """
        try:
            ans = math.pow(math.pi, (float(arg)))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_exp(self, arg):
        """
        Euler's Number raised to the argument.

        Argument: value
        """
        try:
            ans = math.exp(float(arg))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Statistics
    def do_mean(self, arg):
        """
        Return the mean of a list of numbers.

        Argument: list(csv)
        """
        try:
            ans = statistics.fmean(float(i) for i in arg.split(','))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_median(self, arg):
        """
        Return the median of a list of numbers.

        Argument: list(csv)
        """
        try:
            ans = statistics.median(float(i) for i in arg.split(','))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_mode(self, arg):
        """
        Return the mode of a list of numbers.

        Argument: list(csv)
        """
        try:
            ans = statistics.mode(float(i) for i in arg.split(','))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Polynomials
    def do_quad(self, arg):
        """
        Return the roots of a quadratic polynomial.

        Argument: no argument
        """
        try:
            print("ax^2 + bx + c = 0")
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            ans = numpy.roots([a, b, c])
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_cubic(self, arg):
        """
        Find the roots of a cubic polynomial.

        Argument: no argument
        """
        try:
            print("ax^3 + bx^2 + cx + d = 0")
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            d = float(input("d: "))
            ans = numpy.roots([a, b, c, d])
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_quart(self, arg):
        """
        Return the roots of a quartic polynomial.

        Argument: no argument
        """
        try:
            print("ax^4 + bx^3 + cx^2 + dx + e = 0")
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            d = float(input("d: "))
            e = float(input("e: "))
            ans = numpy.roots([a, b, c, d, e])
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_quint(self, arg):
        """
        Return the roots of a quintic polynomial.

        Argument: no argument
        """
        try:
            print("ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0")
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            d = float(input("d: "))
            e = float(input("e: "))
            f = float(input("f: "))
            ans = numpy.roots([a, b, c, d, e, f])
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Linear Algebra
    def do_sys2(self, arg):
        """
        Return the values of x,y in system of 2 equations.

        Argument: no argument
        """
        try:
            print("Eq 1: a1x + b1y = c1")
            print("Eq 2: a2x + b2y = c2")
            a1 = float(input("a1: "))
            b1 = float(input("b1: "))
            c1 = float(input("c1: "))
            a2 = float(input("a2: "))
            b2 = float(input("b2: "))
            c2 = float(input("c2: "))
            first = numpy.array([[a1, b1], [a2, b2]])
            second = numpy.array([c1, c2])
            ans = numpy.linalg.solve(first, second)
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_sys3(self, arg):
        """
        Return the values of x,y,z in system of 3 equations.

        Argument: no argument
        """
        try:
            print("Eq 1: a1x + b1y c1z = d1")
            print("Eq 2: a2x + b2y c2z = d2")
            print("Eq 3: a3x + b3y c3z = d3")
            a1 = float(input("a1: "))
            b1 = float(input("b1: "))
            c1 = float(input("c1: "))
            d1 = float(input("d1: "))
            a2 = float(input("a2: "))
            b2 = float(input("b2: "))
            c2 = float(input("c2: "))
            d2 = float(input("d2: "))
            a3 = float(input("a3: "))
            b3 = float(input("b3: "))
            c3 = float(input("c3: "))
            d3 = float(input("d3: "))
            first = numpy.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
            second = numpy.array([d1, d2, d3])
            ans = numpy.linalg.solve(first, second)
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Power
    def do_pow(self, arg):
        """
        Return first argument raised to second argument.

        Argument 1: base
        Argument 2: exponent
        """
        try:
            array = parse(arg)
            ans = math.pow(float(array[0]), float(array[1]))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_sqrt(self, arg):
        """
        Return the square root of a given number.

        Argument: value
        """
        try:
            ans = math.sqrt(float(arg))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_cbrt(self, arg):
        """
        Return the cube root of argument.

        Argument: value
        """
        try:
            ans = math.pow(float(arg), (1 / 3))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Circles
    def do_carea(self, radius):
        """
        Return the area of a circle with radius r.

        Argument: radius
        """
        try:
            ans = math.pi * (float(radius) ** 2)
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_circum(self, radius):
        """
        Return the circumference of a circle with radius r.

        Argument: radius
        """
        try:
            ans = math.pi * 2 * (float(radius))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Variables
    def do_set(self, arg):
        """
        Set a variable equal to a value.

        Argument: variable = value
        """
        try:
            array = arg.split()
            if array[1] == "=" and float(array[2]):
                self.variables[array[0]] = array[2]
        except Exception as e:
            print("You made a syntax mistake.")
            print(e)

    def do_get(self, arg):
        """
        Return the value of a variable.

        Argument: variable
        """
        try:
            if arg in self.variables:
                print(self.variables[arg])
            else:
                print("No such variable.")
        except Exception as e:
            print(e)

    # History
    def do_anshis(self, arg):
        """
        Return history of answers to mathematical functions performed in this console.

        Argument: no argument
        """
        try:
            for ans in self.ans_his:
                print(ans)
        except Exception as e:
            print(e)

    def do_his(self, arg):
        """
        Return command history.

        Argument: no argument
        """
        try:
            for command in self.history:
                print(command)
        except Exception as e:
            print(e)

    # Counting
    def do_comb(self, arg):
        """
        Return combination with n total and r select.

        Argument 1: n
        Argument 2: r
        """
        try:
            array = parse(arg)
            ans = math.comb(int(array[0]), int(array[1]))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_perm(self, arg):
        """
        Return the permutation of n total r select.

        Argument 1: n
        Argument 2: r
        """
        try:
            array = parse(arg)
            ans = math.perm(int(array(0)), int(array(1)))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_fact(self, arg):
        """
        Return the factorial of a given number.

        Argument: value
        """
        try:
            ans = math.factorial(float(arg))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_prod(self, arg):
        """
        Calculate product of items in sequence.

        Argument: list(csv)
        """
        try:
            ans = math.prod(float(i) for i in arg.split(','))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_rem(self, arg):
        """
        Calculate remainder of first argument divided by second.

        Argument 1: dividend
        Argument 2: divisor
        """
        try:
            array = parse(arg)
            ans = math.remainder(float(array[0]), float(array[1]))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_sum(self, arg):
        """
        Return the sum of a list of numbers.

        Argument: list(csv)
        """
        try:
            ans = math.fsum(float(i) for i in arg.split(','))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Conversion
    def do_degtorad(self, arg):
        """
        Convert degrees to radians.

        Argument: value in degrees
        """
        try:
            ans = math.radians(float(arg))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_radtodeg(self, arg):
        """
        Convert radians to degrees.

        Argument: value in radians
        """
        try:
            ans = math.degrees(float(arg))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_dectofrac(self, arg):
        """
        Convert decimal to fraction.

        Argument: decimal
        """
        try:
            ans = fractions.Fraction(float(arg))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Other
    def do_gcd(self, arg):
        """
        Return the greatest common divisor of 2 numbers.

        Argument 1: value 1
        Argument 2: value 2
        """
        try:
            array = parse(arg)
            ans = math.gcd(int(array[0]), int(array[1]))
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_dist(self, arg):
        """
        Find the distance between 2 points.

        Argument 1: coordinates -> x,y
        Argument 2: coordinates -> x,y
        """
        try:
            array = parse(arg)
            cod1 = (float(i) for i in (array[0]).split(','))
            cod2 = (float(i) for i in (array[1]).split(','))
            ans = math.dist(cod1, cod2)
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    def do_eval(self, arg):
        """
        Evaluate mathematical expression.

        Argument: no argument
        """
        try:
            exp = input("Expression: ")
            ans = eval(exp)
            self.ans_his.append(ans)
            print(ans)
        except Exception as e:
            print(e)

    # Console
    @staticmethod
    def do_about(arg):
        """
        Return information about console.

        Argument: no argument
        """
        print("""
            Welcome to the Extended Basic Calculator.
            
            This console was designed for you to be able to use all the functions of a simple fx-95 calculator and more.
            A handy, efficient and fast tool to conduct numerous mathematical calculations with ease.
            
            This application is a command line interpreter (CLI) built with python's standard library module cmd, and 
            depends on numerous modules from the python standard library such as math, statistics, and fractions.
            
            It also makes use of the NumPy library for functions concerned with calculating the roots of higher degree 
            polynomials and solving systems of equations (linear algebra).
            
            This application also features trigonometric, inverse trigonometric, and reciprocal trigonometric 
            identities, as well as functions to calculate the circumference or area of a circle.
            
            There are conversion features as well that include degrees to radians and vice versa, as well as decimals
            to fractions.
            
            This application has a very long list of commands and functions that aim to encompass both easy and higher 
            mathematical algorithms that any student might need.
            
            Type ? to view all available commands, and ? <command> to review its documentation.
        """)

    @staticmethod
    def do_clear(arg):
        """
        Clear console window.

        Argument: no argument
        """
        try:
            os.system('cls')
        except OSError:
            os.system('clear')

    @staticmethod
    def do_exit(arg):
        """
        Exit console.

        Argument: no argument
        """
        quit()

    @staticmethod
    def do_open(arg):
        """
        Open a file or folder.

        Argument: no argument
        """
        try:
            path = input("Path: ")
            os.startfile(path)
        except Exception as e:
            print(e)

    @staticmethod
    def do_menu(arg):
        """
        Return the menu of the console.

        Argument: no argument
        """
        print("A few basic commands:")
        print("To evaluate expression, type eval.")
        print("To solve quadratic equation, type quad.")
        print("To solve cubic equations, type cubic.")
        print("To solve quartic equations (power 4), type quart.")
        print("To solve quintic equations (power 5), type quint.")
        print("To solve a System of 2 Unknowns, type sys2.")
        print("To solve a System of 3 Unknowns, type sys3.")
        print("To search for definitions, type dict.")
        print("To see available options, type menu.")
        print("To open a file or folder, type open.")
        print("To see the current date and time, type date.")
        print("To learn more about the console, type about.")
        print("To exit program, type quit.")

    def do_prompt(self, arg):
        """
        Change prompt of console.

        Argument: no argument
        """
        try:
            self.prompt = arg
        except Exception as e:
            print(e)

    @staticmethod
    def do_date(arg):
        """
        Return current date and time.

        Argument: no argument
        """
        print(f"{datetime.datetime.today()}")

    @staticmethod
    def do_cal(arg):
        """
        Print calendar for current month.

        Argument: no argument
        """
        print(calendar.month(datetime.datetime.now().year, datetime.datetime.now().month))

    def precmd(self, line):
        """Append executed line to history."""
        self.history.append(line)
        return line


def parse(arg):
    """Return list of arguments."""
    array = arg.split()
    return array


app = App()
app.cmdloop()
