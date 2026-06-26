Skip to content
BatatoHackerman
Jogo
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
Files
Go to file
t
T
audio
images
01auto-highlight.rpy
README.md
errors.txt
gui.rpy
log.txt
options.rpy
project.json
screens.rpy
script.rpy
traceback.txt
Jogo
/
script.rpy
in
main

Edit

Preview
Indent mode

Spaces
Indent size

4
Line wrap mode

No wrap
Editing script.rpy file contents
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
﻿image agressor arrependido = At("images/agressorReacoes/agressor-arrependido.png", sprite_highlight('agressor'))
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
    show agressor surpreso at left onlayer chars
    V "Eu quero ficar sozinha."
    V "Sai daqui, por favor."

    "Verônica correu sem esperar a resposta dele."
    hide agressor onlayer chars
    hide veronica onlayer chars
    with dissolve
jump finalbom

label finalbom:

    scene escritorio_noite
    with fade

    "Depois de tanto tempo tentando lidar com tudo sozinha, Veronica decide pedir ajuda."
    "Entre lágrimas e desabafos, ela começa a enxergar que o amor não deveria causar medo, isolamento ou culpa."
    "Ao confiar em alguém, ela encontra a força necessária para começar uma nova fase da sua vida."
    with dissolve
    return

label mstart1:
    scene escritorio_copa
    with fade

    show colega1 preocupado at left onlayer chars
    show amigo neutro at center
    show colega2 neutro at right
    with dissolve

    c1 "Gente, e a Verô? ela está bastante sumida ultimamente."
    c1 "Dificilmente ela interage com a gente, será que está bem?"
    c2 " Ela estava falando sobre estar ocupada com mudanças e o trabalho ..."
    show colega2 desconfiado at right
    c2 "Mas eu acho que tem alguma coisa além disso."
    c2 "Pode ter haver com o Alisson, talvez eles tenham discutido recentemente, ou algo do tipo."
    show amigo preocupado at center

    "Suas colegas suspeitam de algo envolvendo o relacionamento da sua melhor amiga Verônica."

    menu:
        "Como você reagirá?"
        "Se esquivar das perguntas":
            show amigo ajudando at center
            a "Eu não acho legal me meter no relacionamento deles"
            a "independentemente do que tenha ocorrido."
            a "Deveria ficar somente entre eles."
            jump mstart2

        "Se juntar ao questionamento":
            show amigo reflexivo at center
            a "Realmente, ela anda um pouco afastada."
            a "Eu gostaria de compreender o que está acontecendo."
            show amigo feliz at center
            a "Acho que irei tentar conversar com ela sobre."
            a "Para tentar descobrir alguma coisa sobre a situação."



Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
 
