
@echo off
::设置7z的命令行程序路径
set zip7=D:\software\7-Zip\7z.exe
::设置压缩包保存路径
set Save=C:\Users\pan.ji\Desktop\testUser
::当天日期，备份文件名
set curdate=%date:~0,4%-%date:~5,2%-%date:~8,2%
::设置要打包压缩的文件夹
set file=C:\Users\pan.ji\Desktop\testUser\Jmeter\3rdparty
set n=1
::压缩命令 -xr!.svn过滤.svn文件夹
"%zip7%" a -tzip "%Save%\%curdate%-%n%.zip" "%file%" -mx0 -xr!.svn
echo  -------------第%n%次压缩-------------
::设置压缩次数
set m=3
:next
::设置要再次打包压缩的压缩包
set reZip=C:\Users\pan.ji\Desktop\testUser\%curdate%-%n%.zip

set /a n+=1
::压缩命令 -xr!.svn过滤.svn文件夹
"%zip7%" a  "%Save%\%curdate%-%n%.zip" "%reZip%" -mx0 -xr!.svn

set /a x=n-1
if %x% gtr 0  (del /f /s /q "%Save%\%curdate%-%x%.zip")

echo  -------------第%n%次压缩-------------

if  %n%==%m% pause
goto next

pause