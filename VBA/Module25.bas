Attribute VB_Name = "Module25"
Sub �s�W�������_loop()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.xlsx")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
           '�s�W�@��
            Columns("B:B").Insert CopyOrigin:=xlFormatFromLeftOrAbove
    
            '�]�w��W
            Range("B1").Value = "�������"
            Range("B1").Font.Name = "�L�n������"
    
            '�g�J�����æ۰ʶ�
            Range("B2").Select
            ActiveCell.FormulaR1C1 = "=IF(R[-1]C[-1]=RC[-1],R[-1]C+1,1)"
            Selection.AutoFill Destination:=Range("B2:B" & [B2].CurrentRegion.Rows.Count)
    
            '�s�W�@��ȶK�W
            Columns("C:C").Insert CopyOrigin:=xlFormatFromLeftOrAbove
            Columns("B:B").Copy
            Columns("C:C").PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
                :=False, Transpose:=False
            Application.CutCopyMode = False
            Range("A1").Select
    
            '�R��B��
            Columns("B:B").Delete Shift:=xlToLeft

            ActiveWorkbook.Save
            ActiveWorkbook.Close

        mFile = Dir()
    Loop
End Sub

