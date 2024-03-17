Attribute VB_Name = "Module22"
Sub 合併相同值的連續儲存格()
    
    '關閉警示
    Application.DisplayAlerts = False
    
    Dim intRow As Variant
    Dim i As Long
    
    '用 With...End With 省略所有出現在.之前的"ActiveSheet"
    'intRow 回傳"列數"
    '從最後一列到第2列 每次前進-1步
    With ActiveSheet
        intRow = .Range("A1").End(xlDown).Row
        For i = intRow To 2 Step -1
            If .Cells(i, "B").Value = .Cells(i - 1, "B").Value Then
                .Range(.Cells(i - 1, "B"), .Cells(i, "B")).Merge
            End If
        Next
    End With
    
    Application.DisplayAlerts = True
            
End Sub
