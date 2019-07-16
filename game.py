# -*- coding: utf8 -*- 

import os
import random
from termcolor import cprint
from colorama import init
from linker.linker import styleInput

while True:
	init()

	mods = os.listdir('mods')

	col = random.randint(1, 7)

	color_to_number = {
	
		1: 'red',
		2: 'green',
		3: 'yellow',
		4: 'blue',
		5: 'magenta',
		6: 'cyan',
		7: 'white',

	}

#cprint('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■', color_to_number[col])
#cprint('■   ■■■■■■    ■■■■■■   ■■     ■■  ■■      ■     ■■■     ■', color_to_number[col])
#cprint('■  ■      ■  ■      ■  ■ ■   ■ ■  ■ ■     ■    ■   ■    ■', color_to_number[col])
#cprint('■  ■         ■      ■  ■  ■ ■  ■  ■  ■    ■    ■   ■    ■', color_to_number[col])
#cprint('■   ■■■■■■   ■      ■  ■   ■   ■  ■   ■   ■   ■     ■   ■', color_to_number[col])
#cprint('■         ■  ■      ■  ■       ■  ■    ■  ■   ■■■■■■■   ■', color_to_number[col])
#cprint('■  ■      ■  ■      ■  ■       ■  ■     ■ ■  ■       ■  ■', color_to_number[col])
#cprint('■   ■■■■■■    ■■■■■■   ■       ■  ■      ■■  ■       ■  ■', color_to_number[col])
#cprint('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■', color_to_number[col])
	a = styleInput('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n■   ■■■■■■    ■■■■■■   ■■     ■■  ■■      ■     ■■■     ■\n■  ■      ■  ■      ■  ■ ■   ■ ■  ■ ■     ■    ■   ■    ■\n■  ■         ■      ■  ■  ■ ■  ■  ■  ■    ■    ■   ■    ■\n■   ■■■■■■   ■      ■  ■   ■   ■  ■   ■   ■   ■     ■   ■\n■         ■  ■      ■  ■       ■  ■    ■  ■   ■■■■■■■   ■\n■  ■      ■  ■      ■  ■       ■  ■     ■ ■  ■       ■  ■\n■   ■■■■■■    ■■■■■■   ■       ■  ■      ■■  ■       ■  ■\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■', str(color_to_number[col]), 'Моды', 'Настройки')

	if a == 1:
		a = styleInput('Моды:', 'no', mods)

		os.system('python\python.exe mods/{}/main.py'.format(mods[a-1]))