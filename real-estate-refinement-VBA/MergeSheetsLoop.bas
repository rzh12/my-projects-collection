Attribute VB_Name = "Module20"
Sub 合併工作表_loop_for_local()
    '複製表頭
    Sheets(1).Select
    Worksheets.Add
    Sheets(1).Name = "Combined"
    Sheets(2).Activate
    Range("A1").EntireRow.Select
    Selection.Copy Destination:=Sheets(1).Range("A1")
    
    '複製除表頭外之表格_loop
    Dim J As Integer
    For J = 2 To Sheets.Count
        Sheets(J).Activate
        Range("A1").Select
        Selection.CurrentRegion.Select
        Selection.Offset(1, 0).Resize(Selection.Rows.Count - 1).Select
        Selection.Copy Destination:=Sheets(1).Range("A1048576").End(xlUp).Offset(1, 0)
    Next
    
End Sub

