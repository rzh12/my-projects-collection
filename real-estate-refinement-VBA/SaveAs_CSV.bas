Attribute VB_Name = "Module15"
Sub �t�s��csv��()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.XLS")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
            '�t�s��csv
            ActiveWorkbook.SaveAs _
                FileFormat:=xlCSV
            ActiveWorkbook.Close
       mFile = Dir()
    Loop


End Sub
