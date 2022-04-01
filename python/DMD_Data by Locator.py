# @description Data by Locators
# @author DMDComposer
# @version 1.1
# @about
#   Reaper replication of Cubase's Data by Locators (loop range in reaper)
# reapy -- https://python-reapy.readthedocs.io/en/latest/api_guide.html#://

from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def getAllTracks():
    listOfIds = []
    i = 0
    while i < RPR.CountTracks(0):
        track = RPR.GetTrack(0, i)
        listOfIds.append(track)
        i += 1
    return listOfIds


def getParentFolders(selectedTrack, tracksWithDataInLoopRange):
    parentFolders = []
    parentFolderExist = 1
    parentTrack = RPR.GetParentTrack(selectedTrack)

    if parentTrack in tracksWithDataInLoopRange:
        return parentFolders

    while parentFolderExist != 0:
        (retVal, track, trackName, buff_sz) = RPR.GetTrackName(parentTrack, "", 2048)
        parentFolderExist = retVal

        if retVal == 1:
            parentFolders.append(track)

        parentTrack = RPR.GetParentTrack(track)

        if parentTrack in tracksWithDataInLoopRange:
            return parentFolders

    return parentFolders


def getItemsWithinLoopRange():
    (isSet, isLoop, loopStart, loopEnd, allowautoseek) = RPR.GetSet_LoopTimeRange(
        False, True, 0, 0, False
    )

    tracksWithDataInLoopRange = []

    i = 0
    while i < RPR.CountMediaItems(0):
        mediaItem = RPR.GetMediaItem(
            0, i
        )  # RPR.GetMediaItem(currProject = 0, iterationValue)
        mediaItemLength = RPR.GetMediaItemInfo_Value(mediaItem, "D_LENGTH")
        mediaItemPositionStart = RPR.GetMediaItemInfo_Value(mediaItem, "D_POSITION")
        mediaItemPositionEnd = mediaItemPositionStart + mediaItemLength
        mediaParentTrack = RPR.GetMediaItem_Track(mediaItem)

        if (mediaItemPositionEnd > loopStart) & (mediaItemPositionStart < loopEnd):
            tracksWithDataInLoopRange.append(mediaParentTrack)
            parentFolders = getParentFolders(
                mediaParentTrack, tracksWithDataInLoopRange
            )

            # grab parent folders
            if parentFolders != None:
                for folderTrack in parentFolders:
                    tracksWithDataInLoopRange.append(folderTrack)

        i += 1

    return tracksWithDataInLoopRange


def hideTracksWithoutItemsInLoopRange(results):
    for track in results:
        RPR.SetMediaTrackInfo_Value(track, "B_SHOWINTCP", 0)  # 0 is hide, 1 is show

    RPR.TrackList_AdjustWindows(False)
    # RPR.UpdateArrange() # Don't believe you need this...
    return


def Main():
    RPR.Undo_BeginBlock()

    allTracks = getAllTracks()
    results = getItemsWithinLoopRange()  # Disable ParentFolders, set param1 to False

    for i in results:
        try:
            allTracks.remove(i)
        except:
            pass
            # (retVal, track, trackName, buff_sz) = RPR.GetTrackName(i, "", 2048)
            # print(trackName)

    hideTracksWithoutItemsInLoopRange(allTracks)

    RPR.Undo_EndBlock("Data by Locators", -1)

    return


with inside_reaper():
    Main()

# the below method is ~0.08 faster, but at the cost of a visual hiccup. Each their own...

""" from reapy import print, inside_reaper

import reapy.reascript_api as RPR


def getParentFolders(selectedTrack, tracksWithDataInLoopRange):
    parentFolders = []
    parentFolderExist = 1
    parentTrack = RPR.GetParentTrack(selectedTrack)

    if parentTrack in tracksWithDataInLoopRange:
        return parentFolders

    while parentFolderExist != 0:
        (retVal, track, trackName, buff_sz) = RPR.GetTrackName(parentTrack, "", 2048)
        parentFolderExist = retVal

        if retVal == 1:
            parentFolders.append(track)

        parentTrack = RPR.GetParentTrack(track)

        if parentTrack in tracksWithDataInLoopRange:
            return parentFolders

    return parentFolders


def getAllTracks():
    listOfIds = []

    i = 0
    while i < RPR.CountTracks(0):
        track = RPR.GetTrack(0, i)
        listOfIds.append(track)
        i += 1

    return listOfIds


def getItemsWithinLoopRange():
    RPR.Main_OnCommand(40623, 0)  # Time selection: Copy loop points to time selection
    RPR.Main_OnCommand(40717, 0)  # Item: Select all items in current time selection

    tracksWithDataInLoopRange = []

    i = 0
    while i < RPR.CountSelectedMediaItems(0):
        currItem = RPR.GetSelectedMediaItem(0, i)
        mediaParentTrack = RPR.GetMediaItem_Track(currItem)
        tracksWithDataInLoopRange.append(mediaParentTrack)
        parentFolders = getParentFolders(mediaParentTrack, tracksWithDataInLoopRange)

        # grab parent folders
        if parentFolders != None:
            for folderTrack in parentFolders:
                tracksWithDataInLoopRange.append(folderTrack)

        i += 1

    return tracksWithDataInLoopRange


def hideTracksWithoutItemsInLoopRange(results):
    for track in results:
        RPR.SetMediaTrackInfo_Value(track, "B_SHOWINTCP", 0)  # 0 is hide, 1 is show

    RPR.TrackList_AdjustWindows(False)
    return


def Main():
    RPR.Undo_BeginBlock()

    storeSelected = RPR.GetSelectedMediaItem(0, 0)

    allTracks = getAllTracks()
    results = getItemsWithinLoopRange()  # Disable ParentFolders, set param1 to False

    for i in results:
        try:
            allTracks.remove(i)
        except:
            (retVal, track, trackName, buff_sz) = RPR.GetTrackName(i, "", 2048)
            print(trackName)
            pass

    hideTracksWithoutItemsInLoopRange(allTracks)

    RPR.Main_OnCommand(40289, 0)  # Item: Unselect (clear selection of) all items

    if storeSelected:
        RPR.SetMediaItemSelected(storeSelected, True)
        RPR.UpdateArrange()

    RPR.Undo_EndBlock("Data by Locators", -1)

    return


with inside_reaper():
    Main()
 """
