"""
Є строчка "Exception breakpoints: suspend the program when Exception or its subclasses are thrown.
In PyCharm, you can set breakpoints for Python exceptions.",
потрібно замінити усі пробіли на підчоркуючий знак "_".
"""
text = '"Exception breakpoints: suspend the program when Exception or its subclasses are thrown.\n\
In PyCharm, you can set breakpoints for Python exceptions."'
print(text.replace(" ", "_"))
