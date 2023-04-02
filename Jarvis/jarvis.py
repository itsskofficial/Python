#Jarvis
import pyttsx3,datetime,wikipedia,webbrowser,os,smtplib;
import speechRecognition as sr;
engine=pyttsx3.init("sapi5");
voices=engine.getProperty('voices');
engine.setProperty('voice',voices[0].id);

def speak(audio):
	engine.say(audio);
	engine.runAndWait();

def wishMe():
	hour=int(datetime.now().hour);
	if hour>=0 and hour<12:
		speak("Good Morning Sir!");
	elif hour>12 and hour<18:
		speak("Good Afternoon Sir!");
	elif hour>18 and hour<21:
		speak("Good Evening Sir!");

def intro():
	speak("How can I help you Sir?");

def takeCommand():
	"""It takes microphone input from the user and returns string output"""
	with sr.Microphone() as source:
		print("Listening...");
	sr.Recogniser.pause_threshold=1;	
	audio=sr.Recognizer.listen(source);
	
	try:
		print ("Recognizing...");
		query=r.recognize_google(audio,language='en-in');
		print (f"User said: {query}\n");
	except Exception as e:
		print (e);
		speak("Say that again please...");
		return 'None';
	return query;

def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587);
	server.ehlo();
	server.starttls();
	server.login('your email','your pass');
	server.send('recipients email',to,content);
	
def poweroff():
	speak("Powering off Sir.....");
	quit();

def wikipedia():
	speak("Searching Wikipedia...");
			query=query.replace("wikipedia"," ");
			results=wikipedia.summary(query,sentences=3);
			speak("According to Wikipedia...");	
			print (results);
			speak(results);

def open_websites(query):
	query_split=query.split(' ');
	open_index=query_split.index('open');
	website_index=open_index+1;
	website=query_split[website_index];
	speak(f"Opening  {website}.com...");
	webbrowser.open(f'{website}.com');

def open_apps(query):
	query_split=query.split(' ');
	open_index=query_split.index('open');
	app_index=open_index+1;
	app=query_split[app_index];
	speak(f"Opening  {app}...");
	appPath=os.path.abspath(f'{app}');
	os.startfile(appPath);

def play_random_music():
	music_dir=os.path.abspath('Music');
	songs=os.listdir(music_dir);
	no_of_songs=len(songs);
	speak("Playing song sir...");
	os.startfile(os.path.join(music_dir,songs[random.randint(0,no_of_songs)]):
	
def play_song(query):
	query_split=query.split(' ');
	song_index=query_split.index('song');
	songname_index=song_index+1;
	songname=query_split[songname_index];
	speak(f"Playing  {songname}...");
	music_dir=os.path.abspath('Music');
	songs=os.listdir(music_dir);
	if songname in songs:
		for song in songs:
			if song==songname:
				play_song_index=songs.index(song);
				os.startfile(os.path.join(music_dir,songs[play_song_index]);
			else:
				continue;
	else:
		speak("Song not found Sir!");
	
if __name__='__main__':
	wishMe();
	while True:
		query=takeCommand().lower();
		#Logic for executing tasks on query
		if 'wikipedia' in query:
			wikipedia();
		elif 'open' in query:
			speak("Website or App Sir?");				
			answer=takecommand();
			if answer='website':
				open_websites(query);
			elif answer='app':
				open_apps(query);		
		elif 'play music' in query:
			play_random_music();			

		elif 'play song' in query:
			play_song(query);

		elif 'the time' in query:
			strTime=datetime.datetime.now().strftime("%H:%M:%S");
			speak(f"Sir, the time is {strTime}");
		
		elif 'open visual studio code' in query:
			filePath="Put the path here";
			os.startfile(filePath);
		
		elif 'email to sk' in query:
			try:
				speak("What should I say to SK?");
				content=takeCommand();
				to="recipients email";
				sendEmail(to,content);
				speak("Email has been sent Sir!");
			except Exception as e:
				print (e);
				speak("Sir I can't send this email");
		
		elif 'power off' in query:
			poweroff();
									
										
	
	

	