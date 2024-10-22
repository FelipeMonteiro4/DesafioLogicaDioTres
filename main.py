nome = "Roberto"
idade = 18
classe = "monge"


def classes():
    ataque = ""

    if classe == "mago":
        ataque = "magia"

    if classe == "guerreiro":
        ataque = "espada"

    if classe == "monge":
        ataque = "artes marciais"

    if classe == "ninja":
        ataque = "shuriken"

    print("o " + classe + " atacou usando " + ataque)


classes()