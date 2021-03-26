import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

message = "Hello World! We can write anything we want here Using Python"
xbmcgui.Dialog().ok(addonname, line1)
