from pip._internal import main as pip

failed = []
try:
    
    pip(['install', 'install-requires[datetime]'])
    
except:
    failed += ["datetime"]
    pass
try:
    
    pip(['install', 'install-requires[os]'])
except:
    failed += ["os"]
    pass
try:
    
    pip(['install', 'install-requires[discord]'])
except:
    failed += ["discord"]
    pass
try:
    
    pip(['install', 'install-requires[asyncio]'])
except:
    failed += ["asyncio"]
    pass
try:
    pip(['install', 'install-requires[colorama]'])
    
except:
    failed += ["colorama"]
    pass
try:
    pip(['install', 'install-requires[discord-py-slash-command]'])
except:
    failed += ["discord-py-slash-command"]
    pass
try:
    pip(['install', 'install-requires[discord.py]'])
except:
    failed += ["discord.py"]
    pass
try:
    pip(['install', 'install-requires[urllib.request]'])
except:
    failed += ["urllib.request"]
    pass
try:
    
    pip(['install', 'install-requires[Image]'])
except:
    failed += ["Image"]
    pass
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
if not failed:
    for i in range(1):
        print(Fore.GREEN + 'Successfully installed all the modules!')
        print(Fore.RED + 'You may close the program.')
        time.sleep(3)
else:
    print(Fore.CYAN + "Installed all the modules possible, these modules may have already been installed or there was an issue installing them: "+ str(failed))
    time.sleep(5)






