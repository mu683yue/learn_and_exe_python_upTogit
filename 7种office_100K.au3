#include <File.au3>
#include <MsgBoxConstants.au3>

Dim $TITLE[7]
Dim $FileName[7]
;doc�ļ�
$TITLE[0] = "100Kdoc����.doc [����ģʽ] - Word"
$FileName[0] = "100Kdoc����.doc"
;docx�ļ�
$TITLE[1] = "100Kdocx����.docx - Word"
$FileName[1] = "100Kdocx����.docx"
;xls�ļ���
$TITLE[2] = "100Kxls����.xls  [����ģʽ] - Excel"
$FileName[2] = "100Kxls����.xls"
;xlsx�ļ���
$TITLE[3] = "100K����xlsx.xlsx - Excel"
$FileName[3] = "100K����xlsx.xlsx"
;ppt�ļ���
$TITLE[4] = "100Kppt����.ppt [����ģʽ] - PowerPoint"
$FileName[4] = "100Kppt����.ppt"
;pptx�ļ���
$TITLE[5] = "100Kpptx����.pptx - PowerPoint"
$FileName[5] = "100Kpptx����.pptx"
;pdf�ļ���
$TITLE[6] = "100Kdoc����.pdf - Adobe Acrobat Reader DC"
$FileName[6] = "100Kdoc����.pdf"

Test()
Func Test()
   FileDelete("filelog_100K.log")
   $sLogPath = @ScriptDir & "\filelog_100K.log";�����Ĭ�ϱ������ű�����·��

   For $n = 0 to 6 Step 1
	  ;�ļ���3�Σ������ʱ
	  For $i = 1 to 3 Step 1
		 $begin = TimerInit();��ýű�ִ�е�����ʱ��ʱ���
		 ShellExecute($FileName[$n])
		 WinWait($TITLE[$n])
		 If WinExists($TITLE[$n]) Then
		    $dif = TimerDiff($begin) ;���ʱ����
		    $time = $dif/1000
		    _FileWriteLog($sLogPath,"��" & $i & "�δ�" & $FileName[$n] & "�ļ���ʱ��" & $time & "��")
		    Local $hWnd = WinGetHandle($TITLE[$n])
		    WinClose($hWnd)
		    Sleep(2000)
		 Else
		    MsgBox($MB_SYSTEMMODAL, "Error", "δ��ȡ�ļ�title�����飡", 10)
		 EndIf
		 If @error Then
		 MsgBox($MB_SYSTEMMODAL, "", "An error occurred when trying to open the file")
		 _FileWriteLog($sLogPath, "stop=========stop")
		 Exit
		 EndIf
	  Next
   Next
   ;���
   MsgBox($MB_SYSTEMMODAL, "stop", "����ִ�����", 10)
EndFunc