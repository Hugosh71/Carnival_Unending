init:
    default Vclothes = False
    default Cclothes = False
    default Mclothes = False
    default Tclothes = False
    default choice_A1_made=False
    default choice_A2_made=False
    default choice_A3_made=False
    default choice_A4_made=False
    default choice_C1_made=False
    default choice_C2_made=False
    default choice_C3_made=False
    default choice_C4_made=False


label start:
    "{i}{cps=20}Che cos'è il crollo? Semplice, è la fine di tutto. La morte senza pace, la morte senza senso. Indossate le maschere, bambini, e ignorate la melodia delle bombe.{/cps}{/i}"
    "{cps=30}Your consciousness stirs as sound comes into focus. It’s coming from outside.{/cps}"
    "{cps=30}You roll around in bed as your nerves slowly come back online from slumber, and your sense of smell brings in the brackish water of the canals, the floral breeze of various patios, and the mirad fried pastries and tarts that are being sold out of stands and bakeries nearby.{/cps}"
    "{cps=30}Your memory returns to you as you process this unique potpourri, you are a tourist in the city of Venice during the {color=#308CDD}{b}Carnevale di Venezia{/b}{/color}.{/cps}"
    #change bg HOTEL
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
    jump continueA1

label A2:
    $ choice_A2_made=True
    "{cps=30}You check the time on your watch...{/cps}"
    "{cps=30}It is currently 9:47 am.{/cps}"
    jump prologuemenu

label A3:
    $ choice_A3_made=True
    "{cps=30}You take time to unpack your bags...{/cps}"
    "{cps=30}You find 15 money in one of your bags !{/cps}"
    jump prologuemenu

label A4:
    $ choice_A4_made=True
    "{cps=30}You decide to leave the room and explore the city.{/cps}"
    jump nextScene

label continueA1:

    menu:
        "A fierce, unique outfit. One that showcases my personality.":
            jump B1
        "A comfortable, modern outfit. One that I can walk around in.":
            jump B2
        "A minimalistic, ‘just crawled out of bed’ outfit. One that tells everyone ‘I didn’t sleep well last night’.":
            jump B3
        "A traditional, carnival-specific outfit. One that hides my identity.":
            jump B4

label B1:
    "{cps=30}You put on the outfit, bright colors and tassles envelop you. You still leave a good amount of skin showing, naturally.{/cps}"

    $ Vclothes = True

    jump prologuemenu

label B2:
    "{cps=30}You put on some jeans, a jacket, a t-shirt, and tennis shoes. You also get your water bottle, just in case.{/cps}"

    $ Cclothes = True

    jump prologuemenu

label B3:
    "{cps=30}You put on sweatpants, a t-shirt, and flip flops. You massage the bags under your eyes lightly, and make a mental note to grab some coffee later.{/cps}"

    $ Mclothes = True

    jump prologuemenu

label B4:
    "{cps=30}You put on an ornate mask you purchased for the carnival, along with a cloak. It feels nice, a bit itchy, but nice.{/cps}"

    $ Tclothes = True

    jump prologuemenu

label nextScene:
    if Vclothes or Cclothes or Mclothes or Tclothes:
        "{cps=30}You walk outside in your outfit, ready to seize the day!{/cps}"
        "{cps=30}After locking your door behind you, walking down the stairs, and grabbing a quick coffee from the complimentary breakfast buffet, you finally step out of the hotel into the surrounding street.{/cps}"
        #change bg street
        jump street
        
        

    else:
        "{cps=30}You walk outside, still fully nude after your shower…{/cps}"
        "{cps=30}Either you forgot to put on clothes due to morning lethargy, or you are just a very aggressive nudist.{/cps}"
        "{cps=30}Either way, as you walk out of your hotel room with a whistle, you hear screams and gasps of the simultaniously surprised and offended locals.{/cps}"
        "{cps=30}One thing leads to another, and you eventually find yourself in the back of a police car, being driven off to the nearest station.{/cps}"
        "{cps=30}Whoops.{/cps}"
        jump prologuemenu

label street:
    "{cps=30}The street is crowded, choked with people wearing costumes, eating food, and making conversation.{/cps}"
    "{cps=30}You try to get your bearings for long enough to make a choice on where you want to go, but the tight streets and waves of pedestrians eventually push you against your control.{/cps}"
    "{cps=30}You eventually stop trying to push against the people, letting them cart you away...{/cps}"
    jump plaza

label plaza:
    #change bg plaza
    "{cps=30}You find yourself in a large plaza, with stands and attractions filling the usually empty space.{/cps}"
    "{cps=30}People seem to be less clumped together here, which allows you enough space to ambulate of your own volitons.{/cps}"
    "{cps=30}You see a small stage, an inviting looking shopkeeper's stand, and a sign pointing to the canals.{/cps}"
    "{cps=30}Where do you go ?{/cps}"

label plazamenu:
    menu:
        #Started implementing the Act one , choices are not finished
        "I go to the small stage.":
            if not choice_C1_made: 
                jump A1
            else:
                "{cps=30}You already did that.{/cps}"
                jump prologuemenu
        "I go to the shopkeeper's stand.":
            if not choice_C2_made: 
                jump A2
            else:
                "{cps=30}You already did that.{/cps}"
                jump prologuemenu
        "I go to the canals.":
            if not choice_C3_made: 
                jump A3
            else:
                "{cps=30}You already did that.{/cps}"
                jump prologuemenu
        "I beg for money.":
            if not choice_C4_made:
                jump A4
            else:
                "{cps=30}You already did that.{/cps}"










