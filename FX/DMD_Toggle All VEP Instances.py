# @description Toggle All VEP Instances
# @author DMDComposer
# @version 1.0
# @about
#   Toggle All VEP Instances

# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def main():
    projectTrackCount = RPR.CountTracks(0)
    i = 0
    while i <= projectTrackCount:
        currTrack = RPR.GetTrack(0, i)
        instrument = RPR.TrackFX_GetByName(currTrack, "Vienna Ensemble", False)

        if instrument != -1:
            isOpened = RPR.TrackFX_GetOpen(currTrack, instrument)
            if isOpened == True:
                RPR.TrackFX_Show(currTrack, instrument, 2)
            else:
                RPR.TrackFX_Show(currTrack, instrument, 3)

        i += 1

    return


with inside_reaper():
    main()
