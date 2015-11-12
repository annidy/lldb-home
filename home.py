#!/usr/bin/python

import lldb


homedir = None

def home(debugger, command, result, internal_dict):
    global homedir
    if homedir is None:
        frame = debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame()
        homedir = frame.EvaluateExpression("(char*)[NSHomeDirectory() UTF8String]").GetSummary()
    print >>result, homedir
    debugger.HandleCommand('platform shell open '+homedir)

# And the initialization code to add your commands 
def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f home.home home')
    print 'The "home" python command has been installed and is ready for use.'