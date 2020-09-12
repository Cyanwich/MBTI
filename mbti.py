import spacy
nlp = spacy.load("./mbti profile model")
def MBTIDoc(txtfile="./A.txt"):
	file = open(txtfile)
	text = file.read()
	
	lm = spacy.load('en')
	lmtarget = lm(text)
	lmstring = ''
	for word in lmtarget:
		lmstring = lmstring + word.lemma_ + ' '
	text = lmstring.lower()
	
	doc = nlp(text)
	MBTIResults = doc.cats
	#print(text)

	if MBTIResults['INTROVERTED'] > 0.5:
		print('I___')
	else:
		print('E___')
	if MBTIResults['INTUTIVE'] > 0.5:
		print('_N__')
	else:
		print('_S__')
	if MBTIResults['THINKING'] > 0.5:
		print('__T_')
	else:
		print('__F_')
	if MBTIResults['JUDGEMENTAL'] > 0.5:
		print('___J')
	else:
		print('___P')
	
	XXxx = max([MBTIResults['EN'],MBTIResults['IS'],MBTIResults['ES'],MBTIResults['IN']])
	XxXx = max([MBTIResults['EF'],MBTIResults['IT'],MBTIResults['ET'],MBTIResults['IF']])
	XxxX = max([MBTIResults['EP'],MBTIResults['EJ'],MBTIResults['IP'],MBTIResults['IJ']])
	xXXx = max([MBTIResults['NT'],MBTIResults['SF'],MBTIResults['ST'],MBTIResults['NF']])
	xXxX = max([MBTIResults['SP'],MBTIResults['SJ'],MBTIResults['NP'],MBTIResults['NJ']])
	xxXX = max([MBTIResults['TJ'],MBTIResults['TP'],MBTIResults['FJ'],MBTIResults['FP']])
		
	if XXxx == MBTIResults['EN']:
		print('EN__')
	elif XXxx == MBTIResults['IS']:
		print('IS__')
	elif XXxx == MBTIResults['ES']:
		print('ES__')
	elif XXxx == MBTIResults['IN']:
		print('IN__')
	
	if XxXx == MBTIResults['EF']:
		print('E_F_')
	elif XxXx == MBTIResults['IT']:
		print('I_T_')
	elif XxXx == MBTIResults['ET']:
		print('E_T_')
	elif XxXx == MBTIResults['IF']:
		print('I_F_')
	
	if XxxX == MBTIResults['EP']:
		print('E__P')
	elif XxxX == MBTIResults['EJ']:
		print('E__J')
	elif XxxX == MBTIResults['IP']:
		print('I__P')
	elif XxxX == MBTIResults['IJ']:
		print('I__J')
	
	if xXXx == MBTIResults['NT']:
		print('_NT_')
	elif xXXx == MBTIResults['SF']:
		print('_SF_')
	elif xXXx == MBTIResults['ST']:
		print('_ST_')
	elif xXXx == MBTIResults['NF']:
		print('_NF_')
	
	if xXxX == MBTIResults['SP']:
		print('_S_P')
	elif xXxX == MBTIResults['SJ']:
		print('_S_J')
	elif xXxX == MBTIResults['NP']:
		print('_N_P')
	elif xXxX == MBTIResults['NJ']:
		print('_N_J')
	
	if xxXX == MBTIResults['TJ']:
		print('__TJ')
	elif xxXX == MBTIResults['TP']:
		print('__TP')
	elif xxXX == MBTIResults['FJ']:
		print('__FJ')
	elif xxXX == MBTIResults['FP']:
		print('__FP')
		
		
def MBTI(text):
	lm = spacy.load('en')
	lmtarget = lm(text)
	lmstring = ''
	for word in lmtarget:
		lmstring = lmstring + word.lemma_ + ' '
	text = lmstring.lower()
	
	doc = nlp(text)
	MBTIResults = doc.cats
	#print(MBTIResults)

	if MBTIResults['INTROVERTED'] > 0.5:
		print('I___')
	else:
		print('E___')
	if MBTIResults['INTUTIVE'] > 0.5:
		print('_N__')
	else:
		print('_S__')
	if MBTIResults['THINKING'] > 0.5:
		print('__T_')
	else:
		print('__F_')
	if MBTIResults['JUDGEMENTAL'] > 0.5:
		print('___J')
	else:
		print('___P')
	
	XXxx = max([MBTIResults['EN'],MBTIResults['IS'],MBTIResults['ES'],MBTIResults['IN']])
	XxXx = max([MBTIResults['EF'],MBTIResults['IT'],MBTIResults['ET'],MBTIResults['IF']])
	XxxX = max([MBTIResults['EP'],MBTIResults['EJ'],MBTIResults['IP'],MBTIResults['IJ']])
	xXXx = max([MBTIResults['NT'],MBTIResults['SF'],MBTIResults['ST'],MBTIResults['NF']])
	xXxX = max([MBTIResults['SP'],MBTIResults['SJ'],MBTIResults['NP'],MBTIResults['NJ']])
	xxXX = max([MBTIResults['TJ'],MBTIResults['TP'],MBTIResults['FJ'],MBTIResults['FP']])
		
	if XXxx == MBTIResults['EN']:
		print('EN__')
	elif XXxx == MBTIResults['IS']:
		print('IS__')
	elif XXxx == MBTIResults['ES']:
		print('ES__')
	elif XXxx == MBTIResults['IN']:
		print('IN__')
	
	if XxXx == MBTIResults['EF']:
		print('E_F_')
	elif XxXx == MBTIResults['IT']:
		print('I_T_')
	elif XxXx == MBTIResults['ET']:
		print('E_T_')
	elif XxXx == MBTIResults['IF']:
		print('I_F_')
	
	if XxxX == MBTIResults['EP']:
		print('E__P')
	elif XxxX == MBTIResults['EJ']:
		print('E__J')
	elif XxxX == MBTIResults['IP']:
		print('I__P')
	elif XxxX == MBTIResults['IJ']:
		print('I__J')
	
	if xXXx == MBTIResults['NT']:
		print('_NT_')
	elif xXXx == MBTIResults['SF']:
		print('_SF_')
	elif xXXx == MBTIResults['ST']:
		print('_ST_')
	elif xXXx == MBTIResults['NF']:
		print('_NF_')
	
	if xXxX == MBTIResults['SP']:
		print('_S_P')
	elif xXxX == MBTIResults['SJ']:
		print('_S_J')
	elif xXxX == MBTIResults['NP']:
		print('_N_P')
	elif xXxX == MBTIResults['NJ']:
		print('_N_J')
	
	if xxXX == MBTIResults['TJ']:
		print('__TJ')
	elif xxXX == MBTIResults['TP']:
		print('__TP')
	elif xxXX == MBTIResults['FJ']:
		print('__FJ')
	elif xxXX == MBTIResults['FP']:
		print('__FP')
		


