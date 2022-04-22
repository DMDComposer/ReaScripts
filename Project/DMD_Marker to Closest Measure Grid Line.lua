-- @description Marker to Closest Measure Grid Line
-- @author DMDComposer
-- @version 1.0
-- @about
--   Move marker to downbeat of the closest measure.
local function main()
    reaper.Undo_BeginBlock()

    cursorPos = reaper.GetCursorPositionEx(0)
    markerIndex, regionIndex = reaper.GetLastMarkerAndCurRegion(0, cursorPos)
    retval, isrgn, pos, rgnend, name, markrgnindexnumber =
        reaper.EnumProjectMarkers2(0, markerIndex)

    cmdID = reaper.NamedCommandLookup("_BR_MOVE_M_GRID_TO_EDIT_CUR")
    reaper.Main_OnCommand(cmdID, 0)

    cursorPos = reaper.GetCursorPositionEx(0)
    moveMarker = reaper.SetProjectMarker4(0, markrgnindexnumber, 0, cursorPos,
                                          0, name, 0, 0)

    reaper.Undo_EndBlock("Marker to Closest Measure Grid Line", -1)
end

main()
