# CSharpAutoIncrementBuild
Auto Increment C# Project with Python

With this two python files you can autoincremnet the build number of a c# project.
In my case I use this files in combilation with Jenkins.
The idea is this one:

  - I start a compilation with Jenkins.
  - Jenkins will lunch the "setversion.py" four times to all the foud ".cs" files.
  - The "setversion.py" get the current version from the ".cs" and it will change only the BuildNumber, the other (Major, Minor and Revision) will be kept the same as before.
  - The "set_package_version.py" do the same as the "setversion.py" but on the "Package.appxmanifest" insthead
  
On both the scripts, it's mandatory to provide: path + build number in command line like:

"Cpython.exe" .\setversion.py  "PATH" "BUILD_NUMBER"

You can of course use the general jenkins variable %BUILD_NUMBER% and do something like:

"Cpython.exe" .\setversion.py  "\AssemblyInfo.cs" %BUILD_NUMBER%

