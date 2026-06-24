image agressor-arrependido = "images/agressorReacoes/agressor-arrependido.png"
image agressor-assustado = "images/agressorReacoes/agressor-assustado.png"
image agressor-ciumento = "images/agressorReacoes/agressor-ciumento.png"
image agressor-confiante = "images/agressorReacoes/agressor-confiante.png"
image agressor-confuso = "images/agressorReacoes/agressor-confuso.png"
image agressor-constrangido = "images/agressorReacoes/agressor-constrangido.png"
image agressor-debochado = "images/agressorReacoes/agressor-debochado.png"
image agressor-defensivo = "images/agressorReacoes/agressor-defensivo.png"
image agressor-desdenhoso = "images/agressorReacoes/agressor-desdenhoso.png"
image agressor-desinterresado = "images/agressorReacoes/agressor-desinterresado.png"
image agressor-disposto = "images/agressorReacoes/agressor-disposto.png"
image agressor-espanto = "images/agressorReacoes/agressor-espanto.png"
image agressor-feliz = "images/agressorReacoes/agressor-feliz.png"
image agressor-gag = "images/agressorReacoes/agressor-gag.png"
image agressor-impaciente = "images/agressorReacoes/agressor-impaciente.png"
image agressor-irritado = "images/agressorReacoes/agressor-irritado.png"
image agressor-neutro = "images/agressorReacoes/agressor-neutro.png"
image agressor-reflexivo = "images/agressorReacoes/agressor-reflexivo.png"
image agressor-serio = "images/agressorReacoes/agressor-serio.png"

default Agname= "???"
default Amname= "???"
default Vname= "???"
default c1name= "???"
default c2name= "???"
default f1name= "???"
default f2name= "???"



define N = Character(None, callback=partial(blur_callback, None))
define e = Character('[Agname]', color="#ff0000", callback=partial(blur_callback, "e"), image= "agressor-neutro")
define a = Character('[Amname]', color="#5ffe50", callback=partial(blur_callback, "a"), image= "amigo-neutro")
define c1 = Character('[c1name]', callback=partial(blur_callback, "c1"), image= "colega1-neutro")
define c2 = Character('[c2name]', callback=partial(blur_callback, "c2"), image= "colega2-neutro")
define f1 = Character('[f1name]', callback=partial(blur_callback, "f1"), image= "figurante1-neutro")
define f2 = Character('[f2name]', callback=partia    l(blur_callback, "f2"), image= "figurante2-neutro")
define V = Character('[Vname]', color="#ed33e1", callback=partial(blur_callback, "V"), image= "veronica-neutra")

define N_nvl = Character(None, kind=nvl, callback=Phone_ReceiveSound)
define e_nvl = Character('Agressor', kind=nvl, callback=Phone_ReceiveSound)
define c1_nvl = Character('Colega1', kind=nvl, callback=Phone_ReceiveSound)
define c2_nvl = Character('Colega2', kind=nvl, callback=Phone_ReceiveSound)
define V_nvl = Character('Verônica', kind=nvl, callback=Phone_SendSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

transform mindfog:
    blur 4
