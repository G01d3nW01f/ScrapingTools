# Clone the Target Site.
##  use the useful module: pywebcopy

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
