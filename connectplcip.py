import clr
clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V16\PublicAPI\\V16\\Siemens.Engineering.dll')
from System.IO import DirectoryInfo, FileInfo
import Siemens.Engineering as tia
import Siemens.Engineering.HW.Features as hwf
import Siemens.Engineering.HW as hw
import Siemens.Engineering.Compiler as comp
import Siemens.Engineering.Download as dl
import os

#List Open TIA processes
processes = tia.TiaPortal.GetProcesses()
#for process in processes:
#    print(process.Attach().Projects[0].Path)
########################
mytia = processes[0].Attach()
myproject = mytia.Projects[0]

#List Devices in Project
n_interfaces = []
for device in myproject.Devices:
    #print(device)
    device_item_aggregation = device.DeviceItems[1].DeviceItems
    for DevItem in device_item_aggregation:
        print(DevItem.Name)
        network_service = tia.IEngineeringServiceProvider(DevItem).GetService[hwf.NetworkInterface]() 
        if type(network_service) is hwf.NetworkInterface:
            n_interfaces.append(network_service)


#plc = n_interfaces[0].Nodes[0]
#print(plc.ConnectedSubnet)
#subnet = plc.ConnectToSubnet("Siemens.Engineering.HW.Subnet")
#print(subnet)


#for interfaces in n_interfaces:
#    for node in interfaces.Nodes:
#        print(node.GetAttribute('Name'))
        
#print(n_interfaces[0].Nodes[0].Name)

#print(n_interfaces[0].Nodes[0].GetAttribute('Address'))