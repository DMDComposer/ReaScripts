# @description Set Selected Tracks REC to Stereo Output
# @author DMDComposer
# @version 1.0
# @about
#   Select tracks and change the record mode to stere out
# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def newNotification():
    from winotify import Notification  # https://github.com/versa-syahptr/winotify
    from pathlib import Path, PurePath

    cwd = Path().absolute()
    filePath = PurePath(cwd, "reaperIco.ico")
    if Path(filePath).is_file() == False:
        filePath = PurePath(RPR.GetExePath(), "reaperIco.ico")

    toast = Notification(
        app_id="Reaper",
        title="Set Selected Tracks to REC: Stereo Ouput",
        msg="Success!",
        icon=filePath,
    )

    toast.show()


def main():
    trackCount = RPR.CountSelectedTracks(0)
    if trackCount == 0:
        return

    i = 0
    while i < trackCount:
        currTrack = RPR.GetSelectedTrack(0, i)
        RPR.SetMediaTrackInfo_Value(
            currTrack, "I_RECMODE", 1
        )  # 1 is REC: stereo output
        i += 1
    return


with inside_reaper():
    main()
    newNotification()
