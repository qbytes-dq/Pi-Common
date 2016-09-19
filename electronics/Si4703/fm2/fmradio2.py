import si4703
fm = si4703.si4703()
fm.init()

fm.POWER_CONFIG.DMUTE = 1   ##Turn off mute
fm.SYS_CONFIG_2.VOLUME = 15 ##Turn the volume up to max
#fm.write_registry()  ## Since the above two lines of code only change local variables on the Pi, we need to write those variables to the Si4703.
