-- functions
function log(args)
    reaper.ClearConsole()
    reaper.ShowConsoleMsg(args)
end

-- code

function dialog(title, defaultValue)
    local ret, retvals = reaper.GetUserInputs(title, 1,
                                              "Ok is Offline | Cancel is Online",
                                              defaultValue)

    if ret then return true end
    return false

end

function main()
    start, startEnd = reaper.GetSet_LoopTimeRange( false, true, start, startEnd, true )
    log(start)
    log(startEnd)
end

main()

-- for i = 1, reaper.CountSelectedTracks(0) do
--   tr = reaper.GetSelectedTrack(0,i-1)
--   reaper.SetMediaTrackInfo_Value( tr, "I_RECMODE", 2 )
--   reaper.SetMediaTrackInfo_Value( tr, "I_RECINPUT", -1 )
-- end
