# @description Add FX to selected tracks
# @author DMDComposer
# @version 1.0
# @about
#   Add FX to selected tracks function

# reapy # https://python-reapy.readthedocs.io/en/latest/api_guide.html#://


import reapy.reascript_api as RPR
import sys


def addFXToSelectedTracks(FX):
    RPR.Undo_BeginBlock()

    TrackIdx = 0
    TrackCount = RPR.CountSelectedTracks(0)
    while TrackIdx < TrackCount:
        track = RPR.GetSelectedTrack(0, TrackIdx)
        fxIdx = RPR.TrackFX_AddByName(track, FX, False, -1)
        RPR.TrackFX_Show(track, fxIdx, 3)

        TrackIdx += 1

    RPR.Undo_EndBlock("Insert FX Plugin: " + FX, -1)
    return


sys.modules[__name__] = addFXToSelectedTracks
