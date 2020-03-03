# import a function form another file
from myModule import myFunction
"""
A folder be a package folder in python when a __init__.py also be include in the folder. so when a folder or subfolder is created then also include the __init__.py file always.But nothing have to written into __init__.py file
"""  
# import the some_main_script file from package named MyMainPackage
from MyMainPackage import some_main_script
# import the my_sub_script file from subpackage named SubPackage
from MyMainPackage.SubPackage import my_sub_script


myFunction()

some_main_script.reportMain()

my_sub_script.subReport()
