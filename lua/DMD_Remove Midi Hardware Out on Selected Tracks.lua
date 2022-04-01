for i = 1, reaper.CountSelectedTracks(0) do
  tr = reaper.GetSelectedTrack(0,i-1)
  reaper.SetMediaTrackInfo_Value(tr,"I_MIDIHWOUT", -1)
end

