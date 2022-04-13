# @description Add ReaControlMidi to selected tracks input fx
# @author DMDComposer
# @version 1.0
# @about
#   Add ReaControlMidi to selected tracks input fx

# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def Main():
    RPR.Undo_BeginBlock()

    FX = "ReaControlMIDI"

    TrackIdx = 0
    TrackCount = RPR.CountSelectedTracks(0)
    while TrackIdx < TrackCount:
        track = RPR.GetSelectedTrack(0, TrackIdx)
        fxIdx = RPR.TrackFX_AddByName(track, FX, True, -1)

        # adding 0x1000000 allows to target the rec input fx
        RPR.TrackFX_Show(track, fxIdx | 0x1000000, 3)

        TrackIdx += 1

    RPR.Undo_EndBlock("Insert FX Plugin: " + FX, -1)
    return


with inside_reaper():
    Main()
