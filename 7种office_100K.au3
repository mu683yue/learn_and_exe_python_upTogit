#include <File.au3>
#include <MsgBoxConstants.au3>

Dim $TITLE[7]
Dim $FileName[7]
;doc文件
$TITLE[0] = "100Kdoc工作.doc [兼容模式] - Word"
$FileName[0] = "100Kdoc工作.doc"
;docx文件
$TITLE[1] = "100Kdocx工作.docx - Word"
$FileName[1] = "100Kdocx工作.docx"
;xls文件名
$TITLE[2] = "100Kxls工作.xls  [兼容模式] - Excel"
$FileName[2] = "100Kxls工作.xls"
;xlsx文件名
$TITLE[3] = "100K工作xlsx.xlsx - Excel"
$FileName[3] = "100K工作xlsx.xlsx"
;ppt文件名
$TITLE[4] = "100Kppt工作.ppt [兼容模式] - PowerPoint"
$FileName[4] = "100Kppt工作.ppt"
;pptx文件名
$TITLE[5] = "100Kpptx工作.pptx - PowerPoint"
$FileName[5] = "100Kpptx工作.pptx"
;pdf文件名
$TITLE[6] = "100Kdoc工作.pdf - Adobe Acrobat Reader DC"
$FileName[6] = "100Kdoc工作.pdf"

Test()
Func Test()
   FileDelete("filelog_100K.log")
   $sLogPath = @ScriptDir & "\filelog_100K.log";将结果默认保存至脚本所在路径

   For $n = 0 to 6 Step 1
	  ;文件打开3次，计算耗时
	  For $i = 1 to 3 Step 1
		 $begin = TimerInit();获得脚本执行到此行时的时间戳
		 ShellExecute($FileName[$n])
		 WinWait($TITLE[$n])
		 If WinExists($TITLE[$n]) Then
		    $dif = TimerDiff($begin) ;获得时间间隔
		    $time = $dif/1000
		    _FileWriteLog($sLogPath,"第" & $i & "次打开" & $FileName[$n] & "文件耗时：" & $time & "秒")
		    Local $hWnd = WinGetHandle($TITLE[$n])
		    WinClose($hWnd)
		    Sleep(2000)
		 Else
		    MsgBox($MB_SYSTEMMODAL, "Error", "未获取文件title，请检查！", 10)
		 EndIf
		 If @error Then
		 MsgBox($MB_SYSTEMMODAL, "", "An error occurred when trying to open the file")
		 _FileWriteLog($sLogPath, "stop=========stop")
		 Exit
		 EndIf
	  Next
   Next
   ;完毕
   MsgBox($MB_SYSTEMMODAL, "stop", "程序执行完毕", 10)
EndFunc