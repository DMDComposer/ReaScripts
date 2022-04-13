# @description Add Pro-C 2 to selected tracks
# @author DMDComposer
# @version 1.0
# @about
#   Add Pro-C 2 to selected tracks

# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def Main():
    RPR.Undo_BeginBlock()

    FX = "Pro-C 2"

    TrackIdx = 0
    TrackCount = RPR.CountSelectedTracks(0)
    while TrackIdx < TrackCount:
        track = RPR.GetSelectedTrack(0, TrackIdx)
        fxIdx = RPR.TrackFX_AddByName(track, FX, False, -1)
        RPR.TrackFX_Show(track, fxIdx, 3)

        TrackIdx += 1

    RPR.Undo_EndBlock("Insert FX Plugin: " + FX, -1)
    return


with inside_reaper():
    Main()
