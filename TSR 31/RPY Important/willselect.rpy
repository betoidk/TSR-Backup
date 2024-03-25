label will_chapter_select:

show black with dissolve

#Point reset (keep an eye on this)
$ SW_Points =0
$ DD_Points =0
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
$ unlocked_journal_pages = 0
$ STAGNIGHT_Points = 0
$ STAGDAY_Points = 0
$ CITYHALLNIGHT_Points = 0
$ CITYHALLDAY_Points = 0
$ PORINT_Points = 0
$ MININT_Points = 0
$ ETHINT_Points = 0
$ HARINT_Points = 0
$ CYNINT_Points = 0
$ DORINT_Points = 0
$ BG_Light = 0
$ willstag1interview = False
$ willstag2interview = False
$ willstag3interview = False
$ willstag1interview2 = False
$ willstag2interview2 = False
$ willchall1interview = False
$ willchall2interview = False
$ willchall3interview = False
$ willmanorportrait1 = False
$ willmanorkitchen1 = False
$ willmanorlivingroom1 = False
$ willjamesfile = False
$ willjamesfolder = False
$ willjamestrash = False
$ chnighttext = "I should go to city hall."
$ chnighttextes = "Debería ir al ayuntamiento"
$ stagnighttext = "I wonder what folks at the stag might have to offer?"
$ stagnighttextes = " Me pregunto qué podrían ofrecer la gente del ciervo."
$ cynthiatext = ".."
$ cynthiatextes = ".."
$ jamestext = "Hendricks is usually up to something. Worst thing is, it's probably not illegal."
$ jamestextes = " Hendricks suele estar metido en algo. Lo peor es que probablemente no sea ilegal."
$ portertext = "City Hall holds a lot of secrets."
$ portertextes = "El Ayuntamiento guarda muchos secretos."
$ changtext = "Could a CGCS employee placed a hit on Cliff, or was it somebody else?"
$ changtextes = "¿Podría un empleado de CGCS haber ordenado matar a Cliff, o fue otra persona?"
$ huxley1 = "I need to find Reed."
$ huxley1es = "Necesito encontrar a Reed."
$ huxley2 = "Marcy may know what happened to the gun."
$ huxley2es = "Marcy podría saber qué pasó con el arma."
$ huxley3 = "So what was Reed up to if he didn't place a hit on Cliff?"
$ huxley3es = "Entonces, ¿qué estaba haciendo Reed si no mató a Cliff?"
$ etheltext = "The workers at the hip are the best source of information in town."
$ etheltextes = "Los trabajadores del Hip son la major fuente de información del pueblo."
$ harlantext = "The staff at the hip turned a saloon in the middle of nowhere into a world-famous attraction."
$ harlantextes = "El personal del Hip convirtió un salón en medio de la nada en una atracción de fama mundial."
$ jamesimage = "todddumb"
$ huxley4 = "The body was in a ditch."
$ huxley4es = "El cuerpo estaba en una zanja."
$ gumtext = "Tutti-frutti."
$ gumtextes = "Tutti-frutti."
$ kanetext = "Do I feel like making a mistake? Maybe."
$ kanetextes = "¿Siento ganas de cometer un error?\nTal vez."
$ filmtext = "This looks like one of the film rolls Murdoch's used before."
$ filmtextes = "Esto parece uno de los rollos de película que Murdoch ha usado antes."
$ jartext = "One of these flowers is definitely mugwart."
$ jartextes = "Una de estas flores es definitivamente artemisa."
$ dolltext = "A doll in the basement."
$ dolltextes = "Una muñeca en el sótano."
$ marcydolltext = "..."
$ marcydolltextes = "..."
$ samtoddtext = "Slick, fellahs..."
$ samtoddtextes = "Calenturientos, amigos..."
$ shroudtext = "Her grandma's shroud was in the bed... I have a pretty good idea of what we'd find if we opened it."
$ shroudtextes = "La mortaja de su abuela estaba en la cama... Tengo una buena idea de lo que encontraríamos si la abriéramos."
$ murdochtext = "It's probably nothing."
$ murdochtextes = "Probablemente no sea nada."
$ portraittext = "I need to get a good look at the portrait of James the First..."
$ portraittextes = "Necesito ver bien el retrato de\nJames I..."
$ manortext = "Is there anything James is hiding?"
$ manortextes = "¿Hay algo que James esté ocultando?"
$ investigorder = "first"
$ investigorderes = "primero"
$ KaneChoice = False

#Chapter 1 label - can skip directly

if (chapter_value == 1):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    scene powderroom with dissolve
    jump williamroute

#Chapter 2 label - can skip directly

if (chapter_value == 2):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    play background "sfx/crickets.ogg" fadein 3.0
    jump williamroute2

#Chapter 3 label:

menu:
    "When William confides in you his feelings about his wife arriving in echo, what did you tell him?"

    "Nothing. You reminded him of his heartbeat.":
        $ SW_Points +=1
    "You said that his duty to his family was noble.":
        $ SW_Points +=0
    "You told him he made a hard choice.":
        $ SW_Points +=1
    "You told him it's okay to be a little bit selfish.":
        $ SW_Points +=1



menu:
    "Did you reveal yourself to Harlan after Dora talks to him about the box?"

    "Yes":
        $ DD_Points +=1

    "No":
        menu:
            "Where did you hide?"

            "I crouched and waited for him to leave.":
                $ DD_Points +=1
            "I slipped into the office quickly.":
                $ DD_Points +=0



menu:
    "When William wondered what was wrong with his judgement in the mines, you:"

    "Assured him he's done nothing wrong.":
        $ SW_Points +=0
    "Said that people sometimes hallucinate.":
        $ SW_Points +=1
    "Joked about witches influencing him.":
        $ SW_Points +=1
    "Talked about gasses in the mines.":
        $ SW_Points +=1

if (chapter_value == 3):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    jump williamroute3

#End of last update label:

menu:
    "As William, did you get Sam off in the bedroom?"

    "Yes.":
        $ SW_Points +=1
    "No.":
        $ SW_Points +=0


$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
$ unlocked_journal_pages += 7

menu:
    "Where did you go investigate first in the day?"

    "City Hall.":
        $ unlocked_journal_pages += 6
        $ CITYHALLDAY_Points +=1
        $ STAGNIGHT_Points +=1
        $ MININT_Points +=1
        $ stagnighttext = "Harlan gets into fights with James? He usually keeps things professional."
        $ stagnighttextes = "¿Harlan se pelea con James? Suele ser profesional."
        $ willstag1interview2 = True

    "The Stag.":
        $ unlocked_journal_pages += 6
        $ STAGDAY_Points +=1
        $ CITYHALLNIGHT_Points +=1
        $ PORINT_Points +=1
        $ chnighttext = "Apparently, at least one person who works at the hip is leaking information to James."
        $ chnighttextes = "Al parecer, al menos una persona que trabaja en el Hip está filtrando información a James."


$ huxley1 = "According to Reed, Huxley's gun was pawned. Sales records indicate Huxley repurchased it."
$ huxley1es = "Según Reed, el arma de Huxley fue empeñada. Los registros de ventas indican que Huxley la recompró."
$ huxley3 = "Huxley was an alcoholic who needed more money for his drinking habit. I wonder where he was getting the cash?"
$ huxley3es = "Huxley era un alcohólico que necesitaba más dinero para su adicción a la bebida. Me pregunto de dónde sacaba el dinero."
$ huxley2 = "Marcy may know what happened to the gun."
$ huxley2es = "Marcy podría saber qué pasó con el arma."
$ changtext = "{s}Could a CGCS employee placed a hit on Cliff, or was it somebody else?{/s} Seems like the CGCS employees loyal to the company don't even get along. Some favor James. Some favor Briggs."
$ changtextes = "{s}¿Podría un empleado de CGCS haber ordenado matar a Cliff, o fue otra persona?{/s} Parece que los empleados leales a CGCS ni siquiera se llevan bien entre ellos. Algunos apoyan a James. Otros apoyan a Briggs."
$ jamestext = "Made James bleed. Was funny."
$ jamestextes = "Hice sangrar a James. Fue divertido."
$ jamesimage = "wn8"
$ willchall1interview = True
$ willchall2interview = True
$ willstag1interview = True
$ willstag2interview2 = True
$ willstag3interview = True
$ unlocked_journal_pages += 2
$ cynthiatext = "Maybe Cynthia does too."
$ cynthiatextes = "Quizá Cynthia también."



menu:
    "Who did you interview at the Hip?"

    "Dora.":
        $ DORINT_Points +=1

    "Harlan.":
        if  MININT_Points > 0:
            $ HARINT_Points += 1
            $ harlantext = "Harlan has a grudge against James and has regular access to most of Dora's information."
            $ harlantextes = "Harlan guarda rencor a James y tiene acceso regular a la mayor parte de la información de Dora."

    "Ethel.":
        if  PORINT_Points > 0:
            $ ETHINT_Points +=1
            $ etheltext = "Ethel reacted to a hollow threat of exposure. She's probably the one leaking information to James."
            $ etheltextes = "Ethel reaccionó a una amenaza vacía de revelación. Ella es probablemente la que filtra información a James."

    "Cynthia.":
        $ CYNINT_Points +=1

$ unlocked_journal_pages += 9
$ marcydolltext = "It used to belong to Marcy's sister."
$ marcydolltextes = "Solía pertenecer a la hermana de Marcy."
$ current_journal_page = 23

if (chapter_value == 4):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    play music "music/quiet.ogg" fadein 3.0
    window show
    scene bg darkroom
    show mur shock at center,red
    show gre f frown at left,red
    with dissolve
    jump williamroute3b

$ willmanorportrait1 = True
$ willmanorkitchen1 = True
$ willmanorlivingroom1 = True
$ willjamesfile = True
$ willjamesfolder = True
$ willjamestrash = True
$ portraittext = "The Hendricks house has hollow walls that the owners claim not to understand, entirely. The painting at the top of the stairs in the foyer has hinges."
$ portraittextes = "La casa de los Hendricks tiene paredes huecas que los propietarios dicen no entender, del todo. El cuadro que hay en lo alto de la escalera del vestíbulo tiene bisagras."
$ manortext = "There is a vanity full of hand mirrors near the basement of the Hendricks mansion. The amount and variety of them is more than excessive."
$ manortextes = "Hay un tocador lleno de espejos de mano cerca del sótano de la mansión Hendricks. La cantidad y variedad de ellos es más que excesiva."
$ unlocked_journal_pages += 4
$ current_journal_page = 27

if (chapter_value == 5):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    window show
    scene bg hipwashroom
    show cyn serious a at centerleft
    show cli at right
    with dissolve
    jump williamroute3c
