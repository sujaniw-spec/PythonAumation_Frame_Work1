import moment
x = moment.now()
print(x)
y = moment.now().strftime("%H-%M-%S_%d-%m-%y")
print(y)