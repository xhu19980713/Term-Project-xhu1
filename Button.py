def startButtton(self):
	gap=51
	width=326
	height=300
	startX=100
	startY=350
	self.musicToSheetBtn=[startX,startY,width,height,self.lightBlue,\
	                     "musicToSheet"]
	self.sheetToMusicBtn=[startX+gap+width,startY,width,height,self.lightBlue,\
	                     "sheetToMusic"]
	self.musicMakingBtn=[startX+gap*2+width*2,startY,width,height,self.lightBlue,\
	                     "musicMaking"]
	self.startBtnList=[self.musicToSheetBtn,self.sheetToMusicBtn,self.musicMakingBtn]

def musicToSheetButton(self):
	#circle buttons: circle(Surface, color, pos, radius, width=0)
	cx1=400
	cy1=400
	gap=80
	radius=175
	self.importFile=[self.lightBlue,cx1,cy1,radius]
	self.recordMusic=[self.lightBlue,self.width-cx1,cy1,radius]
	self.musicToSheetBtnList=[self.importFile,self.recordMusic]

def sheetToMusicButton(self):
	pass 

def musicMakingButton(self):
	pass 

def allButton(self):
	startButtton(self)
	musicMakingButton(self)
	musicToSheetButton(self)
	sheetToMusicButton(self)

['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'holomdl2assets', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'microsoftofficepreviewfont', 'msofficesymbolregular', 'msofficesymbol', 'msofficesymbolsemibold', 'msofficesymbolsemilight', 'msofficesymbolextralight', 'agencyfb', 'algerian', 'bookantiqua', 'arialrounded', 'baskervilleoldface', 'bauhaus93', 'bell', 'bernardcondensed', 'bodoni', 'bodoniblack', 'bodonicondensed', 'bodonipostercompressed', 'bookmanoldstyle', 'bradleyhanditc', 'britannic', 'berlinsansfb', 'berlinsansfbdemi', 'broadway', 'brushscript', 'bookshelfsymbol7', 'californianfb', 'calisto', 'castellar', 'centuryschoolbook', 'centaur', 'century', 'chiller', 'colonna', 'cooperblack', 'copperplategothic', 'curlz', 'dubai', 'dubaimedium', 'dubairegular', 'elephant', 'engravers', 'erasitc', 'erasdemiitc', 'erasmediumitc', 'felixtitling', 'forte', 'franklingothicbook', 'franklingothicdemi', 'franklingothicdemicond', 'franklingothicheavy', 'franklingothicmediumcond', 'freestylescript', 'frenchscript', 'footlight', 'garamond', 'gigi', 'gillsans', 'gillsanscondensed', 'gillsansultracondensed', 'gillsansultra', 'gloucesterextracondensed', 'gillsansextcondensed', 'centurygothic', 'goudyoldstyle', 'goudystout', 'harlowsolid', 'harrington', 'haettenschweiler', 'hightowertext', 'imprintshadow', 'informalroman', 'blackadderitc', 'edwardianscriptitc', 'kristenitc', 'jokerman', 'juiceitc', 'kunstlerscript', 'widelatin', 'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 'lucidasansregular', 'lucidasansroman', 'lucidasanstypewriterregular', 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'magneto', 'maiandragd', 'maturascriptcapitals', 'mistral', 'modernno20', 'monotypecorsiva', 'niagaraengraved', 'niagarasolid', 'ocraextended', 'oldenglishtext', 'onyx', 'msoutlook', 'palacescript', 'papyrus', 'parchment', 'perpetua', 'perpetuatitling', 'playbill', 'poorrichard', 'pristina', 'rage', 'ravie', 'msreferencesansserif', 'msreferencespecialty', 'rockwellcondensed', 'rockwell', 'rockwellextra', 'script', 'showcardgothic', 'snapitc', 'stencil', 'twcen', 'twcencondensed', 'twcencondensedextra', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'wingdings2', 'wingdings3', 'extra', 'icomoon', 'antonio', 'antonioregular', 'square721', 'parkavenue', 'staccato222', 'cataneo', 'blackletter686', 'calligraphic421', 'misterearl', 'olddreadfulno7', 'holidaypi', 'jokermanletplain10', 'johnhandyletplain10', 'orangeletplain10', 'academyengravedletplain10', 'universityromanletplain10', 'victorianletplain10', 'milanolet', 'smudgerletplain10', 'westwoodletplain10', 'ruachletplain10', 'rageletplain10', 'labambaletplain10', 'quixleyletplain10', 'pumpdemiletplain10', 'tirantisolidletplain10', 'mekanikletplain', 'onestrokescriptletplain', 'highlightletplain10', 'odessaletplain10', 'scruffletplain10', 'helvlightregular', 'lato', 'loveloblack', 'lovelolinelight', 'lovelolinebold', 'arvo', 'eastseadokdoregular']

