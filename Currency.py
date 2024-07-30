co = int(input("quede en peso: "))
pe = int(input("quede en soles: "))
br = int(input("quede en reales: "))

s = co * 0.0578
s = pe * 0.2800
s = br * 0.2140
usd = co + pe + br
print(usd)