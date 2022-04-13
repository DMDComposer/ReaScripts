-- @description remove any hardware outs on selected tracks
-- @author DMDComposer
-- @version 1.0
-- @about
--   Created to remove general midi hardware outs on tracks
for i = 1, reaper.CountSelectedTracks(0) do
    tr = reaper.GetSelectedTrack(0, i - 1)
    reaper.SetMediaTrackInfo_Value(tr, "I_MIDIHWOUT", -1)
end

