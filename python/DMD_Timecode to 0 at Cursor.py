# local SCRIPT_NAME = ({reaper.get_action_context()})[2]:match("([^/\\_]+)%.lua$")

# local MODE = ({
#   ['time'    ] =  0,
#   ['seconds' ] =  3,
#   ['frames'  ] =  5,
#   ['set to 0'] = -1,
# })[SCRIPT_NAME:match('%(([^%)]+)%)') or 'time']

# assert(MODE, "Internal error: unknown timecode format")
# assert(reaper.SNM_GetDoubleConfigVar, "SWS is required to use this script")

# local curpos = reaper.GetCursorPosition()
# local timecode = 0

# if MODE >= 0 then
#   timecode = reaper.format_timestr_pos(curpos, '', MODE)
#   local ok, csv = reaper.GetUserInputs(SCRIPT_NAME, 1, "Timecode,extrawidth=50", timecode)

#   if not ok then
#     reaper.defer(function() end)
#     return
#   end

#   timecode = reaper.parse_timestr_len(csv, 0, MODE)
# end

# reaper.SNM_SetDoubleConfigVar('projtimeoffs', timecode - curpos)
# reaper.UpdateTimeline()

from reapy import Project, print
import reapy.reascript_api as RPR

print(RPR_GetProjectTimeOffset( Project(), False ))