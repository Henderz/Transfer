
import ctypes
import os
#my_dll = ctypes.CDLL('D:\\DeveloperStuff\\Cpp\\Microphone_Info\\x64\\Release\\Microphone_Info_DLL.dll')  
my_dll = ctypes.CDLL(f"{os.getcwd()}\\Microphone_Info_DLL.dll")  
my_dll.getMicUsage_JSON.restype = ctypes.c_char_p
result = my_dll.getMicUsage_JSON()
result_str = result.decode('utf-8')

import json
print(json.loads(result_str))

#
#import ctypes
#
## Load the DLL
##my_dll = ctypes.CDLL('D:\\DeveloperStuff\\Python\\WindowsAutomations\\Microphone_Info\\Microphone_Info_DLL.dll') 
#
#my_dll = ctypes.CDLL('D:\\DeveloperStuff\\Cpp\\Microphone_Info\\x64\\Release\\Microphone_Info_DLL.dll')  
#
## Define the MicrophoneDataHandle type
#MicrophoneDataHandle = ctypes.c_void_p
#
## Define the return type for the functions
#my_dll.getMicrophoneUsageStats.restype = MicrophoneDataHandle
#
#my_dll.printMicUsageStats_JSON.argtypes = [MicrophoneDataHandle]
#
## Call the function to get microphone usage stats
#microphone_data = my_dll.getMicrophoneUsageStats()
## Call the function to print microphone usage stats
#my_dll.printMicUsageStats_JSON(microphone_data)
#
#
#
#
#
#import ctypes
#my_dll = ctypes.CDLL('D:\\DeveloperStuff\\Cpp\\Microphone_Info\\x64\\Release\\Microphone_Info_DLL.dll')  
#my_dll.getMicrophoneUsageStatsJsonWrapper.restype = ctypes.c_char_p
#json_str = my_dll.getMicrophoneUsageStatsJsonWrapper()
#print(json_str)
#
#json_str = my_dll.getMicrophoneUsageStatsJsonWrapper().decode('utf-8')
## Parse the JSON string
#microphone_json = json.loads(json_str)
#
## Now, you can work with the JSON data in Python
#print(microphone_json)
#
#import ctypes
#my_dll = ctypes.CDLL('D:\\DeveloperStuff\\Cpp\\Microphone_Info\\x64\\Release\\Microphone_Info_DLL.dll')  
#my_dll.get_greeting.restype = ctypes.c_char_p
#result = my_dll.get_greeting()
#result_str = result.decode('utf-8')
#print(result_str)
#
#import ctypes
#my_dll = ctypes.CDLL('D:\\DeveloperStuff\\Cpp\\Microphone_Info\\x64\\Release\\Microphone_Info_DLL.dll')  
#my_dll.getMicUsage_JSON.restype = ctypes.c_char_p
#result = my_dll.getMicUsage_JSON()
#result_str = result.decode('utf-8')
#print(result_str)
#
#
##
### Define the MicrophoneDataHandle type
##MicrophoneDataHandle = ctypes.c_void_p
##
### Declare the function prototype
##get_mic_usage_stats_json = my_dll.getMicUsageStats_JSON
##get_mic_usage_stats_json.restype = ctypes.c_char_p  # The return type is a C string (char*)
##
### Call the function to get the microphone usage stats as JSON
##mic_data_handle = my_dll.getMicrophoneUsageStats()
##json_string = get_mic_usage_stats_json(mic_data_handle)
##
### Convert the C string to a Python string
##json_string = json_string.decode('utf-8')
##
### Print or use the JSON string as needed
##print(json_string)
##
### Remember to free the memory allocated by the C code
###mic_stats_dll.freeMicData.argtypes = [MicrophoneDataHandle]
###mic_stats_dll.freeMicData(mic_data_handle)