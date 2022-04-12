# @description Toggle Solo on Selected Items within the Midi Editor
# @author DMDComposer
# @version 1.0
# @about
#   Toggle solo on selected items within the Midi editor.
# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def main():
    RPR.Undo_BeginBlock()

    RPR.Main_OnCommand(41557, 0)

    RPR.Undo_EndBlock("Toggle Solo on Selected Items", 1)
    return


with inside_reaper():
    main()
