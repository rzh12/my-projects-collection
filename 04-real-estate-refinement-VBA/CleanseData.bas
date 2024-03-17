Attribute VB_Name = "Module14"
Sub Cleanse()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.XLS")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
            '表格刪除
            Cells(Rows.Count, 1).End(xlUp).CurrentRegion.Clear
            '存檔並關閉
            ActiveWorkbook.Save
            ActiveWorkbook.Close
       mFile = Dir()
    Loop

End Sub
