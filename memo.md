# Clone the Target Site.
##  use the useful module: pywebcopy


why I have to tried the programming to web clone? 
let me use the fucking useful module please.

if that's not there, I will give up and make by my self

however now that is here, 
okay stop the wank, go back the job 


LINK: https://www.geeksforgeeks.org/how-to-clone-webpage-using-pywebcopy-in-python/

```
Install: pip3 install pywebcopy
```

#Sample:

```
from pywebcopy import save_webpage

kwargs = {'project_name': 'site folder'}

save_webpage(
	
	# url pf the website
	url='https://www.geeksforgeeks.org/data-structures/linked-list/',
	
	# folder where the copy will be saved
	project_folder='F:/ro/geek',
	**kwargs
)

```
