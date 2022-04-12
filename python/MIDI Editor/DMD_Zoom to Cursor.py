# @description Zoom to Cursor within Midi Editor
# @author DMDComposer
# @version 1.0
# @about
#   Zoom to Cursor within Midi Editor.
# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def main():
    # Is there an active MIDI editor?
    editor = RPR.MIDIEditor_GetActive()
    if editor == "(HWND)0x0000000000000000":
        return

    # Checks OK, so start undo block
    RPR.Undo_BeginBlock2(0)
    RPR.PreventUIRefresh(1)

    # Store any pre-existing loop range
    (
        proj,
        isSet,
        isLoop,
        loopStart,
        loopEnd,
        allowautoseek,
    ) = RPR.GetSet_LoopTimeRange2(0, False, True, 0, 0, False)

    mouseTimePos = RPR.GetCursorPositionEx(0)
    (
        beats,
        proj,
        tpos,
        measures,
        cmlOutOptional,
        fullbeatsOutOptional,
        cdenomOutOptional,
    ) = RPR.TimeMap2_timeToBeats(0, mouseTimePos, 0, 0, 0, 0)

    # Zoom!
    import math

    measuresToZoom = 10
    zoomStart = RPR.TimeMap2_beatsToTime(0, 0, measures - 1)
    zoomEnd = RPR.TimeMap2_beatsToTime(0, 0, measures + math.ceil(measuresToZoom / 2))
    RPR.GetSet_LoopTimeRange2(0, True, True, zoomStart[0], zoomEnd[0], False)
    RPR.MIDIEditor_OnCommand(editor, 40726)  # Zoom to project loop selection

    # Reset the pre-existing loop range
    RPR.GetSet_LoopTimeRange2(0, True, True, loopStart, loopEnd, False)

    RPR.PreventUIRefresh(-1)
    RPR.UpdateTimeline()
    RPR.Undo_EndBlock2(0, "Zoom to Cursor within Midi Editor", -1)
    return


with inside_reaper():
    main()
