[Setup]
AppName=Moonlight Repacked
AppVersion=6.1.0
DefaultDirName={commonpf}\Moonlight Repacked
DefaultGroupName=Moonlight Repacked
OutputDir=.
OutputBaseFilename=MoonlightRepackedSetup-x64-6.1.0
Compression=lzma
SolidCompression=yes
[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
[Files]
Source: "..\build\deploy-x64-release\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "..\LICENSE"; DestDir: "{app}"; Flags: isreadme
[Icons]
Name: "{group}\Moonlight Repacked"; Filename: "{app}\Moonlight Repacked.exe"