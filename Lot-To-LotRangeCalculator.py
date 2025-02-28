#from string import Template
# Online Python - IDE, Editor, Compiler, Interpreter

print("Welcome to the lot-2-lot calc baby.")
a = float(input('Enter the original LOW result: '))
b = float(input('Enter the original HIGH result: '))

a_str = str(a)
a_split = a_str.split(".")
a_len = len(a_split[1]) + 1
b_str = str(b)
b_split = b_str.split(".")
b_len = len(b_split[1]) + 1


a_low = a - (a*0.2)
a_high = a + (a*0.2)
b_low = b - (b*0.2)
b_high = b + (b*0.2)

a_low_formatted = f"{a_low:.{a_len}f}"
a_high_formatted = f"{a_high:.{a_len}f}"
b_low_formatted = f"{b_low:.{b_len}f}"
b_high_formatted = f"{b_high:.{b_len}f}"

#print("Low-20%: ", a_low_formatted)
#print("Low+20%: ", a_high_formatted)

#print("High-20%: ", b_low_formatted)
#print("High+20%: ", b_high_formatted)

#Range_template = Template("($Low - $High)")
#Range_output = Range_template.substitute(Low = a_low_formatted, High = a_high_formatted)

print("Low Range: ", f"({a_low_formatted} - {a_high_formatted})")
print("High Range: ", f"({b_low_formatted} - {b_high_formatted})")
