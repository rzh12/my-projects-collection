Attribute VB_Name = "Module14"
Sub Cleanse()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.XLS")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
            '���R��
            Cells(Rows.Count, 1).End(xlUp).CurrentRegion.Clear
            '�s�ɨ�����
            ActiveWorkbook.Save
            ActiveWorkbook.Close
       mFile = Dir()
    Loop

End Sub
