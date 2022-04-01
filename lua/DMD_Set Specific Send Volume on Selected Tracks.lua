-- @description Set Specific Send Volume on Selected Tracks
-- @author DMDComposer
-- @version 1.0
-- @about
--   Starting with 1, set the specific send, and then the volume +-
--   for all selected tracks.
local function log(args)
    -- reaper.ClearConsole()
    if type(args) == "table" then
        for k, v in pairs(args) do
            local s = k .. ":" .. v .. "\n" -- concatenate key/value pairs, with a newline in-between
            reaper.ShowConsoleMsg(s)
        end
        return
    end
    reaper.ShowConsoleMsg(tostring(args) .. "\n")
end

local function getTrackSendNames(tr, numSends)
    local sendNames = ""
    for i = 1, numSends do
        retval, sendName = reaper.GetTrackSendName(tr, i - 1)
        sendNames = sendName .. "," .. sendNames
    end
    return sendNames
end

local function main()
    reaper.ClearConsole()

    local tr = reaper.GetSelectedTrack(0, 0)
    local numSends = reaper.GetTrackNumSends(tr, 0)
    local trackSendNames = getTrackSendNames(tr, numSends)
    local userResponse, retVals = reaper.GetUserInputs("Select which send?", 3,
                                                       "extrawidth=-1" ..
                                                           trackSendNames, -6)

    -- log(userResponse)
    if userResponse == true then
        userRetVals = {}
        for k, v in string.gmatch(retVals, '([^,]+)') do log(k) end
        for i = 1, numSends do
            reaper.SetTrackSendUIVol(tr, i - 1, vol, 0)
        end
        -- reaper.SetTrackSendUIVol( tr, 1, vol, 0 )
    end
end

main()

-- function main()

--     tr = reaper.GetSelectedTrack(0, 0)
--     retval = reaper.GetMediaTrackInfo_Value(tr, "I_FXEN")
--     -- log(reaper.TrackFX_GetCount( tr ))

--     for i = 1, reaper.CountSelectedTracks(0) do
--         tr = reaper.GetSelectedTrack(0, i - 1)
--         for i = 1, reaper.TrackFX_GetCount(tr) do
--             reaper.TrackFX_SetOffline(tr, i - 1, fxOffline)
--         end
--     end

-- end

-- main()

-- for i = 1, reaper.CountSelectedTracks(0) do
--     tr = reaper.GetSelectedTrack(0, i - 1)
--     reaper.SetMediaTrackInfo_Value(tr, "I_RECMODE", 2)
--     reaper.SetMediaTrackInfo_Value(tr, "I_RECINPUT", -1)
-- end
