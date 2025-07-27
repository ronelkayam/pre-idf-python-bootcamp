euro = 4
nis = 2.58
coin = input("please enter euro or dolar:")
dolar = int(input("please enter nis count to change"))
if (coin == "dolar"):
    print(f"your bill ={nis * dolar}")
else:
    print(f"your bill = {nis * euro}")
