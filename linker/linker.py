import os
from termcolor import cprint
import keyboard
import time
from colorama import init

fullend = 0
inputSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z', 'u', 'i', 'v']

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
	exvar = ''


	while True:
		os.system('cls')
		
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

		if key == 'up' and var > 1:
			var -= 1
			exvar = str(var)

		elif key == 'down' and var < len(treets):
			var += 1
			exvar = str(var)

		elif key == 'space':
			time.sleep(0.1)
			break

		elif hasattr(inputSymbols, key):
			print('exvar')
			exvar += key

	return exvar

def endGame(text, ending):
	os.system('cls')
	print(text)
	print('Концовка {} из {}'.format(ending, fullend))
	os.system('pause')
	time.sleep(0.2)

def setEndCount(num):
	global fullend
	fullend = num