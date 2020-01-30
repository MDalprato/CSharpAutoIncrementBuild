#https://heejune.me/2017/09/22/tip-python-snippet-increases-the-uwp-product-version/

#"\Applications\Client\Client\Package.appxmanifest"


import re
import sys

#input "file" "buildversion"

def set_version(infocs, target_version):
    if not infocs or not target_version:
        raise Exception('invalid param')
        
    with open(infocs, "r+") as f:
        appxmanifest_path_cs = f.read()

        #TODO modificare questo comando per fare in modo di modificare solo un parametro e non l'intero buildnumber

        pattern_1 = re.compile(r'\s(Version=\"([0-9]+).([0-9]+).([0-9]+).([0-9]+)\")', re.MULTILINE)

        #Leggo i parametri attuali dal file .cs in ingresso

        version_search = re.search('\s(Version=\"([0-9]+).([0-9]+).([0-9]+).([0-9]+)\")', appxmanifest_path_cs, re.IGNORECASE)

        if version_search:
            MajorVersion    = version_search.group(2)
            MinorVersion    = version_search.group(3)
            BuildNumber     = version_search.group(4)
            Revision        = version_search.group(5)
            
 
            #compongo la stringa

            BuildNumber  = target_version

            newAssemblyVersion =  MajorVersion + "." + MinorVersion + "." + BuildNumber + "." + Revision 

            print(newAssemblyVersion)
            sub1 = r' Version="{}"'.format(newAssemblyVersion)
            
            phase_1 = re.sub(pattern_1, sub1, appxmanifest_path_cs)

            print("File version updated to " + newAssemblyVersion )
        
            f.seek(0)
            f.write(phase_1)
            f.truncate()



if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        raise Exception ( "BMLauncher Module", "Some or all parameters are missing" )
    
    try:
        dataDict = dict()
      
        dataDict['appxmanifest_path'] = sys.argv[1] #AssemblyInfo
        dataDict['build_number'] = sys.argv[2]

        #need to replace only the thrid value
        #[assembly: AssemblyVersion("10.2.180.0")]
        #[assembly: AssemblyFileVersion("10.2.180.0")]

        set_version(dataDict['appxmanifest_path'],dataDict['build_number'])

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
