# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, Project

project = Project()  # Current project
print("Saving project...")
project.save(True)
