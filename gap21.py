#-----------------------------------------------------------------------------
# Name:      GAP
# Purpose:   Graphics Agnostic Python
#
# Author:    Ti Leyon
#
# Created:   04/07/2017
# Copyright: (c) Ti Leyon 2017
# Licence:   This work is licensed under the
#            Creative Commons Attribution-ShareAlike 4.0
#            International License.
#            To view a copy of this license, visit:
#            http://creativecommons.org/licenses/by-sa/4.0/
#            or send a letter to:
#            Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
#-----------------------------------------------------------------------------

class unipage(object):

    def __init__(self, kivy, screen_size):
        self.kivy = kivy
        self.screen_size = screen_size
        self.unibuttons = []
        self.unitexts = []
        self.unilabels = []
        self.unimages = []
        self.uniframes = []
        self.xratio = self.screen_size[0] / 800.0
        self.yratio = self.screen_size[1] / 600.0

    def setscreen(self):
        if self.kivy:
            from kivy.config import Config
            Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
            from kivy.uix.floatlayout import FloatLayout
            from kivy.core.window import Window
            from kivy.utils import platform as core_platform
            self.root = FloatLayout()
            if (self.xratio == 0) or (self.yratio == 0):
                if core_platform == 'android':
                    self.screen_size = Window.size
                    if self.screen_size[0] < self.screen_size[1]:
                        x = self.screen_size[0]
                        y = self.screen_size[0] / 4 * 3
                        self.screen_size = (x, y)
                else:
                    self.screen_size = (800, 600)
                self.xratio = self.screen_size[0] / 800.0
                self.yratio = self.screen_size[1] / 600.0

            if core_platform == 'android':
                Window.softinput_mode = 'pan'
            else:
                Window.size = self.screen_size
        else:
            import ui
            if (self.xratio == 0) or (self.yratio == 0):
                ss1 = ui.get_screen_size()[0]
                ss3 = ui.get_screen_size()[1]
                notoptimal = True
                while notoptimal:
                    if ss1 % 8 == 0:
                        notoptimal = False
                    else:
                        ss1 -= 1
                ss2 = (ss1 / 4) * 3
                title_bar_height = int(ss3 / 600 * 90)
                if ss2 > ss3 - title_bar_height:
                    ss2 = ss3 - title_bar_height
                    notoptimal = True
                    while notoptimal:
                        if ss2 % 6 == 0:
                            notoptimal = False
                        else:
                            ss2 -= 1
                    ss1 = (ss2 / 3) * 4
                self.screen_size = (ss1, ss2)
                self.xratio = ss1 / 800
                self.yratio = ss2 / 600

            self.root = ui.View(frame=(0,0,self.screen_size[0], \
                        self.screen_size[1]))

    def unibutton(self, params):
        self.unibuttons.append([])
        if len(params) == 6:
            function = params[5]
        else:
            function = nofunction
        if self.kivy:
            from kivy.uix.button import Button
            self.unibuttons[len(self.unibuttons) - 1] = Button(
            text = params[4],
            size_hint_y = None,
            size_hint_x = None,
            height = params[3] * self.yratio,
            width = params[2] * self.xratio,
            font_size = 17.5 * self.yratio,
            pos = (params[0] * self.xratio, params[1] * self.yratio),
            on_press = function )
            self.root.add_widget(self.unibuttons[len(self.unibuttons) - 1])
        else:
            import ui
            self.unibuttons[len(self.unibuttons) - 1] = ui.Button(frame= \
                (params[0] * self.xratio, (600 - params[1] - \
                params[3]) * self.yratio, \
                params[2] * self.xratio, params[3] * self.yratio), \
                title = params[4])
            self.unibuttons[len(self.unibuttons) - 1].background_color \
                = (0.4,0.4,0.4)
            self.unibuttons[len(self.unibuttons) - 1].action = function
            self.unibuttons[len(self.unibuttons) - 1].height = params[3] * \
                self.xratio
            self.unibuttons[len(self.unibuttons) - 1].width = params[2] * \
                self.yratio
            self.unibuttons[len(self.unibuttons) - 1].tint_color = 'white'
            self.unibuttons[len(self.unibuttons) - 1].font = ('<system>', \
                17.5 * self.yratio)
            self.root.add_subview(self.unibuttons[len(self.unibuttons) - 1])

    def unitext(self, params):
        self.unitexts.append([])
        if self.kivy:
            from kivy.uix.textinput import TextInput
            self.unitexts[len(self.unitexts) - 1] = TextInput (
            id = 'text' + str(len(self.unitexts) - 1),
            size_hint_y = None,
            size_hint_x = None,
            height = params[3] * self.yratio,
            width = params[2] * self.xratio,
            text = params[4],
            multiline = True,
            font_size = 17.5 * self.yratio,
            pos = (params[0] * self.xratio, params[1] * self.yratio))
            self.root.add_widget(self.unitexts[len(self.unitexts) - 1])
        else:
            import ui
            self.unitexts[len(self.unitexts) - 1] = ui.TextField(frame=
                (params[0] * self.xratio, (600 - params[1] - params[3]) * \
                self.yratio, params[2] * self.xratio, params[3] * self.yratio))
            self.unitexts[len(self.unitexts) - 1].bordered = False
            self.unitexts[len(self.unitexts) - 1].background_color = 'white'
            self.unitexts[len(self.unitexts) - 1].font = ('<system>', 17.5 * \
                self.yratio)
            self.unitexts[len(self.unitexts) - 1].text = params[4]
            self.root.add_subview(self.unitexts[len(self.unitexts) - 1])

    def unilabel(self, params):
        self.unilabels.append([])
        if self.kivy:
            from kivy.uix.label import Label
            self.unilabels[len(self.unilabels) - 1] = Label(pos = \
                (params[0] * self.xratio, params[1] * self.yratio), \
                size_hint=(1.0,1.0), halign="left", \
                valign="bottom", text = params[4])
            self.unilabels[len(self.unilabels) - 1].font_size = 17.5 * \
                self.yratio
            self.unilabels[len(self.unilabels) - 1].bind(size= \
                self.unilabels[len(self.unilabels) - 1].setter('text_size'))
            self.root.add_widget(self.unilabels[len(self.unilabels) - 1])

        else:

            import ui
            self.unilabels[len(self.unilabels) - 1] = ui.Label(frame= \
                (params[0] * self.xratio,  (600 - params[1] - params[3]) * \
                self.yratio, params[2] * self.xratio, params[3] * self.yratio))
            self.unilabels[len(self.unilabels) - 1].text = params[4]
            self.unilabels[len(self.unilabels) - 1].text_color = 'white'
            self.unilabels[len(self.unilabels) - 1].alignment = \
                ui.ALIGN_LEFT
            self.unilabels[len(self.unilabels) - 1].font = ('<system>', 18 * \
                self.yratio)
            self.root.add_subview(self.unilabels[len(self.unilabels) - 1])

    def unimage(self, params):
        self.unimages.append([])
        if self.kivy:
            from kivy.uix.image import Image
            self.unimages[len(self.unimages) - 1] = Image( source= params[4],
                allow_stretch = True, size_hint = (None, None),
                size=(params[2] * self.xratio, params[3] * self.yratio),
                pos=(params[0] * self.xratio, params[1] * self.yratio))

            self.root.add_widget(self.unimages[len(self.unimages) - 1])

        else:
            import ui
            self.unimages[len(self.unimages) - 1] = (ui.ImageView
            (name = 'Image', frame = (params[0] * self.xratio, \
            (600 - params[1] - params[3]) * self.yratio, \
            params[2] * self.xratio, params[3] * self.yratio)))

            self.root.add_subview (self.unimages[len(self.unimages) - 1])
            self.unimages[len(self.unimages) - 1].image = \
                ui.Image.named(params[4])

    def uniframe(self, params):
        if self.kivy:
            from kivy.graphics import Color
            from kivy.graphics import Rectangle
            self.root.canvas.add(Color (params[4][0],params[4][1], \
                params[4][2]))
            self.root.canvas.add(Rectangle(pos = (params[0] * self.xratio, \
                params[1] * self.yratio), size = (params[2] * self.xratio, \
                params[3] * self.yratio)))
        else:
            import ui
            self.uniframes.append([])
            self.uniframes[len(self.uniframes) - 1] = \
                ui.View(frame=(params[0] * self.xratio, \
                (600 - params[1] - params[3]) * self.yratio, \
                params[2] * self.xratio, params[3] * self.yratio))
            self.uniframes[len(self.uniframes) - 1].background_color = \
                (params[4][0],params[4][1], params[4][2],1.0)
            self.root.add_subview(self.uniframes[len(self.uniframes) - 1])

    def showpage(self):
        if self.kivy:
            from kivy.base import runTouchApp
            runTouchApp(self.root)
        else:
            self.root.present('sheet')

class uniscreen(unipage):
    def __init__(self, screendef):
        try:
            from kivy.uix.floatlayout import FloatLayout
            kivy = True
        except:
            import ui
            kivy = False
        unipage.__init__(self, kivy, screendef[0])
        self.setscreen()
        self.screendef = screendef

    def setpage(self):
        for k in range(1, len(self.screendef)):
            self.screendef[k][0](self, self.screendef[k][1])

def closepage(sender):
    try:

        from kivy.utils import platform as core_platform
        from kivy.core.window import Window
        import sys

        if core_platform == 'android':
            sys.exit()
        else:
            Window.close()

    except:

        sender.superview.close()

def nofunction(sender):
    pass

ss = [(800,600)]
gui_object = object
if uniscreen(ss).kivy == True:
    from kivy.uix.widget import Widget
    gui_object = Widget
else:
    import ui
    gui_object = ui.View

class movables(gui_object):

    def touch_began(self, touch):
        self.new_objs = new_widgets.new_objs
        self.selected_obj = new_widgets.selected_obj
        class new_touch(object):
            def __init__(self):
                self.x = touch.location.x
                self.y = touch.location.y

        Touch = new_touch()
        self.touch_down (None, Touch)

    def touch_moved(self, touch):
        class new_touch(object):
            def __init__(self):
                self.x = touch.location.x
                self.y = touch.location.y

        Touch = new_touch()
        self.touch_move (None, Touch, True)

    def close(self):
        ui.View.close(self)

    def update_all(self):
        if self.selected_obj != None:
            mypage.unitexts[0].text = str(
                self.new_objs[self.selected_obj].pos[0])
            mypage.unitexts[1].text = str(
                self.new_objs[self.selected_obj].pos[1])
            mypage.unitexts[2].text = str(
                self.new_objs[self.selected_obj].width)
            mypage.unitexts[3].text = str(
                self.new_objs[self.selected_obj].height)
        else:
            for x in range (4):
                mypage.unitexts[x].text = 'None'
        if mypage.kivy == False:
            new_widgets.selected_obj = self.selected_obj

    def is_in_box(self, obj, touch):
        obj_clicked = False
        if (touch.x >= obj.x) and (touch.x <= (obj.x + obj.width)):
            if (touch.y >= obj.y) and(touch.y <= (obj.y + obj.height)):
                obj_clicked = True
        return obj_clicked

    def good_move(self, x, y, disp):
        if disp:
            y = (600 * mypage.yratio) - y
        if self.new_objs [self.selected_obj].width  + x > (698 * mypage.xratio):
            x = (698 * mypage.xratio) - self.new_objs [self.selected_obj].width
        if x < (12 * mypage.xratio):
            x = (12 * mypage.yratio)
        if self.new_objs [self.selected_obj].height + y > (594 * mypage.yratio):
            y = (594 * mypage.yratio) - self.new_objs [self.selected_obj].height
        if y < (80 * mypage.yratio):
            y = (80 * mypage.yratio)
        if disp:
            y = (600 * mypage.yratio) - y - self.new_objs [self.selected_obj].height
        return (round(x), round(y))

    def good_height(self, h):
        if self.new_objs [self.selected_obj].y  + h > (594 * mypage.yratio):
            h = (594  * mypage.yratio) - self.new_objs [self.selected_obj].y
        if h < (30 * mypage.yratio):
            h = 30 * mypage.yratio
        return (round(h))

    def good_width(self, w):
        if self.new_objs [self.selected_obj].x  + w > (698 * mypage.xratio):
            w = (698 * mypage.xratio) - self.new_objs [self.selected_obj].x
        if w < (40 * mypage.xratio):
            w = 40 * mypage.xratio
        return round(w)

    def touch_down(self, sender, touch):
        if mypage.kivy:
            bottom = touch.y > 80 * mypage.yratio
        else:
            bottom = touch.y < 525 * mypage.yratio
        if touch.x < (698 * mypage.xratio) and bottom:
            cur_obj = len(self.new_objs) -1
            check_pos = cur_obj >= 0
            while check_pos:
                if self.is_in_box (self.new_objs[cur_obj], touch):
                    check_pos = False
                else:
                    cur_obj -= 1
                    if cur_obj == -1:
                        check_pos = False
            if cur_obj == -1:
                if self.selected_obj != None:
                    self.new_objs[self.selected_obj].background_color = \
                        self.new_objs[self.selected_obj].color
                    self.selected_obj = None
            else:
                if self.selected_obj != None:
                    self.new_objs[self.selected_obj].background_color = \
                        self.new_objs[self.selected_obj].color
                self.selected_obj = cur_obj
                self.new_objs[self.selected_obj].background_color = (1,0,0,1)
                self.start_x = (touch.x)
                self.start_y = (touch.y)
            self.update_all()

    def check_size_change(self):
        if mypage.unibuttons[8].background_color == [0, 1, 0, 1] or \
            mypage.unibuttons[9].background_color == [0, 1, 0, 1] \
            or mypage.unibuttons[8].background_color == (0, 1, 0, 1) or \
            mypage.unibuttons[9].background_color == (0, 1, 0, 1):
                return True
        else:
            return False

    def touch_move(self, sender, touch, disp=False):
        if mypage.kivy:
            bottom = touch.y > 80 * mypage.yratio
        else:
            bottom = touch.y < 525 * mypage.yratio
        if self.selected_obj != None and touch.x < (698 * mypage.xratio) \
            and bottom:
            size_change = self.check_size_change()
            if size_change:
                if mypage.unibuttons[8].background_color == [0, 1, 0, 1] \
                    or mypage.unibuttons[8].background_color == (0, 1, 0, 1):
                    self.new_objs[self.selected_obj].width = \
                        self.good_width (self.new_objs[self.selected_obj].width \
                            - self.start_x + touch.x)
                    self.start_x = touch.x
                if mypage.unibuttons[9].background_color == [0, 1, 0, 1] \
                    or mypage.unibuttons[9].background_color == (0, 1, 0, 1):
                    self.new_objs[self.selected_obj].height = \
                        self.good_height ( \
                        self.new_objs[self.selected_obj].height  \
                            - self.start_y + touch.y)

                    if mypage.kivy == False:
                        full_height = self.new_objs[self.selected_obj].y + \
                            self.new_objs[self.selected_obj].height
                        if full_height > round(525 * mypage.yratio):
                            self.new_objs[self.selected_obj].height -= \
                                full_height - round(525 * mypage.yratio)
                self.start_y = touch.y

            else:

                self.new_objs[self.selected_obj].pos = \
                    self.good_move(touch.x, touch.y, disp)
                if not(mypage.kivy):
                    self.new_objs[self.selected_obj].x = \
                        round(self.new_objs[self.selected_obj].pos[0])
                    self.new_objs[self.selected_obj].y = \
                        round(self.new_objs[self.selected_obj].pos[1])
            self.update_all()

class newobjects (movables):

    def __init__(self):
        import os
        self.fullpath = (__file__)
        self.base_py = os.path.basename(__file__)
        self.new_objs = []
        self.selected_obj = None
        self.count_objs = 0
        self.start_x = None
        self.start_y = None

    def new_button(self):

        a_caption = 'Button' + '{:02d}'.format(self.count_objs)
        self.count_objs += 1
        mypage.unibutton((40, 80, 80, 40, a_caption))
        a_button = mypage.unibuttons [-1]

        a_button.color = a_button.background_color
        if mypage.kivy:
            a_button.bind(on_touch_move=self.touch_move)
            a_button.bind(on_touch_down=self.touch_down)
        else:
            a_button.touch_enabled = False
            a_button.color = a_button.background_color
            a_button.pos = (a_button.x, a_button.y)
        self.new_objs.append(a_button)


    def new_text(self):

        def android_focus(sender, value):
            sender.focus = False

        a_caption = 'Text' + '{:02d}'.format(self.count_objs)
        self.count_objs += 1
        mypage.unitext((40, 160, 200, 30, a_caption))
        a_text = mypage.unitexts [-1]
        a_text.height = 30.0 * mypage.yratio

        a_text.color = a_text.background_color
        if mypage.kivy:
            a_text.bind(on_touch_down=self.touch_down)
            a_text.bind(on_touch_move=self.touch_move)
            from kivy.utils import platform as core_platform
            if core_platform == 'android':
                a_text.bind(focus=android_focus)
        else:
            a_text.touch_enabled = False
            a_text.pos = (a_text.x, a_text.y)
        self.new_objs.append(a_text)

    def new_label(self):
        a_caption = 'Label' + '{:02d}'.format(self.count_objs)
        self.count_objs += 1
        mypage.unilabel((40, 240, 80, 20, a_caption))
        a_label = mypage.unilabels [-1]
        a_label.size_hint=(None,None)
        a_label.width = 240 * mypage.xratio
        a_label.height = 20 * mypage.yratio
        if mypage.kivy:
            a_label.background_color = a_label.color
            a_label.bind(on_touch_down=self.touch_down)
            a_label.bind(on_touch_move=self.touch_move)
        else:
            a_label.touch_enabled = False
            a_label.pos = (a_label.x, a_label.y)
            a_label.color = a_label.background_color
        self.new_objs.append(a_label)

    def new_image(self):
        a_caption = 'Image' + '{:02d}'.format(self.count_objs)
        self.count_objs += 1
        mypage.unibutton((40, 360, 80, 80, a_caption))
        an_image = mypage.unibuttons [-1]
        an_image.background_color = (0,1,0,1)
        an_image.color = an_image.background_color
        if mypage.kivy:
            an_image.bind(on_touch_move=self.touch_move)
            an_image.bind(on_touch_down=self.touch_down)
        else:
            an_image.touch_enabled = False
            an_image.color = an_image.background_color
            an_image.pos = (an_image.x, an_image.y)
        self.new_objs.append(an_image)

    def new_frame(self):
        a_caption = 'Frame' + '{:02d}'.format(self.count_objs)
        self.count_objs += 1
        mypage.unibutton((40, 480, 80, 80, a_caption))
        a_frame = mypage.unibuttons [-1]
        a_frame.background_color = (0,0,1,1)
        a_frame.color = a_frame.background_color
        if mypage.kivy:
            a_frame.bind(on_touch_move=self.touch_move)
            a_frame.bind(on_touch_down=self.touch_down)
        else:
            a_frame.touch_enabled = False
            a_frame.color = a_frame.background_color
            a_frame.pos = (a_frame.x, a_frame.y)
        self.new_objs.append(a_frame)

def set_toggle(sender):
    if sender.background_color == [0, 0, 1, 1] or \
        sender.background_color == (0, 0, 1, 1):
        sender.background_color = (0, 1, 0, 1)
        if mypage.kivy:
            sender.text = sender.text[:6].strip() + ' on'
        else:
            sender.title = sender.title[:6].strip() + ' on'
    else:
        sender.background_color = (0, 0, 1, 1)
        if mypage.kivy:
            sender.text = sender.text[:6].strip() + ' off'
        else:
            sender.title = sender.title[:6].strip() + ' off'

def do_label(sender):
    new_widgets.new_label()

def do_text(sender):
    new_widgets.new_text()

def do_button(sender):
    new_widgets.new_button()

def do_image(sender):
    new_widgets.new_image()

def do_frame(sender):
    new_widgets.new_frame()

def drags(sender):
    new_widgets.new_button()
    new_widgets.new_text()
    new_widgets.new_label()

    for x in range (len(new_widgets.new_objs)):
        mypage.root.add_widget (new_widgets.new_objs[x])

def delete_object(sender):
    if new_widgets.selected_obj != None:
        dead_obj = new_widgets.new_objs.pop(new_widgets.selected_obj)
        if mypage.kivy:
            mypage.root.remove_widget(dead_obj)
        else:
            mypage.root.remove_subview(dead_obj)
        new_widgets.selected_obj = None

def modify_object(sender):
    if mypage.kivy:
        disp = False
    else:
        disp = True
    if new_widgets.selected_obj != None:
        try:

            if disp:
                mypage.unitexts[1].text = str(float(mypage.unitexts[1].text) \
                    + new_widgets.new_objs[new_widgets.selected_obj].height)

            new_widgets.new_objs[new_widgets.selected_obj].pos = \
                new_widgets.good_move(float(mypage.unitexts[0].text), \
                float(mypage.unitexts[1].text), disp)
        except:
            pass
        try:
            new_widgets.new_objs[new_widgets.selected_obj].width = \
                new_widgets.good_width(float(mypage.unitexts[2].text))
        except:
            pass
        try:
            new_widgets.new_objs[new_widgets.selected_obj].height = \
                new_widgets.good_height(float(mypage.unitexts[3].text))
        except:
            pass

        if mypage.kivy == False:
            new_widgets.new_objs[new_widgets.selected_obj].x = \
                new_widgets.new_objs[new_widgets.selected_obj].pos[0]
            new_widgets.new_objs[new_widgets.selected_obj].y = \
                new_widgets.new_objs[new_widgets.selected_obj].pos[1]

        new_widgets.update_all()

def delete_all():
    for x in range(len(new_widgets.new_objs)):
        new_widgets.selected_obj = 0
        delete_object(delete_all)

def function_holders(objs):
    funcs = ''
    for obj in objs:
        try:
            s = obj.text
        except:
            s = obj.title
        if s[0] == 'B':
            funcs = funcs + '\ndef do_' + s + '(sender):\n'
            funcs = funcs + '    pass\n\n'
    return funcs

def build_obj(obj, disp):

    def fix(number, height):
        if not(disp):
            number= 600 - (abs(round(number + (80 * 4/3 * 7/8)))) + 6 - height
        return str(number)

    try:
        s = obj.text
    except:
        s = obj.title
    kind = ['unibutton', 'unitext', 'unilabel', 'unimage', 'uniframe']
    obj_type = kind[['B','T','L','I','F'].index(s[0])]
    string_out = '(' + obj_type + ", (" + \
        str(round((obj.x - (12 * mypage.xratio)) / mypage.xratio * 4/3 * 7/8) \
        ) + ', ' + fix(round((obj.y - (80 * mypage.yratio)) / mypage.yratio * \
        4/3 * 7/8), round(obj.height  / mypage.yratio* 4/3 * 7/8)) + ', ' \
        + str(round(obj.width / mypage.xratio * 4/3 * 7/8)) + ', ' + \
        str(round(obj.height  / mypage.yratio * 4/3 * 7/8))
    if obj_type == 'uniframe':
        string_out += ', (.5,.5,.5)'
    elif obj_type == 'unimage':
        if disp:
            string_out += ", 'data/logo/kivy-icon-512.png'"
        else:
            string_out += ", 'test:Pythonista'"
    else:
        string_out += ", '" + s + "'"
    if obj_type == 'unibutton':
        string_out += ", do_" + s
    string_out += ')),'
    return string_out

def save_page(sender):
    page_in = open(new_widgets.base_py, 'r')
    lines = page_in.readlines()
    s = mypage.unitexts[4].text
    if s[-3:] != '.py':
        s = s + '.py'
    try:
        page_out = open(s, 'w')
        cnt = 0
        for z in range (258):
            s = lines[z]
            if z == 1:
                s = s[0:len(s)-1] + ' (Output)\n'
            page_out.writelines(s)
            cnt = cnt + 1
        page_out.writelines(function_holders(new_widgets.new_objs))
        page_out.writelines("if __name__ == '__main__':\n")
        page_out.writelines('    unilabel = unipage.unilabel\n')
        page_out.writelines('    uniframe = unipage.uniframe\n')
        page_out.writelines('    unitext = unipage.unitext\n')
        page_out.writelines('    unibutton = unipage.unibutton\n')
        page_out.writelines('    unimage = unipage.unimage\n')
        page_out.writelines('    widgets = [(600, 450),\n')
        for x in range (len(new_widgets.new_objs)):
            page_out.writelines('        ' + build_obj(new_widgets.new_objs[x], \
            mypage.kivy) +  '\n')
        page_out.writelines('        ]\n')
        page_out.writelines('    mypage = uniscreen(widgets)\n')
        page_out.writelines('    mypage.setpage()\n')
        page_out.writelines('    mypage.showpage()\n')

        page_in.close()
        page_out.close()
        mypage.unitexts[5].text = 'Save successful'
    except:
        mypage.unitexts[5].text = 'Save failed'

def open_page(sender):

    def find_var(cnt, var):
        cnt2 = 0

        while cnt > 0:
            s = lines[cnt]
            x = s.find(var)
            if x > 0:
                cnt2 = cnt
                cnt = 0
            else:
                cnt -=1
        return cnt2, x

    def baby_parse(s, cnt2, kk, no_stop, no_error):

        while no_stop and no_error:
            depth = 0
            z = s.find(',', kk)
            if z < 0:
                depth += 1
                z = s.find('\\', kk)
                if z < 0:
                    depth += 1
                    z = s.find(']', kk)
                    if z < 0:
                        if s.strip() == '':
                            depth = 1
                        else:
                            no_error = False
                    else:
                        no_stop = False
            else:
                z = s.find('\\', kk)
                if z > 0:
                    depth = 1
                elif s.find('uni', kk) < 0:
                    depth = 1
                else:
                    z = s.find(']', kk)
                    if z > 0:
                        no_stop = False

            if depth == 1:
                cnt2 += 1
                if cnt2 < cnt:
                    s = lines[cnt2]
                    kk = 0
            if depth == 2:
                no_stop = False
            if no_error and no_stop:
                z = s.find('uni', kk)
                if z > 0:
                    kk = z
                    z = s.find(',', kk)
                    if z > 0:
                        s2 = s[kk: z]
                        kk = z
                        z = s.find('(', kk)
                        if z > 0:
                            kk = z
                            z = s.find(')', kk)
                            if z > 0:
                                s3 = s[kk + 1: z]
                                an_obj = [s2] + s3.replace(' ', '').split(',')
                                all_objs.append(an_obj)
                else:
                    if s.find(']') > 0:
                        no_stop = False
        return depth, no_error, no_stop


    no_error = True
    temp_objs = []
    all_objs = []
    s = mypage.unitexts[4].text
    if s[-3:] != '.py':
        s = s + '.py'
    try:
        page_in = open(s, 'r')
        lines = page_in.readlines()
        cnt = len(lines) - 1
        cnt2, x = find_var(cnt, 'uniscreen')
        k = 0
        if cnt2 > 248:
            s = lines[cnt2]
            y = s.find('(', x)
            if y > x:
                z = s.find(')',y)
                if z > y:
                    k = z - y
            if k < 1:
                no_error = False
        else:
            no_error = False
        if no_error:
            s2 = s[y + 1:k + y]
        cnt2, x = find_var(cnt2-1, s2)
        if no_error:
            s = lines[cnt2]
            y = s.find('(', x)
            if y > x:
                z = s.find(')',y)
                if z > y:
                    k = z - y
            if k < 1:
                no_error = False
        else:
            no_error = False
        if no_error:
            s2 = s[y + 1:k + y].replace(' ', '').split(',')
            temp_objs.append(s2)

            no_stop = True
            kk = k+y
            depth, no_error, no_stop = baby_parse(s, cnt2, kk, \
                no_stop, no_error)
        page_in.close()
    except:
        no_error = False
    if no_error:
        delete_all()
        creator ={'unibutton':do_button,'unitext':do_text,
            'unilabel':do_label, 'unimage':do_image, 'uniframe':do_frame}
        new_widgets.count_objs = 0

        for k in range(2):
            index_objs = -1
            for ob in all_objs:
                index_objs += 1
                if k == 0:
                    creator[ob[0]](open_page)
                for x in range(4):
                    converted = float(ob[x+1]) * 3/4 * 8/7 * mypage.xratio
                    if x == 0:
                        converted += 12 * mypage.xratio
                    if x == 1:
                        converted += 80 * mypage.yratio

                        if mypage.kivy == False:
                            converted -= 80 * mypage.yratio
                    converted = round(converted)
                    mypage.unitexts[x].text = str(converted)

                new_widgets.selected_obj = index_objs
                modify_object(open_page)

        if mypage.kivy == False:

            for wd in new_widgets.new_objs:
                wd.y = (525 * mypage.yratio) - wd.y - wd.height
                mypage.unitexts[x].text = str(wd.y)
                wd.pos = (wd.pos[0], round(wd.y))
        mypage.unitexts[5].text = 'Open successful'
    else:
        mypage.unitexts[5].text = 'Open failed'

if __name__ == '__main__':
    unilabel = unipage.unilabel
    uniframe = unipage.uniframe
    unitext = unipage.unitext
    unibutton = unipage.unibutton
    unimage = unipage.unimage

    widgets = [(700, 525),
        (uniframe,(0, 0, 800, 600,(.6,.6,.6))),
        (uniframe,(10, 75, 688,520 ,(0,0,0))),

        (unibutton,(710, 560, 80, 30, 'Button', do_button)),
        (unibutton,(710, 520, 80, 30, 'Input', do_text)),
        (unibutton,(710, 480, 80, 30, 'Label', do_label)),
        (unibutton,(710, 440, 80, 30, 'Image', do_image)),
        (unibutton,(710, 400, 80, 30, 'Frame', do_frame)),
        (unibutton,(710, 360, 80, 30, 'Delete', delete_object)),

        (uniframe,(710, 180, 80,150, (0,0,0))),
        (unilabel,(710, 300, 20, 20, 'X')),
        (unilabel,(710, 260, 20, 20, 'Y')),
        (unilabel,(710, 220, 20, 20, 'W')),
        (unilabel,(710, 180, 20, 20, 'H')),

        (unitext,(730, 300, 60, 30, 'None')),
        (unitext,(730, 260, 60, 30, 'None')),
        (unitext,(730, 220, 60, 30, 'None')),
        (unitext,(730, 180, 60, 30, 'None')),
        (unibutton,(710, 140, 80, 30, 'Modify', modify_object)),
        (unibutton,(710, 75, 80, 30, 'Exit', closepage)),

        (uniframe,(10, 5, 215,65 ,(0,0,0))),
        (unibutton,(15, 10, 100, 35, 'Width off', set_toggle)),
        (unibutton,(120, 10, 100, 35, 'Height off', set_toggle)),
        (unilabel,(15, 50, 150, 20, 'Toggle Dimensions')),

        (uniframe,(230, 5, 335,65 ,(0,0,0))),
        (unitext,(235, 10, 150, 35, 'gapout.py')),
        (unibutton,(395, 10, 80, 35, 'Open', open_page)),
        (unibutton,(480, 10, 80, 35, 'Save', save_page)),
        (unilabel,(235, 50, 100, 20, 'Current File')),

        (uniframe,(570, 5, 220,65 ,(0,0,0))),
        (unitext,(575, 10, 210, 35, 'Please read gapinfo.png')),
        (unilabel,(575, 50, 100, 20, 'Feedback')),
        ]

    mypage = uniscreen(widgets)
    if mypage.kivy == False:
        mypage.root = movables(frame=(0,0,mypage.screen_size[0], \
                        mypage.screen_size[1]))
    mypage.setpage()
    if mypage.kivy == False:
        for x in range(4,7):
            mypage.unilabels[x].font = ('<system>', 16 * mypage.xratio)
        for x in range(4):
            mypage.unitexts[x].font = ('<system>', 16 * mypage.xratio)
        for x in range(3, 6):
            mypage.uniframes[3].touch_enabled = False
    new_widgets = newobjects()
    mypage.unibuttons[8].background_color = (0, 0, 1, 1)
    mypage.unibuttons[9].background_color = (0, 0, 1, 1)

    mypage.showpage()

