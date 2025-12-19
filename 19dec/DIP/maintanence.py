from maintanenece_tool import MiantanenceTool
from vechile import Vechile
#service
class Maintanence:
    def __init__(self,tool: MiantanenceTool):
        self.tool = tool
        #diectly dependent on brakeinspection 
    #the problem is if we want other we shold again change copmletely breaking ocp
    #so instead of directly passing class we create object to send as object
    #here we are passing object so can be changed based on need

    def servicevechile(self, vechile: Vechile):
        self.tool.perform_maintanence(vechile)
