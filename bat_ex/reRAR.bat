
@echo off
::����7z�������г���·��
set tar=C:\Program Files\WinRAR\WinRAR.exe
::����ѹ��������·��
set Save=G:\��\����\ѹ��
::�������ڣ������ļ���
set curdate=%date:~0,4%-%date:~5,2%-%date:~8,2%
::����Ҫ���ѹ�����ļ���

set file=G:\��\����\ԭ����\CLCTPolicy\3rdparty
set n=1
::ѹ������ -xr!.svn����.svn�ļ���
"%tar%" a  "%Save%\%curdate%-%n%.rar" "%file%"  -xr!.svn
echo  -------------��%n%��ѹ��-------------

::����ѹ������
set m=3
:next
::����Ҫ�ٴδ��ѹ����ѹ����
set reZip=G:\��\����\ѹ��\%curdate%-%n%.rar
echo %n%
echo %reZip%

set /a n+=1
::ѹ������ -xr!.svn����.svn�ļ���
"%tar%" a  "%Save%\%curdate%-%n%.rar" "%reZip%"  -xr!.svn

set /a x=n-1
if %x% gtr 0  (del /f /s /q "%Save%\%curdate%-%x%.rar")

echo  -------------��%n%��ѹ��-------------

if  %n%==%m% pause
goto next

pause