# conversão de tipos, coerção
# type convertion , typecasting, coercion
# é o ato de converter um tipo em outro
# str, int, float, bool

# print("1" + 1)  # gera um TypeError

print(type(int("1")))

# Coerção
print(int("1") + 1)

# floats somados a inteiros retornam um float
print(type(float("1") + 1))


# Convertendo para bool
print(bool(""))  # Empty string = False
print(bool(" "))  # True


# Convertendo para String
print(type(str(11)))
