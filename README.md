# DISCLAIMER: the DSOonWin fork with embedded python is currently crashing SteamVR!

1. Install Python 3 https://www.python.org/
2. Install the Intel RealSense SDK https://github.com/IntelRealSense/librealsense/releases/tag/v2.50.0
3. Install Steam and SteamVR https://store.steampowered.com/app/250820/SteamVR/
4. Install Arduino IDE.
5. Upload supplied arduino.ino to a microcontroller capable of serial communication. 
6. Take note of the COM port used by the microcontroller.
7. Clone https://github.com/djblazkowicz/Relativty-6DOF-InsideOutTracking
8. Open the solution in Visual Studio 2019.
9. Build solution Release x64 configuration.
10. Verify that build was successful. if not, resolve missing dependencies - although everything should be included in the repository.
11. Clone https://github.com/djblazkowicz/DSOonWin
12. Follow build instructions in README.md.
13. Before the next step, ensure that the screen intended to be used for the VR display is positioned to the right of the primary display in windows display settings.
14. Navigate to \Relativty\resources\settings.
15. Find and open default.vrsettings file.
16. In the Relativty extendedDisplay section, change the windowX value to the resolution width of your primary screen.
17. Change windowWidth,WindowHeight,renderWidth,renderHeight to the resolution of your VR screen.
18. In relativty_hmd section change COMPORT to the COM number of your microcontroller. 
19. Open an administrative command prompt.
20. Navigate to #your steam install folder#\steamapps\common\steamvr\bin\win64.
21. Run this command "vrpathreg.exe adddriver #Relativty-6DOF-InsideOutTracking folder#\Relativty".
22. Plug in all necessary headset cables.
23. Start vio_udp.py and wait until the script starts to output data in the console.
24. If any dependencies are missing, install them using pip or other python library manager tool.
25. Open SteamVR.
26. Once the VR holodeck has opened, press R to reset the orientation - this is required once to reorientate the system.
