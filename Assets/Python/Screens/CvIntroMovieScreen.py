## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005

## Intro Movie Mod for The BAT Mod and Better BAT AI - June 2011 by Lemon Merchant, with unwitting assistance by Dale :)
## (Original idea by Dale, I just made it compatible with BAT - LM :P  )

from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class CvIntroMovieScreen:
	"Intro Movie Screen"
	bMovieState = 0
	def interfaceScreen (self):
		
		self.currentMovie = "ART_DEF_MOVIE_2K_INTRO"
		self.X_SCREEN = 0
		self.Y_SCREEN = 0
		self.W_SCREEN = 1024
		self.H_SCREEN = 768
		self.Y_TITLE = 12
		self.BORDER_HEIGHT = 100
		
		self.X_EXIT = 410
		self.Y_EXIT = 326
		
		game = CyGame()
		if ( game.isNetworkMultiPlayer() or game.isPitbossHost()):
			return
		
		self.createMovieScreen(self.currentMovie)
	
	def createMovieScreen(self, movieArtDef):
	
		if CyUserProfile().getGraphicOption(GraphicOptionTypes.GRAPHICOPTION_NO_MOVIES):
			return
		
		# Create a new screen, called IntroMovieScreen, using the file CvIntroMovieScreen.py for input
		screen = CyGInterfaceScreen( "IntroMovieScreen", CvScreenEnums.INTRO_MOVIE_SCREEN )
		screen.setDimensions(screen.centerX(0), screen.centerY(0), -1, -1)
		screen.setRenderInterfaceOnly(True)
		screen.showWindowBackground( False )
		screen.setShowFor( 0 )
		
		# Show the screen
		screen.showScreen(PopupStates.POPUPSTATE_IMMEDIATE, False)		
		
		# Play the movie
		movieFilePath = CyArtFileMgr().getMovieArtInfo(movieArtDef).getPath()
		screen.playMovie( movieFilePath, -1, -1, -1, -1, 0)
		
	def createLogoScreen(self):
		return

	def closeScreen(self):
		screen = CyGInterfaceScreen( "IntroMovieScreen", CvScreenEnums.INTRO_MOVIE_SCREEN )
		screen.hideScreen()
		
	def hideScreen(self):
		screen = CyGInterfaceScreen( "IntroMovieScreen", CvScreenEnums.INTRO_MOVIE_SCREEN )
		screen.hideScreen()
	
	# Will handle the input for this screen...
	def handleInput (self, inputClass):
		screen = CyGInterfaceScreen( "IntroMovieScreen", CvScreenEnums.INTRO_MOVIE_SCREEN )
		if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_MOVIE_DONE or inputClass.getNotifyCode() == NotifyCode.NOTIFY_CLICKED or inputClass.getNotifyCode() == NotifyCode.NOTIFY_CHARACTER):
			if (inputClass.getNotifyCode() != NotifyCode.NOTIFY_MOVIE_DONE):
				setNoIntroMovie(true)
			
		
		return self.closeScreen()

	def update(self, fDelta):
		return

