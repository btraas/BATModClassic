from CvPythonExtensions import *
import CvUtil
import CvScreensInterface
import CvDebugTools
import CvWBPopups
import PyHelpers
import Popup as PyPopup
import CvCameraControls
import CvTopCivs
import sys
import CvWorldBuilderScreen
import CvAdvisorUtils
import CvTechChooser

gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer
PyInfo = PyHelpers.PyInfo





def onCityRazed(argsList):
		'City Razed'
		city, iPlayer = argsList
		iOwner = city.findHighestCulture()
#### messages - wonder destroyed start ####
		pCity = city		
		NumWonders = pCity.getNumWorldWonders
		if NumWonders ()>0:
                        Counter = 0
                        for i in range(gc.getNumBuildingInfos ()):
                                thisbuilding = gc.getBuildingInfo (i)
                                if pCity.getNumBuilding(i)>0:
                                        iBuildingClass = thisbuilding.getBuildingClassType ()
                                        thisbuildingclass = gc.getBuildingClassInfo (iBuildingClass)
                                        if thisbuildingclass.getMaxGlobalInstances ()==1:
                                                ConquerPlayer = gc.getPlayer(city.getOwner())
                                                iConquerTeam = ConquerPlayer.getTeam()
                                                ConquerName = ConquerPlayer.getName ()
                                                WonderName = thisbuilding.getDescription ()
                                                iX = pCity.getX()
                                                iY = pCity.getY()
                                                for iAllPlayer in range (gc.getMAX_CIV_PLAYERS ()):
                                                        ThisPlayer = gc.getPlayer(iAllPlayer)
                                                        iThisTeam = ThisPlayer.getTeam()
                                                        ThisTeam = gc.getTeam(iThisTeam)
                                                        if ThisTeam.isHasMet(iConquerTeam):
                                                                if iAllPlayer == city.getOwner():
                                                                        CyInterface().addMessage(iAllPlayer,False,15,CyTranslator().getText("TXT_KEY_YOU_DESTROYED_WONDER",(ConquerName,WonderName)),'',0,'Art/Interface/Buttons/General/warning_popup.dds',ColorTypes(gc.getInfoTypeForString("COLOR_RED")), iX, iY, True,True)
                                                                else:
                                                                        CyInterface().addMessage(iAllPlayer,False,15,CyTranslator().getText("TXT_KEY_DESTROYED_WONDER",(ConquerName,WonderName)),'',0,'Art/Interface/Buttons/General/warning_popup.dds',ColorTypes(gc.getInfoTypeForString("COLOR_RED")), iX, iY, True,True)
#### messages - wonder destroyed end ####		
		
		# Partisans!
		if city.getPopulation > 1 and iOwner != -1 and iPlayer != -1:
			owner = gc.getPlayer(iOwner)
			if not owner.isBarbarian() and owner.getNumCities() > 0:
				if gc.getTeam(owner.getTeam()).isAtWar(gc.getPlayer(iPlayer).getTeam()):
					if gc.getNumEventTriggerInfos() > 0: # prevents mods that don't have events from getting an error
						iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(),'EVENTTRIGGER_PARTISANS')
						if iEvent != -1 and gc.getGame().isEventActive(iEvent) and owner.getEventTriggerWeight(iEvent) < 0:
							triggerData = owner.initTriggeredData(iEvent, true, -1, city.getX(), city.getY(), iPlayer, city.getID(), -1, -1, -1, -1)
			
		CvUtil.pyPrint("City Razed Event: %s" %(city.getName(),))
		
		
def onCityAcquiredAndKept(argsList):
		'City Acquired and Kept'
		iOwner,pCity = argsList
#### messages - wonder captured start ####		
		NumWonders = pCity.getNumWorldWonders
		if NumWonders ()>0:
                        Counter = 0
                        for i in range(gc.getNumBuildingInfos ()):
                                thisbuilding = gc.getBuildingInfo (i)
                                if pCity.getNumBuilding(i)>0:
                                        iBuildingClass = thisbuilding.getBuildingClassType ()
                                        thisbuildingclass = gc.getBuildingClassInfo (iBuildingClass)
                                        if thisbuildingclass.getMaxGlobalInstances ()==1:
                                                ConquerPlayer = gc.getPlayer(pCity.getOwner())
                                                iConquerTeam = ConquerPlayer.getTeam()
                                                ConquerName = ConquerPlayer.getName ()
                                                WonderName = thisbuilding.getDescription ()
                                                iX = pCity.getX()
                                                iY = pCity.getY()
                                                for iPlayer in range (gc.getMAX_CIV_PLAYERS ()):
                                                        ThisPlayer = gc.getPlayer(iPlayer)
                                                        iThisTeam = ThisPlayer.getTeam()
                                                        ThisTeam = gc.getTeam(iThisTeam)
                                                        if ThisTeam.isHasMet(iConquerTeam):
                                                                if iPlayer == pCity.getOwner():
                                                                        CyInterface().addMessage(iPlayer,False,15,CyTranslator().getText("TXT_KEY_YOU_CAPTURED_WONDER",(ConquerName,WonderName)),'',0,'Art/Interface/Buttons/General/happy_person.dds',ColorTypes(gc.getInfoTypeForString("COLOR_GREEN")), iX, iY, True,True)
                                                                else:
                                                                        CyInterface().addMessage(iPlayer,False,15,CyTranslator().getText("TXT_KEY_CAPTURED_WONDER",(ConquerName,WonderName)),'',0,'Art/Interface/Buttons/General/warning_popup.dds',ColorTypes(gc.getInfoTypeForString("COLOR_RED")), iX, iY, True,True)
#### messages - wonder captured end ####                                                                        
                                                                
                        
		CvUtil.pyPrint('City Acquired and Kept Event: %s' %(pCity.getName()))