# -*- coding: UTF8 -*- 

import os
import sys
import keyboard
sys.path.append(os.path.abspath('linker'))
from linker import install
from linker import styleInput
from linker import endGame
from linker import setEndCount	

setEndCount(4)

def var1():
	endGame('Самая обычная заброшка. Но как только ты направляешь свой взгляд вверх, ты замечаешь падающего прямо на тебя человека. Ты не успеваешь отойти, поэтому тебя резко бросает прямо на камни, что и убивает тебя.', 2)

a = styleInput('Ты проснулся в своей комнате.', 'no', '1. Уснуть', '2. Выйти из комнаты')

if a == 1:
	endGame('Ты немного поспал и чувствуешь бодрость.', 1)
elif a == 2:
	a = styleInput('Ты подошёл к двери, но та опередила тебя и открылась сама. За дверью заброшенное здание. Везде обломки какого-то заброшенного дома, всё изрисованно графити, но, что самое интересное, оно примыкает к твоей комнате, как быдто бы она часть этого здания.', 'no', '1. Осмотреться', '2. Войти обратно')

	if a == 1:
		var1()	

	elif a == 2:
		a = styleInput('Двери в комнату больше нет, но есть висящий на стене топор.', 'no', '1. Взять топор', '2. Осмотреться')

		if a == 1:
			a = styleInput('Ты берёшь топор. Сзади тебя слышится звук падающих камней.', 'no', '1. Обернуться', '2. Осмотреть топор')

			if a == 1:
				a = styleInput('Ты оборачиваешься и видишь, что на тебя летит человеческое тело.', 'no', '1. Разрубить его', '2. Увернуться')

				#if a == 1:

				if a == 2:
					endGame('У тебя не получается увернуться и тело падает прямо на тебя, сильно ударив об пол.', 4)

			elif a == 2:
				endGame('Это самый обычный пожарный топор. Пока ты его осматриваешь, звуки сзади становятся громче. В конечном итоге, тебя что-то раздавило.', 3)

		elif a == 2:
			var1()

#print('mod or game is corrupted')
