-- @description Set master volume to -12db
-- @author DMDComposer
-- @version 1.0
-- @about
--   reascript to set master volume
local function main()
    tr = reaper.GetMasterTrack(proj)
    reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 0.251)

end

main()
