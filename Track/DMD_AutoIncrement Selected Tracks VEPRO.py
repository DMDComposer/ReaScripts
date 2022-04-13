# @description Auto increment VEPRO channel busses on selected tracks
# @author DMDComposer
# @version 1.0
# @about
#   Select tracks, starting bus, and starting channel.
# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import (
    print,
    Project,
    Track,
    Send,
    get_user_inputs,
    show_message_box,
    inside_reaper,
)

import reapy.reascript_api as RPR

# get selected tracks I_MIDIFLAGS, debugging and info gathering
def getSelectedTracksMidiFlags():
    """trackMidiFlags = []
    while trackID <= 16:
        send = Send(track, 0, track.id, "send")
        # print("1/", trackID, send.get_info("I_MIDIFLAGS"))
        tempStr = "1/" + str(trackID) + " " + str(send.get_info("I_MIDIFLAGS"))
        trackMidiFlags.append(tempStr)
        trackID += 1"""

    selectedTracks = Project().selected_tracks
    cleanString = str(selectedTracks[0]).split('"')[1::2]  # remove Track("")
    currTrack = "".join(cleanString)  # list to str
    track = Track(currTrack, Project())
    send = Send(track, 0, track.id, "send")
    print(send.get_info("I_MIDIFLAGS"))

    return


def userError():
    userResponse = show_message_box(
        "Needs to be a valid channel, 1-16", "ERROR", "retry-cancel"
    )
    if userResponse == "retry":
        userResponse = get_user_inputs("Source + Channel", ["Source", "Channel"])
        setSelectedTracksMidiFlags(userResponse["Source"], userResponse["Channel"])
    return


# set selected tracks I_MIDIFLAGS
def setSelectedTracksMidiFlags(initSource, initChannel):
    # Error checking on userInput
    try:
        initSource = int(initSource)
        initChannel = int(initChannel)
    except:
        userError()

    if (initChannel | initSource) <= 0 | (initChannel | initSource) >= 17:
        userError()
        return

    # B1 4194304, B2 8388608.0 is exactly double
    # 4194336 = 1/1, add 32 to increment to next channel
    # for value of midiFLAG use:
    # print(Send(track, 0, track.id, "send").get_info("I_MIDIFLAGS"))

    flagInit = 4194304 * initSource  # B1
    flagStart = flagInit + (initChannel * 32)

    numberOfSelectedTracks = Project().n_selected_tracks
    selectedTracks = Project().selected_tracks
    i = 0

    while i < numberOfSelectedTracks:
        if flagInit > 67109376:
            flagInit = 4194304
            flagStart = flagInit + 32

        cleanString = str(selectedTracks[i]).split('"')[1::2]  # remove Track("")
        currTrack = "".join(cleanString)  # list to str
        track = Track(currTrack, Project())
        send = Send(track, 0, track.id, "send")
        send.set_info("I_MIDIFLAGS", flagStart)  # set Midi Channel

        if (initChannel % 16) == 0:
            flagInit += 4194304
            flagStart = flagInit

        i += 1
        flagStart += 32
        initChannel += 1

    return


def newNotification():
    from winotify import Notification  # https://github.com/versa-syahptr/winotify
    from pathlib import Path, PurePath

    cwd = Path().absolute()
    filePath = PurePath(cwd, "reaperIco.ico")
    if Path(filePath).is_file() == False:
        filePath = PurePath(RPR.GetExePath(), "reaperIco.ico")

    toast = Notification(
        app_id="Reaper",
        title="Auto Increment Selected Tracks - VEPRO",
        msg="Success!",
        icon=filePath,
    )

    toast.show()


with inside_reaper():
    if len(Project().selected_tracks) == 0:
        show_message_box("Need at least 1 track selected", "ERROR", "ok")
    else:
        try:
            userResponse = get_user_inputs("Source + Channel", ["Source", "Channel"])
            setSelectedTracksMidiFlags(userResponse["Source"], userResponse["Channel"])
            newNotification()
        except (RuntimeError, TypeError, NameError):
            pass

# print(
#     Send(Track(0, Project()), 0, Track(0, Project()).id, "send").get_info("I_MIDIFLAGS")
# )

# All / All = 0
# All / 1 = 32
