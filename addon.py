# -*- coding: utf-8 -*-
import sys
import requests
import xbmcplugin
from xbmcgui import ListItem
from xbmcaddon import Addon

addon_handle = int(sys.argv[1])
my_addon = Addon('plugin.audio.radiorecord')
xbmcplugin.setContent(addon_handle, 'albums')

if __name__ == "__main__":
    station_list = requests.get('https://radiorecord.ru/api/stations/').json().get('result')
    for station in station_list.get('stations'):
        item = ListItem(station.get('title'))
        item.setArt({
            'thumb': station.get('icon_fill_white'),
            'icon': station.get('icon_fill_white'),
            'fanart': my_addon.getAddonInfo('fanart')
        })
        item.setInfo(type="music", infoLabels={"title": station.get('title')})
        item.setProperty('isPlayable', 'true')
        xbmcplugin.addDirectoryItem(addon_handle, station['stream_320'], item, False)
    xbmcplugin.addSortMethod(addon_handle, 1)
    xbmcplugin.endOfDirectory(addon_handle)
