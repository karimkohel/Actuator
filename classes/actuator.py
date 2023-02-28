import pyautogui
import os
from pyvolume import pyvolume


class Actuator():
    """Class containing all main methods of controlling a PC in the HTI context 
    """
    def __init__(self) -> None:
        pass

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