# windows-audio-switcher
Simple python script which cycles through audio devices on serial message from attached Arduino or other serial device.

## How to run:
* Change path in Audio_switcher.bat to appropriate path and put in Windows autostart folder.
* Ensure NirCMD.exe is in the appropriate directory.
* Update device names in serial_listener.py if needed. Add as many as you want to cycle though.

Uses NirCMD for access to Windows default audio device switching - http://www.nirsoft.net/utils/nircmd.html
