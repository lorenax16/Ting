from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lista = instance._data
    contenido = txt_importer(path_file)

    for i in lista:
        if i["nome_do_arquivo"] == path_file:
            return print("Arquivo já processado")

    saida = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(contenido),
        "linhas_do_arquivo": contenido,
    }

    instance.enqueue(saida)
    return print(saida)


def remove(instance):
    lista = instance._data

    if len(lista) == 0:
        return print("Não há elementos")
    remove_arquivo = instance.dequeue()
    caminho = remove_arquivo["nome_do_arquivo"]
    return print(f"Arquivo {caminho} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        contenido = instance.search(position)
        return print(contenido)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
