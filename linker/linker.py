# -*- coding: UTF8 -*-

import os
from termcolor import cprint
import keyboard
import time
from colorama import init

fullend = 0

var = 1 
exvar = '1'

def uparrow():

	global var

	time.sleep(0.1)
	var -= 1
	exvar = str(var)
	print('up')

def preload():
	keyboard.add_hotkey('up', uparrow)

def install(module):
	try:
		installer = open('linker/install_modules.bat', 'r')
	
		sr = ''

		for i in installer:
			if hasattr(i, 'python/Scripts/pip.exe install'):
				sr = i

		temp = installer.read()

		installer.close()

		new = temp.replace(sr, '@echo off\n{}/pip.exe install {}\necho done >> {}\nexit'.format(os.path.abspath('python/Scripts'), module, os.path.abspath('linker/exec.txt')))

		installer = open('linker/install_modules.bat', 'w')
		installer.write(new)
		installer.close()

		os.system('start {}'.format(os.path.abspath('linker/install_modules.bat')))

		ex = open('linker/exec.txt', 'r')

		while ex.read() == '':
			pass

		ex.close()
		ex = open('linker/exec.txt', 'w')
		ex.write('')
		ex.close()

		return 0

	except:
		return 1

def styleInput(msg, get_color, *treets):
	init()	

	var = 1 
	exvar = '1'

	try:
		while True:
			a = os.system('cls')
		
			if a != 0:
				os.system('clear')

			else:
				pass

			if get_color != 'no':
				cprint('{}\n'.format(msg), get_color)

			else:
				print('{}\n'.format(msg))
	
			cnt = 0

			for i in treets:
				cnt += 1
				if cnt == var:
					cprint(i, 'grey', 'on_white')

				else:
					print(i)

			print('\nCommand: {}'.format(exvar))
			
			key = keyboard.read_key()

			#if key == 'up' and var > 1:
				#time.sleep(0.1)
				#var -= 1
				#exvar = str(var)

			if key == 'down' and var < len(treets):
				time.sleep(0.1)
				var += 1
				exvar = str(var)

			elif key == 'enter':
				time.sleep(0.1)
				break

			elif key == 'backspace':
				exvar = exvar[:-1]
				time.sleep(0.1)

			elif key != 'up' and key != 'down':
				exvar += key
				time.sleep(0.1)

	except ImportError:
		os.system('clear')

		if get_color != 'no':
			cprint('{}\n'.format(msg), get_color)

		else:
			print('{}\n'.format(msg))

		for i in treets:
			print(i)

		exvar = input('\nCommand: ')

	if exvar == 'exit':
		raise ImportError('exit')

	return var

def endGame(text, ending):
	a = os.system('cls')
	
	if a != 0:
		os.system('clear')

	print(text)
	print('Концовка {} из {}'.format(ending, fullend))
	
	a = os.system('pause')

	if a != 0:
		os.system('clear')
		print(text)
		print('Концовка {} из {}'.format(ending, fullend))
		
		os.system('./linker/linux/buttonAwait.sh')

	time.sleep(0.2)

def setEndCount(num):
	global fullend
	fullend = num
