import re

def check_input(input):
        if re.match(r'(\d{4}-\d{2}-\d{2})', input):
            return True
        else:
            raise ValueError("You entered incorrect date")