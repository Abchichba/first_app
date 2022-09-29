import time
import threading
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
class Wind(App):
	def build(self):
		Window.clearcolor = (0, 0, 0, 0)#Color of window
		self.groups = [ ]#File
		self.note_names = [ ]
		self.note_bg_col = [ ]
		self.note_fnt_col = [ ]
		self.tags = [ ]
		self.note_cont = [ ]
		self.group_col = [ ]
		self.note_time = [ ]
		self.names_groups = [ ]
		self.one_col_group = [ ]
		try:
			file = open("notebook.txt", "r", encoding = "utf-8")
			file_cont = file.read()
			if file_cont != "":
				file_var = file_cont.split("﷽")
				var22 = file_var[1].split("釁")
				var23 = file_var[3].split("釁")
				var24 = file_var[4].split("釁")
				var25 = file_var[5].split("釁")
				var26 = file_var[6].split("釁")
			for i in range(0, len(var22)):
				self.tags.append(var22[i].split("鬮"))
				self.group_col.append(tuple([int(i) for i in var23[i].split("鬮")]))
				self.note_time.append(var24[i].split("鬮"))
				self.note_bg_col.append(tuple([int(i) for i in var25[i].split("鬮")]))
				self.note_fnt_col.append(tuple([int(i) for i in var26[i].split("鬮")]))
			self.note_names = file_var[0].split("釁")
			self.groups = file_var[2].split("釁")
			self.note_cont = file_var[7].split("釁")
			for i in self.groups:
				if not i in self.names_groups:
					self.names_groups.append(i)
					self.one_col_group.append(self.group_col[self.groups.index(i)])
			file.close()
		except:
			pass
		self.btn73 = Button(text = "Confirm", size_hint = (1, 0.1), pos = (0, Window.height * 0.9), on_press = self.open_note_conf)# Note after search
		self.btn74 = Button(text = "Back", size_hint = (1, 0.1), pos = (0, 0), on_press = self.click)
		self.box61 = BoxLayout(orientation = "vertical")#Results of search
		self.result_box = [ ]
		self.result_anc = [ ]
		self.result_btn1 = [ ]
		self.result_btn2 = [ ]
		for i in range(0, len(self.note_names)):
			var23 = Button(size_hint = (None, None), size = (Window.width * 0.45, Window.height * (0.81 / 4)), background_normal = "", halign = "center", on_press = self.look_note)
			var24 = Button(size_hint = (None, None), size = (Window.width * 0.48, Window.height * (0.864 / 4)), background_normal = "", background_down = "")
			var25 = AnchorLayout(size_hint = (None, None), size = (Window.width * 0.5, Window.height * (0.9 / 4)), anchor_x = "center", anchor_y = "center")
			var25.add_widget(var24)
			var25.add_widget(var23)
			self.result_anc.append(var25)
			self.result_btn1.append(var23)
			self.result_btn2.append(var24)
			if i % 2 == 0:
				self.result_box.append(BoxLayout(orientation = "horizontal", size_hint = (1, None), size = (Window.width, Window.height * (0.9 / 4))))
		box62 = BoxLayout(orientation = "vertical", size_hint = (1, 0.9))
		scr2 = ScrollView(size_hint = (1, 1))
		self.box63 = BoxLayout(orientation = "vertical", size_hint = (1, None))
		self.box63.bind(minimum_height = self.box63.setter("height"))
		self.btn72 = Button(text = "Back", size_hint = (1, 0.1), on_press = self.search_back)
		scr2.add_widget(self.box63)
		box62.add_widget(scr2)
		self.box61.add_widget(box62)
		self.box61.add_widget(self.btn72)
		box60 = BoxLayout(orientation = "vertical")#Search by word or phrase
		self.btn70 = Button(text = "Confirm", size_hint = (1, 0.1 / 0.7), on_press = self.search_by_word)
		self.text11 = TextInput(size_hint = (1, 0.5 / 0.7))
		self.btn71 = Button(text = "Back", on_press = self.ok, size_hint = (1, 0.1 / 0.7))
		box60.add_widget(self.btn70)
		box60.add_widget(self.text11)
		box60.add_widget(self.btn71)
		self.pop13 = Popup(title = "", size_hint = (0.7, 0.7), content = box60)
		self.box55 = BoxLayout(orientation = "vertical")#Search by date add
		self.btn62 = Button(text = "Confirm", size_hint = (1, 0.1), on_press = self.search_by_date)
		box56 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.8))
		box57 = BoxLayout(orientation = "vertical")
		box58 = BoxLayout(orientation = "vertical")
		box59 = BoxLayout(orientation = "vertical")
		date_box = [box57, box58, box59]
		date_names = ["Hours", "Minutes", "Secundes", "Date", "Month", "Year"]
		date_times = [[0, 24], [0, 60], [0, 60], [1, 32], [1, 13], [1900, 2101]]
		self.date_scrs = [ ]
		self.date_btn = [ ]
		self.date_box2 = [ ]
		self.date_values = [0, 0, 0, 0, 0, 0]
		self.date_btn2 = [[ ], [ ], [ ], [ ], [ ], [ ]]
		for a in range(0, 2):
			for b in range(0, 3):
				date_box[b].add_widget(Label(text = date_names[(a * 3) + b], size_hint = (1, 0.05 / 0.8)))
				sup_btn = Button(size_hint = (1, 0.07 / 0.8), on_press = self.open_scr_date)
				self.date_btn.append(sup_btn)
				date_box[b].add_widget(sup_btn)
				sup_box = BoxLayout(orientation = "vertical", size_hint = (1, 0.28 / 0.8))
				self.date_box2.append(sup_box)
				date_box[b].add_widget(sup_box)
				help_box = BoxLayout(orientation = "vertical", size_hint = (1, None))
				help_box.bind(minimum_height = help_box.setter("height"))
				self.date_btn2[(a * 3) + b].append(Button(text = "", size_hint = (1, None), size = (Window.width * (1 / 3), Window.height * 0.07), on_press = self.date_choose))
				help_box.add_widget(self.date_btn2[(a * 3) + b][0])
				for c in range(date_times[(a * 3) + b][0], date_times[(a * 3) + b][1]):
					if len(str(c)) == 1:
						var15 = "0" + str(c)
					else:
						var15 = str(c)
					help_btn = Button(text = var15, size_hint = (1, None), size = (Window.width * (1 / 3), Window.height * 0.07), on_press = self.date_choose)
					self.date_btn2[(a * 3) + b].append(help_btn)
					help_box.add_widget(help_btn)
				help_scr = ScrollView(size_hint = (1, 1))
				help_scr.add_widget(help_box)
				self.date_scrs.append(help_scr)
		self.btn69 = Button(text = "Back", on_press = self.click, size_hint = (1, 0.1))
		for i in date_box:
			box56.add_widget(i)
		self.box55.add_widget(self.btn62)
		self.box55.add_widget(box56)
		self.box55.add_widget(self.btn69)
		box54 = BoxLayout(orientation = "vertical")#Search by name of group
		self.btn60 = Button(text = "Confirm", on_press = self.search_name_group)
		label44 = Label(text = "Enter name of group")
		self.text10 = TextInput(multiline = False)
		self.btn61 = Button(text = "Back", on_press = self.ok)
		box54.add_widget(self.btn60)
		box54.add_widget(label44)
		box54.add_widget(self.text10)
		box54.add_widget(self.btn61)
		self.pop11 = Popup(title = "", size_hint = (0.7, None), size = (Window.width * 0.7, Window.width * 0.7), content = box54)
		box53 = BoxLayout(orientation = "vertical")#Search by group
		self.btn57 = Button(text = "Search by name of group", size_hint = (1, 0.4), on_press = self.open_pop)
		self.btn58 = Button(text = "Search by color of group", size_hint = (1, 0.4), on_press = self.collor)
		self.btn59 = Button(text = "Back", size_hint = (1, 0.2), on_press = self.ok)
		box53.add_widget(self.btn57)
		box53.add_widget(self.btn58)
		box53.add_widget(self.btn59)
		self.pop10 = Popup(title = "", size_hint = (0.7, 0.7), content = box53)
		box51 = BoxLayout(orientation = "vertical")#Search by tag
		self.btn54 = Button(text = "Confirm", size_hint = (1, 0.1 / 0.7), on_press = self.search_by_tags)
		self.box52 = BoxLayout(orientation = "vertical", size_hint = (1, None))
		self.box52.bind(minimum_height = self.box52.setter("height"))
		scr5 = ScrollView(size_hint = (1, 1))
		box61 = BoxLayout(orientation = "vertical", size_hint = (1, 0.4 / 0.7))
		self.btn55 = Button(text = "+", size_hint = (1, 0.1 / 0.7), on_press = self.tag_search_add)
		self.btn56 = Button(text = "Back", on_press = self.ok, size_hint = (1, 0.1 / 0.7))
		scr5.add_widget(self.box52)
		box61.add_widget(scr5)
		box51.add_widget(self.btn54)
		box51.add_widget(box61)
		box51.add_widget(self.btn55)
		box51.add_widget(self.btn56)
		self.pop9 = Popup(title = "", size_hint = (0.7, 0.7), content = box51)
		box50 = BoxLayout(orientation = "vertical")#Search by number
		self.btn52 = Button(text = "Confirm", on_press = self.search_by_number)
		label43 = Label(text = "Enter number of note")
		anc2 = AnchorLayout(anchor_x = "center", anchor_y = "center")
		self.text9 = TextInput(size_hint = (None, None), size = (Window.width * 0.1, Window.width * 0.1), multiline = False)
		self.btn53 = Button(text = "Back", on_press = self.ok)
		anc2.add_widget(self.text9)
		box50.add_widget(self.btn52)
		box50.add_widget(label43)
		box50.add_widget(anc2)
		box50.add_widget(self.btn53)
		self.pop8 = Popup(title = "", size_hint = (0.7, None), size = (Window.width * 0.7, Window.width * 0.7), content = box50)
		box49 = BoxLayout(orientation = "vertical")#Search by name
		self.btn50 = Button(text = "Confirm", on_press = self.search_by_name)
		label42 = Label(text = "Enter name of note")
		self.text8 = TextInput(multiline = False)
		self.btn51 = Button(text = "Back", on_press = self.ok)
		box49.add_widget(self.btn50)
		box49.add_widget(label42)
		box49.add_widget(self.text8)
		box49.add_widget(self.btn51)
		self.pop7 = Popup(title = "", size_hint = (0.7, None), size = (Window.width * 0.7, Window.width * 0.7), content = box49)
		box47 = BoxLayout(orientation = "vertical")#Delete tag
		self.label41 = Label(size_hint = (1, 0.8))
		box48 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.2))
		self.btn48 = Button(text = "Yes", on_press = self.note_del)
		self.btn49 = Button(text = "No", on_press = self.ok)
		box48.add_widget(self.btn48)
		box48.add_widget(self.btn49)
		box47.add_widget(self.label41)
		box47.add_widget(box48)
		self.pop6 = Popup(title = "", size_hint = (0.6, None), size = (Window.width * 0.6, Window.width * 0.6), content = box47)
		self.float5 = FloatLayout()#Information about note
		self.btn44 = Button(background_normal = "", background_down = "")
		self.box42 = BoxLayout(orientation = "vertical")
		self.btn40 = Button(text = "Confirm", size_hint = (1, 0.1), on_press = self.inf_conf)
		self.label21 = Label(text = "Name", size_hint = (1, 0.05))
		self.text7 = TextInput(background_normal = "", size_hint = (1, 0.06), multiline = False)
		self.label26 = Label(text = "Number", size_hint = (1, 0.05))
		self.label27 = Label(text = "", size_hint = (1, 0.05))
		self.label28 = Label(text = "Day when was made", size_hint = (1, 0.05))
		self.box45 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.05))
		self.label29 = Label(text = "Hours")
		self.label30 = Label(text = "Minutes")
		self.label31 = Label(text = "Seconds")
		self.label32 = Label(text = "Day")
		self.label33 = Label(text = "Month")
		self.label34 = Label(text = "Year")
		self.box46 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.05))
		self.label35 = Label(text = "")
		self.label36 = Label(text = "")
		self.label37 = Label(text = "")
		self.label38 = Label(text = "")
		self.label39 = Label(text = "")
		self.label40 = Label(text = "")
		self.label22 = Label(text = "Tags", size_hint = (1, 0.05))
		self.scr3 = ScrollView(size_hint = (None, None), size = (Window.width, Window.height * 0.06))
		self.box43 = BoxLayout(orientation = "horizontal", size_hint = (None, 1))
		self.box43.bind(minimum_width = self.box43.setter("width"))
		self.btn45 = Button(text = "+", size_hint = (None, 1), size = (Window.width * 0.1, Window.height * 0.06), on_press = self.difer_tag)
		self.label23 = Label(text = "Group", size_hint = (1, 0.05))
		widget3 = Widget(size_hint = (1, 0.06))
		self.btn46 = Button(background_normal = "", pos = (0, Window.height * 0.32), size_hint = (1, 0.06), on_press = self.group_in_inf)
		self.scr4 = ScrollView(size_hint = (None, None), size = (Window.width, Window.height * 0.06), pos = (0, Window.height * 0.32))
		self.btn47 = Button(text = "+", size_hint = (None, None), size = (Window.width * 0.1, Window.height * 0.06), on_press = self.open_pop)
		self.box44 = BoxLayout(orientation = "horizontal", size_hint = (None, 1))
		self.box44.bind(minimum_width = self.box44.setter("width"))
		self.label24 = Label(text = "Color of background", size_hint = (1, 0.05))
		self.btn41 = Button(background_normal = "", size_hint = (1, 0.06), on_press = self.collor)
		self.label25 = Label(text = "Color of font", size_hint = (1, 0.05))
		self.btn42 = Button(background_normal = "", size_hint = (1, 0.06), on_press = self.collor)
		self.btn43 = Button(text = "Back", on_press = self.click, size_hint = (1, 0.1))
		for i in range(0, len(self.names_groups)):
			if len(self.names_groups[i]) >= 6:
				var30 = len(self.names_groups[i]) * 28
			else:
				var30 = 168
			self.box44.add_widget(Button(text = self.names_groups[i], size_hint = (None, None), size = (var30, Window.height * 0.06), background_normal = "", background_color = (self.one_col_group[i][0] / 255, self.group_col[i][1] / 255, self.group_col[i][2] / 255, self.group_col[i][3] / 100), on_press = self.group_in_inf))
		self.box44.add_widget(self.btn47)
		self.scr3.add_widget(self.box43)
		self.scr4.add_widget(self.box44)
		self.box43.add_widget(self.btn45)
		self.box45.add_widget(self.label29)
		self.box45.add_widget(self.label30)
		self.box45.add_widget(self.label31)
		self.box45.add_widget(self.label32)
		self.box45.add_widget(self.label33)
		self.box45.add_widget(self.label34)
		self.box46.add_widget(self.label35)
		self.box46.add_widget(self.label36)
		self.box46.add_widget(self.label37)
		self.box46.add_widget(self.label38)
		self.box46.add_widget(self.label39)
		self.box46.add_widget(self.label40)
		self.box42.add_widget(self.btn40)
		self.box42.add_widget(self.label21)
		self.box42.add_widget(self.text7)
		self.box42.add_widget(self.label26)
		self.box42.add_widget(self.label27)
		self.box42.add_widget(self.label28)
		self.box42.add_widget(self.box45)
		self.box42.add_widget(self.box46)
		self.box42.add_widget(self.label22)
		self.box42.add_widget(self.scr3)
		self.box42.add_widget(self.label23)
		self.box42.add_widget(widget3)
		self.box42.add_widget(self.label24)
		self.box42.add_widget(self.btn41)
		self.box42.add_widget(self.label25)
		self.box42.add_widget(self.btn42)
		self.box42.add_widget(self.btn43)
		self.float5.add_widget(self.btn44)
		self.float5.add_widget(self.box42)
		self.float5.add_widget(self.btn46)
		self.float4 = FloatLayout()#Note
		self.btn36 = Button(text = "Confirm", size_hint = (1, 0.1), pos = (0, Window.height * 0.9), on_press = self.open_note_conf)
		self.box36 = BoxLayout(orientation = "vertical", size_hint = (1, 0.8), pos = (0, Window.height * 0.1))
		box37 = BoxLayout(orientation = "horizontal", size_hint = (1, 1 / 8))
		self.btn37 = Button(text = "Information", on_press = self.open_inf_note)
		self.btn38 = Button(text = "Delete", on_press = self.note_ask_del)
		self.text6 = TextInput(size_hint = (1, 7 / 8,), foreground_color = (1, 1, 1, 1))
		self.btn39 = Button(text = "Back", size_hint = (1, 0.1), pos = (0, 0), on_press = self.click)
		box37.add_widget(self.btn37)
		box37.add_widget(self.btn38)
		self.box36.add_widget(box37)
		self.box36.add_widget(self.text6)
		box34 = BoxLayout(orientation = "vertical")#Delete tag
		self.label20 = Label(size_hint = (1, 0.8))
		box35 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.2))
		btn34 = Button(text = "Yes", on_press = self.tag_del)
		self.btn35 = Button(text = "No", on_press = self.ok)
		box35.add_widget(btn34)
		box35.add_widget(self.btn35)
		box34.add_widget(self.label20)
		box34.add_widget(box35)
		self.pop5 = Popup(content = box34, title = "", size_hint = (0.6, None), size = (Window.width * 0.6, Window.width * 0.6))
		self.float2 = FloatLayout()#Color
		self.btn32 = Button(background_normal = "", background_color = (0, 0, 0, 0))
		box17 = BoxLayout(orientation = "vertical")
		self.btn33 = Button(text = "Confirm", size_hint = (1, 0.1), on_press = self.col_conf)
		box31 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.05))
		self.label12 = Label(text = "0")
		self.label13 = Label(text = "0")
		self.label14 = Label(text = "0")
		self.label15 = Label(text = "100")
		box32 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.7))
		self.slider1 = Slider(orientation = "vertical", min = 0, max = 255)
		self.slider2 = Slider(orientation = "vertical", min = 0, max = 255)
		self.slider3 = Slider(orientation = "vertical", min = 0, max = 255)
		self.slider4 = Slider(orientation = "vertical", min = 0, max = 100, value = 100)
		box33 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.05))
		label16 = Label(text = "R")
		label17 = Label(text = "G")
		label18 = Label(text = "B")
		label19 = Label(text = "A")
		self.btn31 = Button(text = "Back", size_hint = (1, 0.1), on_press = self.col_back)
		box31.add_widget(self.label12)
		box31.add_widget(self.label13)
		box31.add_widget(self.label14)
		box31.add_widget(self.label15)
		box32.add_widget(self.slider1)
		box32.add_widget(self.slider2)
		box32.add_widget(self.slider3)
		box32.add_widget(self.slider4)
		box33.add_widget(label16)
		box33.add_widget(label17)
		box33.add_widget(label18)
		box33.add_widget(label19)
		box17.add_widget(self.btn33)
		box17.add_widget(box31)
		box17.add_widget(box32)
		box17.add_widget(box33)
		box17.add_widget(self.btn31)
		self.float2.add_widget(self.btn32)
		self.float2.add_widget(box17)
		box16 = BoxLayout(orientation = "vertical")#Group add
		btn27 = Button(text = "Confirm", on_press = self.group_conf)
		label11 = Label(text = "Enter name of the group")
		self.text5 = TextInput(multiline = False)
		self.btn28 = Button(text = "Color of group", on_press = self.collor, background_normal = "", background_color = (88 / 255, 88 / 255, 88 / 255, 1))
		self.btn29 = Button(text = "Back", on_press = self.ok)
		box16.add_widget(btn27)
		box16.add_widget(label11)
		box16.add_widget(self.text5)
		box16.add_widget(self.btn28)
		box16.add_widget(self.btn29)
		self.pop4 = Popup(content = box16, size_hint = (0.8, None), size = (Window.width * 0.8, Window.width * 0.8), title = "")
		box13 = BoxLayout(orientation = "vertical")#Popup
		self.label10 = Label(size_hint = (1, 0.8), text = "", halign = "center")
		self.btn26 = Button(text = "Ok", size_hint = (1, 0.2), on_press = self.ok)
		box13.add_widget(self.label10)
		box13.add_widget(self.btn26)
		self.pop3 = Popup(content = box13, size_hint = (0.5, None), size = (Window.width / 2, Window.width / 2), title = "")
		box12 = BoxLayout(orientation = "vertical")#Tag add
		btn24 = Button(text = "Confirm", on_press = self.tag_conf)
		label9 = Label(text = "Enter tag")
		self.text4 = TextInput(multiline = False)
		self.btn25 = Button(text = "Back", on_press = self.ok)
		box12.add_widget(btn24)
		box12.add_widget(label9)
		box12.add_widget(self.text4)
		box12.add_widget(self.btn25)
		self.pop2 = Popup(content = box12, size_hint = (0.8, None), size = (Window.width * 0.8, Window.width * 0.8), title = "")
		self.float1 = FloatLayout()#Add
		self.box5 = BoxLayout(orientation = "vertical")
		self.btn16 = Button(text = "Confirm", size_hint = (1, 0.1), on_press = self.add_conf)
		self.label7 = Label(text = "1", size_hint = (1, 0.025))
		widget1 = Widget(size_hint = (1, 0.65))
		self.text2 = TextInput(size_hint = (1, 0.65), pos = (0, Window.height * 0.225))
		self.label8 = Label(text = "1", size_hint = (1, 0.025))
		box6 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.1))
		btn17 = Button(text = "<---", on_press = self.go_add)
		btn18 = Button(text = "--->", on_press = self.go_add)
		self.btn19 = Button(text = "Back", size_hint = (1, 0.1), on_press = self.click)
		self.box10 = BoxLayout(orientation = "vertical", size_hint = (1, 0.65), pos = (0, Window.height * 0.225))
		label4 = Label(text = "Name of note", size_hint = (1, (0.08 / 0.65)))
		self.text3 = TextInput(size_hint = (1, (0.08 / 0.65)), multiline = False)
		label5 = Label(text = "Tags", size_hint = (1, (0.08 / 0.65)))
		self.btn23 = Button(text = "+", on_press = self.difer_tag, size_hint = (None, None), size = (Window.width * 0.1, Window.height * 0.08))
		self.box11 = BoxLayout(orientation = "horizontal", size_hint = (None, 1))
		self.box11.bind(minimum_width = self.box11.setter("width"))
		scr1 = ScrollView(size_hint = (1, (0.08 / 0.65)), size = (Window.width, Window.height))
		box7 = BoxLayout(orientation = "horizontal", size_hint = (1, (0.33 / 0.65)))
		box8 = BoxLayout(orientation = "vertical")
		label6 = Label(text = "Group", size_hint = (1, (0.08 / 0.33)))
		self.btn20 = Button(text = "Color of font", size_hint = (1, (0.25 / 0.33)), on_press = self.collor, background_normal = "", background_color = (88 / 255, 88 / 255, 88 / 255, 1))
		box9 = BoxLayout(orientation = "vertical")
		self.btn21 = Button(text = "Choose group", size_hint = (1, (0.08 / 0.33)), on_press = self.group, background_normal = "", background_color = (88 / 255, 88 / 255, 88 / 255, 1))
		self.box14 = BoxLayout(size_hint = (1, None), orientation = "vertical", pos = (0, Window.height * 0.475))
		self.box14.bind(minimum_height = self.box14.setter("height"))
		for i in range(0, len(self.names_groups)):
			self.box14.add_widget(Button(text = self.names_groups[i], size_hint = (None, None), size = (Window.width / 2, Window.height * 0.1), background_normal = "", background_color = (self.one_col_group[i][0] / 255, self.group_col[i][1] / 255, self.group_col[i][2] / 255, self.group_col[i][3] / 100), on_press = self.final_group))
		self.btn30 = Button(text = "+", on_press = self.open_pop, size_hint = (None, None), size = (Window.width / 2, Window.height * 0.1), background_normal = "", background_color = (50 / 255, 50 / 255, 50 / 255, 1))
		self.box14.add_widget(self.btn30)
		self.scr2 = ScrollView(size_hint = (1, 1), size = (Window.width, Window.height))
		self.box15 = BoxLayout(size_hint = (0.5, 0.475), pos = (Window.width / 2, 0))
		self.box15.add_widget(self.scr2)
		box12 = BoxLayout(orientation = "vertical")
		self.btn22 = Button(text = "Color of background", size_hint = (1, (0.25 / 0.33)), on_press = self.collor, background_normal = "", background_color = (88 / 255, 88 / 255, 88 / 255, 1))
		self.scr2.add_widget(self.box14)
		self.box11.add_widget(self.btn23)
		scr1.add_widget(self.box11)
		box8.add_widget(label6)
		box8.add_widget(self.btn20)
		box9.add_widget(self.btn21)
		box9.add_widget(self.btn22)
		box7.add_widget(box8)
		box7.add_widget(box9)
		self.box10.add_widget(label4)
		self.box10.add_widget(self.text3)
		self.box10.add_widget(label5)
		self.box10.add_widget(scr1)
		self.box10.add_widget(box7)
		box6.add_widget(btn17)
		box6.add_widget(btn18)
		self.box5.add_widget(self.btn16)
		self.box5.add_widget(self.label7)
		self.box5.add_widget(widget1)
		self.box5.add_widget(self.label8)
		self.box5.add_widget(box6)
		self.box5.add_widget(self.btn19)
		self.float1.add_widget(self.box5)
		self.float1.add_widget(self.text2)
		box4 = BoxLayout(orientation = "vertical")#Переход на страницу
		btn14 = Button(text = "Confirm", on_press = self.go_pg_conf)
		label1 = Label(text = "Enter the number of page, \nthat you want go to", halign = "center")
		anc1 = AnchorLayout(anchor_x = "center", anchor_y = "center")
		self.text1 = TextInput(size_hint = (None, None), size = (Window.width * 0.1, Window.width * 0.1), multiline = False)
		self.btn15 = Button(text = "Back", on_press = self.ok)
		anc1.add_widget(self.text1)
		box4.add_widget(btn14)
		box4.add_widget(label1)
		box4.add_widget(anc1)
		box4.add_widget(self.btn15)
		self.pop1 = Popup(title = "", content = box4, size_hint = (0.7, None), size = (Window.width * 0.7, Window.width * 0.7))
		self.box3 = BoxLayout(orientation = "vertical")#Поиск
		grid2 = GridLayout(cols = 2, rows = 4, size_hint = (1, 0.8))
		self.btn5 = Button(text = "Search by name", on_press = self.open_pop)
		self.btn6 = Button(text = "Search by number", on_press = self.open_pop)
		self.btn7 = Button(text = "Search by tags", on_press = self.open_pop)
		self.btn8 = Button(text = "Search by group", on_press = self.open_pop)
		self.btn9 = Button(text = "Search by \ndate added", on_press = self.click)
		self.btn10 = Button(text = "Search by word \nor phrase", on_press = self.open_pop)
		self.btn11 = Button(text = "Search by color \nof background", on_press = self.collor)
		self.btn12 = Button(text = "Search by \ncolor of font", on_press = self.collor)
		self.btn13 = Button(text = "Back", size_hint = (1, 0.2), on_press = self.click)
		grid2.add_widget(self.btn5)
		grid2.add_widget(self.btn6)
		grid2.add_widget(self.btn7)
		grid2.add_widget(self.btn8)
		grid2.add_widget(self.btn9)
		grid2.add_widget(self.btn10)
		grid2.add_widget(self.btn11)
		grid2.add_widget(self.btn12)
		self.box3.add_widget(grid2)
		self.box3.add_widget(self.btn13)
		self.mainbox = BoxLayout(orientation = "vertical")#mainbox
		self.float3 = FloatLayout()#menu
		self.box1 = BoxLayout(orientation = "vertical")
		self.btn1 = Button(text = "Add", size_hint = (1, 0.1), on_press = self.spec_open)
		box2 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.1))
		btn2 = Button(text = "<---", on_press = self.minus_pg)
		self.btn14 = Button(text = "Go to defenite page", on_press = self.open_pop)
		btn3 = Button(text = "--->", on_press = self.plus_pg)
		self.label2 = Label(text = "1", size_hint = (1, 0.025))
		widget1 = Widget(size_hint = (1, 0.65))
		box36 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.65), size = (Window.width, Window.height * 0.65), pos = (0, Window.height * 0.125))
		box37 = BoxLayout(orientation = "vertical")
		box38 = BoxLayout(orientation = "vertical")
		box39 = BoxLayout(orientation = "horizontal", size_hint = (1, 0.65), size = (Window.width, Window.height * 0.65), pos = (0, Window.height * 0.125))
		box40 = BoxLayout(orientation = "vertical")
		box41 = BoxLayout(orientation = "vertical")
		self.boxes1 = [ ]
		self.boxes2 = [ ]
		self.buttons1 = [ ]
		self.buttons2 = [ ]
		for i in range(0, 8):
			var4 = BoxLayout(orientation = "vertical", padding = Window.width * (1 / 216))
			var5 = BoxLayout(orientation = "vertical", padding = Window.width * (1 / 54))
			self.boxes2.append(var4)
			self.boxes1.append(var5)
			self.buttons2.append(Button(background_normal = "", background_down = ""))
			self.buttons1.append(Button(background_normal = "", halign = "center", on_press = self.look_note))
			if i % 2 == 0:
				box37.add_widget(var4)
				box40.add_widget(var5)
			else:
				box38.add_widget(var4)
				box41.add_widget(var5)
		self.label3 = Label(text = "1", size_hint = (1, 0.025))
		self.btn4 = Button(text = "Search", size_hint = (1, 0.1), on_press = self.click)
		box36.add_widget(box37)
		box36.add_widget(box38)
		box39.add_widget(box40)
		box39.add_widget(box41)
		box2.add_widget(btn2)
		box2.add_widget(self.btn14)
		box2.add_widget(btn3)
		self.box1.add_widget(self.btn1)
		self.box1.add_widget(box2)
		self.box1.add_widget(self.label2)
		self.box1.add_widget(widget1)
		self.box1.add_widget(self.label3)
		self.box1.add_widget(self.btn4)
		self.float3.add_widget(self.box1)
		self.float3.add_widget(box36)
		self.float3.add_widget(box39)
		self.mainbox.add_widget(self.float3)
		self.orient_lbl()
		self.cl_opn = {self.btn4 : self.box3, self.btn13 : self.float3, self.btn1 : self.float1, self.btn19 : self.float3, self.btn28 : self.float2, self.btn31 : self.float1, self.btn30 : self.float1, self.btn20 : self.float2, self.btn22 : self.float2, self.btn16 : self.float3, self.btn39 : self.float3, self.btn37 : self.float5, self.btn43 : self.float4, self.btn33 : self.float1, self.btn40 : self.float4, self.btn48 : self.float3, self.btn9 : self.box55, self.btn69 : self.box3, self.btn36 : self.float3, self.btn73 : self.box61, self.btn74 : self.box61}#Variables
		self.cl_cls = {self.btn4 : self.float3, self.btn13 : self.box3, self.btn1 : self.float3, self.btn19 : self.float1, self.btn28 : self.float1, self.btn31 : self.float2, self.btn30 : self.float2, self.btn20 : self.float1, self.btn22 : self.float1, self.btn16 : self.float1, self.btn39 : self.float4, self.btn37 : self.float4, self.btn43 : self.float5, self.btn33 : self.float2, self.btn40 : self.float5, self.btn48 : self.float4, self.btn9 : self.box3, self.btn69 : self.box55, self.btn36 : self.float4, self.btn73 : self.float4, self.btn74 : self.float4}
		self.ok_cls = {self.btn15 : self.pop1, self.btn25 : self.pop2, self.btn26 : self.pop3, self.btn29 : self.pop4, self.btn35 : self.pop5, self.btn49 : self.pop6, self.btn51 : self.pop7, self.btn53 : self.pop8, self.btn56 : self.pop9, self.btn59 : self.pop10, self.btn71 : self.pop13, self.btn61 : self.pop11}
		self.addpg = [self.text2, self.box10]
		self.popopen = {self.btn14 : self.pop1, self.btn23 : self.pop2, self.btn30 : self.pop4, self.btn45 : self.pop2, self.btn47 : self.pop4, self.btn38 : self.pop6, self.btn5 : self.pop7, self.btn6 : self.pop8, self.btn7 : self.pop9, self.btn8 : self.pop10, self.btn10 : self.pop13, self.btn57 : self.pop11, self.btn50 : self.pop7, self.btn52 : self.pop8, self.btn54 : self.pop9, self.btn60 : self.pop10, self.btn70 : self.pop13}
		self.check_text = {}
		self.potok = ""
		self.tag_for_del = ""
		self.var2 = "Closed"
		self.one_tags = [ ]
		self.search_tags_add = [ ]
		self.result_note = [ ]
		self.tag_for_check = [ ]
		self.search_back_var = ""
		self.group_choose_var = "No"
		self.inf_widg = [self.label26, self.label27, self.label28, self.label29, self.label30, self.label31, self.label32, self.label33, self.label34, self.label35, self.label36, self.label37, self.label38, self.label39, self.label40, self.label21, self.label22, self.label23, self.label24, self.label25, self.btn46]
		self.for_tag_add = ""
		self.tag_box = {self.btn23 : self.box11, self.btn45 : self.box43}
		self.tag_size = {self.btn23 : 0.08, self.btn45 : 0.06}
		self.what_tag_del = ""
		return self.mainbox
	def click(self, instance):
		self.mainbox.remove_widget(self.cl_cls[instance])
		self.mainbox.add_widget(self.cl_opn[instance])
	def open_pop(self, instance):
		self.popopen[instance].open()
	def ok(self, instance):
		self.ok_cls[instance].dismiss()
	def go_add(self, instance):
		self.label7.text = str(3 - int(self.label7.text))
		self.label8.text = str(3 - int(self.label8.text))
		self.float1.remove_widget(self.addpg[1 - (int(self.label7.text) - 1)])
		self.float1.add_widget(self.addpg[int(self.label7.text) - 1])
	def tag_conf(self, instance):
		if self.text_check(self.text4) == 0:
			return
		elif self.text4.text in self.one_tags:
			self.label10.text = "There is already \ntag with such name"
			self.pop3.open()
		else:
			self.pop2.dismiss()
			self.one_tags.append(self.text4.text)
			self.tag_box[self.for_tag_add].remove_widget(self.for_tag_add)
			if len(self.text4.text) >= 6:
				var27 = len(self.text4.text) * 28
			else:
				var27 = 168
			sup_btn = Button(text = self.text4.text, size_hint = (None, None), size = (var27, Window.height * self.tag_size[self.for_tag_add]), on_press = self.tag_ask_del)
			try:
				sup_btn.color = self.note_fnt_col[self.note_names.index(self.var_for_inf)][0] / 255, self.note_fnt_col[self.note_names.index(self.var_for_inf)][1] / 255, self.note_fnt_col[self.note_names.index(self.var_for_inf)][2] / 255, self.note_fnt_col[self.note_names.index(self.var_for_inf)][3] / 100
			except:
				pass
			if self.what_tag_del == self.btn1:
				sup_btn.color = (1, 1, 1, 1)
			self.tag_box[self.for_tag_add].add_widget(sup_btn)
			self.tag_box[self.for_tag_add].add_widget(self.for_tag_add)
			self.text4.text = ""
	def tag_ask_del(self, instance):
		self.label20.text = "Do you really want \nto delete tag \"" + instance.text + "\"?"
		self.pop5.open()
		self.tag_for_del = instance
	def tag_del(self, instance):
		self.pop5.dismiss()
		self.one_tags.remove(self.tag_for_del.text)
		if self.what_tag_del == self.btn1:
			self.box11.remove_widget(self.tag_for_del)
		else:
			self.box43.remove_widget(self.tag_for_del)
	def group(self, instance):
		if self.var2 == "Closed":
			self.float1.add_widget(self.box15)
			self.var2 = "Opened"
		elif self.var2 == "Opened":
			self.float1.remove_widget(self.box15)
			self.var2 = "Closed"
	def thr1(self):
		while not self.potok == "Stop":
			self.label12.text = str(int(self.slider1.value // 1))
			self.label13.text = str(int(self.slider2.value // 1))
			self.label14.text = str(int(self.slider3.value // 1))
			self.label15.text = str(int(self.slider4.value // 1))
			self.btn32.background_color = (self.slider1.value / 255, self.slider2.value / 255, self.slider3.value / 255, self.slider4.value / 100)
	def collor(self, instance):
		self.col_var = instance
		if instance == self.btn28:
			self.pop4.dismiss()
		if instance == self.btn11 or instance == self.btn12 or instance == self.btn58:
			self.mainbox.remove_widget(self.box3)
			self.mainbox.add_widget(self.float2)
			if instance == self.btn58:
				self.pop10.dismiss()
		elif self.what_tag_del == self.btn1:
			self.click(instance)
		else:
			self.mainbox.remove_widget(self.float5)
			self.mainbox.add_widget(self.float2)
		self.slider1.value = instance.background_color[0] * 255
		self.slider2.value = instance.background_color[1] * 255
		self.slider3.value = instance.background_color[2] * 255
		self.slider4.value = instance.background_color[3] * 100
		if instance == self.btn11 or instance == self.btn12 or instance == self.btn58:
			self.slider1.value = 88
			self.slider2.value = 88
			self.slider3.value = 88
			self.slider4.value = 100
		self.potok = ""
		threading.Thread(target = self.thr1, args = "").start()
	def col_conf(self, instance):
		self.result_note.clear()
		if self.col_var != self.btn11 and self.col_var != self.btn12 and self.col_var != self.btn58:
			self.potok = "Stop"
			self.col_var.background_color = (self.slider1.value / 255, self.slider2.value / 255, self.slider3.value / 255, self.slider4.value / 100)
		if self.col_var == self.btn11:
			self.search_back_var = "Color"
			if not (self.slider1.value // 1, self.slider2.value // 1, self.slider3.value // 1, self.slider4.value // 1) in self.note_bg_col:
				self.label10.text = "Note with such backgound \n color does not exist"
				self.pop3.open()
			else:
				self.potok = "Stop"
				for i in range(0, len(self.note_bg_col)):
					if (self.slider1.value // 1, self.slider2.value // 1, self.slider3.value // 1, self.slider4.value // 1) == self.note_bg_col[i]:
						self.result_note.append(self.note_names[i])
				self.mainbox.remove_widget(self.float2)
				self.show_result()
		elif self.col_var == self.btn12:
			self.search_back_var = "Color"
			if not (self.slider1.value // 1, self.slider2.value // 1, self.slider3.value // 1, self.slider4.value // 1) in self.note_fnt_col:
				self.label10.text = "Note with such color \nof font does not exist"
				self.pop3.open()
			else:
				self.potok = "Stop"
				for i in range(0, len(self.note_fnt_col)):
					if (self.slider1.value // 1, self.slider2.value // 1, self.slider3.value // 1, self.slider4.value // 1) == self.note_fnt_col[i]:
						self.result_note.append(self.note_names[i])
				self.mainbox.remove_widget(self.float2)
				self.show_result()
		elif self.col_var == self.btn58:
			self.search_back_var = "Color"
			if not (self.slider1.value // 1, self.slider2.value // 1, self.slider3.value // 1, self.slider4.value // 1) in self.group_col:
				self.label10.text = "Group with such \ncolor does not exist"
				self.pop3.open()
			else:
				self.potok = "Stop"
				for i in range(0, len(self.group_col)):
					if (self.slider1.value // 1, self.slider2.value // 1, self.slider3.value // 1, self.slider4.value // 1) == self.group_col[i]:
						self.result_note.append(self.note_names[i])
				self.mainbox.remove_widget(self.float2)
				self.show_result()
		elif self.what_tag_del == self.btn1:
			self.click(instance)
		else:
			self.mainbox.remove_widget(self.float2)
			self.mainbox.add_widget(self.float5)
		if self.col_var == self.btn28:
			self.pop4.open()
	def col_back(self, instance):
		self.potok = "Stop"
		self.mainbox.remove_widget(self.float2)
		if self.col_var == self.btn11 or self.col_var == self.btn12 or self.col_var == self.btn58:
			self.mainbox.add_widget(self.box3)
		elif self.what_tag_del == self.btn1:
			self.mainbox.add_widget(self.float1)
		else:
			self.mainbox.add_widget(self.float5)
		if self.col_var == self.btn28:
			self.pop4.open()
		if self.col_var == self.btn58:
			self.pop10.open()
	def group_conf(self, instance):
		if self.text_check(self.text5) == 0:
			return
		elif self.text5.text in self.names_groups:
			self.label10.text = "There is already \ngroup with such name"
			self.pop3.open()
		elif (int((self.btn28.background_color[0] * 255) // 1), int((self.btn28.background_color[1] * 255) // 1), int((self.btn28.background_color[2] * 255) // 1), int((self.btn28.background_color[3] * 100) // 1)) in self.one_col_group:
			self.label10.text = "There is already group with \nsuch background color"
			self.pop3.open()
		else:
			self.names_groups.append(self.text5.text)
			self.one_col_group.append(self.btn28.background_color)
			self.pop4.dismiss()
			self.box14.remove_widget(self.btn30)
			self.box14.add_widget(Button(text = self.text5.text, size_hint = (None, None), size = (Window.width / 2, Window.height * 0.1), background_color = self.btn28.background_color, background_normal = "", on_press = self.final_group))
			self.box14.add_widget(self.btn30)
			self.box44.remove_widget(self.btn47)
			if len(self.text5.text) >= 6:
				var31 = len(self.text5.text) * 28
			else:
				var31 = 168
			help_btn = Button(text = self.text5.text, size_hint = (None, None), size = (var31, Window.height * 0.06), background_color = self.btn28.background_color, background_normal = "", on_press = self.group_in_inf)
			try:
				help_btn.color = self.note_fnt_col[self.note_names.index(self.var_for_inf)][0] / 255, self.note_fnt_col[self.note_names.index(self.var_for_inf)][1] / 255, self.note_fnt_col[self.note_names.index(self.var_for_inf)][2] / 255, self.note_fnt_col[self.note_names.index(self.var_for_inf)][3] / 1001
			except:
				pass
			if self.what_tag_del == self.btn1:
				help_btn.color = (1, 1, 1, 1)
			self.box44.add_widget(help_btn)
			self.box44.add_widget(self.btn47)
			self.text5.text = ""
			self.btn28.background_color = (88 / 255, 88 / 255, 88 / 255, 1)
	def final_group(self, instance):
		self.btn21.text = instance.text
		self.btn21.background_color = instance.background_color
		self.float1.remove_widget(self.box15)
		self.var2 = "Closed"
		self.group_choose_var = "Yes"
	def add_conf(self, instance):
		if self.text2.text == "":
			self.label10.text = "You didn't enter \ncontent of note"
			self.pop3.open()
		elif self.text3.text == "":
			self.label10.text = "You didn't enter \nname of note"
			self.pop3.open()
		elif self.text_check(self.text3) == 0 or self.text_check(self.text2) == 0:
			return
		elif self.text3.text in self.note_names:
			self.label10.text = "Note with such a \nname already exist"
			self.pop3.open()
		elif self.group_choose_var == "No":
			self.label10.text = "You didn't choose \ngroup of note"
			self.pop3.open()
		else:
			self.note_names.append(self.text3.text)
			self.tags.append(self.one_tags)
			self.groups.append(self.btn21.text)
			self.note_bg_col.append((int((self.btn22.background_color[0] * 255) // 1), int((self.btn22.background_color[1] * 255) // 1), int((self.btn22.background_color[2] * 255) // 1), int((self.btn22.background_color[3] * 100) // 1)))
			self.note_fnt_col.append((int((self.btn20.background_color[0] * 255) // 1), int((self.btn20.background_color[1] * 255) // 1), int((self.btn20.background_color[2] * 255) // 1), int((self.btn20.background_color[3] * 100) // 1)))
			self.note_cont.append(self.text2.text)
			self.group_col.append((int((self.btn21.background_color[0] * 255) // 1), int((self.btn21.background_color[1] * 255) // 1), int((self.btn21.background_color[2] * 255) // 1), int((self.btn21.background_color[3] * 100) // 1)))
			var7 = time.localtime(time.time())
			self.note_time.append([time.strftime("%H", var7), time.strftime("%M", var7), time.strftime("%S", var7), time.strftime("%d", var7), time.strftime("%m", var7), time.strftime("%Y", var7)])
			var3 = (len(self.note_names) % 8) - 1
			var17 = Button(size_hint = (None, None), size = (Window.width * 0.45, Window.height * (0.81 / 4)), background_normal = "", halign = "center", on_press = self.look_note)
			self.result_btn1.append(var17)
			var18 = Button(size_hint = (None, None), size = (Window.width * 0.48, Window.height * (0.864 / 4)), background_normal = "")
			self.result_btn2.append(var18)
			var19 = AnchorLayout(size_hint = (None, None), size = (Window.width * 0.5, Window.height * (0.9 / 4)), anchor_x = "center", anchor_y = "center")
			self.result_anc.append(var19)
			var19.add_widget(var18)
			var19.add_widget(var17)
			if len(self.note_names) % 2 != 0:
				self.result_box.append(BoxLayout(orientation = "horizontal", size_hint = (1, None), size = (Window.width, Window.height * (0.9 / 4))))
			self.text2.text = ""
			self.btn22.background_color = (88 / 255, 88 / 255, 88 / 255, 1)
			self.btn20.background_color = (88 / 255, 88 / 255, 88 / 255, 1)
			self.btn21.background_color = (88 / 255, 88 / 255, 88 / 255, 1)
			self.btn21.text = "Choose group"
			for i in self.box11.walk():
				self.box11.remove_widget(i)
			self.box11.add_widget(self.btn23)
			self.text3.text = ""
			self.group_choose_var = "No"
			self.click(instance)
			if (len(self.note_names) - 1) % 8 == 0 and len(self.note_names) != 1:
				self.label2.text = str(int(self.label2.text) + 1)
				self.label3.text = str(int(self.label3.text) + 1)
			self.orient_lbl()
			self.save()
	def orient_lbl(self):
		for i in range(0, 8):
			self.boxes1[i].clear_widgets()
			self.boxes2[i].clear_widgets()
		var6 = ""
		if int(self.label2.text) * 8 > len(self.note_names):
			var6 = len(self.note_names)
		else:
			var6 = int(self.label2.text) * 8
		for i in range (((int(self.label2.text) * 8) - 8), var6):
			self.buttons2[i % 8].background_color = (self.group_col[i][0] / 255, self.group_col[i][1] / 255, self.group_col[i][2] / 255, self.group_col[i][3] / 100)
			self.boxes2[i % 8].add_widget(self.buttons2[i % 8])
			self.buttons1[i % 8].text = "№" + str(i + 1) + "\n" + self.note_names[i]
			self.buttons1[i % 8].background_color = [self.note_bg_col[i][0] / 255, self.note_bg_col[i][1] / 255, self.note_bg_col[i][2] / 255, self.note_bg_col[i][3] / 100]
			self.buttons1[i % 8].color = [self.note_fnt_col[i][0] / 255, self.note_fnt_col[i][1] / 255, self.note_fnt_col[i][2] / 255, self.note_fnt_col[i][3] / 100]
			self.boxes1[i % 8].add_widget(self.buttons1[i % 8])
	def go_pg_conf(self, instance):
		if self.text1.text == "":
			self.label10.text = "You didn't enter anything"
			self.pop3.open()
		else:
			try:
				var7 = int(self.text1.text)
				if var7 < 1 or var7 > (((len(self.note_names) - 1) // 8) + 1):
					self.label10.text = "Page with such a number doesn't exist"
					self.pop3.open()
				else:
					self.pop1.dismiss()
					self.label2.text = self.text1.text
					self.label3.text = self.text1.text
					self.text1.text = ""
					self.orient_lbl()
			except:
				self.label10.text = "You have to enter number"
				self.pop3.open()
	def plus_pg(self, instance):
		if len(self.note_names) > 8:
			self.label2.text = str(int(self.label2.text) + 1)
			self.label3.text = str(int(self.label3.text) + 1)
			if self.label2.text == str(((len(self.note_names) - 1) // 8) + 2):
				self.label2.text = "1"
				self.label3.text = "1"
			self.orient_lbl()
	def minus_pg(self, instance):
		if len(self.note_names) > 8:
			self.label2.text = str(int(self.label2.text) - 1)
			self.label3.text = str(int(self.label3.text) - 1)
			if self.label2.text == "0":
				self.label2.text = str(((len(self.note_names) - 1) // 8) + 1)
				self.label3.text = str(((len(self.note_names) - 1) // 8) + 1)
			self.orient_lbl()
	def look_note(self, instance):
		self.float4.clear_widgets()
		if instance in self.buttons1:
			self.float4.add_widget(self.btn36)
			self.float4.add_widget(self.btn39)
			self.mainbox.remove_widget(self.float3)
		else:
			self.float4.add_widget(self.btn73)
			self.float4.add_widget(self.btn74)
			self.mainbox.remove_widget(self.box61)
		self.float4.add_widget(self.box36)
		self.mainbox.add_widget(self.float4)
		self.var_for_inf = instance.text.split("\n")[1]
		self.text6.text = self.note_cont[self.note_names.index(instance.text.split("\n")[1])]
		self.text6.background_color = (self.note_bg_col[self.note_names.index(instance.text.split("\n")[1])][0] / 255, self.note_bg_col[self.note_names.index(instance.text.split("\n")[1])][1] / 255, self.note_bg_col[self.note_names.index(instance.text.split("\n")[1])][2] / 255, self.note_bg_col[self.note_names.index(instance.text.split("\n")[1])][3] / 100)
		self.text6.foreground_color = (self.note_fnt_col[self.note_names.index(instance.text.split("\n")[1])][0] / 255, self.note_fnt_col[self.note_names.index(instance.text.split("\n")[1])][1] / 255, self.note_fnt_col[self.note_names.index(instance.text.split("\n")[1])][2] / 255, self.note_fnt_col[self.note_names.index(instance.text.split("\n")[1])][3] / 100)
		self.what_tag_del = instance

	def open_inf_note(self, instance):
		self.one_tags = self.tags[self.note_names.index(self.var_for_inf)].copy()
		for i in self.inf_widg:
			i.color = (self.note_fnt_col[self.note_names.index(self.var_for_inf)][0] / 255,
					   self.note_fnt_col[self.note_names.index(self.var_for_inf)][1] / 255,
					   self.note_fnt_col[self.note_names.index(self.var_for_inf)][2] / 255,
					   self.note_fnt_col[self.note_names.index(self.var_for_inf)][3] / 100)
		self.btn44.background_color = (self.note_bg_col[self.note_names.index(self.var_for_inf)][0] / 255,
									   self.note_bg_col[self.note_names.index(self.var_for_inf)][1] / 255,
									   self.note_bg_col[self.note_names.index(self.var_for_inf)][2] / 255,
									   self.note_bg_col[self.note_names.index(self.var_for_inf)][3] / 100)
		self.btn41.background_color = (self.note_bg_col[self.note_names.index(self.var_for_inf)][0] / 255,
									   self.note_bg_col[self.note_names.index(self.var_for_inf)][1] / 255,
									   self.note_bg_col[self.note_names.index(self.var_for_inf)][2] / 255,
									   self.note_bg_col[self.note_names.index(self.var_for_inf)][3] / 100)
		self.btn42.background_color = (self.note_fnt_col[self.note_names.index(self.var_for_inf)][0] / 255,
									   self.note_fnt_col[self.note_names.index(self.var_for_inf)][1] / 255,
									   self.note_fnt_col[self.note_names.index(self.var_for_inf)][2] / 255,
									   self.note_fnt_col[self.note_names.index(self.var_for_inf)][3] / 100)
		self.text7.text = self.var_for_inf
		self.label27.text = str(self.note_names.index(self.var_for_inf) + 1)
		self.btn46.text = self.groups[self.note_names.index(self.var_for_inf)]
		self.btn46.background_color = (self.group_col[self.note_names.index(self.var_for_inf)][0] / 255,
									   self.group_col[self.note_names.index(self.var_for_inf)][1] / 255,
									   self.group_col[self.note_names.index(self.var_for_inf)][2] / 255,
									   self.group_col[self.note_names.index(self.var_for_inf)][3] / 100)
		for i in range(0, 6):
			self.inf_widg[i + 9].text = self.note_time[self.note_names.index(self.var_for_inf)][i]
		self.box43.clear_widgets()
		for i in self.one_tags:
			if len(i) >= 6:
				var29 = len(i) * 28
			else:
				var29 = 168
			self.box43.add_widget(
				Button(text=i, size_hint=(None, None), size=(var29, Window.height * 0.06), on_press=self.tag_ask_del,
					   color=(self.note_fnt_col[self.note_names.index(self.var_for_inf)][0] / 255,
							  self.note_fnt_col[self.note_names.index(self.var_for_inf)][1] / 255,
							  self.note_fnt_col[self.note_names.index(self.var_for_inf)][2] / 255,
							  self.note_fnt_col[self.note_names.index(self.var_for_inf)][3] / 100)))
		self.btn45.color = (self.note_fnt_col[self.note_names.index(self.var_for_inf)][0] / 255,
							self.note_fnt_col[self.note_names.index(self.var_for_inf)][1] / 255,
							self.note_fnt_col[self.note_names.index(self.var_for_inf)][2] / 255,
							self.note_fnt_col[self.note_names.index(self.var_for_inf)][3] / 100)
		self.box43.add_widget(self.btn45)
		self.click(instance)
		for i in self.box44.walk():
			i.color = (self.note_fnt_col[self.note_names.index(self.var_for_inf)][0] / 255,
					   self.note_fnt_col[self.note_names.index(self.var_for_inf)][1] / 255,
					   self.note_fnt_col[self.note_names.index(self.var_for_inf)][2] / 255,
					   self.note_fnt_col[self.note_names.index(self.var_for_inf)][3] / 100)

	def difer_tag(self, instance):
		self.for_tag_add = instance
		self.open_pop(instance)

	def spec_open(self, instance):
		self.one_tags = []
		self.what_tag_del = instance
		self.float1.clear_widgets()
		self.float1.add_widget(self.box5)
		self.float1.add_widget(self.text2)
		self.label7.text = "1"
		self.label8.text = "1"
		self.click(instance)

	def group_in_inf(self, instance):
		if instance == self.btn46:
			self.float5.remove_widget(instance)
			self.float5.add_widget(self.scr4)
		else:
			self.btn46.text = instance.text
			self.btn46.background_color = instance.background_color
			self.float5.remove_widget(self.scr4)
			self.float5.add_widget(self.btn46)

	def inf_conf(self, instance):
		if self.text_check(self.text7) == 0:
			return
		elif self.text7.text in self.note_names and self.var_for_inf != self.text7.text:
			self.label10.text = "Note with such a \nname already exist"
			self.pop3.open()
		else:
			self.note_names[self.note_names.index(self.var_for_inf)] = self.text7.text
			self.var_for_inf = self.text7.text
			var9 = self.note_names.index(self.var_for_inf)
			self.note_fnt_col[var9] = (
			int(self.btn42.background_color[0] * 255) // 1, int(self.btn42.background_color[1] * 255) // 1,
			int(self.btn42.background_color[2] * 255) // 1, int(self.btn42.background_color[3] * 100) // 1)
			self.note_bg_col[var9] = (
			int(self.btn41.background_color[0] * 255) // 1, int(self.btn41.background_color[1] * 255) // 1,
			int(self.btn41.background_color[2] * 255) // 1, int(self.btn41.background_color[3] * 100) // 1)
			self.groups[var9] = self.btn46.text
			self.group_col[var9] = (
			int(self.btn46.background_color[0] * 255) // 1, int(self.btn46.background_color[1] * 255) // 1,
			int(self.btn46.background_color[2] * 255) // 1, int(self.btn46.background_color[3] * 100) // 1)
			self.tags[var9] = self.one_tags
			self.text6.background_color = self.btn41.background_color
			self.text6.foreground_color = self.btn42.background_color
			self.click(instance)
			self.orient_lbl()
			self.save()

	def note_ask_del(self, instance):
		self.label41.text = "Do you really want \nto delete note \"" + self.var_for_inf + "\"?"
		self.open_pop(instance)

	def note_del(self, instance):
		if len(self.note_names) % 8 == 1 and self.label2.text == str(
				(len(self.note_names) // 8) + 1) and self.label2.text != "1":
			self.label2.text = str(int(self.label2.text) - 1)
			self.label3.text = self.label2.text
		var10 = self.note_names.index(self.var_for_inf)
		self.note_fnt_col.remove(self.note_fnt_col[var10])
		self.note_bg_col.remove(self.note_bg_col[var10])
		self.groups.remove(self.groups[var10])
		self.group_col.remove(self.group_col[var10])
		self.tags.remove(self.tags[var10])
		self.note_time.remove(self.note_time[var10])
		self.note_cont.remove(self.note_cont[var10])
		self.note_names.remove(self.var_for_inf)
		self.pop6.dismiss()
		self.orient_lbl()
		self.click(instance)
		self.save()

	def open_scr_date(self, instance):
		if self.date_values[self.date_btn.index(instance)] == 0:
			self.date_box2[self.date_btn.index(instance)].add_widget(self.date_scrs[self.date_btn.index(instance)])
		else:
			self.date_box2[self.date_btn.index(instance)].remove_widget(self.date_scrs[self.date_btn.index(instance)])
		self.date_values[self.date_btn.index(instance)] = 1 - self.date_values[self.date_btn.index(instance)]

	def date_choose(self, instance):
		for i in range(0, 6):
			if instance in self.date_btn2[i]:
				var15 = i
		self.date_btn[var15].text = instance.text
		self.date_box2[var15].remove_widget(self.date_scrs[var15])
		self.date_values[var15] = 0

	def search_by_name(self, instance):
		self.search_back_var = instance
		self.result_note.clear()
		if self.text8.text == "":
			self.label10.text = "You didn't enter anything"
			self.pop3.open()
		elif not self.text8.text in self.note_names:
			self.label10.text = "Note with such a name doesn't exist"
			self.pop3.open()
		else:
			self.result_note.append(self.text8.text)
			self.text8.text = ""
			self.pop7.dismiss()
			self.mainbox.remove_widget(self.box3)
			self.show_result()

	def search_by_number(self, instance):
		self.search_back_var = instance
		self.result_note.clear()
		if self.text9.text == "":
			self.label10.text = "You didn't enter anything"
			self.pop3.open()
		else:
			try:
				var10 = int(self.text9.text)
				if var10 < 1 or var10 > len(self.note_names):
					self.label10.text = "The note with such a number doesn't exist"
					self.pop3.open()
				else:
					self.result_note.append(self.note_names[var10 - 1])
					self.text9.text = ""
					self.mainbox.remove_widget(self.box3)
					self.pop8.dismiss()
					self.show_result()
			except:
				self.label10.text = "You have to enter a number"
				self.pop3.open()

	def tag_search_add(self, instance):
		help_text = TextInput(size_hint=(1, None), size=(Window.width * 0.7, Window.height * 0.7 * 0.1),
							  multiline=False)
		self.search_tags_add.append(help_text)
		self.box52.add_widget(help_text)

	def search_by_tags(self, instance):
		self.search_back_var = instance
		self.result_note.clear()
		self.tag_for_check.clear()
		var11 = "No"
		for i in self.search_tags_add:
			if i.text != "":
				self.tag_for_check.append(i.text)
				var11 = "Yes"
		if var11 == "No":
			self.label10.text = "You have to enter \nat least one tag"
			self.pop3.open()
		else:
			for a in range(0, len(self.tags)):
				var12 = "Yes"
				for b in self.tag_for_check:
					if not b in self.tags[a]:
						var12 = "No"
				if var12 == "Yes":
					self.result_note.append(self.note_names[a])
			if len(self.result_note) == 0:
				self.label10.text = "There is no note \nwith such a tags"
				self.pop3.open()
			else:
				self.box52.clear_widgets()
				self.search_tags_add.clear()
				self.pop9.dismiss()
				self.mainbox.remove_widget(self.box3)
				self.show_result()

	def search_name_group(self, instance):
		self.search_back_var = instance
		self.result_note.clear()
		if self.text10.text == "":
			self.label10.text = "You didn't enter anything"
			self.pop3.open()
		else:
			for i in range(0, len(self.groups)):
				if self.text10.text == self.groups[i]:
					self.result_note.append(self.note_names[i])
			if len(self.result_note) == 0:
				self.label10.text = "There is no note \nwith such a group"
				self.pop3.open()
			else:
				self.text10.text = ""
				self.mainbox.remove_widget(self.box3)
				self.pop10.dismiss()
				self.pop11.dismiss()
				self.show_result()

	def search_by_date(self, instance):
		self.search_back_var = instance
		self.result_note.clear()
		self.date_for_check = self.note_names.copy()
		one_date = ["", "", "", "", "", ""]
		for i in self.date_btn:
			if i.text != "":
				one_date[self.date_btn.index(i)] = i.text
		for a in range(0, len(self.note_time)):
			var14 = "Yes"
			for b in one_date:
				if b != "":
					if b != self.note_time[a][one_date.index(b)]:
						var14 = "No"
				else:
					continue
			if var14 == "Yes":
				self.result_note.append(self.note_names[a])
		var13 = "No"
		for i in self.date_btn:
			if i.text != "":
				var13 = "Yes"
		if var13 == "No":
			self.label10.text = "You have to choose anything"
			self.pop3.open()
		elif len(self.result_note) == 0:
			self.label10.text = "There is no note that \nmathes your requirements"
			self.pop3.open()
		else:
			for i in self.date_btn:
				i.text = ""
			self.mainbox.remove_widget(self.box55)
			self.show_result()

	def search_by_word(self, instance):
		self.search_back_var = instance
		self.result_note.clear()
		for i in range(0, len(self.note_cont)):
			if self.note_cont[i].find(self.text11.text) != -1:
				self.result_note.append(self.note_names[i])
		if self.text11.text == "":
			self.label10.text = "You didn't enter anything"
			self.pop3.open()
		elif len(self.result_note) == 0:
			self.label10.text = "There is no note \nthat have such a phrase"
			self.pop3.open()
		else:
			self.text11.text = ""
			self.pop13.dismiss()
			self.mainbox.remove_widget(self.box3)
			self.show_result()

	def show_result(self):
		self.mainbox.add_widget(self.box61)
		self.box63.clear_widgets()
		for i in range(0, len(self.result_note)):
			if i % 2 == 0:
				self.var16 = self.result_box[int(i / 2)]
				self.var16.clear_widgets()
				self.box63.add_widget(self.var16)
			self.var16.add_widget(self.result_anc[i])
			self.result_btn2[i].background_color = self.group_col[self.note_names.index(self.result_note[i])][0] / 255, \
												   self.group_col[self.note_names.index(self.result_note[i])][1] / 255, \
												   self.group_col[self.note_names.index(self.result_note[i])][2] / 255, \
												   self.group_col[self.note_names.index(self.result_note[i])][3] / 100
			var20 = self.result_btn1[i]
			var20.text = "№" + str(self.note_names.index(self.result_note[i]) + 1) + "\n" + self.result_note[i]
			var20.color = (self.note_fnt_col[self.note_names.index(self.result_note[i])][0] / 255,
						   self.note_fnt_col[self.note_names.index(self.result_note[i])][1] / 255,
						   self.note_fnt_col[self.note_names.index(self.result_note[i])][2] / 255,
						   self.note_fnt_col[self.note_names.index(self.result_note[i])][3] / 100)
			var20.background_color = (self.note_bg_col[self.note_names.index(self.result_note[i])][0] / 255,
									  self.note_bg_col[self.note_names.index(self.result_note[i])][1] / 255,
									  self.note_bg_col[self.note_names.index(self.result_note[i])][2] / 255,
									  self.note_bg_col[self.note_names.index(self.result_note[i])][3] / 100)

	def search_back(self, instance):
		self.mainbox.remove_widget(self.box61)
		if self.search_back_var == "Color":
			self.mainbox.add_widget(self.float2)
			self.potok = ""
		elif self.search_back_var == self.btn62:
			self.mainbox.add_widget(self.box55)
		else:
			self.mainbox.add_widget(self.box3)
			self.open_pop(self.search_back_var)
			if self.search_back_var == self.btn60:
				self.pop11.open()

	def my_join(self, x, y):
		z = ""
		for i in x:
			z = z + str(i) + str(y)
		w = z[0:(len(z) - len(str(y)))]
		return w

	def save(self):
		file = open("notebook.txt", "w", encoding = "utf-8")
		if len(self.note_names) != 0:
			var_list1 = []
			for i in self.tags:
				var_list1.append(self.my_join(i, "鬮"))
			var_list2 = []
			for i in self.group_col:
				var_list2.append(self.my_join(i, "鬮"))
			var_list3 = []
			for i in self.note_time:
				var_list3.append(self.my_join(i, "鬮"))
			var_list4 = []
			for i in self.note_bg_col:
				var_list4.append(self.my_join(i, "鬮"))
			var_list5 = []
			for i in self.note_fnt_col:
				var_list5.append(self.my_join(i, "鬮"))
			file.write(self.my_join(
				[self.my_join(self.note_names, "釁"), self.my_join(var_list1, "釁"), self.my_join(self.groups, "釁"),
				 self.my_join(var_list2, "釁"), self.my_join(var_list3, "釁"), self.my_join(var_list4, "釁"),
				 self.my_join(var_list5, "釁"), self.my_join(self.note_cont, "釁")], "﷽"))
		file.close()

	def open_note_conf(self, instance):
		if self.text_check(self.text6) == 0:
			return
		else:
			self.note_cont[self.note_names.index(self.var_for_inf)] = self.text6.text
			self.click(instance)
			self.save()

	def text_check(self, k):
		var = k.text
		if var == "":
			self.label10.text = "You didn't enter anything"
			self.pop3.open()
			return 0
		elif "﷽" in var:
			self.label10.text = "You can enter symbol \"﷽\" nowhere"
			self.pop3.open()
			return 0
		elif "釁" in var:
			self.label10.text = "You can enter symbol \"釁\" nowhere"
			self.pop3.open()
			return 0
		elif "鬮" in self.text6.text:
			self.label10.text = "You can enter symbol \"鬮\" nowhere"
			self.pop3.open()
			return 0
		else:
			return 1
Wind().run()
