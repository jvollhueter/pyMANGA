from ProjectLib import XMLtoProject
from TimeLoopLib import TreeDynamicTimeStepping
import unittest
#from pathlib2 import Path
from TreeModelLib import TreeModel
from TreeModelLib import AbovegroundCompetition

#class TestNeueKlasse_2(unittest.TestCase):	
#    	def test_code_run_files_without_errors(self):
#        	try:
#            		prj = XMLtoProject(xml_project_file="Demo.xml")
#            		time_stepper = TreeDynamicTimeStepping(prj)
#            		prj.runProject(time_stepper)
#			
#			
#        	except:
#            		self.fail("Fehler")
#if __name__ == '__main__':
#    unittest.main()
#
#class TestNeueKlasse_2(unittest.TestCase):	
#	def test_Eingangsdatei_Format(self):
#		try:
#			prj = XMLtoProject(xml_project_file="Demo.xml")
#			x = Path("demo.xml").suffix
#			print("Druck:",x)
#		except:
#			self.fail("Die Eingangsdatei liegt nicht im xml-Format vor")
#if __name__ == '__main__':
#    unittest.main()

class TestNeueKlasse_23(unittest.TestCase):	
	def test_Wachstumsdateien(self):
		try:
			#aboveground_competition = SimpleTest
			#case.AbovegroundCompetition = SimpleTest
			#x = AbovegroundCompetition()
			#print("TESTDRUCK:",x.case)
			x = AbovegroundCompetition.iniSimpleTest
			y = AbovegroundCompetition.getConceptType(self)
			print("IIIIIIII", x, y)
		except:
			self.fail("Fehler")
if __name__ == '__main__':
    unittest.main()