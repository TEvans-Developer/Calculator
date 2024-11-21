import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40 , "bold")
SMALL_FONT_STYLE= ("Arial", 16)
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    """
    A class to create the Calculator

    Attributes
        __init__
            tk.TK = Initializes Tkinter application and creates the main window
            .geometry = Configures the height and width of the Calculator
            .resizable = (0,0) == (false,false); Confirms that window for the application is not resizeable
            .title = title of application
            .display_frame = creates a display frame for the application
            .display_frame = creaetes a button frame for the application
            .total_expression =  the total expression to be displayed by default(0) or after operations
            .current_expression = the current expression to be displayed by default (0) or after operations
            .digits = dictionary of digits for calculator
            .operations = dictionary to map the arithmetic operation in python to operatior symbols.
            .create_digit_buttons() = creates digit buttons for calculator
            .create_operator_buttons() = creates operator buttons for calculator
            .create_special_buttons() = creates special symbol buttons for calculator
            .create_clear_button() = creates clear button
            .create_equals_button() = crerates equals button
            .rowconfigure = expand row to fill in empty row space
            .columnconfigure = expand column to fill in empty column space
            
    Methods:
        run(): runs the application indefinitely
        create_display_frame(): creates a display frame that expands, fills and returns the frame
        create_buttons_frame(): creates button frame expan, fills and returns the button
        create_display_label(): displays the total_expression and current_expression as labels on the east portion of the display frame while returning both label and total label
        create_digit_buttons(): creates grid that adds each button from dictionary to digit screen via row and column
        create_operator_buttons(): loops over opertions dictionary to add operation symbols for their button frame  
        create_clear_button(): method used to create clear button
        create_equals_button(): method used to create equals button
    """
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
    
        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_label()

        self.digits={
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }

        self.operations={ "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label
    
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)
    
    def create_operator_buttons(self):
        i = 0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
            
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
    
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame
    
    def run(self):
        self.window.mainloop()

#Object "calc" will run calc.py is ran as a script from the terminial
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
