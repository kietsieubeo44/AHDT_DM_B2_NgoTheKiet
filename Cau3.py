from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def btn_sort_click(self, **event_args):
        input_string = self.txt_numbers.text
        numbers = list(map(int, input_string.split()))
        
        # Thực hiện sắp xếp bằng Bubble Sort
        n = len(numbers)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        
        self.lbl_result.text = "Dãy số sau khi sắp xếp: " + ' '.join(map(str, numbers))


