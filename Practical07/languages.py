from Practical07.ProgrammingLanguage import ProgrammingLanguage

def details():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    language = [ruby, python, vb]
    print(ruby)
    print(python)
    print(vb)
    print("Languages that are Dynamic")
    for self in language:
        if self.is_dynamic():
            print(self.language)

details()