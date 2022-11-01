from passgen import generate_password_by_pip, generate_password

def run():
  quantity_characters = int(input("Ingresa la cantidad digitos o caracteres: ")) #We receive a number
  password = generate_password(quantity_characters)
  print(password)


if __name__ == "__main__":
  run()