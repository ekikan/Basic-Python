s = int(123456)
h = s//3600
m = s%3600//60
s = s%60
print(f"{h}:{m}:{s}")