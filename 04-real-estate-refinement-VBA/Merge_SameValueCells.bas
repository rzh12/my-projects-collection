Attribute VB_Name = "Module22"
Sub �X�֬ۦP�Ȫ��s���x�s��()
    
    '����ĵ��
    Application.DisplayAlerts = False
    
    Dim intRow As Variant
    Dim i As Long
    
    '�� With...End With �ٲ��Ҧ��X�{�b.���e��"ActiveSheet"
    'intRow �^��"�C��"
    '�q�̫�@�C���2�C �C���e�i-1�B
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
