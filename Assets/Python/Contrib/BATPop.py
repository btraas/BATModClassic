## Sid Meier's Civilization 4
## Copyright Firaxis Games 2006

## BAT Starting Popup.  Ported to a BUG module by Lemon Merchant.
## Original code by The_J


from CvPythonExtensions import *
import CvUtil
import CvScreensInterface
import PyHelpers
import Popup as PyPopup
import sys
import CvAdvisorUtils
import CvTechChooser
import CvIntroMovieScreen

gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer
PyInfo = PyHelpers.PyInfo




def onGameStart(argsList):
	'Called at the start of the game'

# display mod's intro movie
	introMovie = CvIntroMovieScreen.CvIntroMovieScreen()
	introMovie.interfaceScreen()
	
###starting popup - begin
	if (gc.getGame().getGameTurnYear() == gc.getDefineINT("START_YEAR") and not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ADVANCED_START)):
		for iPlayer in range(gc.getMAX_PLAYERS()):
			player = gc.getPlayer(iPlayer)
			if (player.isAlive() and player.isHuman()):
				
				popupInfo = CyPopupInfo()
				popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_TEXT)
				szBody = localText.getColorText("TXT_KEY_MOD_HEADER", (), gc.getInfoTypeForString("COLOR_YELLOW")) + "\n\n" + localText.getText("TXT_KEY_MOD_TEXT_1", ()) + "\n" + localText.getText("TXT_KEY_MOD_TEXT_2", ()) + "\n\n" + localText.getText("TXT_KEY_MOD_TEXT_3", ()) + "\n" + localText.getText("TXT_KEY_MOD_TEXT_4", ()) + "\n\n" + localText.getText("TXT_KEY_MOD_TEXT_5", ())
				popupInfo.setText(szBody)
				popupInfo.addPopup(iPlayer)                                        
###starting popup - end 

                                  

	CvAdvisorUtils.resetNoLiberateCities()