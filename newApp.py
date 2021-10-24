from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from  kivy.uix.textinput import TextInput
import pyttsx3 
class FirstScr(Screen):
	def __init__(self, name='first'):
		super().__init__(name=name) # здесь надо передавать имя. Что будет, если не передать?
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')
		self.txtInput = TextInput(text='Озвучь меня!')
		vl.add_widget(self.txtInput)
		self.btnVoice = Button(text="Озвучить")
		self.btnVoice.on_press = self.Play
		#Кнопка для категории "Дом"
		self.btnHome = Button(text="Дом")
		self.btnHome.on_press = self.toHome
		self.btnStreet = Button(text="Улица")
		self.btnStreet.on_press = self.toStreet
		self.btnTransport = Button(text="Транспорт")
		self.btnTransport.on_press = self.toTransport
		self.btnSOS = Button(text="SOS", background_color =(1, 0, 0, 1)  )
		self.btnSOS.on_press = self.toSOS
		
		vl.add_widget(self.btnVoice)
		vl.add_widget(self.btnHome)
		vl.add_widget(self.btnStreet)
		vl.add_widget(self.btnTransport)
		vl.add_widget(self.btnSOS)
		self.add_widget(vl)

	def Play(self):
		self.engine.say(self.txtInput.text)
		self.engine.runAndWait()
	def toHome(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'second'
	def toStreet(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'third'
	def toTransport(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'fourth'
	def toSOS(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'SOS'

class SecondScr(Screen):
	def __init__(self, name='second'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')
		#Создайте кнопки для озвучки
		#Хочу есть
		btnEat = Button(text="Хочу есть")
		vl.add_widget(btnEat)
		btnEat.on_press = lambda : self.Play("Хочу есть")
		#Нужно в туалет
		btnToilet = Button(text="Нужно в туалет")
		vl.add_widget(btnToilet)
		btnToilet.on_press = lambda : self.Play("Нужно в туалет")
		#Пойдем гулять
		btnWalk = Button(text="Пойдем гулять")
		vl.add_widget(btnWalk)
		btnWalk.on_press = lambda : self.Play("Пойдем гулять")
		#Кнопка "Назад"'''
		btnBack = Button(text="Главное меню")
		btnBack.on_press = self.next
		vl.add_widget(btnBack)
		self.add_widget(vl)
		
	def next(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first'
	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class ThirdScr(Screen):
	def __init__(self, name='third'):
		super().__init__(name=name)
		#
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')
		#Создайте кнопки для озвучки
		#Хочу есть
		btnSecurity = Button(text="Вызовите охрану")
		vl.add_widget(btnSecurity)
		btnSecurity.on_press = lambda : self.Play("Вызовите охрану")
		#Нужно в туалет
		btnTrafficlights = Button(text="Вызовите светофор")
		vl.add_widget(btnTrafficlights)
		btnTrafficlights.on_press = lambda : self.Play("Вызовите светофор")
		#Пойдем гулять
		btnRoad = Button(text="Помогите перейти дорогу")
		vl.add_widget(btnRoad)
		btnRoad.on_press = lambda : self.Play("Помогите перейти дорогу")
		#Кнопка "Назад"'''
		btnBack = Button(text="Главное меню")
		btnBack.on_press = self.next
		vl.add_widget(btnBack)
		self.add_widget(vl)
		
	def next(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first'
	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class FourthScr(Screen):
	def __init__(self, name='fourth'):
		super().__init__(name=name)
		#
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')
		#Создайте кнопки для озвучки
		#Хочу есть
		btnTaxi = Button(text="Помогите вызвать такси")
		vl.add_widget(btnTaxi)
		btnTaxi.on_press = lambda : self.Play("Помогите вызвать такси")
		#Нужно в туалет
		btnBus = Button(text="Какой автобус едет до школы?")
		vl.add_widget(btnBus)
		btnBus.on_press = lambda : self.Play("Какой автобус едет до школы?")
		#Пойдем гулять
		btnRamp = Button(text="Опустите пандус")
		vl.add_widget(btnRamp)
		btnRamp.on_press = lambda : self.Play("Опустите пандус")
		#Кнопка "Назад"'''
		btnBack = Button(text="Главное меню")
		btnBack.on_press = self.next
		vl.add_widget(btnBack)
		self.add_widget(vl)
		
	def next(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first'
	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class SOSScr(Screen):
	def __init__(self, name='SOS'):
		super().__init__(name=name)
		#
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')
		#Создайте кнопки для озвучки
		#Хочу есть
		btnAmbulance = Button(text="Вызовите скорую")
		vl.add_widget(btnAmbulance)
		btnAmbulance.on_press = lambda : self.Play("Вызовите скорую")
		#Нужно в туалет
		btnBadly = Button(text="Мне плохо")
		vl.add_widget(btnBadly)
		btnBadly.on_press = lambda : self.Play("Мне плохо")
		#Пойдем гулять
		btnPolice = Button(text="вызовите полицию")
		vl.add_widget(btnPolice)
		btnPolice.on_press = lambda : self.Play("вызовите полицию")
		#Кнопка "Назад"'''
		btnBack = Button(text="Главное меню")
		btnBack.on_press = self.next
		vl.add_widget(btnBack)
		self.add_widget(vl)
		
	def next(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first'
	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()
class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(FirstScr(name='first'))
		sm.add_widget(SecondScr(name='second'))
		sm.add_widget(ThirdScr(name='third'))
		sm.add_widget(FourthScr(name='fourth'))
		sm.add_widget(SOSScr(name='SOS'))


		return sm

app = MyApp()
app.run()