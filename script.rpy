define N = Character(None, callback=partial(blur_callback, None))
define e = Character('Agressor', callback=partial(blur_callback, "e"))
define c1 = Character('colega1', callback=partial(blur_callback, "c1"))
define c2 = Character('colega2', callback=partial(blur_callback, "c2"))
define f1 = Character('figurante1', callback=partial(blur_callback, "f1"))
define f2 = Character('figurante2', callback=partial(blur_callback, "f2"))
define V = Character("Verônica", callback=partial(blur_callback, "V"))

define N_nvl = Character(none, kind=nvl, callback=Phone_ReceiveSound)
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
    e_nvl "Já chegou na empresa?"
    show agressor-espanto at right onlayer chars
    e_nvl "Você não respondeu ainda."
    e_nvl "Está tudo bem??"
    show agressor-arrependido at right onlayer chars
    e_nvl "Eu fiz alguma coisa? Me responde por favor" 
    e_nvl "Estou esperando você na entrada." 
    show agressor-assustado at right onlayer chars 
    e_nvl "Estou preocupado com você ."
    jump start2 

label start2:
    
    scene 1
    with fade
    show veronica-neutra at left onlayer chars
    show agressor-serio at right onlayer chars
    
    e "Algo aconteceu no caminho?"
    e "Por que você não respondeu nenhuma das minhas mensagens?"
    show veronica-triste at left onlayer chars
    e "Eu fico preocupado quando você age assim, você anda tão distraída ultimamente..."
    e "Você sabe como o mundo é perigoso."
    show agressor-preocupado at right onlayer chars
    e "Eu só quero a sua segurança."
    show veronica-confusa at left onlayer chars
    V "Não é nada disso..."
    V "O ônibus estava muito cheio e era difícil pegar o celular e responder as mensagens."
    V "Talvez você esteja exagerando sobre isso."
    show agressor-raiva at right onlayer chars
    e "Exagerando?"
    e "Eu só estava preocupado com você."
    e "Fiquei a manhã inteira sem saber se estava tudo bem."
    show agressor-triste at right onlayer chars
    e "Às vezes parece que eu me importo mais com você do que você se importa comigo."
    show veronica-triste at left onlayer chars
    show agressor-neutro at right onlayer chars
   

    V "Eu entendo que você tenha ficado preocupado."
    V "Só não achei que fosse algo tão sério."
    V "Mas da próxima vez eu aviso se acontecer algum atraso."
    show veronica-neutra at left onlayer chars
    show agressor-triste at right onlayer chars
    e "É só isso que eu peço."
    e "Você sabe que faço tudo pelo seu bem."
    show agressor-feliz at right onlayer chars
    e "Eu realmente me importo com você querida. "
    show agressor-neutro at right onlayer chars
    "Agressor sai de cena."
    jump start3
    with fade
label start3:
    scene 2

    "Logo após, o amigo de Verônica se aproxima"
    show veronica-triste at left onlayer chars
    show colega1-neutro at right onlayer chars
    c1 "Nica, tem algo rolando? As meninas estão sentindo que você anda se afastando do nosso grupinho."
    c1 "Antes você era a primeira a marcar alguma coisa para os fins de semana."
    show veronica-neutra at left onlayer chars
    show colega1-preocupado at right onlayer chars
    c1  " Tem algo acontecendo de diferente esses dias?"
    c1 "Se quiser conversar ou algo do tipo, eu estou aqui por você."
    show veronica-abalada at left onlayer chars
    V "Eu só ando meio ocupada com algumas coisas."
    
    menu:
        "O que vai fazer?"

        "Sugerir ir à casa dele.":
        jump encontrofds
        "Negar seus problemas.":
        jump negarencontrofds

label encontrofds:
    
    scene 2
    with fade
    show colega1-neutro at right onlayer chars
    show veronica-feliz at left onlayer chars
    V "Que tal? posso ir à sua casa esse final de semana."
    V "E conversamos sobre isso jantando."
jump start4

label negarencontrofds:
    
    scene 2
    with fade
    
    show colega1-neutro at right onlayer chars
    show veronica-triste at left onlayer chars
    V "Não está acontecendo nada, eu estou bem."
    V "Só ando muito ocupada com o trabalho e outras coisas. Fala para o pessoal não se preocupar comigo."
    show veronica-feliz at left onlayer chars
    V "Quando eu estiver livre do trabalho, a gente tenta marcar alguma coisa."
jump start4


label start4:

    scene copa
    with dissolve 0.3

    "Os colegas de empresa de Veronica estão discutindo sobre a reunião de ontem na copa."
    show veronica-neutra at center
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
    
    scene copa
    with dissolve 0.3

    show veronica-irritada at center onlayer chars
    V "Mais alguma sugestão de como eu deveria lidar com esse projeto?"
    
    show figurante2-assustado at right onlayer chars
    show figurante1-assustado at left onlayer chars
    
    V "Porque até agora eu só ouvi comentários sobre mim. "
    
    show figurante2-envergonhado at right onlayer chars
    show figurante1-envergonhado at left onlayer chars
    
    show veronica-seria at center onlayer chars
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
    
    hide figurante1-assustado, figurante2-assustado
    "Os dois depressa desaparecem nos corredores do prédio."
    show veronica-triste at left onlayer chars
    with fade
jump start5
label Vamarela:    

    scene copa

    show veronica-triste at left onlayer chars
    V "Melhor só deixar isso para lá."
    V "Nem iria adiantar tentar responder esses tipos de comentários."
    show veronica-abalada at left onlayer chars
    V "Eles nem estão discutindo sobre o meu projeto, somente sobre minha capacidade de fazer ou não fazer, por ser mulher."
jump onibus

label onibus:

    scene onibus
    with fade

    show veronica-abalada at left onlayer chars
    N_nvl "..."
    with dissolve 0.3
jump start5

label start5:

    scene onibus
    with fade

    show veronica-neutra at left onlayer chars
    "Verônica está pensativa com tudo o que aconteceu hoje no seu trabalho."
    V "{i}Eles disseram que estavam só tentando ajudar.{/i}"
    show veronica-seria at left onlayer chars
    V "{i}Mas em nenhum momento falaram sobre a proposta.{/i}"
    V "{i}Só falaram sobre o que eu supostamente não conseguiria fazer.{/i}"
    V "{i}O Alisson também diz que só quer me proteger.{/i}"
    V "{i}Mas ele sempre age como se eu não conseguisse me cuidar sozinha.{/i}"
    show veronica-confusa at left onlayer chars
    V "{i}Será que eles realmente estão tentando ajudar?{/i}"
    V "{i}Ou simplesmente não confiam em mim?{/i}"
    
    show veronica-neutra at left onlayer chars
    c1_nvl "Verô, você estava certa na copa"
    show veronica-surpresa at left onlayer chars
    c1_nvl "não deixa aquilo te abalar"
    show veronica-feliz at left onlayer chars
    c2_nvl "Vai rolar um encontro com o pessoal"
    c2_nvl "Você deveria aparecer por lá"
    
    e_nvl "Já saiu da empresa?"
    show veronica-surpresa at left onlayer chars
    e_nvl "Seu amigo parece não gostar muito de mim"
    show veronica-assustada at left onlayer chars
    e_nvl "Acho estranho ele ficar tentando se envolver nos nossos problemas"
    show veronica-desolada at left onlayer chars
    e_nvl " Estou indo para sua casa."
jump start6
with fade

label start6:

    scene casaV
    with fade
    show agressor-raiva at left onlayer chars
    "O Alisson a espera em frente a sua casa para confrontá-la sobre a conversa com seu amigo."
    show veronica-surpresa at right onlayer chars
    show agressor-irritado at left onlayer chars
    e "Seu amiguinho parece se incomodar muito comigo."
    e "Eu vi vocês dois conversando."
    e "E desde então você está estranha."
    show agressor-confuso at left onlayer chars
    e "Se tem alguma coisa te incomodando, por que não fala comigo?"
    show agressor-triste at left onlayer chars
    e "Eu sou seu namorado"
    e "Não deveria precisar procurar outras pessoas para resolver os nossos problemas."
    show agressor-serio at left onlayer chars
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

label justificar:
    scene casaV
    "Verônica começa a chorar desesperadamente."
    with fade
    
    show agressor-serio at left onlayer chars
    show veronica-chorando at right onlayer chars
    V "Me escuta, por favor."
    V "Não é nada disso que você está pensando."
    V "Ele só entendeu errado."
    show veronica-triste at right onlayer chars
    V "Achou que eu estava me afastando deles por sua causa, mas não é nada disso."
    V " Só ando ocupada com o trabalho e as reformas para morarmos juntos."

    show agressor-neutro at right onlayer chars
    e "Viu? Era só isso que eu queria entender."
    show agressor-feliz at right onlayer chars
    e "Às vezes você deixa as outras pessoas te influenciarem demais, querida."
    e "Agora vamos. Me deixe cuidar de você."
    e "Eu sei o que é melhor para você."
    hide veronica-triste, agressor-feliz

    "Eles entram em casa juntos. Verônica passa pela porta ainda soluçando baixinho."
jump finalruim

label finalruim:

    scene finalruim
    with fade

    "Mesmo cercada por sinais de alerta"
    "Veronica ainda acredita que tudo aquilo é apenas preocupação e amor."
    "Enquanto tenta preservar o relacionamento, ela deixa de perceber o quanto sua liberdade e sua confiança estão sendo tiradas pouco a pouco."
    "O ciclo continua."
    with dissolve 1.5
    
label confrontarA:
    
    scene casaV
    with fade

    show agressor-surpreso at left onlayer chars
    show veronica-assustada at right onlayer chars

    V "Eu não quero conversar agora!"
    show veronica-chorando at right onlayer chars
    V "Por favor, me deixa sozinha."
    show veronica-neutro at right onlayer chars
    V "Amanhã, quando estivermos mais calmos, podemos falar sobre isso."
    
    show agressor-raiva at left onlayer chars
    e "Por que você está falando assim?"
    e "Eu só quero conversar."
    show agressor-irritado at left onlayer chars
    e "Você está agindo como se eu tivesse feito alguma coisa errada."
    show agressor-triste at left onlayer chars
    e "Vem cá."
    e "{i}Se aproxima pra um abraço{/i} Deixa eu resolver isso."
    show veronica-irritada at right onlayer chars
    show agressor-surpreso at left onlayer chars
    V "{i}Empurra{/i} Eu não quero conversar agora."
    V "Me deixa em paz!"

    show agressor-irritado at left onlayer chars
    hide veronica-irritada
    "{i}Ele a alcança{/i}"
    with fade
jump finalmediano

label finalmediano:

    scene finalmediano
    "Veronica tenta impor seus limites, mas eles são ignorados."
    "À medida que o clima se torna mais pesado, ela começa a perceber que a preocupação e o cuidado que tanto ouviu podem esconder algo muito diferente."
    "Agora, a dúvida tomou o lugar da certeza."
    with dissolve 1.5

label aceitarA:
    
    scene casaV
    with fade

    show veronica-assustada at right onlayer chars
    show agressor-neutro at left onlayer chars

    V "{i}{/i}"







    return
