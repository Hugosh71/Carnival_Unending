## Here we have the menu screen to display all the locked
## and unlocked achievements.

## This configuration here allows the grid to be displayed even if
## not all elements are visible. You won't get an error for grids
## that are not filled to the max.
define config.allow_underfull_grids = True

## The achievements screen.
screen achievement_menu():

    tag menu

    use game_menu(_("Achievements"), scroll="viewport"):

        style_prefix "achievements"

        text "{:01d}/{}".format(len(persistent.my_achievements), len(achievement_name) if len(persistent.my_achievements) == len(achievement_name) else len(achievement_name) - 1) size 30

        frame:
            
            background None
            padding (20, 20, 20, 20)
            align (0.0, 0.0)

            vpgrid:
                
                cols 2 ## You can change this number depending on the width of your achievements.
                spacing 10

                ## Granted achievements
                for t in persistent.my_achievements:

                    if achievement.has(t.name):
                        
                        frame:
                            
                            background Solid('#0088AA') ## Nice bright blue/turquoise.

                            hbox:
                                yalign 0.5
                                xysize (100, 100)
                                
                                add t.image size (100, 100) yalign 0.5

                                null width 20

                                vbox:
                                    spacing 0
                                    yfill False
                                    
                                    text "[t.name]" style 'achievements_label' color '#000000'
                                    text "[t.message]" color '#000000'

                ## Locked achievements
                for v in achievement_name.values():
                    if not achievement.has(v.name):

                        ## We're doing a check for all achievements that is not a 'platinum'.
                        ## The platinum achievement will not appear in the list.
                        if v.priority != 'platinum':
                            
                            frame:
                                
                                hbox:
                                    
                                    yalign 0.5
                                    xysize (100, 100)
                                    
                                    ## This will display a locked icon.
                                    add 'gui/locked_achievement.png' size (100, 100) yalign 0.5

                                    null width 20

                                    vbox:
                                        
                                        spacing 0
                                        yfill False

                                        ## We're setting the data feedback to represent
                                        ## the None and 'hidden' achievements.
                                        if v.priority is None:
                                        
                                            text "[v.name]" style 'achievements_label' color '#FFFFFF33'
                                            text "[v.message]" color '#FFFFFF33'
                                        
                                        else:

                                            text _('Hidden Achievement') style 'achievements_label' color '#FFFFFF33'


init python:

    ## These two functions are the ones that will be used
    ## to handle the list as achievements are added to it.

    def achievement_notification_show():
        ## This is to force the notification to show if
        ## the list is not empty.
        store.achievement_is_done = False
        if achievement_notification_list:
            store.achievement_notification_list.pop(0)


    def achievement_notification_done():
        ## This is to tell RenPy that the notification list
        ## is now empty and sets the variable to True.
        if not achievement_notification_list:
            store.achievement_is_done = True


    ## Here we have a funtion that is passive.
    def passive_function():
        ## This code here will grant the platinum achievement.
        if len(persistent.my_achievements) >= (len(achievement_name) - 1):
            Achievement.add(achievement_name['wow'])


define config.periodic_callback = passive_function


init python:
    ## Sets the screen above everything else.
    config.always_shown_screens.append('achievement_notification_catcher')
    config.per_frame_screens.append('achievement_notification_catcher')

    ## The achievement notification is set on top of everything else.
    config.top_layers.append('achievement_notificication')


## A list for where achievements will be added to be shown as a notification.
default achievement_notification_list = []
default achievement_is_done = False

## The default timer for how long the achievement will be shown on screen.
default achievement_notification_timer = 4.0

## The notification screen.
## By default, the notification will appear at the top of the screen.
## If you want to change this you'll have to amend the transform 'achievement_appear_'.


## This screen will catch any achievement that is in the list.
screen achievement_notification_catcher():

    zorder 999

    if len(achievement_notification_list) > 0 and not renpy.get_screen('achievement_notification'):
        timer 0.5 repeat True:
            action [SetVariable('achievement_notification_timer', 3.0), ## Resets the timer.
                    SetVariable('achievement_is_done', False), Show('achievement_notification')]

    if not achievement_is_done:
        timer 1.0 repeat True:
            action If(achievement_notification_timer > 0.0,
                      true=SetVariable('achievement_notification_timer', achievement_notification_timer - 1.0), ## Countdown.
                     false=If(len(achievement_notification_list) > 0,
                              true=[Hide("achievement_notification"),
                                    Function(achievement_notification_show)],
                             false=[Function(achievement_notification_done)]))


screen achievement_notification():

    layer 'achievement_notify'

    if achievement_notification_list:

        frame:
            background Solid('#FFFFFF')
            align (0.5, 0.0)
            padding (20, 20, 20, 20)

            hbox:
                xysize (100, 100)
                add achievement_notification_list[0].image
                
                null width 20

                vbox:
                    yalign 0.5
                    xminimum 340
                    xmaximum 440
                    yfill False
                    xfill False

                    text str(achievement_notification_list[0].name):
                        color '#000000'
                        size 25

                    text str(achievement_notification_list[0].message):
                        style 'victory_message_text'
                        size 16

            if persistent.achievement_badge == 'top':
                at achievement_appear_top
            elif persistent.achievement_badge == 'left':
                at achievement_appear_left
            elif persistent.achievement_badge == 'right':
                at achievement_appear_right


default persistent.achievement_badge = 'top'
## If you'd like to make this an option that can be changed you can copy this code below to anywhere in the preferences screen.
##
##
## label _("Achievement Notification Position")
## text 'Choose the position of the achievement badge notification.' size 16
## hbox:
##     style_prefix "radio"
##     textbutton _("Left") action SetField(persistent, "achievement_badge", 'left')
##     textbutton _("Top") action SetField(persistent, "achievement_badge", 'top')
##     textbutton _("Right") action SetField(persistent, "achievement_badge", 'right')
## 
##
## The styling is up to you.

## Achievement appear transforms
## You can amend these to how you see fit.
transform achievement_appear_top:
    subpixel True yalign 0.0
    on show:
        yanchor 1.0
        easein_quad 0.15 yanchor 0.0

    on hide:
        yanchor 0.0
        easeout_quad 0.15 yanchor 1.0

transform achievement_appear_left:
    subpixel True xalign 0.0 yalign 0.5
    on show:
        xanchor 1.0
        easein_quad 0.15 xanchor 0.0

    on hide:
        xanchor 0.0
        easeout_quad 0.15 xanchor 1.0

transform achievement_appear_right:
    subpixel True xalign 1.0 yalign 0.5
    on show:
        xanchor 0.0
        easein_quad 0.15 xanchor 1.0

    on hide:
        xanchor 1.0
        easeout_quad 0.15 xanchor 0.0



style victory_message_text:
    color "#000000"
    size 20


style achievements_vbox is vbox
style achievements_text is text
style achievements_frame is frame

style achievements_vbox:
    minimum (330, 100)
    maximum (360, 100)
    spacing 2
    yfill False

style achievements_label:
    size 26
    outlines [(1, '#00000022', 0, 1)]
    yalign 0.5

style achievements_text:
    size 16
    yalign 0.5

style achievements_locked_text:
    color "#555555"
    size 16

style achievements_frame:
    background Solid('#444444')
    minimum (500, 140)
    align (0.5, 0.5)
    padding (15, 15, 15, 15)


## I haven't fully tested the mobile version.
## Feel free to adjust.
screen achievement_menu():

    tag menu

    variant "touch"

    use game_menu(_("Achievements"), scroll="viewport"):

        style_prefix "achievements"

        text "{:01d}/{}".format(len(persistent.my_achievements), len(achievement_name) if len(persistent.my_achievements) == len(achievement_name) else len(achievement_name) - 1) size 30

        frame:
            
            background None
            padding (10, 10, 10, 10)
            align (0.0, 0.0)

            vpgrid:
                
                cols 1
                spacing 3

                ## Granted achievements
                for t in persistent.my_achievements:
                    
                    if achievement.has(t.name):
                        
                        frame:
                            
                            background Solid('#0088AA')

                            hbox:
                                
                                yalign 0.5
                                xysize (50, 50)
                                
                                add t.image size (50, 50) yalign 0.5

                                null width 15

                                vbox:
                                    
                                    spacing 0
                                    yfill False
                                    
                                    text "[t.name]" style 'achievements_label' color '#000000'
                                    text "[t.message]" color '#000000'

                ## Locked achievements
                for v in achievement_name.values():

                    if not achievement.has(v.name):

                        if v.priority != 'platinum':

                            frame:

                                hbox:

                                    yalign 0.5
                                    xysize (50, 50)

                                    add 'gui/locked_achievement.png' size (50, 50) yalign 0.5

                                    null width 15

                                    vbox:
                                        spacing 0
                                        yfill False

                                        if v.priority is None:
                                            
                                            text "[v.name]" style 'achievements_label' color '#FFFFFF33'
                                            text "[v.message]" color '#FFFFFF33'
                                        
                                        else:
                                        
                                            text _('Hidden Achievement') style 'achievements_label' color '#FFFFFF33'


style achievements_vbox:
    variant 'small'
    xysize (300, 80)

style achievements_label:
    variant 'small'
    size 16

style achievements_text:
    variant 'small'
    size 16

style achievements_locked_text:
    variant 'small'
    size 16

style achievements_frame:
    variant 'small'
    size 16