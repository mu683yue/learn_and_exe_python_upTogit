
@echo off
::����7z�������г���·��
set zip7=D:\software\7-Zip\7z.exe
::����ѹ��������·��
set Save=C:\Users\pan.ji\Desktop\testUser
::�������ڣ������ļ���
set curdate=%date:~0,4%-%date:~5,2%-%date:~8,2%
::����Ҫ���ѹ�����ļ���
set file=C:\Users\pan.ji\Desktop\testUser\Jmeter\3rdparty
set n=1
::ѹ������ -xr!.svn����.svn�ļ���
"%zip7%" a -tzip "%Save%\%curdate%-%n%.zip" "%file%" -mx0 -xr!.svn
echo  -------------��%n%��ѹ��-------------
::����ѹ������
set m=3
:next
::����Ҫ�ٴδ��ѹ����ѹ����
set reZip=C:\Users\pan.ji\Desktop\testUser\%curdate%-%n%.zip

set /a n+=1
::ѹ������ -xr!.svn����.svn�ļ���
"%zip7%" a  "%Save%\%curdate%-%n%.zip" "%reZip%" -mx0 -xr!.svn

set /a x=n-1
if %x% gtr 0  (del /f /s /q "%Save%\%curdate%-%x%.zip")

echo  -------------��%n%��ѹ��-------------

if  %n%==%m% pause
goto next

pause