local function log(args)
    reaper.ClearConsole()
    reaper.ShowConsoleMsg(tostring(args))
end

local function main()
    track = reaper.GetTrack(0, 11)
    _, trackName = reaper.GetSetMediaTrackInfo_String(track, 'P_NAME', '', 0)
    if trackName == "MASTER" then
        reaper.SetMediaTrackInfo_Value(track, "D_VOL", 0.5)
    else
        log("master is on different channel number")
    end
end

main()
