import bcrypt

password = b"%KM041286)zz%"  # замените на желаемый пароль
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())
