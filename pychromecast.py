import time
import pychromecast


chromecasts = pychromecast.get_chromecasts()
[cc.device.friendly_name for cc in chromecasts]
cast = next(cc for cc in chromecasts if cc.device.friendly_name == "devicename")
cast.wait()
print(cast.device)
print(cast.status)
mc = cast.media_controller
mc.play_media('media','media_type/media_format')#example('hi.mp4','video/mp4')
mc.block_until_active()
print(mc.status)
mc.pause()
time.sleep(5)
mc.play()
