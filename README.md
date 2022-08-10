1. Install Python 3 https://www.python.org/

2. Install Steam and SteamVR https://store.steampowered.com/app/250820/SteamVR/

2. clone https://github.com/djblazkowicz/Relativty-6DOF-InsideOutTracking

3. open Relativty_Driver.sln in Visual Studio 2019

4. Build solution Release x64 configuration

5. verify that build was successful. if not, resolve missing dependencies - although everything should be included in the repository.

6. before the next step, ensure that the screen intended to be used for the VR display is positioned to the right of the primary display in windows display settings

6. navigate to <relativty-6dof-insideouttracking folder>\Relativty\resources\settings

7. find and open default.vrsettings file

8. in the Relativty_extendedDisplay section, change the windowX value to the resolution width of your primary screen

9. change windowWidth,WindowHeight,renderWidth,renderHeight to the resolution of your VR screen



5. Open an administrative command prompt

6. navigate to <steam installation library>\steamapps\common\steamvr\bin\win64

7. 