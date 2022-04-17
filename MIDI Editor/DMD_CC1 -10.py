# @description CC1 - 10 on selected CC
# @author DMDComposer
# @version 1.1
# @about
#   Select specific cc1 points, and decrease by 10

# reapy # https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def Main():
    editor = RPR.MIDIEditor_GetActive()
    if not editor:
        return

    take = RPR.MIDIEditor_GetTake(editor)
    if not take:
        return

    RPR.Undo_BeginBlock()

    """ RPR.Main_OnCommand(40683, 0)  # changes points to bezier
    RPR.Main_OnCommand(40887, 0)  # calls up reduce number of points script
    RPR.Undo_EndBlock("Invert selected CC event values", 4) """

    ccIdx = -1
    while True:
        ccIdx = RPR.MIDI_EnumSelCC(take, ccIdx)
        if ccIdx == -1:
            break
        # msg3Out is the CC value
        (
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
        ) = RPR.MIDI_GetCC(take, ccIdx, False, False, 0, 0, 0, 0, 0)

        ccNewVal = msg3Out - 10

        if (ccNewVal) >= 127:
            ccNewVal = 127

        if (ccNewVal) <= 0:
            ccNewVal = 0

        RPR.MIDI_SetCC(
            take,
            ccIdx,
            selectedOut,
            mutedOut,
            ppqPosOut,
            chanMsgOut,
            chanOut,
            msg2Out,
            ccNewVal,
            True,
        )

    RPR.MIDI_Sort(take)

    # Hack to make Reaper recognize that the item was altered
    item = RPR.GetMediaItemTake_Item(take)
    RPR.SetMediaItemSelected(item, False)
    RPR.SetMediaItemSelected(item, True)

    RPR.Undo_EndBlock("Invert selected CC event values", 4)


with inside_reaper():
    Main()
