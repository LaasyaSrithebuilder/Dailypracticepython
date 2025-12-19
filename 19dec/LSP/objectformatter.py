import json
from vechile import Vechile

class ObjectFormatter:
    def vechile_to_json(self,vechile: Vechile):
        return json.dumps({
            "VechileMake": vechile.make,
            "VechileModel": vechile.model,
            "VechileYear": vechile.year
        })