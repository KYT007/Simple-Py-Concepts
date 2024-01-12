import pyinputplus as pyip
def calculate(w, h):
    term = w / (h **2) * 703
    print(round(term))

def main():
    maadi = pyip.inputFloat("Enter weight in pounds: ")
    moodi = pyip.inputFloat("Enter total height in inches only: ")
    calculate(maadi, moodi)
    
main()