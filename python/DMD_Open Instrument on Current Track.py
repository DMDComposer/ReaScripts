# @description Open Instrument on Current Track
# @author DMDComposer
# @version 1.1
# @about
#   open first instrument on selected track
#   toggle if already opened
# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def main():
    currTrack = RPR.GetSelectedTrack(0, 0)
    instrument = RPR.TrackFX_GetInstrument(currTrack)
    isOpened = RPR.TrackFX_GetOpen(currTrack, instrument)

    if instrument >= 0:
        if isOpened == True:
            RPR.TrackFX_Show(currTrack, instrument, 2)
        else:
            RPR.TrackFX_Show(currTrack, instrument, 3)
        return

    return


with inside_reaper():
    main()
