import platform
import winsound

def playSound(filePath):
		if platform.system() == "Windows":
			winsound.PlaySound(filePath,winsound.SND_ASYNC) # Windows, 2nd arg plays sound asynchroniously
		elif platform.system() == "Linux":
			os.system(f"aplay {filePath}&") # Linux, '&' plays sound asynchroniously
		elif platform.system() == "Darwin":
			os.system(f"afplay {filePath}&") # MacOs