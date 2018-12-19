# Sid Meier's Civilization 4
# Copyright Firaxis Games 2006
# 
# GreatPersonEvents

from CvPythonExtensions import *
import CvUtil
import CvEventManager
import sys
import CvDebugTools
import PyHelpers
import GreatPersonScreen
import RandomNameUtils


gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
g_bGreatPersonModFeaturesEnabled = true
g_iCount = 0     # autoincrement global used as the primary key for dictionary
g_dict = dict()  # holds information transferred from here to GreatPersonScreen.py


		
def onGreatPersonBorn(argsList):
	'Great Person Born'
	pUnit, iPlayer, pCity = argsList
	pPlayer = gc.getPlayer(iPlayer)
	
	if g_bGreatPersonModFeaturesEnabled:
		if not pUnit.isNone() or not pCity.isNone():			
			# If Person doesn't have unique name, give him a random one
			if(len(pUnit.getNameNoDesc()) == 0):
				iCivilizationType = pPlayer.getCivilizationType()
				pUnit.setName(RandomNameUtils.getRandomCivilizationName(iCivilizationType))
				
			# Show popup if a human player received the great person:
			if pPlayer.isHuman():
			
				global g_dict
				global g_iCount
				
				g_dict[g_iCount] = (pUnit, iPlayer, pCity)													
				popupInfo = CyPopupInfo()
				popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
				popupInfo.setData1(g_iCount)
				g_iCount += 1
				popupInfo.setText(u"showGreatPersonScreen")
				popupInfo.addPopup(iPlayer)	
				
		
	else:	
		return
		
		
        
		
				
		    
		

		
	