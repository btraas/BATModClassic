# MovieMod.py -- Play religion and Nat Wonder movies - EmperorFool and Phungus420

from CvPythonExtensions import *

gc = CyGlobalContext()

def onBuildingBuilt(argsList): # Took out arg 'self' - not required
		'Building Completed'
		pCity, iBuildingType = argsList
		game = gc.getGame()
		if ( (not gc.getGame().isNetworkMultiPlayer()) and (pCity.getOwner() == gc.getGame().getActivePlayer()) ):
			if ( gc.getBuildingInfo(iBuildingType).getMovie() and not isWorldWonderClass(gc.getBuildingInfo(iBuildingType).getBuildingClassType()) ):
					
				popupInfo = CyPopupInfo()
				popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
				popupInfo.setData1(iBuildingType)
				popupInfo.setData2(pCity.getID())
				popupInfo.setData3(0)
				popupInfo.setText(u"showWonderMovie")
				popupInfo.addPopup(pCity.getOwner())
	