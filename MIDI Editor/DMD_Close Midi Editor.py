# @description Close Midi Editor & Unsolo Items
# @author DMDComposer
# @version 1.1
# @about
#   Close Midi Editor & Unsolo Items.
# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def main():
    RPR.Undo_BeginBlock()

    RPR.MIDIEditor_OnCommand(RPR.MIDIEditor_GetActive(), 2)
    RPR.Main_OnCommand(41560, 0)

    RPR.Undo_EndBlock("Close Midi Editor & Unsolo Items", 1)
    return


with inside_reaper():
    main()
