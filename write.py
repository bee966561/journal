import datetime
import journal_functions as j

today	=	datetime.datetime.now()

today	=	today.strftime("%F")

todayFile	=	today	+	'.txt'
journalEntry	=	[]
i	=	''
emp	=	''
try:
	with open(todayFile) as f:
		True
except FileNotFoundError:
	with open(todayFile,'w') as m:
		m.write(f"Date: {today}\n")
		j.end_entry(m)
		m.write('\n')
while	True:
	i	=	input('Make an Entry:\n')
	if	i	==	'end':
		break
	i	=	j.enc(i)
	i	=	emp.join(i)
	journalEntry.append(i)
with open(todayFile,'a') as myFile:
	j.time_now(myFile)
	for	sentence	in	journalEntry:
		myFile.write(f"\n{sentence}\n")
	j.end_entry(myFile)
	myFile.write('\n')

