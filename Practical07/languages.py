from Practical07.ProgrammingLanguage import ProgrammingLanguage

def details():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    language_list = [ruby, python, vb]

details()