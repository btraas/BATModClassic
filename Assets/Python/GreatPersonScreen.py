## Sid Meier's Civilization 4
from CvPythonExtensions import *
import PyHelpers
import CvUtil
import ScreenInput
import CvScreenEnums
import string
import BugPath
import GreatPersonEvents

# ScS  import the new file that we created with the .bat file
# ScS  import os.path to deal with checking whether files exist.

PyPlayer = PyHelpers.PyPlayer
PyInfo = PyHelpers.PyInfo

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

# ScS Variable to snage the art Path from the .bat file.

class GreatPersonScreen:
	"Great Person Screen"
	
	def __init__(self):
                
		self.X_SCREEN = 255
		self.Y_SCREEN = 40
		self.W_SCREEN = 515
		self.H_SCREEN = 570
		self.Z_BACKGROUND = -1.1
		self.Z_CONTROLS = self.Z_BACKGROUND - 0.2
		self.DZ = -0.2
		self.iMarginSpace = 15		
		self.Y_TITLE = self.Y_SCREEN + 25		
		self.W_PORTRAIT = 460
		self.H_PORTRAIT = 460				
		self.X_EXIT = self.X_SCREEN + self.W_SCREEN/2 - 66
		self.Y_EXIT = self.Y_SCREEN + self.H_SCREEN - 50
		self.W_EXIT = 120
		self.H_EXIT = 30		
		self.PICTURE_BASE = "Art/GreatPeople/%s.dds"
				
	
	def interfaceScreen (self, iData):

		d = GreatPersonEvents.g_dict
		pUnit, iPlayer, pCity = d.pop(iData)
		player = gc.getPlayer(iPlayer)
		
		CvUtil.pyPrint("Great Person Popup: Name:<%s> Player:<%s> City:<%s>"%(pUnit.getNameNoDesc(), player.getName(), pCity.getName()))
		
		szArtPath = BugPath.getModDir() + '\\Assets\Art\GreatPeople\\'
		CvUtil.pyPrint("GreatPersonScreen: szArtPath: " + szArtPath)
				
		szPersonName = pUnit.getNameNoDesc()
						 	
		# szUnitType will be UNIT_PROPHET, UNIT_MERCHANT, UNIT_ARTIST, etc.
		szUnitType = gc.getUnitInfo(pUnit.getUnitType()).getType()
				
		# if the name is the empty string, then create a new, generic name from the unit type.
		if szPersonName == "" :
			szPersonName = self.type2str(szUnitType)
		
		szImageName = szPersonName
				
		# if there is a file in the GreatPeople directory with the name, we'll load it.		
		szImageFilename = szArtPath + szImageName + ".dds"		
		CvUtil.pyPrint("Great Person Popup: Image Filename: " + szImageFilename)
		#CyInterface().addImmediateMessage(str(szImageFilename), "")
		
		if not BugPath.isfile(szImageFilename):			
			#if not, load the great "type of person" file
			szImageName = self.type2str(szUnitType)
			szImageFilename = szArtPath + szImageName + ".dds"
			
			if not BugPath.isfile(szImageFilename):
				#if not, load the great person file
				szImageName = "Great Person"
				
		szPicturePath = str(self.PICTURE_BASE %(szImageName))
		#CvUtil.pyPrint("Great Person Popup: Picture Path: " + szPicturePath)

		screen = CyGInterfaceScreen( "GreatPersonScreen", CvScreenEnums.ERA_MOVIE_SCREEN)
		screen.addPanel("GreatPersonPanel", "", "", true, true,
		self.X_SCREEN, self.Y_SCREEN, self.W_SCREEN, self.H_SCREEN, PanelStyles.PANEL_STYLE_MAIN)		
		screen.showWindowBackground(True)
		screen.setSound("AS2D_NEW_ERA")
		screen.showScreen(PopupStates.POPUPSTATE_MINIMIZED, False)
		screen.setDimensions(screen.centerX(0), screen.centerY(0), 1024, 768)
		screen.setRenderInterfaceOnly(False)					
                
		# Header...
		szHeader = localText.getText("TXT_KEY_MISC_GP_BORN", (szPersonName, pCity.getName()))  #ScS
		szHeaderId = "GreatPersonTitleHeader"
		screen.setText(szHeaderId, "Background", szHeader, CvUtil.FONT_CENTER_JUSTIFY,
		self.X_SCREEN + self.W_SCREEN / 2, self.Y_TITLE, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
		screen.setButtonGFC("GreatPersonExit", localText.getText("TXT_KEY_MAIN_MENU_OK", ()), "", self.X_EXIT, self.Y_EXIT, self.W_EXIT, self.H_EXIT, WidgetTypes.WIDGET_CLOSE_SCREEN, -1, -1, ButtonStyles.BUTTON_STYLE_STANDARD )
		screen.addDDSGFC("GreatPersonPortrait", szPicturePath, self.X_SCREEN + 27, self.Y_SCREEN + 50, self.W_PORTRAIT, self.H_PORTRAIT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		return 0
	
	def type2str(self, szUnitType):
		szTemp = szUnitType[5:]
		if szTemp[:6] == "GREAT_":
			szTemp = szTemp[6:]
		return "Great " + szTemp.capitalize() 
		
	# Will handle the input for this screen...
	def handleInput (self, inputClass):
		return 0

	def update(self, fDelta):
		return

