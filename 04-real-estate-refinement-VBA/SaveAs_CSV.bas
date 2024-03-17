Attribute VB_Name = "Module15"
Sub 另存為csv檔()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.XLS")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
            '另存成csv
            ActiveWorkbook.SaveAs _
                FileFormat:=xlCSV
            ActiveWorkbook.Close
       mFile = Dir()
    Loop


End Sub
