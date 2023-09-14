# import os to grab all .mp3 songs from folder
# and random to pick a random song from the song list
import os
import random
from kivy.uix.label import Label
from kivy.uix.image import Image
#import kivy library for UI design
import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp
# import soundloader to load song in kivy
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.clock import Clock


Window.size = (400,600)


class MyApp(MDApp):
    def build(self):

        layout = MDRelativeLayout(md_bg_color=[0, 0, 0, 1])

        self.music_dir="/Users/gabrielprasenaraj/PycharmProjects/pythonProject"

        self.music_files=os.listdir(self.music_dir)

        print(self.music_files)

        self.song_list = [x for x in self.music_files if x.endswith(('mp3'))]

        self.song_count= len(self.song_list)

        print((self.song_list))

        self.playbutton = MDIconButton(pos_hint={'center_x': 0.4,'center_y': 0.05}, icon='playbtn.png', on_press=self.playaudio)

        self.stopbutton = MDIconButton(pos_hint={'center_x': 0.55, 'center_y': 0.05}, icon='pausebtn.png', on_press=self.stopaudio, disabled=True)

        self.albumimage = Image(pos_hint={'center_x': 0.5, 'center_y': 0.55}, size_hint=(.8, .75))

        self.songLabel = Label(pos_hint={'center_x': 0.4, 'center_y': 0.96}, size_hint=(1, 1), font_size=18)

        layout.add_widget(self.playbutton)
        layout.add_widget(self.stopbutton)
        layout.add_widget(self.songLabel)
        layout.add_widget(self.albumimage)

        Clock.schedule_once(self.playaudio)



        return layout

    def playaudio(self,obj):
        self.playbutton.disabled=True
        self.stopbutton.disabled=False
        self.song_title = self.song_list[random.randrange(0,self.song_count)]
        self.sound= SoundLoader.load('{}/{}'.format(self.music_dir,self.song_title))



        self.songLabel.text="tranquiltone is playing" + self.song_title[2:-4]
        self.albumimage.source= self.song_title[0]+".jpg"
        self.sound.play()

    def stopaudio(self,obj):
        self.playbutton.disabled=False
        self.stopbutton.disabled=True
        self.sound.stop()


if __name__ == '__main__':
    MyApp().run()