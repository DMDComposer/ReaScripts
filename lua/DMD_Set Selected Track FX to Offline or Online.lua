-- @description Toggle selected tracks FX to offline
-- @author DMDComposer
-- @version 1.0
-- @about
--   Toggle selected tracks FX to offline
--   Ok is Offline | Cancel is Online
function log(args)
    reaper.ClearConsole()
    reaper.ShowConsoleMsg(args)
end

function dialog(title, defaultValue)
    local ret, retvals = reaper.GetUserInputs(title, 1,
                                              "Ok is Offline | Cancel is Online",
                                              defaultValue)

    if ret then return true end
    return false

end

function main()
    local fxOffline = dialog("Offline Status for FX", 1)

    tr = reaper.GetSelectedTrack(0, 0)
    retval = reaper.GetMediaTrackInfo_Value(tr, "I_FXEN")
    -- log(reaper.TrackFX_GetCount( tr ))

    for i = 1, reaper.CountSelectedTracks(0) do
        tr = reaper.GetSelectedTrack(0, i - 1)
        for n = 1, reaper.TrackFX_GetCount(tr) do
            reaper.TrackFX_SetOffline(tr, n - 1, fxOffline)
        end
    end

end

main()
