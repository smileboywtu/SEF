# -*- coding: utf-8 -*-

"""

	print the color output

	TEXT COLOR	CODE	TEXT STYLE	CODE	BACKGROUND COLOR	CODE
		Black	30		No effect	0			Black			40
		Red		31		Bold		1			Red				41
		Green	32		Underline	2			Green			42
		Yellow	33		Negative1	3			Yellow			43
		Blue	34		Negative2	5			Blue			44
		Purple	35								Purple			45
		Cyan	36								Cyan			46
		White	37								White			47


"""

class Colors:

	FBASE= 30
	BBASE= 40
	SBASE = 0
	STYLES = 'NORMAL', 'BOLD', 'UNDERLINE', 'NEGATIVE1', 'NEGATIVE2'
	COLORS = 'BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'PURPLE', 'CYAN', 'WHITE'

	@staticmethod
	def colors():
		return colors

	@staticmethod
	def styles():
		return styles

	@staticmethod
	def colorize(msg, forground, backgroud='WHITE', style='NORMAL'):
		"""colorize the message for output usage

		"""
		style = style.upper()
		forground = forground.upper()
		backgroud = backgroud.upper()

		start = '\033['
		end = '\033[0m'

		scode = Colors.STYLES.index(style) + Colors.SBASE
		fcode = Colors.COLORS.index(forground) + Colors.FBASE
		bcode = Colors.COLORS.index(backgroud) + Colors.BBASE

		code = ';'.join([str(scode), str(fcode), str(bcode)]) + 'm'

		return  start + code + msg + end


if __name__ == '__main__':

	msg = 'hello, colorful terminal.'

	print Colors.colorize(msg, forground='RED', backgroud='WHITE', style='BOLD')
	print Colors.colorize(msg, forground='CYAN', backgroud='BLACK', style='BOLD')
