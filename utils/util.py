def gerador_senha(tamanho: int) -> str:
    import string as s
    from random import SystemRandom as sr

    caracteres_excluidos = "\"[])({}.=<>?#:,/\\;`´'"
    caracteres_especiais = "".join(
        c for c in s.punctuation if c not in caracteres_excluidos
    )
    alfabeto = s.ascii_letters + s.digits + caracteres_especiais

    return "".join(sr().choices(alfabeto, k=tamanho))
