image agressor arrependido = "images/agressorReacoes/agressor-arrependido.png"
image agressor assustado = "images/agressorReacoes/agressor-assustado.png"
image agressor ciumento = "images/agressorReacoes/agressor-ciumento.png"
image agressor confiante = "images/agressorReacoes/agressor-confiante.png"
image agressor confuso = "images/agressorReacoes/agressor-confuso.png"
image agressor constrangido = "images/agressorReacoes/agressor-constrangido.png"
image agressor debochado = "images/agressorReacoes/agressor-debochado.png"
image agressor defensivo = "images/agressorReacoes/agressor-defensivo.png"
image agressor desdenhoso = "images/agressorReacoes/agressor-desdenhoso.png"
image agressor desinterresado = "images/agressorReacoes/agressor-desinterresado.png"
image agressor disposto = "images/agressorReacoes/agressor-disposto.png"
image agressor espanto = "images/agressorReacoes/agressor-espanto.png"
image agressor feliz = "images/agressorReacoes/agressor-feliz.png"
image agressor gag = "images/agressorReacoes/agressor-gag.png"
image agressor impaciente = "images/agressorReacoes/agressor-impaciente.png"
image agressor irritado = "images/agressorReacoes/agressor-irritado.png"
image agressor neutro = "images/agressorReacoes/agressor-neutro.png"
image agressor reflexivo = "images/agressorReacoes/agressor-reflexivo.png"
image agressor serio = "images/agressorReacoes/agressor-serio.png"

image amigo empatico = "images/amigoReacoes/amigo-empatico.png"
image amigo feliz = "images/amigoReacoes/amigo-feliz.png"
image amigo preocupado = "images/amigoReacoes/amigo-preocupado.png"
image amigo neutro = "images/amigoReacoes/amigo-neutro.png"
image amigo duvida = "images/amigoReacoes/amigo-duvida.png"
image amigo determinado = "images/amigoReacoes/amigo-determinado.png"
image amigo desconfiado = "images/amigoReacoes/amigo-desconfiado.png"
image amigo indignado = "images/amigoReacoes/amigo-indignado.png"
image amigo frustrado = "images/amigoReacoes/amigo-frustrado.png"
image amigo reflexivo = "images/amigoReacoes/amigo-reflexivo.png"
image amigo surpreso = "images/amigoReacoes/amigo-surpreso.png"
image amigo ajudando = "images/amigoReacoes/amigo-ajudando.png"

image veronica neutra = "At('images/vitimaReacoes/veronica-neutra.png', sprite_highlight('[Vname]'))"
image veronica feliz = "images/vitimaReacoes/veronica-feliz.png"
image veronica assustada = "images/vitimaReacoes/veronica-assustada.png"
image veronica culpada = "images/vitimaReacoes/veronica-culpada.png"
image veronica desolada = "images/vitimaReacoes/veronica-desolada.png"
image veronica aliviada = "images/vitimaReacoes/veronica-aliviada.png"
image veronica triste = "images/vitimaReacoes/veronica-triste.png"
image veronica confusa = "images/vitimaReacoes/veronica-confusa.png"    
image veronica pensativa = "images/vitimaReacoes/veronica-pensativa.png"
image veronica sorriso forcado = "images/vitimaReacoes/veronica-sorriso-forcado.png"
image veronica cansada = "images/vitimaReacoes/veronica-cansada.png"
image veronica chorando = "images/vitimaReacoes/veronica-chorando.png"
image veronica determinada = "images/vitimaReacoes/veronica-determinada.png"
image veronica surpresa = "images/vitimaReacoes/veronica-surpresa.png"
image veronica medo = "images/vitimaReacoes/veronica-medo.png"
image veronica sorriso timido = "images/vitimaReacoes/veronica-sorriso-timido.png"



default Agname= "Alisson"
default Amname= "Marcelo"
default Vname= "Verônica"
default c1name= "Colega 1"
default c2name= "Colega 2"
default f1name= "Roberto"
default f2name= "Fábio"



define N = Character(None, callback=partial(blur_callback, None))
define e = Character('[Agname]', color="#ff0000", callback=multi_callback, cb_name='[Agname]', image= "agressor-neutro")
define a = Character('[Amname]', color="#5ffe50", callback=multi_callback, cb_name='[Amname]', image= "amigo-neutro")
define c1 = Character('[c1name]', callback=multi_callback, cb_name='[c1name]', image= "colega1-neutro")
define c2 = Character('[c2name]', callback=multi_callback, cb_name='[c2name]', image= "colega2-neutro")
define f1 = Character('[f1name]', callback=multi_callback, cb_name='[f1name]', image= "figurante1-neutro")
define f2 = Character('[f2name]', callback=multi_callback, cb_name='[f2name]', image= "figurante2-neutro")
define V = Character('[Vname]', color="#ed33e1", callback=multi_callback, cb_name='[Vname]', image= "veronica-neutra")

define N_nvl = Character(None, kind=nvl, callback=Phone_ReceiveSound)
define e_nvl = Character('[Agname]', kind=nvl, callback=Phone_ReceiveSound)
define c1_nvl = Character('[c1name]', kind=nvl, callback=Phone_ReceiveSound)
define c2_nvl = Character('[c2name]', kind=nvl, callback=Phone_ReceiveSound)
define V_nvl = Character('[Vname]', kind=nvl, callback=Phone_SendSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

transform mindfog:
    blur 4

label start:

    scene onibus
    with fade
    show veronica neutra at right onlayer chars

    c1_nvl "Bom dia, Nica!"
    c1_nvl "A apresentação de ontem foi incrível."
    c1_nvl "A diretoria ficou comentando sua proposta."
    show veronica feliz at right onlayer chars
    c2_nvl "Sério, você salvou aquela reunião. "
    c2_nvl "Eu não teria pensado naquela solução."
    e_nvl "Já chegou na empresa?"
    show veronica assustada at right onlayer chars
    e_nvl "Você não respondeu ainda."
    e_nvl "Está tudo bem??"
    show veronica culpada at right onlayer chars
    e_nvl "Eu fiz alguma coisa? Me responde por favor" 
    e_nvl "Estou esperando você na entrada." 
    show veronica desolada at right onlayer chars 
    e_nvl "Estou preocupado com você ."
jump start2 

label start2:
    
    scene 1
    with fade
    show veronica neutra at left onlayer chars
    show agressor serio at right onlayer chars
    
    e "Algo aconteceu no caminho?"
    e "Por que você não respondeu nenhuma das minhas mensagens?"
    show veronica triste at left onlayer chars
    e "Eu fico preocupado quando você age assim, você anda tão distraída ultimamente..."
    e "Você sabe como o mundo é perigoso."
    show agressor arrependido at right onlayer chars
    e "Eu só quero a sua segurança."
    show veronica surpresa at left onlayer chars
    V "Não é nada disso..."
    show veronica culpada at left onlayer chars
    V "O ônibus estava muito cheio e era difícil pegar o celular e responder as mensagens."
    V "Talvez você esteja exagerando sobre isso."
    show agressor irritado at right onlayer chars
    e "Exagerando?"
    e "Eu só estava preocupado com você."
    e "Fiquei a manhã inteira sem saber se estava tudo bem."
    show agressor arrependido at right onlayer chars
    e "Às vezes parece que eu me importo mais com você do que você se importa comigo."
    show veronica triste at left onlayer chars
    show agressor neutro at right onlayer chars
   

    V "Eu entendo que você tenha ficado preocupado."
    V "Só não achei que fosse algo tão sério."
    V "Mas da próxima vez eu aviso se acontecer algum atraso."
    show veronica neutra at left onlayer chars
    show agressor arrependido at right onlayer chars
    e "É só isso que eu peço."
    e "Você sabe que faço tudo pelo seu bem."
    show agressor feliz at right onlayer chars
    e "Eu realmente me importo com você querida. "
    show agressor neutro at right onlayer chars
    hide agressor 
    "Agressor sai de cena."
    jump start3
    with fade
label start3:
    scene 1

    "Logo após, o amigo de Verônica se aproxima"
    show veronica triste at left onlayer chars
    show amigo empatico at right onlayer chars
    c1 "Nica, tem algo rolando? As meninas estão sentindo que você anda se afastando do nosso grupinho."
    c1 "Antes você era a primeira a marcar alguma coisa para os fins de semana."
    show veronica neutra at left onlayer chars
    show amigo preocupado at right onlayer chars
    c1  " Tem algo acontecendo de diferente esses dias?"
    c1 "Se quiser conversar ou algo do tipo, eu estou aqui por você."
    show veronica abalada at left onlayer chars
    V "Eu só ando meio ocupada com algumas coisas."
    
    menu:
        "O que vai fazer?"

        "Sugerir ir à casa dele.":
            jump encontrofds
        "Negar seus problemas.":
            jump negarencontrofds

label encontrofds:
    
    scene 1
    with fade
    show amigo neutro at right onlayer chars
    show veronica feliz at left onlayer chars
    V "Que tal? posso ir à sua casa esse final de semana."
    V "E conversamos sobre isso jantando."
    hide amigo 
    hide veronica
jump start4

label negarencontrofds:
    
    scene 1
    with fade
    
    show amigo neutro at right onlayer chars
    show veronica triste at left onlayer chars
    V "Não está acontecendo nada, eu estou bem."
    V "Só ando muito ocupada com o trabalho e outras coisas. Fala para o pessoal não se preocupar comigo."
    show veronica sorriso-forcado at left onlayer chars
    V "Quando eu estiver livre do trabalho, a gente tenta marcar alguma coisa."
    hide amigo 
    hide veronica
jump start4


label start4:

    scene 3
    with dissolve 

    "Os colegas de empresa de Veronica estão discutindo sobre a reunião de ontem na copa."
    show veronica neutra at center
    show figurante1-neutro at left onlayer chars
    show figurante2-neutro at right onlayer chars
    f1 "Você viu a proposta da Verônica?"
    f1 "Olha, ela é um verdadeiro colírio aqui na empresa."
    f1 "Tem um jeito que conquista qualquer cliente."
    show figurante1-desdenhoso at left onlayer chars
    f1 "Mas aquele projeto tinha que ser liderado por alguém que conseguisse realmente lidar com a pressão de verdade."
    f1 "Não consigo imaginar ela liderando um projeto tão importante."
    show figurante2-desdenhoso at right onlayer chars
    f2 "Pode parar com essa ladainha, não precisa ficar tentando agradar."
    f2 "A gente sabe muito bem por que essa ideia não vai para frente."
    show figurante2-feliz at right onlayer chars
    f2 "Não importa o quanto ela tente."
    show figurante2-desdenhoso at right onlayer chars
    f2 "Ninguém vai apostar um projeto importante nas mãos dela."
    f2 "Quem levaria essa ideia adiante sabendo que uma mulher que deu início ao projeto?"

    menu:
        "Como você responderá a isso?"

        "Confrontá-los":
            jump Vconfronta

        "Não fazer nada.":
            jump Vamarela

label Vconfronta:
    
    scene 3
    with dissolve 

    show veronica sorriso forcado at center onlayer chars
    V "Mais alguma sugestão de como eu deveria lidar com esse projeto?"
    
    show figurante2-assustado at right onlayer chars
    show figurante1-assustado at left onlayer chars
    
    V "Porque até agora eu só ouvi comentários sobre mim. "
    
    show figurante2-envergonhado at right onlayer chars
    show figurante1-envergonhado at left onlayer chars
    
    show veronica neutra at center onlayer chars
    V "Nenhum de vocês falou sobre a proposta."
    V "Se existe algum problema no projeto, eu gostaria de ouvir."
    
    show figurante2-irritado at right onlayer chars
    f2 "Não precisa ficar tão seria assim, Só estamos tentando ser sinceros e dar o nosso feedback."
    show figurante2-desdenhoso at right onlayer chars
    f2 "Nem toda crítica precisa ser levada para o lado pessoal."
    show figurante2-irritado at right onlayer chars
    f2 "Se você não consegue lidar nem com isso, como pretende lidar com um projeto desse tamanho?"
    
    show figurante1-assustado at left onlayer chars
    f1 " Você tá totalmente certa verô!"
    show figurante1-feliz at left onlayer chars

    show figurante2-assustado at right onlayer chars

    f1 "Acho que houve um mal-entendido."
    f1 "Já estamos de saída, pode ter certeza de que vamos pensar nisso que você falou."
    show figurante1-assustado at left onlayer chars
    f1 "Vamos logo Fábio, antes que o intervalo termine."
    
    hide figurante1-assustado
    hide figurante2-assustado
    "Os dois depressa desaparecem nos corredores do prédio."
    show veronica triste at left onlayer chars
    with fade
jump start5
label Vamarela:    

    scene 3

    show figurante1-desdenhoso at left 
    show figurante2-desdenhoso at right 
    show veronica triste at center onlayer chars
    V "Melhor só deixar isso para lá."
    V "Nem iria adiantar tentar responder esses tipos de comentários."
    show veronica desolada at left onlayer chars
    V "Eles nem estão discutindo sobre o meu projeto, somente sobre minha capacidade de fazer ou não fazer, por ser mulher."
jump onibus

label onibus:

    scene onibus
    with fade

    show veronica desolada at left onlayer chars
    N_nvl "..."
    with dissolve 
jump start5

label start5:

    scene onibus
    with fade

    show veronica neutra at left onlayer chars
    "Verônica está pensativa com tudo o que aconteceu hoje no seu trabalho."
    V "{i}Eles disseram que estavam só tentando ajudar.{/i}"
    show veronica pensativa at left onlayer chars
    V "{i}Mas em nenhum momento falaram sobre a proposta.{/i}"
    V "{i}Só falaram sobre o que eu supostamente não conseguiria fazer.{/i}"
    V "{i}O Alisson também diz que só quer me proteger.{/i}"
    V "{i}Mas ele sempre age como se eu não conseguisse me cuidar sozinha.{/i}"
    show veronica confusa at left onlayer chars
    V "{i}Será que eles realmente estão tentando ajudar?{/i}"
    V "{i}Ou simplesmente não confiam em mim?{/i}"
    
    show veronica neutra at left onlayer chars
    c1_nvl "Verô, você estava certa na copa"
    show veronica surpresa at left onlayer chars
    c1_nvl "não deixa aquilo te abalar"
    show veronica feliz at left onlayer chars
    c2_nvl "Vai rolar um encontro com o pessoal"
    c2_nvl "Você deveria aparecer por lá"
    
    e_nvl "Já saiu da empresa?"
    show veronica surpresa at left onlayer chars
    e_nvl "Seu amigo parece não gostar muito de mim"
    show veronica assustada at left onlayer chars
    e_nvl "Acho estranho ele ficar tentando se envolver nos nossos problemas"
    show veronica desolada at left onlayer chars
    e_nvl " Estou indo para sua casa."
jump start6
with fade

label start6:

    scene 4
    with fade
    show agressor raiva at left onlayer chars
    "O Alisson a espera em frente a sua casa para confrontá-la sobre a conversa com seu amigo."
    show veronica surpresa at right onlayer chars
    show agressor irritado at left onlayer chars
    e "Seu amiguinho parece se incomodar muito comigo."
    e "Eu vi vocês dois conversando."
    e "E desde então você está estranha."
    show agressor confuso at left onlayer chars
    e "Se tem alguma coisa te incomodando, por que não fala comigo?"
    show agressor triste at left onlayer chars
    e "Eu sou seu namorado"
    e "Não deveria precisar procurar outras pessoas para resolver os nossos problemas."
    show agressor serio at left onlayer chars
    e "Vamos conversar."

    menu:
        "Alisson quer conversar com você"
        "O que você fará?"

        "Tentar se justificar para manter o relacionamento":
            jump justificarA

        "Pedir para que ele se afaste e tentar entrar em casa":
            jump confrontarA
        
        "Se afastar imediatamente e correr para um lugar seguro":
            jump aceitarA

label justificarA:
    scene 4
    "Verônica começa a chorar desesperadamente."
    with fade
    
    show agressor serio at left onlayer chars
    show veronica chorando at right onlayer chars
    V "Me escuta, por favor."
    V "Não é nada disso que você está pensando."
    V "Ele só entendeu errado."
    show veronica triste at right onlayer chars
    V "Achou que eu estava me afastando deles por sua causa, mas não é nada disso."
    V " Só ando ocupada com o trabalho e as reformas para morarmos juntos."

    show agressor neutro at right onlayer chars
    e "Viu? Era só isso que eu queria entender."
    show agressor feliz at right onlayer chars
    e "Às vezes você deixa as outras pessoas te influenciarem demais, querida."
    e "Agora vamos. Me deixe cuidar de você."
    e "Eu sei o que é melhor para você."
    hide veronica triste
    hide agressor feliz

    "Eles entram em casa juntos. Verônica passa pela porta ainda soluçando baixinho."
jump finalruim

label finalruim:

    scene 5
    with fade

    "Mesmo cercada por sinais de alerta"
    "Veronica ainda acredita que tudo aquilo é apenas preocupação e amor."
    "Enquanto tenta preservar o relacionamento, ela deixa de perceber o quanto sua liberdade e sua confiança estão sendo tiradas pouco a pouco."
    "O ciclo continua."
    with dissolve
    
label confrontarA:
    
    scene 4
    with fade

    show agressor surpreso at left onlayer chars
    show veronica assustada at right onlayer chars

    V "Eu não quero conversar agora!"
    show veronica chorando at right onlayer chars
    V "Por favor, me deixa sozinha."
    show veronica neutra at right onlayer chars
    V "Amanhã, quando estivermos mais calmos, podemos falar sobre isso."
    
    show agressor raiva at left onlayer chars
    e "Por que você está falando assim?"
    e "Eu só quero conversar."
    show agressor irritado at left onlayer chars
    e "Você está agindo como se eu tivesse feito alguma coisa errada."
    show agressor triste at left onlayer chars
    e "Vem cá."
    e "{i}Se aproxima pra um abraço{/i} Deixa eu resolver isso."
    show veronica triste at right onlayer chars
    show agressor surpreso at left onlayer chars
    V "{i}Empurra{/i} Eu não quero conversar agora."
    V "Me deixa em paz!"

    show agressor irritado at left onlayer chars
    hide veronica triste
    "{i}Ele a alcança{/i}"
    with fade
jump finalmediano

label finalmediano:

    scene 5
    "Veronica tenta impor seus limites, mas eles são ignorados."
    "À medida que o clima se torna mais pesado, ela começa a perceber que a preocupação e o cuidado que tanto ouviu podem esconder algo muito diferente."
    "Agora, a dúvida tomou o lugar da certeza."
    with dissolve

label aceitarA:
    
    scene 4
    with fade

    show veronica assustada at right onlayer chars
    show agressor neutro at left onlayer chars

    V "{i}Se prepara para correr{/i} Se você realmente se importa comigo, então me escuta."
    V "Eu não quero conversar agora."
    V "Eu quero ficar sozinha."
    V "Por favor, vai embora."
    
    show agressor irritado at left onlayer chars
    e "O que está acontecendo com você!?"
    e "Eu só estou tentando conversar."
    show agressor impaciente at left onlayer chars
    e "Mas você continua me afastando como se eu fosse o problema."
    e "Eu já disse que só quero o seu bem."
    show agressor arrependido at left onlayer chars
    e "Me deixa ficar aqui."

    show veronica medo at right onlayer chars
    V "Você diz que quer o meu bem, então respeita o que eu to pedindo."
    show veronica culpada at right onlayer chars
    V "Eu quero ficar sozinha."
    V "Sai daqui, por favor."

    "Verônica correu sem esperar a resposta dele."
    

jump finalbom

label finalbom:

    scene 5
    with fade

    "Depois de tanto tempo tentando lidar com tudo sozinha, Veronica decide pedir ajuda."
    "Entre lágrimas e desabafos, ela começa a enxergar que o amor não deveria causar medo, isolamento ou culpa."
    "Ao confiar em alguém, ela encontra a força necessária para começar uma nova fase da sua vida."
    with dissolve
     
    return