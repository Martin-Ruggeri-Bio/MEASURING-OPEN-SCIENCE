from paper import Paper
from procesador_papers import generar_paper
import random
import json
from pandas import json_normalize
import pandas as pd


def main():
    lista_papers = []
    lista_dict_papers = []
    for i in range(100):
        titulo, author, category, email, country, date, institucion = generar_paper()
        paper = Paper(titulo, author, category, email, country, date, institucion)
        lista_papers.append(paper)
    for i in range(10000):
        paper = random.choice(lista_papers)
        paper2 = random.choice(lista_papers)
        if paper.titulo != paper2.titulo:
            paper.add_citations(paper2)
    for paper in lista_papers:
        #paper.calcular_info_citas()
        lista_dict_papers.append(paper.__dict__)
    print(lista_dict_papers)
    json_papers = json.dumps(lista_dict_papers)
    print(json_papers)
    info = json.loads(json_papers)
    df = json_normalize(info) #Results contain the required data
    print(df.head())
    df.to_csv('dataframe_papers.csv')


if __name__ == "__main__":
    main()