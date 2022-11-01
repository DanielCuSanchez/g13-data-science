import random
# https://pypi.org/project/random-password-generator/
from password_generator import PasswordGenerator
def generate_password(quantity_characters):
  capital_letters = ('A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J',  'K',  'L',  'M', 'N','Ñ','O','P','Q','R','S','T','U','V','X','Y','Z')
  lower_case = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
  numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
  symbols = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"', " ")
  all_posibilities = capital_letters + lower_case + numbers + symbols
  password = ""
  for i in range(quantity_characters):
    char = random.choice(all_posibilities)
    password = password + char
  return password


def generate_password_by_pip(quantity_characters):
  password = PasswordGenerator() #Constructor
  password.minlen = quantity_characters #Config len
  return password.generate() #Return password