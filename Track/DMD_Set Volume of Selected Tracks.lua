-- @description Set Volume on Selected Tracks
-- @author DMDComposer
-- @version 1.1
-- @about
--   Set volume for selected track(s), edited by , original idea by spk77
--   range:
--   min: -inf
--   max: 12
function dialog(title, def_value)
    local ret, retvals = reaper.GetUserInputs(title, 1,
                                              "Set volume for selected track(s)",
                                              def_value)
    if ret then return retvals end
    return ret
end

----------
-- Main --
----------

function main()
    local tr_count = reaper.CountSelectedTracks(0)
    if tr_count == 0 then return end

    local def_value = 0.0

    if tr_count == 1 then
        -- if only one track is selected -> show current pan value in edit box
        def_value = reaper.GetMediaTrackInfo_Value(
                        reaper.GetSelectedTrack(0, 0), "D_VOL")
        def_value = 20 * math.log(def_value, 10)
        if def_value < -150 then def_value = "-inf" end
    end

    local new_vol = dialog("Set volume for selected track(s)", def_value)

    if not new_vol then
        return
    elseif new_vol == "-inf" then
        new_vol = 0.0
    elseif not tonumber(new_vol) then
        return
    else
        new_vol = tonumber(new_vol)
        if new_vol > 12 then new_vol = 12 end
        new_vol = 10 ^ (new_vol / 20)
    end

    for i = 1, tr_count do
        local tr = reaper.GetSelectedTrack(0, i - 1)
        if tr ~= nil then
            reaper.SetMediaTrackInfo_Value(tr, "D_VOL", new_vol)
        end
    end
    reaper.Undo_OnStateChangeEx("Set volume for selected track(s)", -1, -1)
end

reaper.defer(main)
