1. Install Python 3 https://www.python.org/

2. Install Steam and SteamVR https://store.steampowered.com/app/250820/SteamVR/

3. install arduino IDE

4. upload supplied arduino.ino to a microcontroller capable of serial communication
NOTE: requirement for a microcontroller will be removed once the driver code is properly reworked

5. take note of the COM port used by the microcontroller

6. clone https://github.com/djblazkowicz/Relativty-6DOF-InsideOutTracking

7. open Relativty_Driver.sln in Visual Studio 2019

8. Build solution Release x64 configuration

9. verify that build was successful. if not, resolve missing dependencies - although everything should be included in the repository.

10. before the next step, ensure that the screen intended to be used for the VR display is positioned to the right of the primary display in windows display settings

11. navigate to <relativty-6dof-insideouttracking folder>\Relativty\resources\settings

12. find and open default.vrsettings file

13. in the Relativty_extendedDisplay section, change the windowX value to the resolution width of your primary screen

14. change windowWidth,WindowHeight,renderWidth,renderHeight to the resolution of your VR screen

15. in relativty_hmd section change COMPORT to the COM number of your microcontroller.
NOTE: requirement for a microcontroller will be removed once the driver code is properly reworked

16. Open an administrative command prompt

17. navigate to <steam installation library>\steamapps\common\steamvr\bin\win64

18. run this command "vrpathreg.exe adddriver <relativty-6dof-insideouttracking folder>\Relativty"

19. plug in all necessary headset cables

20. start vio_udp.py and wait until the script starts to output data in the console

20. open SteamVR

21. once the VR holodeck has opened, press R to reset the orientation - this is required once to reorientate the system.
