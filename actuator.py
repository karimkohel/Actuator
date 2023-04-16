import pyautogui
import math
from sys import platform
#from pyvolume import pyvolume


class Actuator():
    """Class containing all main methods of controlling a PC in the HTI context 
    """
    def __init__(self, numOfRegions: int = 4) -> None:
        """Actuator constructor, to manage windows and mouse control

        Parameters
        ----------
        numOfRegions : int, required
            Number of divisions for the main screen, should be 4, 9, 16 and so on

            Regions should be numbered starting from 0 which is the top left corner to bottom right corner,
            moving horizontally each increment and then start over from next row

        """

        self.numOfRegions = numOfRegions
        self.regionsCenters = self._getRegionCenters(self.numOfRegions)

    def _getRegionCenters(self, numOfRegions: int) -> list[int]:
        """private method to get the coordinates of each region's center in the main screen

        Parameters
        ----------
        numOfRegions : int, required
            Number of divisions for the main screen, defaults to 4 regions 

        Returns
        ----------
        list[int]: a list containing all regions' centers as int
            relative to the main screen only, ordered in the the standard order for the regions
        """
        self.screenGridSize = int(math.sqrt(self.numOfRegions))
        self.screenSize = {
            'width': pyautogui.size().width,
            'height': pyautogui.size().height
        }
        
        regionWidth = self.screenSize['width'] / self.screenGridSize
        regionHeight = self.screenSize['height'] / self.screenGridSize

        # center = (x,y)
        regionCenter = (int(regionWidth/2), int(regionHeight/2))

        centers = []
        for i in range(self.screenGridSize):
            heightCenter = regionCenter[1] + (i*regionHeight)
            for j in range(self.screenGridSize):
                widthCenter = regionCenter[0] + (j*regionWidth)
                centers.append((widthCenter, heightCenter))

        return centers

    def pointToRegion(self, regionNum: int) -> None:
        """Method to drive the mouse to point to the center of a specified region on the screen

        Parameters
        ----------
        regionNum : int, required
            the specific region number to center the mouse at (can be 0,1,2,3... depending on the number of regions) 

        Raises
        ----------
        IndexError: if the region number passed was larger than the available regions
        """

        if regionNum >= self.numOfRegions:
            raise IndexError(f"Region number is out of range of available regions specified in the class constructor, which is {self.numOfRegions} starting from 0")

        pyautogui.moveTo(self.regionsCenters[regionNum][0], self.regionsCenters[regionNum][1])

        

    @staticmethod
    def copy() -> None:
        """Copy selected text into clipboard
        """
        pyautogui.hotkey('ctrl', 'c')
    
    @staticmethod
    def paste() -> None:
        """paste wherever the I beam is from local clipboard
        """
        pyautogui.hotkey('ctrl', 'v')

    @staticmethod
    def setVolume(volumeLevel: int) -> None:
        """Set the system master volume to a specific number out of 100

        Parameters
        ----------
        volumeLevel : int, required
            The actual volume level to set in the system
        """
        pyvolume(level=volumeLevel)

    @staticmethod
    def arrowPress(arrowKey: str, presses: int = 1) -> None:
        """Simulate a press of keyboard arrow key 

        Parameters
        ----------
        arrowKey: str, required
            must be one of ('left', 'right', 'up', 'down') 

        presses : int, optional
            The number of times to simulate the keypress
            
            defaults to 1
        """
        pyautogui.press(arrowKey, presses=presses)

    @staticmethod
    def scrollUp(scrollAmount: int = 25) -> None:
        """Simulate a mouse scroll up event

        Parameters
        ----------
        scrollAmount: int, optional
            the amount of scrolling out of 100, defaults to 25  

        """
        pyautogui.scroll(scrollAmount)
    
    @staticmethod
    def scrollDown(scrollAmount: int = 25) -> None:
        """Simulate a mouse scroll down event

        Parameters
        ----------
        scrollAmount: int, optional
            the amount of scrolling out of 100, defaults to 25  

        """
        pyautogui.scroll(-scrollAmount)

    @staticmethod
    def volumeUp():
        if platform == "linux" or platform == "linux2":
        # linux
        elif platform == "darwin":