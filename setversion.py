#https://heejune.me/2017/09/22/tip-python-snippet-increases-the-uwp-product-version/

#"\Applications\Client\BaseLib\Properties\AssemblyInfo.cs"
#"\Applications\Client\ControlsLib\Properties\AssemblyInfo.cs"
#"\Applications\Client\Client\Properties\AssemblyInfo.cs"
#"\Applications\Shared\CoreLib\Properties\AssemblyInfo.cs"

import re
import sys

#input "file" "buildversion"

def set_version(infocs, target_version):
    if not infocs or not target_version:
        raise Exception('invalid param')
        
    with open(infocs, "r+") as f:
        assemblyinfo_cs = f.read()

        #TODO modificare questo comando per fare in modo di modificare solo un parametro e non l'intero buildnumber

        pattern_1 = re.compile(r'AssemblyVersion\("[0-9]+(\.([0-9]+|\*)){1,3}"\)', re.MULTILINE)
        pattern_2 = re.compile(r'AssemblyFileVersion\("[0-9]+(\.([0-9]+|\*)){1,3}"\)', re.MULTILINE)

        #Leggo i parametri attuali dal file .cs in ingresso

        version_search = re.search('AssemblyVersion\(\"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)"\)', assemblyinfo_cs, re.IGNORECASE)

        if version_search:
            MajorVersion    = version_search.group(1)
            MinorVersion    = version_search.group(2)
            BuildNumber     = version_search.group(3)
            Revision        = version_search.group(4)
            
            #compongo la stringa

            BuildNumber  = target_version

            newAssemblyVersion =  MajorVersion + "." + MinorVersion + "." + BuildNumber + "." + Revision 
            newAssemblyFileVersion =  MajorVersion + "." + MinorVersion + "." + BuildNumber + "." + Revision 


            sub1 = r'AssemblyVersion("{}")'.format(newAssemblyVersion)
            sub2 = r'AssemblyFileVersion("{}")'.format(newAssemblyFileVersion)
            
            phase_1 = re.sub(pattern_1, sub1, assemblyinfo_cs)
            phase_2 = re.sub(pattern_2, sub2, phase_1)

            print("File version updated to " + newAssemblyVersion )
        
        f.seek(0)
        f.write(phase_2)
        f.truncate()



if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        raise Exception ( "BMLauncher Module", "Some or all parameters are missing" )
    
    try:
        dataDict = dict()
      
        dataDict['assemblyInfo_path'] = sys.argv[1] #AssemblyInfo
        dataDict['build_number'] = sys.argv[2]

        #need to replace only the thrid value
        #[assembly: AssemblyVersion("10.2.180.0")]
        #[assembly: AssemblyFileVersion("10.2.180.0")]

        set_version(dataDict['assemblyInfo_path'],dataDict['build_number'])

    except Exception as e:
        msg = str()
        for s in e.args:
            msg += ",\t"
            msg += s
        print( 'Something has stopped the building task:\n\t' + msg )
        sys.exit("Some error has occured: setversion.py, Main")
        pass
        
else:
    dummyinput = input( "No configuration file has been found, no way to continue..." )
