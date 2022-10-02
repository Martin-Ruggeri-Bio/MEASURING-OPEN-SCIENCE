from html.entities import name2codepoint
import random
from datetime import datetime

def generar_paper():
    category = random.choice(["Math", "Palaeontology", "Computing", "Chemistry", "Anthropology", "Physics", "Biology", "Geography", "Economy", "Astronomy", "Psychology", "Biochemistry", "Physiology", "Philosophy"])
    titulo = category + " aplicada"
    author = random.choice(["Juan", "Luis","Jessica", "Ben", "Carl", "Jackie", "Wendy", "Martin", "Eduardo", "Tomas", "Lucas",'Jane', 'Jack', 'Jill', 'Jean'])
    email = author.lower() + "@gmail.com"
    country = random.choice(["Argentina", "Germany", "Russia", "United States", "Canada", "Brazil", "Chile", "Spain", "England"])
    date = random.randint(1990, 2022)
    institucion = random.choice(["UM", "UNC", "UTN", "UCA"])
    return titulo, author, category, email, country, date, institucion
