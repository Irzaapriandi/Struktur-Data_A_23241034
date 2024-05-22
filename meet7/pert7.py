# Tabel kebenaran (logika Boolean)
# and or not xor

# NOT
print ("***********Logika NOT***********")
x = False
y = not x
print (" nilai dari x = ", x)
print (" nilai dari y = ", y)

# AND (akan bernilai True, selama keduanya True)
# akan bernilai salah, selama ada satu aja yang salah
print ("***********Logika AND***********")
x = False
y = False
z = x and y
print (x, "and", y, "=", z)

x = True
y = False
z = x and y
print (x, "and", y, "=", z)

x = False
y = True
z = x and y
print (x, "and", y, "=", z)

x = True
y = True
z = x and y
print (x, "and", y, "=", z)

# OR (akan bernilai true, selama ada satu aja yang true,)
# akan bernilai salah, ketika keduanya salah
print ("***********Logika OR***********")
x = False
y = False
z = x or y
print (x, "or", y, "=", z)

x = False
y = True
z = x or y
print (x, "or", y, "=", z)

x = True
y = False
z = x or y
print (x, "or", y, "=", z)

x = True
y = True
z = x or y
print (x, "or", y, "=", z)

# xor
x = 12
y = 10
print (x ^ y)

x = 9
y = 14
print (x ^ y)

x = 4
y = 2
print (x ^ y)

x = True
y = False
print (x ^ y)

x = False
y = True
print (x ^ y)

x = True
y = True
print (x ^ y)

x = False
y = False
print (x ^ y)
