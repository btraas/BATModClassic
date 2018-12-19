## Female CEO Mod.py  08/22/10 - Lemon Merchant and SaibotLieh
## Allows the use of Saibotlieh's Female Missionary, CEO, and female units in the BAT Mod 
## This is a BUG module, and requires the BUG mod for use.


from CvPythonExtensions import *
import CvUtil
import CvScreensInterface
import PyHelpers
import Popup as PyPopup
import CvCameraControls
import CvTopCivs
import sys
import CvAdvisorUtils
import CvTechChooser
import CvScreenEnums

gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer
PyInfo = PyHelpers.PyInfo
"""
## new testing code
def onBeginPlayerTurn(argsList):
		'Called at the beginning of a players turn'
		iGameTurn, iPlayer = argsList
		return
		
		pPlayer = gc.getPlayer(iPlayer)
		screen = CyGInterfaceScreen( "MainInterface", CvScreenEnums.MAIN_INTERFACE )

		if pPlayer.isHuman() == True:
			CvScreensInterface.showMainInterface()
			screen.moveToBack( "MiniMapPanel" )
			screen.moveToBack( "InterfaceRightBackgroundWidget" )
			screen.moveToBack( "InterfaceCenterBackgroundWidget" )
			screen.moveToBack( "InterfaceCenterRightBackgroundWidget" )
			screen.moveToBack( "InterfaceTopLeftBackgroundWidget" )
			screen.moveToBack( "InterfaceTopLeft" )
			screen.moveToBack( "InterfaceTopCenter" )
"""
## End test			
			
def onUnitBuilt(argsList):
		'Unit Completed'
		city = argsList[0]
		unit = argsList[1]
		player = PyPlayer(city.getOwner())
		iplayer = gc.getPlayer(city.getOwner())
		
# Female CEO begin

		iUnitType = unit.getUnitType()
		UnitInfo = gc.getUnitInfo(iUnitType)
		sUnitType = UnitInfo.getType()
		sMixedUnitType = 'UNIT_MIXED'+sUnitType[4:]
		iMixedUnitType = gc.getInfoTypeForString(sMixedUnitType)
	
		if UnitInfo.getDefaultUnitAIType() == gc.getInfoTypeForString('UNITAI_MISSIONARY'):
			sUnitBuilt = gc.getInfoTypeForString(sUnitType[:20])
			
			if sUnitBuilt == "UNITCLASS_EXECUTIVE_":
				sCEOType = gc.getInfoTypeForString(sUnitType[20:])
				iFemaleUnitType = CvUtil.findInfoTypeNum(gc.getUnitInfo,gc.getNumUnitInfos(),sUnitBuilt+sCEOType+'_FEMALE')
				
			else:		
				sFemaleUnitType = 'UNIT_FEMALE'+sUnitType[4:]
				iFemaleUnitType = gc.getInfoTypeForString(sFemaleUnitType)
			
			iRnd = CyGame().getSorenRandNum(100, "female CEO")
			if iplayer.isCivic(gc.getInfoTypeForString("CIVIC_EMANCIPATION")):
				iRnd -= 35
			if iRnd <= 20:	## Changed from 15 to 20 - better chance of generating female unit without Emancipation
				oldunit = unit				
				pFemaleUnit = iplayer.initUnit(iFemaleUnitType,oldunit.getX(),oldunit.getY(),UnitAITypes.NO_UNITAI,DirectionTypes.DIRECTION_SOUTH)
				pFemaleUnit.convert(oldunit)
				if oldunit.getGroup().isAutomated():
					pFemaleUnit.getGroup().setAutomateType(AutomateTypes.AUTOMATE_RELIGION)
				oldunit.kill(false,oldunit.getOwner())
		# End Female CEO code
		
		# Female Modern Soldiers - saibotlieh - start
		
		elif iMixedUnitType > -1:
			if iplayer.isCivic(gc.getInfoTypeForString('CIVIC_EMANCIPATION')):
				iFemaleChance = 50
			else:
				iFemaleChance = 15
			
			NumOfFemales = 0
			iRnd = CyGame().getSorenRandNum(100, "First Person Female")
			if iRnd < iFemaleChance:
				NumOfFemales+=1
			iRnd = CyGame().getSorenRandNum(100, "Second Person Female")
			if iRnd < iFemaleChance:
				NumOfFemales+=1
			iRnd = CyGame().getSorenRandNum(100, "Third Person Female")
			if iRnd < iFemaleChance:
				NumOfFemales+=1
				
			if NumOfFemales > 0:
				if NumOfFemales == 2:
					iMixedUnitType = gc.getInfoTypeForString(sMixedUnitType+'12')
				if NumOfFemales == 3:
					iMixedUnitType = gc.getInfoTypeForString(sMixedUnitType+'03')
				
				oldunit = unit				
				pMixedUnit = iplayer.initUnit(iMixedUnitType,oldunit.getX(),oldunit.getY(),UnitAITypes.NO_UNITAI,DirectionTypes.DIRECTION_SOUTH)
				pMixedUnit.convert(oldunit)
				oldunit.kill(false,oldunit.getOwner())

		# Female Modern Soldiers - saibotlieh - end
		CvAdvisorUtils.unitBuiltFeats(city, unit)
				
		 
