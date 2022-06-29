import clr
clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V16\PublicAPI\\V16\\Siemens.Engineering.dll')
from System.IO import DirectoryInfo, FileInfo
import Siemens.Engineering as tia
import Siemens.Engineering.HW.Features as hwf
import Siemens.Engineering.HW as hw
import Siemens.Engineering.Compiler as comp
import Siemens.Engineering.Download as dl
import os

processes = tia.TiaPortal.GetProcesses()
mytia = processes[1].Attach()
myproject = mytia.Projects[0]
plc = myproject.Devices[0].DeviceItems[1]
print(plc.Name)
software_container = tia.IEngineeringServiceProvider(plc).GetService[hwf.SoftwareContainer]()
software_base = software_container.Software
#comumfolder = software_base.BlockGroup.Groups[1]
plc_block = software_base.BlockGroup.Blocks.Find("MainFC")
plc_block.Export(FileInfo(r'C:\Users\Matheus\Documents\Codes\TIA_Addins\MainFC.xml'), tia.ExportOptions.WithDefaults)
#plc_block = software_base.BlockGroup.Blocks.Find("FB1_TESTES")
#plc_block.Export(FileInfo(r'C:\Users\Matheus\Documents\Codes\TIA_Addins\FB1.xml'), tia.ExportOptions.WithDefaults)
#print(dir(plc))

    
    
#software_container = tia.IEngineeringServiceProvider(PLC1.DeviceItems[1]).GetService[hwf.SoftwareContainer]()