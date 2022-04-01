retval, retvals_csv = reaper.GetUserInputs( 'Set track offset in ms', 1, 'offset (in ms)', 0 )
if retval and tonumber(retvals_csv) then
  for i = 1, reaper.CountSelectedTracks(0) do
    tr = reaper.GetSelectedTrack(0,i-1)
    reaper.SetMediaTrackInfo_Value( tr, 'I_PLAY_OFFSET_FLAG', 0 )
    reaper.SetMediaTrackInfo_Value( tr, 'D_PLAY_OFFSET', tonumber(retvals_csv / 1000) ) 
  end
end
