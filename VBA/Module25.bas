Attribute VB_Name = "Module25"
Sub 新增交易次數_loop()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.xlsx")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
           '新增一欄
            Columns("B:B").Insert CopyOrigin:=xlFormatFromLeftOrAbove
    
            '設定欄名
            Range("B1").Value = "交易次數"
            Range("B1").Font.Name = "微軟正黑體"
    
            '寫入公式並自動填滿
            Range("B2").Select
            ActiveCell.FormulaR1C1 = "=IF(R[-1]C[-1]=RC[-1],R[-1]C+1,1)"
            Selection.AutoFill Destination:=Range("B2:B" & [B2].CurrentRegion.Rows.Count)
    
            '新增一欄值貼上
            Columns("C:C").Insert CopyOrigin:=xlFormatFromLeftOrAbove
            Columns("B:B").Copy
            Columns("C:C").PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
                :=False, Transpose:=False
            Application.CutCopyMode = False
            Range("A1").Select
    
            '刪除B欄
            Columns("B:B").Delete Shift:=xlToLeft

            ActiveWorkbook.Save
            ActiveWorkbook.Close

        mFile = Dir()
    Loop
End Sub

