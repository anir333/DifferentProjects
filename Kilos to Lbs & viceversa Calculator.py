# Kilos to Lbs or Lbs to Kilos calculator

# Enter a weight you want to translate units
while True:
    weight = int(input("Weight: "))

# Ask if the weight entered is in unit kilos or lbs
    lork = input("(L)bs or (K)g: ")



    if lork.upper() == "L":
        converted = weight * 0.45
        print(f'You are {converted} kilos')
    elif lork.upper() == "K":
        converted = weight // 0.45
        print(f'You are {converted} pounds')
