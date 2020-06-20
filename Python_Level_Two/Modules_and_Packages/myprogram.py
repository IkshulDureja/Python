import mymodule
mymodule.func_in_module()

import mymodule as mm
mm.func_in_module()

from mymodule import func_in_module
func_in_module()

# not recommended because it waste a lot of memory importing everything with htis asterisks
from mymodule import *
func_in_module()
