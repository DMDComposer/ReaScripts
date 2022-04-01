# reapy # https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def Main():
    RPR.Undo_BeginBlock()

    # RPR.Main_OnCommand(41866, 0)  # selects volume envelope for current track

    RPR.Main_OnCommand(40153, 0)  # opens midi editor
    HWND = RPR.MIDIEditor_GetActive()  # get MIDIEditor Number

    currTake = RPR.MIDIEditor_GetTake(HWND)
    RPR.MIDI_SelectAll(currTake, True)

    # select CC1
    # msg3Out is the CC value
    """ (
        retVal,
        take,
        ccIdx,
        selectedOut,
        mutedOut,
        ppqPosOut,
        chanMsgOut,
        chanOut,
        msg2Out,
        msg3Out,
    ) = RPR.MIDI_GetCC(take, ccIdx, False, False, 0, 0, 0, 0, 0) """

    return

    copycc_id = RPR.NamedCommandLookup(
        "_BR_ME_CC_TO_ENV_LINEAR_CLEAR", 0
    )  # copies cc1 lane event to envelope
    RPR.MIDIEditor_OnCommand(HWND, copycc_id)

    closeeditor = RPR.NamedCommandLookup(
        "_RS7d3c_e0cd2a44410da646d94b2a5f7689da62970fc08a", 0
    )  # close midi editors
    RPR.MIDIEditor_OnCommand(HWND, closeeditor)

    RPR.Main_OnCommand(40332, 0)  # selects all envelope points
    RPR.Main_OnCommand(40683, 0)  # changes points to bezier
    RPR.Main_OnCommand(41622, 0)  # toggle zoom selected item
    RPR.Main_OnCommand(40887, 0)  # calls up reduce number of points script

    OpenEditorCommand_id = RPR.NamedCommandLookup(
        "_RS0ff4cded2383187077d9eeca4e95032cd553d57c", 0
    )  # opens midi editor and zooms to content
    RPR.Main_OnCommand(OpenEditorCommand_id, 0)

    HWND2 = RPR.MIDIEditor_GetActive()  # get MIDIEditor Number

    ConvertEnv = RPR.NamedCommandLookup(
        "_BR_ME_ENV_TO_CC_CLEAR", 0
    )  # converts envelope to cc lane
    RPR.MIDIEditor_OnCommand(HWND2, ConvertEnv)

    SetToCC1 = RPR.NamedCommandLookup("_S&M_SETCCLANES_ME2", 0)  # restore to CC 1
    RPR.MIDIEditor_OnCommand(HWND, SetToCC1)

    RPR.MIDIEditor_OnCommand(HWND2, command_id)  # selects cc1 lane
    RPR.MIDIEditor_OnCommand(HWND2, 42085)  # turns cc1 lane shape to bezier
    RPR.MIDIEditor_OnCommand(HWND2, 40671)  # unselects all CC events

    RPR.Main_OnCommand(40333, 0)  # delete all selected points
    RPR.Main_OnCommand(41150, 0)  # hide envelopes

    closeeditor = RPR.NamedCommandLookup(
        "_RS7d3c_e0cd2a44410da646d94b2a5f7689da62970fc08a", 0
    )  # close midi editors
    RPR.MIDIEditor_OnCommand(HWND2, closeeditor)

    RPR.Main_OnCommand(41622, 0)  # toggle zoom selected item

    RPR.Undo_EndBlock("Shape CC", -1)


with inside_reaper():
    import time

    t0 = time.time()

    Main()

    t1 = time.time()
    print(t1 - t0)
