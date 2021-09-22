import work
work.job('carpenter','gwarimpa','kuje')
work.job('Doctor','kubwa')
#from module_name import function_name
from work import job
job('lawyer','kuje')
#from module_name import function_name as fn
from work import job as j
j('teacher','gwagwalada')
#import module_name as mn
import work as wk
wk.job('pilot','state house')
#from module_name import *
from work import *
job('artist','lagos')
