from vechile import Vechile

from maintanenece_tool import MiantanenceTool

class BrakeInspection(MiantanenceTool):
    def perform_maintanence(self,vechile:Vechile):
        print("Performming brake inspection on {vechile.make} {vechile.model}".format(vechile=vechile))

