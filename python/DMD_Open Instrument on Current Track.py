# @description Open Instrument on Current Track
# @author DMDComposer
# @version 1.0
# @about
#   open first instrument on selected track
# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def main():
    currTrack = RPR.GetSelectedTrack(0, 0)
    instrument = RPR.TrackFX_GetInstrument(currTrack)

    if instrument >= 0:
        RPR.TrackFX_Show(currTrack, instrument, 3)

    return


with inside_reaper():
    main()
