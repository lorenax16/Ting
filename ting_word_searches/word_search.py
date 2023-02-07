def exists_word(word, instance):
    data = []
    lower_case = word.lower()
    lines = 0

    for i in range(len(instance)):

        file = instance.search(i)

        saida = {
            "palavra": lower_case,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

    for linea in file["linhas_do_arquivo"]:
        lines += 1
        if lower_case in linea.lower():
            saida["ocorrencias"].append({"linha": lines})

    if saida["ocorrencias"]:
        data.append(saida)
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
