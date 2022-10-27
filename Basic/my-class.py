class Alumno:
  name = ""
  age = ""
  gen = ""

  def __init__(self, name, age, gen):
    self.name = name
    self.age = age
    self.gen = gen


joaquin = Alumno("Joaquin", "25", "Gen 13")

print(joaquin)

print(type(joaquin))
