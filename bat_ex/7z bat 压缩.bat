@echo off
Color a9
Del G:\林\代码\压缩\7zBAT压缩.rar
"C:\Program Files\7-Zip\7z.exe" a -t7z  G:\林\代码\压缩\7zBAT压缩.7z G:\林\代码\原代码\CLCTPolicy\3rdparty\DBProviderServerAndClient.pb.cc
Pause