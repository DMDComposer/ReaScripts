local function main()
    tr = reaper.GetMasterTrack(proj)
    reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 0.125)

end

main()