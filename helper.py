#preciso dar um jeito de criar uma função subdividade em 3 partes.

#  1 - criar pasta com tabelas
#  2 - verificar erros
#  3 - juntar tudo mesmo que meio fudido

import shutil
from pathlib import Path

#cria objeto "MapaTabelas que para cada município cria uma lista ordenada dos dados do município"
#sendo igual as posições a tabela será a mesma para diferentes municípios (na teoria)
from pathlib import Path

MapaTabelas = {}

def chave(p):
    partes = p.stem.split("-")
    return (
        int(partes[partes.index("page") + 1]),
        int(partes[partes.index("table") + 1]),
    )

for municipio_folder in sorted(Path("municipios").iterdir()):
    arquivos = sorted(municipio_folder.glob("*.csv"), key=chave)
    MapaTabelas[municipio_folder.name] = arquivos





#cria pasta tabelas de cada município sobre respectivo índice 
def cria_tabelas_pop(pos,path):
    Path('pop_area')
    Path('dataIn').mkdir(exist_ok=True)
    caminho = Path('dataIn') / path
    caminho.mkdir(exist_ok=True)

    for municipio in MapaTabelas.keys():
        origem = MapaTabelas[municipio][pos]
        destino = caminho / f"{municipio}.csv"
        shutil.copy2(origem, destino)


