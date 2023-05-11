python early:


    class Achievement(NoRollback):
        def __init__(self, name='', image='', message='', priority=None, **kwargs):
            ## The name of the achievement.
            self.name = name

            ## The image of the achievement.
            if image == '':
                ## If image is None, a default image will be used.
                self.image = Transform('gui/trophy_icon.png', fit='contain')
            else:
                self.image = Transform(image, fit='contain')

            ## The message associated with the achievement.
            self.message = message

            ## Set the priority of the achievement.
            ##            None = default (greyed out and can see the name and description of the achievement.)
            ##        'hidden' = Achievements with this tag will be displayed as 'hidden'.
            ##      'platinum' = The final achievement to be granted once all other achievements have been granted.
            self.priority = priority

        def __eq__(self, value):
            ## Since we are using a persistent list we need to do an equality check.
            ## Below we are simply checking 'self.name == value.name, self.message == value.message'
            return all((self.name == value.name, self.message == value.message))

        def add(trophy):
            ## Add/Grant Trophies/Achievements to the list.
            ## As a standard python expression  ::  Achievement.add( <trophy> )
            ## As a screen action  ::  Function( Achievement.add, <trophy> )
            if not achievement.has(trophy.name):
                achievement.grant(trophy.name)
                store.achievement_is_done = False
                store.achievement_notification_timer = 3.0
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                ## New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)
            achievement.sync()

        def purge(self):
            ## This will clear the achievements AND persistent list.
            ## As a standard python expression  ::  achievements.purge()
            ## As a screen action  ::  Function( achievements.purge )
            achievement.clear_all()
            persistent.my_achievements.clear()


## DO NOT TOUCH/REUSE/CHANGE THIS AT ANY TIME!
## To clear this list use ::  achievements.purge()
default persistent.my_achievements = []
default achievements = Achievement()

init python:

    ## Note - This has not been implemented to work with Steam.
    ##        You'll have to work that out on your own if you want it to work with steam.
    ##        I have left some Steam stuff in place, but these haven't been elaborated upon.
    achievement.steam_position = "bottom right"

    achievement_name = {

        ## -------------------------- IMPORTANT (1) --------------------------
        ## 
        ## How to set up achievements
        ## "achievement_key": Achievement(name=_("Name of Achievement"), message=_("Description"), image='<image_path_here>', priority='<type>'),

        ## -------------------------- IMPORTANT (2) --------------------------
        ## Note: If you decide to add/amend any achievement's data long after the game has started or
        ##       an achievement has been granted you will have to do a full reset of the game for those
        ##       changes to be reflected. I.e. Delete persistent data.

        ## -------------------------- EXAMPLES -------------------------- 
        "places": Achievement(name=_("Places!"), message=_("Start the show."), image='gui/trophy_icon.png', priority=None),

        ## The prio, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these terms to describe the types of achievements;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as 'hidden'.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "finale": Achievement(name=_("Finale?"), message=_("Is that it?"), image='gui/trophy_icon.png', priority=None),
        "onestar": Achievement(name=_("One Star Performance"), message=_("Broke a leg."), image='gui/trophy_icon.png', priority=None),
        "afraid": Achievement(name=_("Afraid"), message=_("Watch him shiver."), image='gui/trophy_icon.png', priority='hidden'),
        "happy": Achievement(name=_("Happy"), message=_("Watch him smile."), image='gui/trophy_icon.png', priority='hidden'),
        "sad": Achievement(name=_("Sad"), message=_("Watch him cry."), image='gui/trophy_icon.png', priority='hidden'),
        "violent": Achievement(name=_("Angry"), message=_("Watch them fight."), image='gui/trophy_icon.png', priority='hidden'),
        "circus": Achievement(name=_("Acting"), message=_("Watch him say goodbye."), image='gui/trophy_icon.png', priority='hidden'),
        "collapsed": Achievement(name=_("ERROR:%collapsed%offscript%falling%"), message=_("%watch%her%jump%"), image='gui/trophy_icon.png', priority='hidden'),
        "nude": Achievement(name=_("Crude, Nude and Full a' Tude!"), message=_("get naked"), image='gui/trophy_icon.png', priority=None),
        "legal": Achievement(name=_("this is probably legal and good"), message=_("Work for an apathetic weirdo."), image='gui/trophy_icon.png', priority=None),
        "wfind": Achievement(name=_("Word Find"), message=_("Solve a word search."), image='gui/trophy_icon.png', priority=None),
        "attack": Achievement(name=_("Attack a Police Officer"), message=_("Wait, what-"), image='gui/trophy_icon.png', priority=None),
        "casa": Achievement(name=_("Casanova"), message=_("Watch them kiss."), image='gui/trophy_icon.png', priority=None),
        "chase": Achievement(name=_("Chase Sequence"), message=_("It's just REALLY hidden, so chill"), image='gui/trophy_icon.png', priority=None),
        "centhusiast": Achievement(name=_("Clock Enthusiast"), message=_("THERE IS NO TIME SYSTEM, ITS JUST TEXT"), image='gui/trophy_icon.png', priority=None),
        "cannoli": Achievement(name=_("mmmmMMmm cannoli mmMMmmMm"), message=_("Eat a cannoli"), image='gui/trophy_icon.png', priority=None),
        "tcritic": Achievement(name=_("Theater Critic"), message=_("See Everything."), image='gui/trophy_icon.png', priority='platinum'),
        ## More of this is explained in 'achievement_screen.rpy'.

    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v.name)

