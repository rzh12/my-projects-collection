Attribute VB_Name = "Module21"
Sub �X�֬���ï_for_local()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.xlsx")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
       
       ActiveSheet.Copy _
        Before:=ThisWorkbook.Sheets("�u�@��1")
        
       Workbooks(mFile).Close

    mFile = Dir()
  Loop
End Sub


