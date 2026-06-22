define N = Character(None, callback=partial(blur_callback, None))
define e = Character('Agressor', callback=partial(blur_callback, "e"))

transform mindfog:
    blur 4

label start:

    scene 1
    with fade

    "esta é a minha visual novel de teste, para aprender a usar o ren'py."
    "ela é bem simples, mas tem um pouco de tudo o que eu quero aprender a usar."
    with fade

    show agressor-assustado at left onlayer chars
    show agressor-espanto at right onlayer chars
    

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:

        "Quer fazer o que?"

        "Um jogo!":
            jump makegame
        "Nada, só quero testar o Ren'Py.":
            jump test
                

label makegame:

    show agressor-espanto at left onlayer chars
    with dissolve
    e "Fico surpreso que queira fazer um jogo."
    show agressor-disposto at left onlayer chars
    with dissolve
    e "Mas é ótimo! Fazer um jogo é uma ótima maneira de aprender a usar o Ren'Py."

    return
