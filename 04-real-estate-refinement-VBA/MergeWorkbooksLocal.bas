Attribute VB_Name = "Module21"
Sub 合併活頁簿_for_local()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.xlsx")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
       
       ActiveSheet.Copy _
        Before:=ThisWorkbook.Sheets("工作表1")
        
       Workbooks(mFile).Close

    mFile = Dir()
  Loop
End Sub


