-- @description Set master volume to -18db
-- @author DMDComposer
-- @version 1.0
-- @about
--   reascript to set master volume
local function main()
    tr = reaper.GetMasterTrack(proj)
    reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 0.125)

end

main()
