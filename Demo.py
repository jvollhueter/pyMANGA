from ProjectLib import XMLtoProject
from TimeLoopLib import TreeDynamicTimeStepping
import unittest

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> Adds module blink
class TestNeueKlasse(unittest.TestCase):	
    	def test_code_run_files_without_errors(self):
        	try:
            		prj = XMLtoProject(xml_project_file="Demo.xml")
            		time_stepper = TreeDynamicTimeStepping(prj)
            		prj.runProject(time_stepper)
        	except:
            		self.fail("Fehler")
<<<<<<< HEAD
if __name__ == '__main__':
    unittest.main()
=======

class TestNeueKlasse(unittest.TestCase):
    def code_run_files_without_errors(self): #zugriff auf alle Attribute in Klasse
        try:
            prj = XMLtoProject(xml_project_file="Demo3.xml")
            time_stepper = TreeDynamicTimeStepping(prj)
            prj.runProject(time_stepper)
        except:
            self.fail("Fehler")
if __name__ == '__main__':
    unittest.main()
>>>>>>> Erstellung eines ersten Versuchs der Programmierung einer Testabfrage
=======
if __name__ == '__main__':
    unittest.main()
>>>>>>> Adds module blink
