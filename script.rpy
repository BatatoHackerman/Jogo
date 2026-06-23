define N = Character(None, callback=partial(blur_callback, None))
define e = Character('Agressor', callback=partial(blur_callback, "e"))
define c1 = Character('colega1', callback=partial(blur_callback, "c1"))
define c2 = Character('colega2', callback=partial(blur_callback, "c2"))
define V = Character("Verônica", callback=partial(blur_callback, "V"))

define e_nvl = Character('Agressor', kind=nvl, callback=Phone_ReceiveSound)
define c1_nvl = Character('colega1', kind=nvl, callback=Phone_ReceiveSound)
define c2_nvl = Character('colega2', kind=nvl, callback=Phone_ReceiveSound)
define V_nvl = Character("Verônica", kind=nvl, callback=Phone_SendSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

transform mindfog:
    blur 4

label start:

    scene onibus
    with fade
    show agressor-neutro at right onlayer chars

    c1_nvl "Bom dia, Nica!"
    c1_nvl "A apresentação de ontem foi incrível."
    c1_nvl "A diretoria ficou comentando sua proposta."
    show agressor-feliz at right onlayer chars
    c2_nvl "Sério, você salvou aquela reunião. "
    c2_nvl "Eu não teria pensado naquela solução."
    jump start2

label start2:

    scene onibus    
    e_nvl "Já chegou na empresa?"
    show agressor-espanto at right onlayer chars
    e_nvl "Você não respondeu ainda."
    e_nvl "Está tudo bem??"
    show agressor-arrependido at right onlayer chars
    e_nvl "Eu fiz alguma coisa? Me responde por favor" 
    e_nvl "Estou esperando você na entrada." 
    show agressor-assustado at right onlayer chars 
    e_nvl "Estou preocupado com você ."
   

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
