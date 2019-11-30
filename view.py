import datetime
import journal_functions as j
x	=	datetime.datetime.now()
month	=	input('enter month num:')
if month	==	'':
	month	=	x.strftime('%m')
date	=	input('enter date:')
if date	==	'':
	date	=	x.strftime('%d')
year	=	input('enter year')
if year	==	'':
	year	=	x.strftime('%Y')
theFile	=	'day_entry_files/' + year + '-' + month + '-' + date+ '.txt'
with open(theFile) as f:
	allLines	=	f.readlines()
emp	=	''

allEntries	=	[]
indicator	=	1
jline	=	-90
for line in allLines:
	if	indicator	==	1:
		mode	=	'cut'
	else:
		mode	=	'add'
	if	line	==	'\n'	or	allLines[0]	==	line	or	jline	==	1:
		dline	=	line
	else:
		dline	=	j.dec(line)
		dline	=	emp.join(dline)
	if	line	==	'===================================================\n':
		indicator	=	1
		jline	=	0
		continue
	elif	mode	==	'add':
		indicator	=	0
		allEntries[-1]	=	allEntries[-1]	+	dline
	else:
		indicator	=	0
		allEntries.append(dline)
	jline	=	jline	+	1
separatingLine	=	'-----------------------------------------------------------------------\n'
beginningLine	=	'/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n'
allEntries[0]	=	beginningLine+'All entries on '+allEntries[0]
for item in allEntries:
	print(item)
	print(separatingLine)
