#Sayhomes-----By Anjali Reddy
#An App to display images based on various filters, using Kivy Language
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image  
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.config import Config
Config.set('graphics', 'resizable', True) 
kv=Builder.load_string("""
<Image1BHKNorth>:
    bgcolor: 1.0, 0.0, 0.0, 1.0
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'anorth.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed()
        Image:
            source:'bnorth.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed1()
<Image1BHKEast>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size       
        rows:4
        Image:
            source:'aeast.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press()
        Image:
            source:'beast.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press1() 
<Image2BHKTTNorth>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'atte.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed()
        Image:
            source:'btte.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed1()
<Image2BHKTTEast>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'attn.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press()
        Image:
            source:'bttn.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press1()
<Image2BHKTFEast>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'atfe.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed()
        Image:
            source:'btfe.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed1()
<Image2BHKTFENorth>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'atfn.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press()
        Image:
            source:'btfn.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press1()
<Image3BHKTEEast>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'atee.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed()
        Image:
            source:'btee.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed1()
<Image3BHKTENorth>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'aten.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press()
        Image:
            source:'bten.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press1()
<Image3BHKTTNorth>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'a2te.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed()
        Image:
            source:'b2te.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.pressed1()
<Image3BHKTTEast>:
    GridLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows:4
        Image:
            source:'a2tn.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press()
        Image:
            source:'b2tn.jpg'
        Button:
            text:'KnowMoreAbout'
            size_hint_x:0.1
            size_hint_y:0.1
            on_release: root.on_press1()
            
            
""")

class Image1BHKNorth(Screen,ButtonBehavior, Image):
    
    def imagebutton1bhknorth(self):
        return kv
    def pressed(self,*args):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 1BHK"
                           "\n Area - 800\n Direction - North")
        image= Image(source='anorth1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def pressed1(self,*args):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 1BHK"
                           "\n Area - 800\n Direction - North")
        image= Image(source='bnorth1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
      #EAST  
class Image1BHKEast(Screen,ButtonBehavior, Image):
    def imagebutton1bhkeast(self):
        return kv
        
    def on_press(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 1BHK"
                           "\n Area - 800\n Direction - East")
        image= Image(source='aeast1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def on_press1(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 1BHK"
                           "\n Area - 800\n Direction - East")
        image= Image(source='beast1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
class Image2BHKTTEast(Screen,ButtonBehavior, Image):
    def imagebutton2bhktteast(self):
        return kv
        
    def on_press(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 2BHK"
                           "\n Area - 1200\n Direction - East")
        image= Image(source='atte1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def on_press1(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 2BHK"
                           "\n Area - 1200\n Direction - East")
        image= Image(source='btte1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
class Image2BHKTTNorth(Screen,ButtonBehavior, Image):
    
    def imagebutton2bhkttnorth(self):
        return kv
    def pressed(self,*args):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 2BHK"
                           "\n Area - 1200\n Direction - North")
        image= Image(source='attn1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def pressed1(self,*args):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 2BHK"
                           "\n Area - 1200\n Direction - North")
        image= Image(source='bttn1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
class Image2BHKTFEast(Screen,ButtonBehavior, Image):
    def imagebutton2bhkTFeast(self):
        return kv
        
    def on_press(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 2BHK"
                           "\n Area - 1500\n Direction - East")
        image= Image(source='atfe1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def on_press1(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 2BHK"
                           "\n Area - 1500\n Direction - East")
        image= Image(source='btfe1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
class Image2BHKTFNorth(Screen,ButtonBehavior, Image):
    def imagebutton2bhkTFnorth(self):
        return kv
        
    def on_press(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 2BHK"
                           "\n Area - 1500\n Direction - North")
        image= Image(source='atfn1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def on_press1(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 2BHK"
                           "\n Area - 1500\n Direction - North")
        image= Image(source='btfn1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
        
class Image3BHKTEEast(Screen,ButtonBehavior, Image):
    def imagebutton3bhkTEeast(self):
        return kv
        
    def on_press(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 3BHK"
                           "\n Area - 1800\n Direction - East")
        image= Image(source='atee1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def on_press1(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 3BHK"
                           "\n Area - 1800\n Direction - East")
        image= Image(source='btee1.png')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
class Image3BHKTENorth(Screen,ButtonBehavior, Image):
    def imagebutton3bhkTEnorth(self):
        return kv
        
    def on_press(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 3BHK"
                           "\n Area - 1800\n Direction - North")
        image= Image(source='aten1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def on_press1(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 3BHK"
                           "\n Area - 1800\n Direction - North")
        image= Image(source='bten1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
class Image3BHKTTNorth(Screen,ButtonBehavior, Image):
    def imagebutton3bhkTTnorth(self):
        return kv
        
    def on_press(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 3BHK"
                           "\n Area - 2200\n Direction - North")
        image= Image(source='a2tn1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def on_press1(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 3BHK"
                           "\n Area - 2200\n Direction - North")
        image= Image(source='b2tn1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
class Image3BHKTTEast(Screen,ButtonBehavior, Image):
    def imagebutton3bhkTTeast(self):
        return kv
        
    def on_press(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 3BHK"
                           "\n Area - 2200\n Direction - East")
        image= Image(source='a2te1.jpg')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)
    def on_press1(self):        
        layout = GridLayout(cols=2,rows=2) 
        popupLabel = Label(text = "         Details"
                           "\n House Type - 3BHK"
                           "\n Area - 2200\n Direction - East")
        image= Image(source='b2te1.png')
        closeButton = Button(text = "Close",size_hint_x=0.1,size_hint_y=0.1)  
        layout.add_widget(popupLabel) 
        layout.add_widget(image)
        layout.add_widget(closeButton)
        popup = Popup(title ='                        Details', 
                      content = layout)   
        popup.open()    
        closeButton.bind(on_press = popup.dismiss)


class CustomScreen(Screen):
    def __init__(self, **kwargs):
        super(CustomScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.spinnerObject = Spinner(text ="House", 
              values =("1BHK", "2BHK", "3BHK"), 
              background_color =(0.784, 0.443, 0.216, 1))  
      
        self.spinnerObject.size_hint = (0.2, 0.2) 
      
        self.spinnerObject.pos_hint ={'x': .35, 'y':.40}
        layout.add_widget(self.spinnerObject)
        #spinner-selection
        self.spinnerObject.bind(text=self.spinner_select)
        self.spinnerSelection = Label(text="%s"%self.spinnerObject.text)
        layout.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint={'x': .1, 'y':.3}
        #second spinner
        self.spinnerObject1 = Spinner(text ="Area", 
              values =("800","1200", "1500", "1800", "2200"), 
              background_color =(0.784, 0.443, 0.216, 1))  
        self.spinnerObject1.size_hint = (0.2, 0.2) 
      
        self.spinnerObject1.pos_hint ={'x': .35, 'y':.40} 
      
        layout.add_widget(self.spinnerObject1)
        #spinner-selection
        self.spinnerObject1.bind(text=self.spinner_select)
        self.spinnerSelection1 = Label(text="%s"%self.spinnerObject1.text)
        layout.add_widget(self.spinnerSelection1)
        self.spinnerSelection1.pos_hint={'x': .1, 'y':.3}
        #third spinner
        self.spinnerObject2 = Spinner(text ="Directions", 
              values =("North","East"), 
              background_color =(0.784, 0.443, 0.216, 1))  
        self.spinnerObject2.size_hint = (0.2, 0.2)       
        self.spinnerObject2.pos_hint ={'x': .35, 'y':.20}       
        layout.add_widget(self.spinnerObject2)
        #spinner-selection
        self.spinnerObject2.bind(text=self.spinner_select)
        self.spinnerSelection2 = Label(text="%s"%self.spinnerObject2.text)
        layout.add_widget(self.spinnerSelection2)
        self.spinnerSelection2.pos_hint={'x': .1, 'y':.3}

        layout.add_widget(Label(text=self.name, font_size=30))
        navig = BoxLayout(size_hint=(0.2,0.4),pos_hint={'top': 1, 'center_x':0.5})
        next = Button(text='Search')
        next.bind(on_release=self.switch_next)
        navig.add_widget(next)
        layout.add_widget(navig)
        self.add_widget(layout)
    def spinner_select(self,spinner,text):
        self.spinnerSelection.text = "%s"%self.spinnerObject.text
        self.spinnerSelection1.text = "%s"%self.spinnerObject1.text
        self.spinnerSelection2.text = "%s"%self.spinnerObject2.text
#instantiation
        self.ib=Image1BHKNorth()
        self.ib1=Image1BHKEast()
        self.ib2=Image2BHKTTNorth()
        self.ib3=Image2BHKTTEast()
        self.ib4=Image2BHKTFNorth()
        self.ib5=Image2BHKTFEast()
        self.ib6=Image3BHKTENorth()
        self.ib7=Image3BHKTEEast()
        self.ib8=Image3BHKTTNorth()
        self.ib9=Image3BHKTTEast()
        if self.spinnerSelection.text=='1BHK'and self.spinnerSelection1.text=='800' and self.spinnerSelection2.text=='North':
            self.ib.imagebutton1bhknorth()
            sm.add_widget(Image1BHKNorth(name='onebhkn'))
        if self.spinnerSelection.text=='1BHK'and self.spinnerSelection1.text=='800' and self.spinnerSelection2.text=='East':
            self.ib1.imagebutton1bhkeast()
            sm.add_widget(Image1BHKEast(name='onebhke'))
            
        if self.spinnerSelection.text=='2BHK'and self.spinnerSelection1.text=='1200' and self.spinnerSelection2.text=='North':
            self.ib2.imagebutton2bhkttnorth()
            sm.add_widget(Image2BHKTTNorth(name='twobhkttn'))
        if self.spinnerSelection.text=='2BHK'and self.spinnerSelection1.text=='1200' and self.spinnerSelection2.text=='East':
            self.ib3.imagebutton2bhktteast()
            sm.add_widget(Image2BHKTTEast(name='twobhktte'))
            
        if self.spinnerSelection.text=='2BHK'and self.spinnerSelection1.text=='1500' and self.spinnerSelection2.text=='North':
            self.ib4.imagebutton2bhkTFnorth()
            sm.add_widget(Image2BHKTFNorth(name='twobhktfn'))
        if self.spinnerSelection.text=='2BHK'and self.spinnerSelection1.text=='1500' and self.spinnerSelection2.text=='East':
            self.ib5.imagebutton2bhkTFeast()
            sm.add_widget(Image2BHKTFEast(name='twobhktfe'))
            
        if self.spinnerSelection.text=='3BHK'and self.spinnerSelection1.text=='1800' and self.spinnerSelection2.text=='North':
            self.ib6.imagebutton3bhkTEnorth()
            sm.add_widget(Image3BHKTENorth(name='threebhkten'))
        if self.spinnerSelection.text=='3BHK'and self.spinnerSelection1.text=='1800' and self.spinnerSelection2.text=='East':
            self.ib7.imagebutton3bhkTEeast()
            sm.add_widget(Image3BHKTEEast(name='threebhktee'))
            
        if self.spinnerSelection.text=='3BHK'and self.spinnerSelection1.text=='2200' and self.spinnerSelection2.text=='North':
            self.ib8.imagebutton3bhkTTnorth()
            sm.add_widget(Image3BHKTTNorth(name='threebhkttn'))
        if self.spinnerSelection.text=='3BHK'and self.spinnerSelection1.text=='2200' and self.spinnerSelection2.text=='East':
            self.ib9.imagebutton3bhkTTeast()
            sm.add_widget(Image3BHKTTEast(name='threebhktte'))
            
    def switch_next(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.next()

sm = ScreenManager()
sm.add_widget(CustomScreen())

class Sayhomes(App):
    def build(self):
        return sm

if __name__ == '__main__':
    Sayhomes().run()	
