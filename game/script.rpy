init:
    define config.default_music_volume=0.7
    default persistent.restarts=0  
    default persistent.nudistend=0
    default persistent.sleepyend=0
    default persistent.end1=0
    default persistent.end2=0
    default persistent.end3=0
    default persistent.ends=0
    default Vclothes = False
    default Cclothes = False
    default Mclothes = False
    default Tclothes = False
    default choice_A1_made=False
    default choice_A2_made=False
    default choice_A3_made=False
    default choice_A4_made=False
    default choice_C2_made=False
    default choice_C3_made=False
    default choice_C4_made=False
    default PuckMet=False
    default PaleMet=False
    default PathMet=False
    default PrayMet=False
    default PoemMet=False
    default coffeeused=False
    default artsuppliesowned=False
    default cannoliowned=False
    default paperowned=False
    default marionetteowned=False
    default pendantowned=False
    $ money=0
    $ moneymod=0
    $ beggingresult=0
    $ suspicion=0
    $ suspicionmod=0
    $ arrestresult=0
    $ smoochresult=0
    default choice_F1_made=False
    

################## Prologue
label start:
    "{i}{cps=20}Che cos'è il crollo? Semplice, è la fine di tutto. La morte senza pace, la morte senza senso. Indossate le maschere, bambini, e ignorate la melodia delle bombe.{/cps}{/i}"
    $ Achievement.add(achievement_name['places'])
    "{cps=30}Your consciousness stirs as sound comes into focus. It’s coming from outside.{/cps}"
    play music "audio/AMB_Street_1.ogg" volume 0.2 fadein 1.0
    "{cps=30}You roll around in bed as your nerves slowly come back online from slumber, and your sense of smell brings in the brackish water of the canals, the floral breeze of various patios, and the mirad fried pastries and tarts that are being sold out of stands and bakeries nearby.{/cps}"
    "{cps=30}Your memory returns to you as you process this unique potpourri, you are a tourist in the city of Venice during the {color=#308CDD}{b}Carnevale di Venezia{/b}{/color}.{/cps}"
    #change bg HOTEL
    scene bg hotel
    with fade
    "{cps=30}You open your eyes, revealing your hotel room.{/cps}"
    "{cps=30}You have not been staying long, and that is evident in the relative cleanliness of this place. Your suitcases are still mostly unpacked.{/cps}"
    "{cps=30}You stretch and stand up out of your bed.{/cps}" 
    "{cps=30}What do you do?{/cps}"

label prologuemenu:
    menu:
        "I get dressed.":
            if not choice_A1_made: 
                jump A1
            else:
                "{cps=30}You already did that.{/cps}"
                jump prologuemenu
        "I check the time.":
            if not choice_A2_made: 
                jump A2
            else:
                $ Achievement.add(achievement_name['centhusiast'])
                "{cps=30}You already did that.{/cps}"
                jump prologuemenu
        "I unpack my bags.":
            if not choice_A3_made: 
                jump A3
            else:
                "{cps=30}You already did that.{/cps}"
                jump prologuemenu
        "I leave the room.":
            jump A4
    

label A1:
    $ choice_A1_made=True
    "{cps=30}You shower and put on some clothes as the sounds of crowded streets and happy people flow in from your hotel room’s window.{/cps}"
    "{cps=30}What kind of outfit do you put on?{/cps}"
    menu:
        "A fierce, unique outfit. One that showcases my personality.":
            jump B1
        "A comfortable, modern outfit. One that I can walk around in.":
            jump B2
        "A minimalistic, ‘just crawled out of bed’ outfit. One that tells everyone ‘I didn’t sleep well last night’.":
            jump B3
        "A traditional, carnival-specific outfit. One that hides my identity.":
            jump B4

label A2:
    $ choice_A2_made=True
    "{cps=30}You check the time on your watch...{/cps}"
    "{cps=30}It is currently 9:47 am.{/cps}"
    jump prologuemenu

label A3:
    $ choice_A3_made=True
    "{cps=30}You take time to unpack your bags...{/cps}"
    "{cps=30}You find 15 money in one of your bags!{/cps}"
    $ money+=15
    jump prologuemenu

label A4:
    $ choice_A4_made=True
    "{cps=30}You decide to leave the room and explore the city.{/cps}"
    jump clothescheck

label B1:
    "{cps=30}You put on the outfit, bright colors and tassles envelop you. You still leave a good amount of skin showing, naturally.{/cps}"

    $ Vclothes = True
    $ moneymod=2
    $ suspicionmod=4
    jump prologuemenu

label B2:
    "{cps=30}You put on some jeans, a jacket, a t-shirt, and tennis shoes. You also get your water bottle, just in case.{/cps}"

    $ Cclothes = True
    $ moneymod=-1
    $ suspicionmod=-5
    jump prologuemenu

label B3:
    "{cps=30}You put on sweatpants, a t-shirt, and flip flops. You massage the bags under your eyes lightly, and make a mental note to grab some coffee later.{/cps}"

    $ Mclothes = True
    $ moneymod=1
    $ suspicionmod=-2
    jump prologuemenu

label B4:
    "{cps=30}You put on an ornate mask you purchased for the carnival, along with a cloak. It feels nice, a bit itchy, but nice.{/cps}"

    $ Tclothes = True
    $ moneymod=3
    $ suspicionmod=7
    jump prologuemenu

label clothescheck:
    if Vclothes or Cclothes or Mclothes or Tclothes:
        "{cps=30}You walk outside in your outfit, ready to seize the day!{/cps}"
        "{cps=30}After locking your door behind you, walking down the stairs, and grabbing a quick coffee from the complimentary breakfast buffet, you finally step out of the hotel into the surrounding street.{/cps}"
        stop music fadeout 2.0
        play music "audio/Music_1.ogg" volume 0.3 fadein 2.0
        play sound "audio/AMB_Street_1.ogg" volume 0.8 fadein 1.0 
        #change bg street
        scene bg street
        with fade
        jump street
        
    else:
        "{cps=30}You walk outside, still fully nude after your shower…{/cps}"
        "{cps=30}Either you forgot to put on clothes due to morning lethargy, or you are just a very aggressive nudist.{/cps}"
        $ Achievement.add(achievement_name['nude'])
        "{cps=30}Either way, as you walk out of your hotel room with a whistle, you hear screams and gasps of the simultaniously surprised and offended locals.{/cps}"
        "{cps=30}One thing leads to another, and you eventually find yourself in the back of a police car, being driven off to the nearest station.{/cps}"
        "{cps=30}Whoops.{/cps}"
        scene black
        with fade
        $ Achievement.add(achievement_name['onestar'])
        "{cps=30}Bad Ending: Nudist{/cps}"
        return

label street:
    "{cps=30}The street is crowded, choked with people wearing costumes, eating food, and making conversation.{/cps}"
    "{cps=30}You try to get your bearings for long enough to make a choice on where you want to go, but the tight streets and waves of pedestrians eventually push you against your control.{/cps}"
    "{cps=30}You eventually stop trying to push against the people, letting them cart you away...{/cps}"
    jump plaza

############################# ACT 1
label plaza:
    stop sound fadeout 2.0
    play sound "audio/AMB_Street_1.ogg" volume 0.2 fadein 1.0
    define p=Character("Puck",color="#308CDD")
    #change bg plaza
    scene bg plaza
    with fade
    "{cps=30}You find yourself in a large plaza, with stands and attractions filling the usually empty space.{/cps}"
    "{cps=30}People seem to be less clumped together here, which allows you enough space to ambulate of your own voliton.{/cps}"
    "{cps=30}You see a small stage, an inviting looking shopkeeper's stand, and a sign pointing to the canals.{/cps}"
    "{cps=30}Where do you go?{/cps}"

label plazamenu:
    scene bg plaza
    menu:
       
        "I go to the small stage.":
            stop sound fadeout 1.0
            play sound "audio/AMB_Street_2.ogg" volume 0.5 fadein 2.0
            if not PuckMet: 
                jump C1first
            else:
                jump C1                
        "I go to the shopkeeper's stand.":
            stop music fadeout 2.0
            stop sound fadeout 1.0
            play sound "audio/moderncafe.mp3" volume 0.5 fadein 2.0
            if not PaleMet: 
                jump C2first
            else:
                jump C2
                
        "I go to the canals.":
            stop sound fadeout 1.0
            play sound "audio/AMB_Canal.ogg" volume 0.5 fadein 2.0
            if not PathMet: 
                jump C3first
            else:
                jump C3

        "I use an item.":
            "{cps=30}You reach into your bag...{/cps}"
            "{cps=30}What item do you use?{/cps}"
            menu:
                "Coffee.":
                    if not coffeeused: 
                        jump coffee
                    else:
                        "{cps=30}You already did that.{/cps}"
                        jump plazamenu
                "Art Supplies." if artsuppliesowned:
                    "{cps=30}You dont recognize these tools, perhaps a painter could use it better than you?{/cps}"
                    jump plazamenu
                "Peice of Paper." if paperowned:
                    "{cps=30}You pull out the peice of paper...{/cps}"
                "Cannoli." if cannoliowned:
                    "{cps=30}You pull out the Cannoli...{/cps}"
                    "{cps=30}Between this and the coffee, you are starting to question your odd storage habits.{/cps}"
                    "{cps=30}Regardless, you take a bite of your Cannoli.{/cps}"
                    "{cps=30}It's...{/cps}"
                    "{cps=30}Good!{/cps}"
                    $ Achievement.add(achievement_name['cannoli'])
                    "{cps=30}Really good.{/cps}"
                    jump plazamenu
                "Marionette." if marionetteowned:
                    "{cps=30}You pull out the marionette, but you don't really know how to use one.{/cps}"
                    "{cps=30}Maybe you can get someone to teach you?{/cps}"
                    jump plazamenu
                "Pendant." if pendantowned:
                    "{cps=30}You pull out the pendant...{/cps}"
                    "{cps=30}It doesnt seem to be doing anything.{/cps}"
                    "{cps=30}An inscription lies on the back of the pendant.{/cps}"
                    "{cps=30}It reads: 'Nel sonno, che tu possa trovare risposte. Nei sogni, che le domande dell'universo si risolvano da sole.'{/cps}"
                    jump plazamenu
                    
        "I beg for money.":
            jump C4

### Puck's Show

label C1first:
    #change bg Puck
    scene bg pucksshow
    with fade
    "{cps=30}You walk up to the small stage...{/cps}"
    "{cps=30}It seems empty, like the show hasn't started yet.{/cps}"
    "{cps=30}You prepare to leave before...{/cps}"
    p"{cps=30}{size=+10}Heeeellllloooo there!{/size}{/cps}"
    "{cps=30}You hear a voice.{/cps}"
    #enter Puck
    show puck
    p"{cps=30}Welcome, welcome, welcome! I am {color=#308CDD}Puck{/color}, performer, and adorer of anyone that will tolerate me.{/cps}"
    "{cps=30}The strange man bows in a dramatic flourish.{/cps}"
    "{cps=30}He seems incredibly obnoxious, but there is a sparkle of insight in his eyes.{/cps}"
    "{cps=30}He is more aware and sharp than he would like you to know.{/cps}"
    $ PuckMet=True
    p"{cps=30}How can I help you Signore and/or Signora?{/cps}"
    jump Dmenu

label C1:
    scene bg pucksshow
    with fade
    show puck
    p"{cps=30}How can I help you Signore and/or Signora?{/cps}"
    jump Dmenu


label Dmenu:
    menu:
        "Can you tell me about yourself?":
            jump D1
           
        "Can you tell me about the locals?":
            jump D2

        "When is the show?":
            jump D3

        "Can you teach me how to use this puppet?" if marionetteowned:
            jump circusend

        "I return to the plaza.":
            jump D4
            

label D1:
    p "{cps=30}Well friend, I have much to tell!{/cps}" 
    "{cps=30}You can see Puck's demeanor change, like that of an unwinding spring.{/cps}" 
    "{cps=30}He has wanted to talk to someone about his past for a very long time.{/cps}" 
    p "{cps=30}I started my life as a lowly butcher’s son, dreaming of the world outside my rural town in the Tuscan countryside.{/cps}" 
    p "{cps=30}I found my release in theatre and performance, but every night I was forced back into my humdrum home.{/cps}" 
    p "{cps=30}Thats why I hatched a plan… I tricked my father into leaving his keys on the table then used a distraction to draw him outside and buy me enough time to take his car and drive off on the open road!{/cps}" 
    p "{cps=30}Freedom was mine at last!{/cps}" 
    p "{cps=30}I found others on the road who shared my view on art and life, and we formed a quaint theater company together: ‘La compagnia dello specchio e della mente!’{/cps}" 
    p "{cps=30}‘The company of mirror and mind’!{/cps}" 
    "{cps=30}You see fire in his eyes, but behind that… something else…{/cps}" 
    "{cps=30}Sadness. His memories of his company are stained by some kind of old wound, some old mistake.{/cps}" 
    p"{cps=30}Yes, well. Nowadays, I find myself as more of a solo act than I used to be…{/cps}" 
    p"{cps=30}But nothing to feel sorrow over! All that matters is the future, eh amico?{/cps}" 
    jump Dmenu

label D2:
    p"{cps=30}The locals? Most people keep to themselves, but we are in venice, drama and love is never far.{/cps}"
    p"{cps=30}If you are digging for gossip, I have heard on the breeze that a poor gondolier by the name of Path has fallen in love with a fair lady named Poem.{/cps}"
    p"{cps=30}However, she is the daughter of Il Patriarca, who is known for excommunicating any boy who shows a glimmer of interest in his daughter.{/cps}"
    p"{cps=30}I hope those two lovebirds figure it out, but I have seen many a boy in Path’s position.{/cps}"
    p"{cps=30}It never ends well.{/cps}"
    jump Dmenu

label circusend:
    "{cps=30}You can see his body language change, he is astounded.{/cps}"
    p"{cps=30}Of course Amico!{/cps}"
    p"{cps=30}I'll run through the basics with you...{/cps}"
    with fade
    "{cps=30}And he does! He teaches you correct hand positioning, how to control the puppet, how to do a voice...{/cps}"
    p"{cps=30}Good job! You catch on quite well...{/cps}"
    "{cps=30}The performer thinks for a moment.{/cps}"
    p"{cps=30}Say, might you help me with today's show?{/cps}"
    menu:
        "Yes!":
            p"{cps=30}Grazie!{/cps}"
            p"{cps=30}Let me go through the script with you...{/cps}"
            scene black
            with Fade
            $ Achievement.add(achievement_name['finale'])
            "{cps=30}And so it was, you and Puck worked together and performed fantastically!{/cps}"
            "{cps=30}As a duo, you played off each other beautifully (despite your large differences in experience).{/cps}"
            "{cps=30}The rest of the day flew by, as you and Puck performed show after show...{/cps}"
            "{cps=30}Later that night, after he gave you your cut of the profits, you talk in his RV.{/cps}"
            "{cps=30}You both talk about life, about yours pasts, about your dreams, about love.{/cps}"
            "{cps=30}But eventually... your life outside calls.{/cps}"
            "{cps=30}And you return to your home country, despite the screaming of your heart.{/cps}"
            "{cps=30}All performances must end, you suppose.{/cps}"
            $ Achievement.add(achievement_name['circus'])
            "{cps=30}Ending Seven: Acting.{/cps}"
            return
        "No.":
            p"{cps=30}Oh... okay...{/cps}"
            "{cps=30}Puck looks particularly sad...{/cps}"
            "{cps=30}But this is not the first time this has happened to him.{/cps}"
            p"{cps=30}I understand, enjoy your vacation.{/cps}"
            scene black
            with fade
            $ Achievement.add(achievement_name['onestar'])
            "{cps=30}Bad Ending: Bummer.{/cps}"
            return

label D3:
    p"{cps=30}The show is going to be in four hours, please come back later!{/cps}"
    p"{cps=30}It is going to be a thrilling tale of love, triumphant over dark forces in the world!{/cps}"
    p"{cps=30}A five act puppet show, with one actor in eight roles!{/cps}"
    "{cps=30}Sounds like an absolute trainwreck…{/cps}"
    "{cps=30}You should see it as soon as possible.{/cps}"
    jump Dmenu

label D4:
    p"{cps=30}Goodbye, amico!{/cps}"
    p"{cps=30}Have fun, and make the most of Carnevale before Lent rears it’s ugly head.{/cps}"
    hide puck
    scene bg plaza
    with fade
    jump plazamenu
    
### Pale's Shop

label C2first:
    #change bg pale shop
    scene bg caravan
    with fade
    define pa=Character("Pale",color="#AB2BE4")
    $PaleMet=True  
    "{cps=30}You approach the caravan stall…{/cps}"
    "{cps=30}It seems nobody is here.{/cps}"
    "{cps=30}There is a small bell on the counter, which is silhouetted by a visually impenetrable red curtain.{/cps}"
    "{cps=30}You tentatively approach the bell and ring it.{/cps}"
    "{cps=30}As the sound echos out, you hear a rustling behind the curtain…{/cps}"
    "{cps=30}A strange man in a porcelain mask and purple robes leans outward from the red curtain.{/cps}"
    "{cps=30}He speaks in a calm and tired yet rushed and irritated tone.{/cps}"
    #Enter Pale
    show pale
    pa"{cps=30}Yo, what do ya want?{/cps}"
    jump palemenu

label C2:
    scene bg caravan
    with fade
    show pale
    p"{cps=30}Yo, what do ya want?{/cps}"
    jump palemenu

label palemenu:
    menu:
        "Can you tell me about yourself?":
            jump E1

        "Can you tell me about the locals?":
            jump E2

        "Can I have some money?":
            jump E3

        "Can I buy something?":
            jump shopmenu
           
        "I return to the plaza.":
            stop sound fadeout 2.0
            play music "audio/Music_1.ogg" volume 0.3 fadein 2.0
            jump E4

label E1:
    pa"{cps=30}My name is {color=#AB2BE4}Pale{/color}, I am a merchant.{/cps}"
    "{cps=30}The agressively vague description bugs you.{/cps}"
    "{cps=30}You decide to ask him to tell you more.{/cps}"
    pa"{cps=30}Not much more to tell, pal.{/cps}"
    pa"{cps=30}My name is Pale, and I am a merchant.{/cps}"
    pa"{cps=30}Besides, this is not about me…{/cps}"
    pa"{cps=30}This is about you.{/cps}"
    pa"{cps=30}And what you want to buy from me.{/cps}"
    pa"{cps=30}‘Hint, Hint’.{/cps}"
    jump palemenu

label E2:
    if achievement.has(achievement_name['finale'].name):
        pa"{cps=30}The locals?{/cps}"
        pa"{cps=30}Haven't you met most of them already?{/cps}"
        pa"{cps=30}Not much more I can tell you about them...{/cps}"
        pa"{cps=30}Well... there are some things...{/cps}"
        pa"{cps=30}But I don't give out secrets for free.{/cps}"
        jump SecretsMenu
    else:
        pa"{cps=30}The locals? Sure.{/cps}"
        pa"{cps=30}There are four locals you should care about:{/cps}"
        pa"{cps=30}Path, Poem, Puck, and Pray.{/cps}"
        pa"{cps=30}There, told you about the locals.{/cps}"
        pa"{cps=30}Anything else?{/cps}"
        jump palemenu

label SecretsMenu:
    menu:
        "Can you tell me Puck's secret for 75 money?":
            jump PuSec

        "Can you tell me Pray's secret for 80 money?":
            jump PrSec

        "Can you tell me Poem's secret for 90 money?":
            jump PoSec

        "Can you tell me Path's secret for 80 money?":
            jump PaSec

        "I'm not comfortable with this.":
            pa"{cps=30}I know.{/cps}"
            pa"{cps=30}But do you know what else I know about you?{/cps}"
            pa"{cps=30}I know that you care about seeing things, learning things, watching them.{/cps}"
            pa"{cps=30}And I am a very competent merchant, meaning I give people what they want.{/cps}"
            pa"{cps=30}My offer stands.{/cps}"
            jump palemenu

label PuSec:
    if money>75:
        $ money -= 75
        pa"{cps=30}Puck?{/cps}"
        pa"{cps=30}He is mellow and kind now, but he used to be very cruel to his friends.{/cps}"
        pa"{cps=30}When he left home, he buried himself in drugs and vice.{/cps}"
        pa"{cps=30}Trying, hoping that would wash away the guilt of destroying his family.{/cps}"
        pa"{cps=30}Once he founded his company, he started disrupting that family aswell.{/cps}"
        pa"{cps=30}I suppose it's not just the family you find, but the one you keep.{/cps}"
        jump SecretsMenu
    else:
        "{cps=30}You do not have enough money for that.{/cps}"

label PrSec:
    if money>80:
        $ money -= 80
        pa"{cps=30}Pray probably has the most secrets out of them all.{/cps}"
        pa"{cps=30}He used to be in love, deeply and truly.{/cps}"
        pa"{cps=30}But he was lied to, and hurt in ways I cannot quite describe.{/cps}"
        pa"{cps=30}Point being, he adopted a daughter afterwards and became a very devout man.{/cps}"
        pa"{cps=30}And in religion, he found something.{/cps}"
        pa"{cps=30}With his sheer dedication and fury, the papacy made an exception in his case-{/cps}"
        pa"{cps=30}Patriarchs and high-ranking members of the church are not allowed to have daughters, but he still got the station he has now.{/cps}"
        pa"{cps=30}And although I personally find him sour and irritating...{/cps}"
        pa"{cps=30}I cannot lie, I respect him for pulling himself out of the hole he was in.{/cps}"
        jump SecretsMenu
    else:
        "{cps=30}You do not have enough money for that.{/cps}"

label PoSec:
    if money>90:
        $ money -= 90
        pa"{cps=30}Poem is an intresting case.{/cps}"
        pa"{cps=30}She has seen beyond the stage, into the audience.{/cps}"
        pa"{cps=30}She has seen you.{/cps}"
        pa"{cps=30}She is... upset by this discovery{/cps}"
        pa"{cps=30}Understandable, I suppose.{/cps}"
        pa"{cps=30}I hope she doesn't do anything rash about it.{/cps}"
        "{cps=30}The man stifles a laugh.{/cps}"
        jump SecretsMenu
    else:
        "{cps=30}You do not have enough money for that.{/cps}"

label PaSec:
    if money>80:
        $ money -= 80
        pa"{cps=30}Ah, Path.{/cps}"
        pa"{cps=30}He... doesn't really have any secrets.{/cps}"
        pa"{cps=30}I guess he's kinda...{/cps}"
        pa"{cps=30}Shy?{/cps}"
        pa"{cps=30}Look, i'm trying my best but some people are just good and innocent I guess.{/cps}"
        pa"{cps=30}I don't even think he knows what sex is.{/cps}"
        pa"{cps=30}Like, physically.{/cps}"
        pa"{cps=30}It's wild.{/cps}"
        jump SecretsMenu
    else:
        "{cps=30}You do not have enough money for that.{/cps}"

label E3:
    if not choice_F1_made:
        "{cps=30}The strange man looks at you (or at least you presume he does) for a few seconds before responding.{/cps}"
        pa"{cps=30}Sure! If you wanna do some work for me, I'll give you money.{/cps}"
        jump Fmenu
    else: 
        "{cps=30}You can't do that again.{/cps}"
        jump palemenu

label shopmenu:
    pa"{cps=30}Sure. Whaddaya buyin?{/cps}"
    menu:
        "{cps=30}You currently have [money] Money. What do you buy?{/cps}"
        "Art Supplies: 80 Money" if achievement.has(achievement_name['sad'].name):
            if money>80:
                $ money -= 80
                "{cps=30}The man snickers as he hands you the art supplies.{/cps}"
                $ artsuppliesowned=True
                jump shopmenu
            else:
                "{cps=30}You do not have enough money for that.{/cps}"
                jump shopmenu

        "Peice of Paper: 3 Money":
            if money>3:
                $ money -= 3
                "{cps=30}The man hands you a single peice of paper and a pencil.{/cps}"
                $ paperowned=True
                jump shopmenu
            else:
                "{cps=30}You do not have enough money for that.{/cps}"
                jump shopmenu
            
        "Cannoli: 15 Money":
            if money>15:
                $ money -= 15
                "{cps=30}The man puts a cannoli in your hands.{/cps}"
                $ cannoliowned=True
                jump shopmenu
            else:
                "{cps=30}You do not have enough money for that.{/cps}"
                jump shopmenu

        "Marionette: 75 Money" if achievement.has(achievement_name['happy'].name):
            if money>75:
                $ money -= 75
                "{cps=30}The man gives you a Marionette.{/cps}"
                "{cps=30}It looks a bit like you.{/cps}"
                $ marionetteowned=True
                jump shopmenu
            else:
                "{cps=30}You do not have enough money for that.{/cps}"
                jump shopmenu
            
        "Chase Sequence Fund: 15,000,000,000 Money" if achievement.has(achievement_name['afraid'].name):
            if money>15000000000:
                $ money -= 15000000000
                pa"{cps=30}Thanks! We will get started on planning out the fully playable chase sequence.{/cps}"
                pa"{cps=30}Should take around eight months.{/cps}"
                $ Achievement.add(achievement_name['chase'])
                jump shopmenu                
            else:
                "{cps=30}You do not have enough money for that.{/cps}"
                jump shopmenu

        "Strange Pendant: 75 Money" if achievement.has(achievement_name['collapsed'].name):
            if money>75:
                $ money -= 75
                "{cps=30}The man hands you the pendant.{/cps}"
                "{cps=30}It catches the light in an odd way...{/cps}"
                $ pendantowned=True
                jump shopmenu
            else:
                "{cps=30}You do not have enough money for that.{/cps}"
                jump shopmenu

        "Stop Shopping":
            pa"{cps=30}See ya.{/cps}"
            jump palemenu

label Fmenu:
    menu:
        "Okay, nothing else to do.":
            jump F1
        "Uh sorry, I meant free money.":
            jump F2

label F1:
    pa"{cps=30}Cool! Hold this sign and yell at people so they buy stuff from me.{/cps}"
    "{cps=30}The strange man reaches behind the counter, hands you a small sign that just reads: ‘Pale’s Store, We Sell Things. No Refunds’.{/cps}"
    "{cps=30}You then do just that, waving the sign around and yelling at people…{/cps}"
    with fade
    #Fade background, black 3 se
    pa"{cps=30}Good job, I almost got a customer.{/cps}"
    pa"{cps=30}Here, have 165 money. You’ve kinda earned it.{/cps}"
    "{cps=30}Pale then hands you the aforementioned 165 money for three hours of work.{/cps}"
    $ Achievement.add(achievement_name['legal'])
    "{cps=30}Certainly not the worst job in the world.{/cps}"
    $ money += 165
    $ choice_F1_made=True
    jump palemenu

label F2:
    pa"{cps=30}Oh, cool.{/cps}"
    pa"{cps=30}Not gonna do that though, sorry.{/cps}"
    pa"{cps=30}Offer stands if you wanna accept it later.{/cps}"
    jump palemenu

label E4:
    pa"{cps=30}Enjoy the carnival, ciao.{/cps}"
    #fade bg = pale shop into plaza
    scene bg plaza
    with fade
    jump plazamenu

### Path's Canals
label C3first:
    define pat=Character("Path",color="#DAC432")
    #change bg Canals
    scene bg canal
    with fade
    "{cps=30}You walk into the canals.{/cps}"
    "{cps=30}As you walk around a corner, you hear a kind of melodic humming.{/cps}"
    "{cps=30}It is strangely sincere, and you feel a sense of longing sadness with an undercurrent of joy.{/cps}"
    "{cps=30}You round the corner, and…{/cps}"

    #Enter Path
    show path
    pat"{cps=30}{size=+10}Oh!{/size}{/cps}"
    "{cps=30}You see a nervous gondalier, whose daydreams have been interrupted by your presence.{/cps}"
    "{cps=30}He seems kind, with a deep shyness in his demeanor.{/cps}"
    pat"{cps=30}Uh… bonjourno!{/cps}"
    pat"{cps=30}My name is {color=#DAC432}Path{/color}, I'm a gondolier.{/cps}"
    $ PathMet=True
    pat"{cps=30}How can I help you, signore/signora?{/cps}"
    jump Gmenu

label C3:
    scene bg canal
    with fade
    show path
    pat"{cps=30}How can I help you, signore/signora?{/cps}"
    jump Gmenu

label Gmenu:
    menu:
        "Can you tell me about yourself?":
            jump G1
           
        "Can you tell me about the locals?":
            jump G2

        "Can I go on a gondola ride?":
            jump G3
           
        "I return to the plaza.":
            jump G4

label G1:
    "{cps=30}The man shifts around uncomfortably.{/cps}"
    pat"{cps=30}Well, I’m twenty two, for starters.{/cps}"
    pat"{cps=30}Haha…{/cps}"
    pat"{cps=30}Um, I got this job from my father.{/cps}"
    pat"{cps=30}He and my mother are… {size=-5}gone{/size}.{/cps}"
    pat"{cps=30}But you know, doing this reminds me of times I spent as a kid!{/cps}"
    pat"{cps=30}My mother and father on the gondola with me, slowly moving through the canals… {/cps}"
    "{cps=30}Path looks out at the water for a moment, both floral and sewage-scented, before meeting your gaze once more.{/cps}"
    pat"{cps=30}It’s a magical memory.{/cps}"
    pat"{cps=30}I’m so lucky… to be here...{/cps}"
    pat"{cps=30}To be alive.{/cps}"
    jump Gmenu

label G2:
    pat"{cps=30}The locals?{/cps}"
    pat"{cps=30}Theres a lot of wonderful people around here!{/cps}"
    pat"{cps=30}Especially Po-{/cps}"
    "{cps=30}He ‘catches’ himself and starts blushing.{/cps}"
    pat"{cps=30}E-especially Poem.{/cps}"
    pat"{cps=30}She is the daughter of the Patriarch of Venice, and the fairest lady in the city.{/cps}"
    pat"{cps=30}I’ve been trying to write her a letter ever since that night she took my gondola, but I haven't quite found the words…{/cps}"
    pat"{cps=30}I’m close though! That Pale guy sold me a nice pen, and ever since i’ve been writing the letter much more easily.{/cps}"
    jump Gmenu

label G3:
    pat"{cps=30}Sure! Its a flat rate of 65 money right now, while the carnival is in town.{/cps}"
    pat"{cps=30}Do you wanna go?{/cps}"
    jump Hmenu

label Hmenu:
    menu:
        "Yes, I pay 65 Money.":
            if money>65:
                $ money -= 65
                jump H1
            else:
                "{cps=30}You don't have enough money.{/cps}"
                jump Hmenu
        "No, maybe later.":
            jump H2

label H1:
    "{cps=30}You hand Path 65 money.{/cps}"
    pat"{cps=30}Thanks, let's get going!{/cps}"
    "{cps=30}You hop onto the gondola and give him your destination: a church that you have wanted to see as part of your vacation.{/cps}"
    "{cps=30}He starts taking you both through the canals…{/cps}"
    jump Act2

label H2:
    pat"{cps=30}Okay! Maybe another time.{/cps}"
    jump Gmenu

label G4:
    pat"{cps=30}Okay, talk to you later!{/cps}"
    stop sound fadeout 2.0
    jump plazamenu


###PlazaItems
label coffee:
    "{cps=30}You drink the complementary coffee...{/cps}"
    "{cps=30}You feel 30 percent more awake!{/cps}"
    "{cps=30}But you know, deep in your heart...{/cps}"
    "{cps=30}That this low-quality coffee's aftertaste is going to be in your mouth for an hour.{/cps}"
    $ coffeeused=True
    jump plazamenu

###Begging
label C4:
    "{cps=30}You start begging for money…{/cps}"
    $ arrestresult=renpy.random.randint(1,100) + suspicionmod + suspicion
    if arrestresult>95:
        "{cps=30}As you hold out your palms for money, you feel a hand on your shoulder.{/cps}"
        "{cps=30}You turn around and see two police officers standing behind you.{/cps}"
        "{cps=30}'Singore/Signora, you are aware that begging is banned in Venice?'{/cps}"
        "{cps=30}'We are going to request your passport and papers, please.'{/cps}"
        "{cps=30}What do you do?{/cps}"
        menu:
            "I distract the police officers with a cool dance and song, cuban pete style.":
                jump ArrestSong

            "I throw a brick at one of them.":
                jump AssaultOfficer

            "I do exactly what they say.":
                jump BootLicker

            "I make out with them.":
                jump BootKisser
    else:
        $ suspicion+=2
        $ beggingresult=renpy.random.randint(1, 10) + moneymod
        $ money+=beggingresult
        "{cps=30}You got [beggingresult] money!{/cps}"
        "{cps=30}You currently have [money] money.{/cps}"
        $ beggingresult=0
        jump plazamenu

label ArrestSong:
    "{cps=30}You start dancing, to everyone's dismay.{/cps}"
    "{cps=30}'W... what are you doing?'{/cps}"
    "{cps=30}You yell out 'This, baby!'{/cps}"
    "{cps=30}You start singing after hitting a cool pose.{/cps}"
    "{cps=30}'I'm just a lil guy, and I kinda wonder why, everyone wants to limit me, wants me to die!'{/cps}"
    "{cps=30}'I'm just a ity dude, and I gotta lotta tude, so don't try to stop me, stop being rude!'{/cps}"
    "{cps=30}'Just… dance… to… this… song! It's not wrong, sing along!'{/cps}"
    "{cps=30}'Nod your head, clap your hands, take a stance, take a chance!'{/cps}"
    "{cps=30}You look back over at the police officers, who are both doing a conga line with literally every single person in the plaza.{/cps}"
    "{cps=30}You join them, and the rest of the day is a blur.{/cps}"
    scene black
    with fade
    "{cps=30}Meanwhile, on an international news station's programming:{/cps}"
    "{cps=30}'Breaking news!'{/cps}" 
    "{cps=30}'Every single person in Venice and surrounding territories have entered a trance-like state and have started forming strange, seemingly choreographed dance routines.'{/cps}"
    "{cps=30}'It appears these people have been dancing for three hours straight, and this condition seems to effect anyone who hears a song radiating through the cities plaza and emergency broadcast system.'{/cps}"
    "{cps=30}'More on this incident after the break...'{/cps}"
    $ Achievement.add(achievement_name['onestar'])
    "{cps=30}Bad Ending: Partied too hard.{/cps}"
    return
        
label AssaultOfficer:
    "{cps=30}You bend down, grab an {color=#f00}EXCEEDINGLY CONVENIENT{/color} brick off the ground and throw it at one of the police officers.{/cps}"
    "{cps=30}'Arggh!'{/cps}"
    $ Achievement.add(achievement_name['attack'])
    "{cps=30}'Oh now you've done it!'{/cps}"
    "{cps=30}You knock one of the officers unconcious, but the other one is rushing towards you.{/cps}"
    "{cps=30}How do you react?{/cps}"
    menu:  
        "Dodge":
            "{cps=30}You dodge to the right...{/cps}"
            "{cps=30}But he predicts your plan and sweeps your legs!{/cps}"
            "{cps=30}Everything goes dark...{/cps}"
            scene black
            with fade
            $ Achievement.add(achievement_name['onestar'])
            "{cps=30}Bad Ending: Violence is not the answer.{/cps}"
            return
        "Punch":
            "{cps=30}As the officer runs towards you, you punch him in the face...{/cps}"
            "{cps=30}He falls down in an instant, and you make a break for it!{/cps}"
            scene black
            with fade
            stop music fadeout 2.0
            play music "audio/Music_2.ogg" volume 0.3 fadein 2.0
            $ Achievement.add(achievement_name['finale'])
            "{cps=30}And so it was, you sprinted out of the city and onto the fastest airplane back home.{/cps}"
            "{cps=30}Part of you is sad that you missed out on a large chunk of your vacation, but most of you is glad that you are not in prison for assaulting two officers.{/cps}"
            $ Achievement.add(achievement_name['violent'])
            "{cps=30}Ending Six: Violence is the answer.{/cps}"
            return

label BootLicker:
    "{cps=30}You look down sadly and hold forward your hands to be cuffed.{/cps}" 
    "{cps=30}The officers both nod at each other and bring you over to their car.{/cps}"
    scene black
    with fade
    $ Achievement.add(achievement_name['onestar'])
    "{cps=30}Bad Ending: Boot Licker.{/cps}"
    return

label BootKisser:
    "{cps=30}You decide to utilize your feminine and/or masculine wiles on the officers.{/cps}"
    $ smoochresult=renpy.random.randint(1,4)
    "{cps=30}You swoop your hair, wink, and do a sexy pose.{/cps}"
    "{cps=30}You lean forward to kiss one of them...{/cps}"
    if smoochresult>3:
        "{cps=30}The officer kisses you back, and holds you in his arms.{/cps}"
        "{cps=30}When your lips seperate, he moves a strand of your hair away from your eyes.{/cps}"
        "{cps=30}'You are the most gorgeous person I have ever met'.{/cps}"
        "{cps=30}The other officer looks at him, confused and upset.{/cps}"
        "{cps=30}'Mario! What are you doing?'{/cps}"
        "{cps=30}'You have a wife and child!'{/cps}"
        "{cps=30}The officer who just kissed you looks back at his comrade.{/cps}"
        "{cps=30}'That Mario is dead, I have been reborn in the kiss of this angel.'{/cps}"
        "{cps=30}'Mario, what the fuck is wrong with you?'{/cps}"
        "{cps=30}'You know what, fine.'{/cps}"
        "{cps=30}'I'm leaving.'{/cps}"
        "{cps=30}The officer leaves as Mario holds your body delicately.{/cps}"
        "{cps=30}'You want to have some breakfast in bed?'{/cps}"
        scene black 
        with fade
        stop music fadeout 2.0
        play music "audio/Music_2.ogg" volume 0.3 fadein 2.0
        $ Achievement.add(achievement_name['finale'])
        "{cps=30}And so it was, you boned that police officer.{/cps}"
        "{cps=30}Good job, I guess?{/cps}"
        $ Achievement.add(achievement_name['casa'])
        "{cps=30}Ending Five: Casanova.{/cps}"
        return 
    else:
        "{cps=30}'What are you doing?'{/cps}"
        "{cps=30}You whisper in his ear: 'Trying to kiss you.'{/cps}"
        "{cps=30}'I'm in a devoted relationship with my lovely wife and while I am flattered this does not change the fact we need to take you down do the station.'{/cps}"
        "{cps=30}Well, damn it.{/cps}"
        scene black
        with fade
        $ Achievement.add(achievement_name['onestar'])
        "{cps=30}Bad Ending: Rejected.{/cps}"
        return
        
    
####################### ACT 2
label Act2:
    #change bg outsideChurch fade in
    scene bg churchoutside
    with fade
    show path
    stop sound fadeout 1.0
    play sound "audio/AMB_Church_Inside_Crowded.ogg" volume 0.5 fadein 2.0
    "{cps=30}You pull into a small dock outside the church and Path ties the gondolier to a long wooden pole.{/cps}"
    "{cps=30}He seems uncomfortable around here, afraid of something…{/cps}"
    "{cps=30}Or someone.{/cps}"
    "{cps=30}He looks at you for a second, and an idea flashes through his eyes.{/cps}"
    pat"{cps=30}Hey, friend, could you do me a tiny favor?{/cps}"
    "{cps=30}Normally, you would consider whether or not to accept, but his sincerity wins you over and you blurt out a “sure, what is it?”{/cps}"
    pat"{cps=30}Can you deliver this letter to Poem?{/cps}"
    pat"{cps=30}If you are going to the church anyway I mean, she usually stays around there with her dad.{/cps}"
    pat"{cps=30}If you could just deliver this letter to her without letting her dad know, I’d be so grateful!{/cps}"
    pat"{cps=30}I’ll stop holding you up now, enjoy the church!{/cps}"
    hide path
    "{cps=30}This part of this city is much less crowded than the plaza, but there are still pedestrians walking from to and fro.{/cps}"
    "{cps=30}You see the entrance to the church, a small park next to it with many benches, and the path to the canals where you came from.{/cps}"
    "{cps=30}Where do you go?{/cps}"
    jump churchmenu

label churchmenu:
    menu:
        "I go into the church":
            "{cps=30}You walk into the church…{/cps}"
            #change bg church , fade in
            scene bg churchinside
            with fade
            stop music fadeout 2.0
            stop sound fadeout 2.0
            play sound "audio/FugueChurchOrgan.ogg" volume 0.5 fadein 2.0
            if not PrayMet:
                jump I1first
            else:
                jump I1
        "I go to the small park":
            "{cps=30}You walk over to the benches.{/cps}"
            if not PoemMet:
                jump I2first
            else:
                jump I2
        "I jump into the canal water":
            "{cps=30}You jump into the can-{/cps}"
            "{cps=30}Wait what?{/cps}"
            "{cps=30}Why?{/cps}"
            menu:
                "its funny":
                    "{cps=30}It really isn't.{/cps}"
                    "{cps=30}So... you jump into the canal water. I guess.{/cps}"
                    "{cps=30}Its really cold and gross and uncomfortable now{/cps}"
                    "{cps=30}You start to drown...{/cps}"
                    scene black
                    with fade
                    $ Achievement.add(achievement_name['onestar'])
                    "{cps=30}Bad Ending: Sewage Lover.{/cps}"
                    return

label I1first:
    "{cps=30}An ornate, astounding church meets you. {/cps}"
    "{cps=30}You assume most people that usually worship here are out on the town, celebrating.{/cps}"
    "{cps=30}But that doesn’t mean the church is empty, you see a group of people wearing crosses talking in a corner.{/cps}"
    "{cps=30}At your look at them, one of the men whip their head around towards you.{/cps}"
    "{cps=30}He is wearing a red mask with no other affects of holiday celebration.{/cps}"
    "{cps=30}He walks up to you, with mild confusion.{/cps}"
    #Enter Pray center
    show pray
    define pr=Character("Pray",color="#962121")
    pr"{cps=30}Hello, my child.{/cps}"
    pr"{cps=30}I am {color=#962121}Pray{/color}, are you lost?{/cps}"
    pr"{cps=30}The church is not open right now, why are you here?{/cps}"
    pr"{cps=30}Do you need anything?{/cps}"
    jump Jmenu

label I1:
    show pray
    pr"{cps=30}Do you need anything?{/cps}"
    jump Jmenu

label Jmenu:
    menu:
        "Can you tell me about yourself?":
            jump J1
           
        "Can you tell me about the locals?":
            jump J2

        "Give him Path's letter.":
            jump J3
           
        "Leave the church.":
            jump J4


label J1:
    "{cps=30}You see a expression of pride start to form on his mouth.{/cps}"
    pr"{cps=30}I am the current patriarch of venice, leader of the churches here and one of the four patriarchs of the latin catholic chuch. {/cps}"
    pr"{cps=30}I am not in my full ceremonial robes right now, but I am tasked with a very high station.{/cps}"
    pr"{cps=30}Without forces like ours, venice would devolve morally.{/cps}"
    pr"{cps=30}That is why our jobs as representatives and administrators of the church matter so much…{/cps}"
    pr"{cps=30}We are the front line against…{/cps}"
    "{cps=30}As Pray continues talking, you start to zone out.{/cps}"
    "{cps=30}You think that you remember reading something about this somewhere…{/cps}"
    "{cps=30}You think that you remember something about an upcoming vote among the papacy, meaning that its possible Pray will lose his station soon.{/cps}"
    "{cps=30}You mention that to him, asking for more info.{/cps}"
    "{cps=30}He immediately stops talking.{/cps}"
    pr"{cps=30}Well… yes.{/cps}"
    pr"{cps=30}I have needed to… bend certain rules so that I could protect my daughter.{/cps}"
    pr"{cps=30}My collegues in the papacy believe that I have placed personal values over the goals of the church…{/cps}"
    pr"{cps=30}But I argue that expelling any filth from this city directly is aligned with our lord’s will.{/cps}"
    jump Jmenu

label J2:
    pr"{cps=30}The locals? {/cps}"
    pr"{cps=30}I suppose they are out currently, gallivanting throughout the streets in costume.{/cps}"
    pr"{cps=30}Personally, I dislike this holiday.{/cps}"
    pr"{cps=30}I find it to be the wrong way to look at lent, seeing it as a sacrifice that must be endured rather than a choice to limit oneself.{/cps}"
    pr"{cps=30}Then again, human nature cannot truly be argued with I suppose.{/cps}"
    pr"{cps=30}{i}È così.{/i}{/cps}"
    jump Jmenu

label J3:
    "{cps=30}You hand him the letter and he takes it curiously.{/cps}"
    "{cps=30}He reads it to himself, growing redder by each line.{/cps}"
    "{cps=30}When he gets to the end, and sees that is addressed to his daughter, he scowls.{/cps}"
    pr"{cps=30}{size=+5}Who!{/size}{/cps}"
    pr"{cps=30}Who wrote this… sappy, deceptive piece of paper!{/cps}"
    "{cps=30}You ask him in what way it is deceptive.{/cps}"
    pr"{cps=30}All love letters are deceptive, no matter how beautifully worded.{/cps}"
    pr"{cps=30}You think young men write these out of true love?{/cps}"
    pr"{cps=30}A common misconception.{/cps}"
    pr"{cps=30}They write these to trick young women into dating them, at which point they mistreat, harm, and use her.{/cps}"
    pr"{cps=30}Young men are only concerned with feeding their own desires…{/cps}"
    "{cps=30}There is venom in his voice, but not the venom of guilt for past actions...{/cps}"
    "{cps=30}It is a hatred stemming from being hurt in the past, his fear for his daughter’s safety feels like it stems from an old violation of his safety.{/cps}"
    pr"{cps=30}Thank you for bringing this to me.{/cps}"
    pr"{cps=30}Who wrote this?{/cps}"
    jump Kmenu

label Kmenu:
    if persistent.restarts>=3:
        menu:
            "Path wrote it":
                jump K1
            "Puck wrote it":
                jump K2
            "I wrote it":
                jump K3
    else:
        menu:
            "Path wrote it":
                jump K1
            "Puck wrote it":
                jump K2

label K1:
    pr"{cps=30}The gondolier?{/cps}"
    pr"{cps=30}I should have known… {/cps}"
    pr"{cps=30}That boy is in serious trouble!{/cps}"
    "{cps=30}Pray storms out, the two people he was talking to look at each other in concern.{/cps}"
    "{cps=30}You realize that they look like a couple who were talking to Pray about wedding plans, and now that he has stormed out they are talking to themselves about rescheduling.{/cps}"
    "{cps=30}You follow Pray outside.{/cps}"
    jump End1

label K2:
    pr"{cps=30}The performer?{/cps}"
    pr"{cps=30}Thats… unexpected.{/cps}"
    pr"{cps=30}I suppose stranger things have happened.{/cps}"
    "{cps=30}Pray storms out, the two people he was talking to look at each other in concern.{/cps}"
    "{cps=30}You realize that they look like two preists who were talking to him about lent plans, and now that he has stormed out they both roll their eyes and look at eachother.{/cps}"
    "{cps=30}You follow Pray outside.{/cps}"
    jump End2

label K3:
    "{cps=15}BROKEN, SLIP UP, OFF SCRIPT{/cps}"
    #glitch effect for 5 seconds
    #change character pray disappears without fade
    hide pray
    with Pixellate (3,5)
    stop music
    #bg black fade
    scene black
    with fade
    jump EndS

label J4:
    pr"{cps=30}Understood, know that you are always welcome here, child.{/cps}"
    scene bg churchoutside
    stop music fadeout 2.0
    play sound "audio/AMB_Church_Inside_Crowded.ogg" volume 0.5 fadein 2.0
    play music "audio/Music_1.ogg" volume 0.3 fadein 2.0
    jump churchmenu

label I2first:
    define po=Character("Poem",color="#F4D0E5")
    "{cps=30}You can see some people sitting here, either waiting for something/someone or just resting their legs.{/cps}"
    "{cps=30}Your eyes eventually move towards a gorgeous woman with a pink parasol.{/cps}"
    #Enter Poem fade center
    show poem
    "{cps=30}She seems… sad.{/cps}"
    "{cps=30}It is a sadness that feels deeply rooted in her heart, like an old tree that sustains itself on eating her joy.{/cps}"
    "{cps=30}It is the sadness of a realization, or a horrible thought.{/cps}"
    "{cps=30}She turns to meet your gaze, and her expression changes to that of suprise.{/cps}"
    "{cps=30}She mouths something under her breath, and then quickly smiles that ‘nice’ sort of smile you offer a stranger or acquaintance.{/cps}"
    $ PoemMet=True
    po"{cps=30}Hello there.{/cps}"
    po"{cps=30}How are you faring today?{/cps}"
    jump Lmenu

label I2:
    jump PoemStartBookmark

label Lmenu:
    menu:
        "Good":
            jump L1
        "Bad":
            jump L2

label L1:
    po"{cps=30}Good! I’m glad.{/cps}"
    jump PoemStartBookmark

label L2:
    "{cps=30}She doesn’t expect that response, that is not how people are ‘supposed’ to respond to that question.{/cps}"
    po"{cps=30}Oh…{/cps}"
    po"{cps=30}Well, i’m sorry to hear that.{/cps}"
    po"{cps=30}I…{/cps}"
    "{cps=30}Her smile disintegrates like a burning piece of wood, slowly and weakly.{/cps}"
    po"{cps=30}I’m not feeling great either, to be honest.{/cps}"
    po"{cps=30}I feel… like something is missing.{/cps}"
    po"{cps=30}Like someone is missing.{/cps}"
    po"{cps=30}I am without a love, without a person to talk to.{/cps}"
    po"{cps=30}I feel dreadfully alone, incomplete.{/cps}"
    po"{cps=30}I wish I knew someone who understood…{/cps}"
    "{cps=30}She gets lost in thought for a moment, before snapping back.{/cps}"
    po"{cps=30}Sorry about that!{/cps}"
    jump PoemStartBookmark

label PoemStartBookmark:
    show poem
    po"{cps=30}Is there something you would like to talk to me about?{/cps}"
    jump Mmenu

label Mmenu:
    menu:
        "Can you tell me about yourself?":
            jump M1
   
        "Can you tell me about the locals?":
            jump M2

        "Give her the letter.":
            jump M3

        "Give her the Art Supplies" if artsuppliesowned:
            jump artend
           
        "Leave.":
            jump M4

label M1:
    po"{cps=30}My name is {color=#F4D0E5}Poem{/color}, I'm Pray’s daughter.{/cps}"
    po"{cps=30}I am a professor of art, mostly painting with an impressionistic pointalism style.{/cps}"
    po"{cps=30}I am struggling a bit in the inspiration front right now, as no subject or ideas are availing themselves to me.{/cps}"
    po"{cps=30}In time, I suppose.{/cps}"
    po"{cps=30}Ironic isn’t it? {/cps}"
    po"{cps=30}Being in one of the most beautiful cities in the world, during its most colorful celebration, and being at a loss for ideas?{/cps}"
    "{cps=30}At this, she chuckles without humor.{/cps}"
    jump Mmenu

label M2:
    po"{cps=30}I, honestly, don’t know many of the locals. {/cps}"
    po"{cps=30}I’ve been staying with my father in this part of venice during the carnival, but my apartment is in Dorsoduro.{/cps}"
    po"{cps=30}I haven’t really taken the time to meet anyone, but then again, not many people have been taking the time to meet me.{/cps}"
    po"{cps=30}Thanks, by the way.{/cps}"
    po"{cps=30}For spending some time listening to what I have to say.{/cps}"
    po"{cps=30}It's nice.{/cps}"
    jump Mmenu

label M3:
    "{cps=30}You hand her the letter, and she takes it curiously.{/cps}"
    "{cps=30}She opens it up, and then begins to read it.{/cps}"
    "{cps=30}Slowly, tears start to form in her eyes as she continues to read.{/cps}"
    "{cps=30}She finishes the letter, wipes her eyes, and puts it down on the bench beside her.{/cps}"
    po"{cps=30}That was one of the most beautiful things I have ever read.{/cps}"
    po"{cps=30}You are an amazing writer!{/cps}"
    "{cps=30}She immediately sweeps you into a giant hug, and around the same time you feel your back crack from her embrace you realize that she is much stronger than you.{/cps}"
    "{cps=30}Dangerously stronger than you.{/cps}"
    "{cps=30}Okay its really starting to hurt now, better say something quick.{/cps}"
    "{cps=30}You let out an “Ow. Ow. Ow” before she lets go of you, tears streaming down her face like paper-thin waterfalls.{/cps}"
    "{cps=30}She smiles, grabs your hand, and runs over to the canal docks.{/cps}"
    "{cps=30}The shock prevents you from fighting against the force exerted on your arm, as she drags you over to the nearby docks.{/cps}"
    po"{cps=30}You there!{/cps}"
    po"{cps=30}Sir, we would like to book a gondola ride!{/cps}"
    show poem at right
    "{cps=30}She is pointing at Path, who alights with joy apon seeing her.{/cps}"
    # poem goes to right side screen path fades in left
    show path at left
    pat"{cps=30}Oh… o-of course!{/cps}"
    pat"{cps=30}You read the letter?{/cps}"
    po"{cps=30}Yes, it was written beautifully!{/cps}"
    po"{cps=30}You two must have talked about it beforehand, are you guys friends?{/cps}"
    pat"{cps=30}I mean, we just met today, but they are a fantastic person.{/cps}"
    "{cps=30}Path turns over to you.{/cps}"
    pat"{cps=30}I really cannot thank you enough for doing this, I would have been terrified!{/cps}"
    po"{cps=30}Regardless, lets go over to the plaza!{/cps}"
    po"{cps=30}I hear a show is starting soon, and they have some good food around there.{/cps}"
    pat"{cps=30}Uh… all of us?{/cps}"
    po"{cps=30}Of course! How else would we get there?{/cps}"
    pat"{cps=30}Yeah, okay.{/cps}"
    pat"{cps=30}I guess that makes… sense?{/cps}"
    "{cps=30}Path starts to paddle over to the plaza through the canals.{/cps}"
    jump End3

label artend:
    "{cps=30}You hand her the art supplies.{/cps}"
    po"{cps=30}Oh! Thank you.{/cps}"
    po"{cps=30}Would you like to paint with me?{/cps}"
    menu:
        "Yes":
            "{cps=30}She smiles and opens up her bag, pulling out a foldable easel.{/cps}"
            "{cps=30}Over the next few hours, poem and you both set up two small work stations and start painting.{/cps}"
            "{cps=30}What do you paint?{/cps}"
            menu:
                "Something scary":
                    "{cps=30}You paint something scary...{/cps}"
                    "{cps=30}You go a bit too far though, and scare yourself so badly that you have a heart attack!{/cps}"
                    "{cps=30}Whoops.{/cps}"
                    scene black
                    with fade
                    $ Achievement.add(achievement_name['onestar'])
                    "{cps=30}Bad Ending: Master of Fright{/cps}"
                    return
                "Something cute":
                    "{cps=30}You paint something cute...{/cps}"
                    "{cps=30}It's a dog and a kitten cuddling.{/cps}"
                    po"{cps=30}Oh my! What a cute painting!{/cps}"
                    po"{cps=30}I love dogs!{/cps}"
                    po"{cps=30}Can I show you my painting{/cps}"
                    stop music fadeout 2.0
                    stop sound fadeout 2.0
                    "let me out let me out let me out let me out let me out let me out let me out let me out let me out let me out"
                    po"{cps=30}Do you get the meaning? What I am trying to say with this?{/cps}" 
                    po"{cps=30}I need you to understand this painting, and I would like it if you could talk to me more about it 'tommorow'.{/cps}"
                    po"{cps=30}Lets just hope that they{/cps}" 
                    scene black 
                    with pixellate
                    return
                "your mom":
                    "{cps=30}You paint a portrait of poem's mom...{/cps}"
                    po"{cps=30}Wow, great job! Who is she?{/cps}"
                    "{cps=30}You explain that she is Poem's mom.{/cps}"
                    po"{cps=30}Uh... I dont really know what my mom looks like, so I guess that could be her.{/cps}"
                    po"{cps=30}But given that your painting is literally just a stick figure with boobs, I also doubt you really know what my mom looks like.{/cps}"
                    scene black
                    with fade
                    $ Achievement.add(achievement_name['onestar'])
                    "{cps=30}Bad Ending: Abstract Artist{/cps}"
                    return
                "Something romantic":
                    "{cps=30}You paint something romantic...{/cps}"
                    "{cps=30}Your painting depicts Poem on the gondola with Path.{/cps}"
                    po"{cps=30}Is that me? Thanks!{/cps}"
                    po"{cps=30}I like it!{/cps}"
                    po"{cps=30}Who is that?{/cps}"
                    "{cps=30}She points at Path in the painting.{/cps}"
                    "{cps=30}You hand her the letter.{/cps}"
                    "{cps=30}She takes it, reads it, and starts welling up with tears.{/cps}"
                    po"{cps=30}This is...{/cps}"
                    "{cps=30}She looks to her left, as if hearing something far away.{/cps}"
                    po"{cps=30}I don't want to do this again. Please.{/cps}"
                    scene black 
                    with pixellate
                    return

        "No":
            "{cps=30}She sighs.{/cps}"
            po"{cps=30}Okay. Maybe another time?{/cps}"
            jump Mmenu

label M4:
    pat"{cps=30}Okay, addio!{/cps}"
    hide poem
    jump churchmenu


################## ACT 3

label End1:
    #Path suitor ending
    #change bg outside church
    scene bg churchoutside
    with fade
    stop music fadeout 2.0
    play music "audio/Music_1.ogg" volume 0.3 fadein 2.0
    stop sound fadeout 2.0
    play sound "audio/AMB_Church_Inside_Crowded.ogg" fadein 2.0 volume 0.5
    "{cps=30}Pray rushes outside in a power walk of vindictive and fatherly rage.{/cps}"
    "{cps=30}You follow, both out of curiosity and guilt for your breach of Path’s trust.{/cps}"
    "{cps=30}Once you both reach the canal docks, you see Path merrily cleaning any splashed water that got in his boat while whistling.{/cps}"
    #Path fade in right
    show path at right
    "{cps=30}As he hears you and Pray’s footsteps, he turns around with a big grin on his face.{/cps}"
    pat"{cps=30}Hello friend! So thankful for giving h-{/cps}"
    #pray fade in left
    show pray at left
    pr"{cps=30}Hello, boy.{/cps}"
    "{cps=30}Path gulps, mortified.{/cps}"
    pat"{cps=30}Um… greetings, patriarca!{/cps}"
    pat"{cps=30}How may I serve you?{/cps}"
    pr"{cps=30}There is only one way you can help me, boy.{/cps}"
    pat"{cps=30}And that is?{/cps}"
    pr"{cps=30}You can leave Venice, forevermore, and then you ‘might’ find salvation from the pit in Peter's list.{/cps}"
    pr"{cps=30}Otherwise, I cannot guarantee your immortal soul’s safety.{/cps}"
    pr"{cps=30}For lies in the name of lust are terrible sins indeed.{/cps}"
    pat"{cps=30}What?{/cps}"
    pr"{cps=30}Your letter.{/cps}"
    "{cps=30}Pray pulls out the letter and drops it into the canal.{/cps}"
    "{cps=30}Path’s eyes are locked on the letter until it lands in the brackish sewage of the canal.{/cps}"
    "{cps=30}As the ink smears, he looks at you with pure confusion, betrayal and sadness.{/cps}"
    "{cps=30}He then jumps into his gondola, quickly unties it with deft skill, and starts rowing as fast as he can through the canal.{/cps}"
    #path fade out
    hide path
    "{cps=30}Pray yells out in rage, and jumps into a nearby gondola with the gondolier tuning his guitar idly.{/cps}"
    pr"{cps=30}Gondolier!{/cps}"
    "{cps=30}The gondolier turns to Pray.{/cps}"
    pr"{cps=30}Follow that boat!{/cps}"
    "{cps=30}The gondolier shrugs, and starts to untie his boat’s knot.{/cps}"
    "{cps=30}Out of desire to see how this resolves, you jump into the gondola as a high speed gondola chase through Venice begins.{/cps}"
    #pray fade out
    hide pray
    #fade to canals
    scene bg canal
    with fade
    stop sound fadeout 2.0
    play sound "audio/AMB_Canal.ogg" fadein 2.0 volume 0.5
    "{cps=30}After a thrilling and high-budget chase sequence with fancy effects and amazing soundtrack plays, you and Pray find yourselves back at the Plaza’s dock.{/cps}"
    "{cps=30}Pray tips the gondolier and steps off, you do the same.{/cps}"
    "{cps=30}Thats when you both see that Path’s boat has aready been docked.{/cps}"
    #pray fade left
    show pray at left
    pr"{cps=30}Damn it!{/cps}"
    pr"{cps=30}He must be hiding in the plaza somewhere.{/cps}"
    "{cps=30}You assume the same, and you both run up to the plaza.{/cps}"
    #change bg plaza
    scene bg plaza
    show pray at left
    with fade
    stop sound fadeout 2.0
    play sound "audio/AMB_Street_1.ogg" fadein 2.0 volume 0.5
    "{cps=30}You can see a large congregation around Puck’s stage, the show must be starting.{/cps}"
    pr"{cps=30}You don’t think…{/cps}"
    pr"{cps=30}He couldn’t be THAT stupid, right?{/cps}"
    "{cps=30}Pray points at the show and looks at you.{/cps}"
    "{cps=30}You can faintly hear an incredibly high falsetto voice that sounds disapointingly familiar.{/cps}"
    "{cps=30}He is, in fact, that stupid.{/cps}"
    "{cps=30}You walk over to the show stage, hanging your heads in awe of this intellectual failure on the part of Path.{/cps}"
    # change bg Stage
    scene bg pucksshow
    show pray at left
    with fade
    stop sound fadeout 2.0
    play sound "audio/AMB_Street_2.ogg" fadein 2.0 volume 0.5
    "{cps=30}You see that the puppet show has started, and there are two marionettes in the stand: A high-voiced female puppet and a gravelly male puppet.{/cps}"
    "{cps=30}Pray wordlessly walks up to the stand, reaches up, and pulls Path down by his nose.{/cps}"
    #path fade in right
    show path at right
    pat"{cps=30}Ow!{/cps}"
    "{cps=30}Some of the audience laughs, some children cry, and most people are concerned and ticked off.{/cps}"
    pr"{cps=30}Boy. {/cps}"
    pr"{cps=30}Of all the suitors that have tried to claim my daughter, you are by far the most inept.{/cps}"
    pr"{cps=30}How, in any world, was this a good idea? {/cps}"
    pr"{cps=30}Who convinced you to go and hide as a member of a puppet show rather than just run?{/cps}"
    "{cps=30}You turn back to the puppet stand, where puck is sneaking out.{/cps}"
    #puck fade in center
    show puck at center
    p"{cps=30}Hahaha… um…{/cps}"
    p"{cps=30}{size=+20}DISTRACTION!{/size}{/cps}"
    "{cps=30}Puck throws down a smoke bomb and starts running away.{/cps}"
    hide puck
    "{cps=30}Pray is about to chase him aswell, but starts coughing from the smoke.{/cps}"
    pr"{cps=30}{i}Cough{/i} you know what ? {i}Cough{/i}{/cps}"
    pr"{cps=30}You {i}Cough{/i} win.{/cps}"
    pr"{cps=30}Just {i}Cough{/i} leave my daughter alone.{/cps}"
    pr"{cps=30}{i}Cough{/i} okay?{/cps}"
    "{cps=30}Path furiously nods, slowly backing up.{/cps}"
    pat"{cps=30}O-okay sir!{/cps}"
    pat"{cps=30}So sorry about all of this!{/cps}"
    pr"{cps=30}Uggh.{/cps}"
    pr"{cps=30}I’m getting too old for this.{/cps}"
    pr"{cps=30}But I can't stop.{/cps}"
    pr"{cps=30}I need to keep her…{/cps}"
    pr"{cps=30}Ugh…{/cps}"
    pr"{cps=30}Safe.{/cps}"
    pat"{cps=30}Safe from what?{/cps}"
    pr"{cps=30}{i}Cough{/i} Boys like you!{/cps}"
    pr"{cps=30}Boys who look and act kind, but are just there to use you!{/cps}"
    pr"{cps=30}I know what world we live in, and she is the only thing I have left!{/cps}"
    pr"{cps=30}I can't be weak, I can’t let her get hurt the way-{/cps}"
    pr"{cps=5}…{/cps}"
    pr"{cps=30}I’m losing my station soon, and I’m okay with that.{/cps}"
    pr"{cps=30}I’d do what I’ve done {i}per sempre{/i} if it means I can keep her safe.{/cps}"
    "{cps=30}Path looks at Pray with empathy, finally understanding the source of his aggression.{/cps}"
    pat"{cps=30}It’s kinda funny, isn’t it?{/cps}"
    pr"{cps=30}What is?{/cps}"
    pat"{cps=30}That we are terrified of each other.{/cps}"
    "{cps=30}Pray thinks for a moment, looks at Path, then nods.{/cps}"
    pr"{cps=30}I guess that is funny.{/cps}"
    pr"{cps=30}Can I tell you something funnier?{/cps}"
    pr"{cps=30}My fear consumes me.{/cps}"
    pr"{cps=30}Every waking moment of my life is stained by fear.{/cps}"
    pr"{cps=30}Fear of dark streets, fear of death, fear of loss.{/cps}"
    pr"{cps=30}I think that’s something I need to work on.{/cps}"
    pr"{cps=5}…{/cps}"
    pr"{cps=30}I need to stop using this to distract myself.{/cps}"
    pr"{cps=30}My behavior has been irrational and harmful, and I see that now.{/cps}"
    pr"{cps=30}If you wish to talk to my daughter in person, I can call her and explain the situation.{/cps}"
    pr"{cps=30}I think that, perhaps if I start treating her like the adult she is…{/cps}"
    pr"{cps=30}Perhaps some of that fear will go away.{/cps}"
    pr"{cps=30}I need it to.{/cps}"
    scene black
    with fade
    stop music fadeout 2.0
    play music "audio/Music_2.ogg" volume 0.3 fadein 2.0
    $ Achievement.add(achievement_name['finale'])
    "{cps=30}And so it was, Pray and Path may not have got along and certainly would not for years to come, but the two had reached a kind of understanding.{/cps}"
    "{cps=30}Path saw that the patriarch was not as imposing as he seemed, and that Pray was just as, if not more, afraid than he was.{/cps}"
    "{cps=30}And Pray saw that, despite how scary it sounds, It is not just the role of a parent to protect…{/cps}"
    "{cps=30}It is also the role of a parent to cultivate, and eventually, release their child into the open winds of life.{/cps}"
    "{cps=20}Thus ends our tale, a of love, growth and fear.{/cps}"
    $ Achievement.add(achievement_name['afraid'])
    "{cps=30}Ending One: Afraid.{/cps}"
    $ persistent.restarts+=1
    return


label End2:
    #Puck suitor ending
    #change outside church
    scene bg churchoutside
    with fade
    stop music fadeout 2.0
    play music "audio/Music_1.ogg" volume 0.3 fadein 2.0
    stop sound fadeout 2.0
    play sound "audio/AMB_Church_Inside_Crowded.ogg" fadein 2.0 volume 0.5
    "{cps=30}Pray rushes outside in a power walk of vindictive and fatherly rage.{/cps}"
    "{cps=30}You follow, both out of curiosity and guilt for throwing Puck under the bus.{/cps}"
    #pray fade in left
    show pray at left
    "{cps=30}Pray walks up to the nearby canal port, and you walk up behind him.{/cps}"
    "{cps=30}Path is cleaning up the inside of his boat, and stops when he sees Pray.{/cps}"
    #path fade in right
    show path at right
    "{cps=30}Path looks over to you, and you mouth the words ‘Act Natural’ to him.{/cps}"
    "{cps=30}Path nods and turns to look at Pray.{/cps}"
    pat"{cps=30}H-Hello sir!{/cps}"
    pat"{cps=30}How may I h-help you this fine morning?{/cps}"
    pr"{cps=30}We don’t have much time, take us to the Plaza!{/cps}"
    pat"{cps=30}Right away, your holiness!{/cps}"
    "{cps=30}Path starts rowing, uncertainly, through the canals.{/cps}"
    # change bg canals
    scene bg canal
    show pray at left
    show path at right
    with fade
    stop sound fadeout 2.0
    play sound "audio/AMB_Canal.ogg" fadein 2.0 volume 0.5
    "{cps=30}The three of you arrive at the canals outside the plaza, where you and Path get off slowly.{/cps}"
    "{cps=30}Path is about to follow you and Pray, but you motion for him to stay.{/cps}"
    "{cps=30}Path nods.{/cps}"
    pr"{cps=30}Here you go, boy.{/cps}"
    pr"{cps=30}Thank you for your help.{/cps}"
    "{cps=30}Pray tosses some money into Path’s hands, and Path accepts it with a confused and forced smile.{/cps}"
    "{cps=30}You and Pray leave the port and enter the Plaza.{/cps}"
    #change bg plaza
    scene bg plaza
    show pray at left
    with fade
    stop sound fadeout 2.0
    play sound "audio/AMB_Street_1.ogg" fadein 2.0 volume 0.3
    "{cps=30}You and Pray walk out into the plaza. You can see Puck’s show has amassed a large crowd.{/cps}"
    pr"{cps=30}He must be over there.{/cps}"
    pr"{cps=30}I’m going to talk to him, you have already done enough.{/cps}"
    pr"{cps=30}Stay out of this, please.{/cps}"
    "{cps=30}Pray walks up to the show crowd.{/cps}"
    "{cps=30}You continue following him (obviously) but do so at more of a distance.{/cps}"
    #change bg stage
    scene bg pucksshow
    show pray at left
    with fade
    stop sound fadeout 2.0
    play sound "audio/AMB_Street_2.ogg" fadein 2.0 volume 0.5
    "{cps=30}Puck is currently going through a scene where a clever peasant tricks a complacent aristocrat into giving him the aristocrat’s wallet.{/cps}"
    "{cps=30}The crowd laughs, boos, and claps as the scene unfolds, yet Pray remains stagnant, waiting for an intermission so he can talk to Puck backstage.{/cps}"
    "{cps=30}Eventually, that intermission comes. {/cps}"
    #Puck fade in right
    show puck at right
    p"{cps=30}Thank you, thank you!{/cps}"
    p"{cps=30}I shall return to the tale of ‘Brainy and Dull’ after a short five minute intermission.{/cps}"
    p"{cps=30}Please take time to grab snacks, tip money, or just sit and relax until this bell sounds and the show resumes.{/cps}"
    p"{cps=30}Thank you, and see you all soon!{/cps}"
    "{cps=30}Puck walks behind the small puppet booth into a nearby RV, and closes the door behind him.{/cps}"
    "{cps=30}Pray moves as if on cue, walking up to Puck’s RV seconds after.{/cps}"
    "{cps=30}Pray knocks on the door to the RV, and it slowly opens.{/cps}"
    p"{cps=30}Hellooo!{/cps}"
    p"{cps=30}Who could that be at my-{/cps}"
    p"{cps=30}Oh!{/cps}"
    p"{cps=30}Your holiness, at my humble show!{/cps}"
    p"{cps=30}How do you fair this carnevale?{/cps}"
    pr"{cps=30}Busy.{/cps}"
    "{cps=30}Pray reaches into his pocket and pulls out the note.{/cps}"
    pr"{cps=30}Looks Familiar?{/cps}"
    "{cps=30}Puck takes the letter and examines it.{/cps}"
    p"{cps=30}I cannot say it is…{/cps}"
    p"{cps=30}Seems beautifully written though.{/cps}"
    pr"{cps=30}It is a love letter, addressed to my daughter.{/cps}"
    pr"{cps=30}Someone gave it to me earlier, and claimed that you were the one who wrote it.{/cps}"
    p"{cps=30}I don’t-{/cps}"
    "{cps=30}Puck looks out at you, and then further back into the corner where the canals are.{/cps}"
    "{cps=30}You turn, and see Path peeking around that corner, anticipation and nervousness on his face.{/cps}"
    "{cps=30}Puck sees this, and smiles.{/cps}"
    p"{cps=30}Yes, signore.{/cps}"
    p"{cps=30}I wrote that letter.{/cps}"
    pr"{cps=30}But you just said-{/cps}"
    p"{cps=30}I was mistaken, I have a service where I write love letters for people who cannot write them themselves.{/cps}"
    p"{cps=30}Thus, I could not recognize this letter in particular.{/cps}"
    pr"{cps=30}Then who… who hired you?{/cps}"
    p"{cps=30}A man by the name of Mario Finzione, some greasy man from out of town.{/cps}"
    p"{cps=30}I am deeply sorry for this situation, and I will contact Mr Finzione myself.{/cps}"
    pr"{cps=30}Okay… good!{/cps}"
    "{cps=30}Pray storms off, unsatisfied with the result but willing to believe what Puck said.{/cps}"
    #pray fade out   
    hide pray
    "{cps=30}Once he leaves, you and Path walk up to Puck.{/cps}"
    #path fade in left
    show path at left
    p"{cps=30}Hello there Path!{/cps}"
    p"{cps=30}How are you two doing this morning, have you had breakfast yet?{/cps}"
    pat"{cps=30}Sir… what you did for me…{/cps}"
    p"{cps=30}What I did for you?{/cps}"
    p"{cps=30}I’ve done nothing yet! {/cps}"
    p"{cps=30}After the show, i’ll get food for all of us.{/cps}"
    p"{cps=30}My treat.{/cps}"
    "{cps=30}Path seems uncomfortable with this arrangement, feeling guilty for getting so much out of the performer.{/cps}"
    pat"{cps=30}Sir, surely I can p-{/cps}"
    "{cps=30}Puck puts his hand up to shush Path.{/cps}"
    p"{cps=30}We can talk more later, the show is starting.{/cps}"
    "{cps=30}Puck walks back into his booth and the puppet show resumes.{/cps}"
    #Puck fade out
    hide puck
    #path fade in center
    show path at center
    "{cps=30}Path exhales a sigh of relief, and looks you with thankfulness.{/cps}"
    pat"{cps=30}Thank you, for whatever you did.{/cps}"
    pat"{cps=30}That was almost really bad, and both you and Puck managed to turn it around.{/cps}"
    pat"{cps=30}I’m so lucky, to know clever people.{/cps}"
    scene black
    with fade
    stop music fadeout 2.0
    play music "audio/Music_2.ogg" volume 0.3 fadein 2.0
    $ Achievement.add(achievement_name['finale'])
    "{cps=30}And so it was, you three all got food later and discussed the mornings events.{/cps}"
    "{cps=30}Puck never asked for anything in return from Path for what he did, and resolved to never mention it again.{/cps}"
    "{cps=30}Puck also gave Path a lengthy discussion about smarter practices, confidence, respect, and the benefits of online dating.{/cps}"
    "{cps=30}Path never got with Poem, she would move out of Venice for a job in Paris.{/cps}"
    "{cps=30}It would be a major shift for Pray, who lost his station and would die two years later of a heart attack.{/cps}"
    "{cps=20}Thus ends our tale, a tale of love, awkward boat rides, and clever thinking.{/cps}"
    $ Achievement.add(achievement_name['happy'])
    "{cps=20}Ending Two: Happy.{/cps}"
    $ persistent.restarts+=1
    return
    
label End3:
    #miscommunication ending
    #chang bg canals
    scene bg canal
    with fade
    stop music fadeout 2.0
    play music "audio/Music_2.ogg" volume 0.3 fadein 2.0
    stop sound fadeout 2.0
    play sound "audio/AMB_Canal.ogg" fadein 2.0 volume 0.5
    show poem at right
    show path at left
    "{cps=30}You, Poem and Path are slowly moving down the canal. Poem’s eyes are affixed on you, and Path’s eyes are affixed onto her.{/cps}"
    po"{cps=30}So, how are you liking it?{/cps}"
    "{cps=30}You ask her what she means.{/cps}"
    #music cut out
    stop music
    stop sound
    po"{cps=30}This game.{/cps}"
    po"{cps=30}This is a game, isn’t it?{/cps}"
    "{cps=30}she she sh-{/cps}"
    "{cps=30}she looks terrified-{/cps}"
    with pixellate
    #change music fade int
    play sound "audio/AMB_Canal.ogg" fadein 2.0 volume 0.5
    play music "audio/Music_2.ogg" fadein 2.0 volume 0.5
    "{cps=30}She smiles and sighs at you in a loving way.{/cps}"
    "{cps=30}Path does the same, looking at her.{/cps}"
    "{cps=30}You all pull into the dock and she hops out, grabbing your arm.{/cps}"
    "{cps=30}She quickly tips Path and leaves while dragging you behind her.{/cps}"
    "{cps=30}You can see Path has a bouquet of roses that he is holding in his left hand, and when the money enters his outstretched right hand, he looks at it curiously.{/cps}"
    pat"{cps=30}Huh?{/cps}"
    pat"{cps=30}W-Wait!{/cps}"
    "{cps=30}Poem rounds the corner and Path goes out of sight.{/cps}"
    #path fade out
    hide path
    #change bg plaza    
    scene bg plaza
    show poem at right
    with fade
    stop sound fadeout 2.0
    play sound "audio/AMB_Street_1.ogg" fadein 2.0 volume 0.5
    "{cps=30}Poem moves with an unnatural exuberance.{/cps}"
    "{cps=30}Almost like this is all an excuse to distract herself from something.{/cps}"
    po"{cps=30}Oh! There’s a puppet show over there!{/cps}"
    "{cps=30}She points over at the small stage in the Plaza, and sure enough there is a show going on.{/cps}"
    "{cps=30}You and her walk up, and you try to find a good moment to tell her you did not write the letter.{/cps}"
    "{cps=30}But the crowd is so loud, and she seems so full of joy.{/cps}"
    #change bg stage
    scene bg pucksshow
    show poem at right
    with fade
    stop sound fadeout 2.0
    play sound "audio/AMB_Street_2.ogg" fadein 2.0 volume 0.5
    "{cps=30}She sits down, watching the show with rapt attention.{/cps}"
    "{cps=30}Puck’s show is currently playing a scene where two lovers keep passing each other without meeting.{/cps}"
    "{cps=30}As you two sit down to watch, you hear something in the distance.{/cps}"
    pat"{cps=30}Wait!{/cps}"
    "{cps=30}It seems like Path is just full on sprinting through the plaza towards you and Poem.{/cps}"
    #path fade in left
    show path at left
    pat"{cps=30}You f-forgot your parasol!{/cps}"
    pat"{cps=30}And, ya know.{/cps}"
    pat"{cps=30}Me.{/cps}"
    pat"{cps=30}How is the show?{/cps}"
    "{cps=30}Poem looks over at him in confusion.{/cps}"
    po"{cps=30}Thank you.{/cps}"
    po"{cps=20}Uhh…{/cps}"
    po"{cps=30}What’s your name again?{/cps}"
    "{cps=30}Those words shoot through Path’s heart, but he quickly composes himself.{/cps}"
    pat"{cps=30}Oh, I guess we haven’t talked much.{/cps}"
    pat"{cps=30}Did they not say my name? {/cps}"
    pat"{cps=30}I’m Path.{/cps}"
    po"{cps=30}Okay.{/cps}"
    pat"{cps=30}I… I wrote that letter in your hands.{/cps}"
    po"{cps=30}That’s nice.{/cps}"
    po"{cps=30}Have a good day si-{/cps}"
    "{cps=30}Poem blinks twice while processing what he just said.{/cps}"
    po"{cps=30}You… wrote it?{/cps}"
    pat"{cps=30}'When I look at you, I see the sun.'{/cps}"
    pat"{cps=30}'You blind me.'{/cps}"
    pat"{cps=30}'I wish only that, for a moment, I am permitted to know you in this life.' {/cps}"
    pat"{cps=30}'You are the tune I hum, the spring in my step.' {/cps}"
    pat"{cps=30}'I want only the sadness in your eyes to dissolve, and if that were the only thing I did with my life, I would be satisfied.'{/cps}"
    "{cps=30}She looks at you, astounded and embarrassed.{/cps}"
    "{cps=30}You shrug in response, and say “I tried to talk to you, but you are freakishly strong”.{/cps}"
    "{cps=30}She looks at Path.{/cps}"
    po"{cps=30}I’m… I'm sorry.{/cps}"
    po"{cps=30}I got too caught up in all of this, I had felt so sad and when they reached out to me…{/cps}"
    po"{cps=30}I guess I kind of latched on a bit too hard.{/cps}"
    "{cps=30}You massage your sore arm.{/cps}"
    pat"{cps=30}I get it.{/cps}"
    pat"{cps=30}I don’t wanna force you into doing anything, but do you wanna get coffee and talk later?{/cps}"
    "{cps=30}Poem thinks for a moment.{/cps}"
    "{cps=30}You suddenly become aware that everyone in the audience is staring at you three, and the puppet show has stopped.{/cps}"
    "{cps=30}You can even see Puck peeking down from where he controls his marionettes, looking at you with bated breath.{/cps}"
    "{cps=30}Pale is nearby in his caravan and he is fully not paying attention, doing a word search on a newpaper.{/cps}"
    "{cps=30}Poem finally responds.{/cps}"
    po"{cps=30}Sure.{/cps}"
    "{cps=30}The crowd erupts in claps, whistles and celebration.{/cps}"
    "{cps=30}Path smiles with a big goofy grin on his face.{/cps}"
    po"{cps=30}But first, lets finish watching this show.{/cps}"
    stop music fadeout 2.0
    play music "audio/Music_2.ogg" volume 0.3 fadein 2.0
    $ Achievement.add(achievement_name['finale'])
    "{cps=30}And so it was, Poem and Path sat next to each other, actually interacting for the first time.{/cps}"
    "{cps=30}They did later go to that coffee shop to talk, and they found that they had a lot in common.{/cps}"
    "{cps=30}They both liked similar movies, music, and restaraunts around Venice.{/cps}"
    "{cps=30}But alas, not everything was perfect. {/cps}"
    "{cps=30}When the subject turned to Venice itself, Poem made it clear she deeply wished to leave.{/cps}"
    "{cps=30}At this, Path was unsure how to respond.{/cps}"
    "{cps=30}He was in love with Poem, but he was also in love with this city and his profession.{/cps}"
    "{cps=30}It was the only thing he had left of his family.{/cps}"
    "{cps=30}Sat between that impossible choice, between the love of a woman he had idolized…{/cps}"
    "{cps=30}Or the city he had always known and the world he had lived in, Path had to choose.{/cps}"
    "{cps=30}And he did choose, with a lack of hesitation that would seem out of character to most who new him little.{/cps}"
    "{cps=30}In later years, when recounting this story, he said that the moment the quandry was posed to him... he knew.{/cps}"
    "{cps=30}He knew what was right, and would choose it again.{/cps}"
    #change bg black
    scene black
    with fade
    stop sound fadeout 2.0
    stop music fadeout 4.5
    "{cps=30}Two months later, Poem would take an airplane out of the city.{/cps}"
    "{cps=30}No one knew where she was going, not even her father.{/cps}"
    "{cps=30}She simply just disappeared from the face of the world, alive only in the memories of the few people that knew her.{/cps}"
    "{cps=30}Path got very close to knowing her, but it is a goal he could never reach.{/cps}"
    "{cps=20}That idea haunts him, and would continue to do so for many a year beyond.{/cps}"
    "{cps=30}Thus ends our tale, a tale of love, sadness, and lost possabilities.{/cps}"
    $ Achievement.add(achievement_name['sad'])
    "{cps=30}Ending Three: Sad.{/cps}"
    $ persistent.restarts+=1
    return

label EndS:
    #Secret Ending
    #change bg end of the world
    stop sound fadeout 2.0
    stop music fadeout 2.0
    scene bg edge
    with pixellate
    label EdgeLoop:
        "{cps=30}{b}You are not supposed to be here.{/b}{/cps}"
        "{cps=30}{b}Please, restart the game.{/b}{/cps}"
        "{cps=30}{b}You are not supposed to be here.{/b}{/cps}"
        "{cps=30}{b}Please, restart the game.{/b}{/cps}"
        "{cps=30}{b}You are not supposed to be here.{/b}{/cps}"
        "{cps=30}{b}Please, restart the game.{/b}{/cps}"
        jump EdgeLoop
    
    
   










