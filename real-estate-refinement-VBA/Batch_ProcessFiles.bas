Attribute VB_Name = "Module10"
Sub Procedure()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.XLS")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
            Sheets("�D��").Select
            '�s�W7��ó]�w��W
            Columns("BL:BL").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
            Columns("BW:BX").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
            Columns("CC:CD").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
            Columns("CG:CH").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
            Range("BL1").Value = "�O�_�ҵ|"
            Range("BW1").Value = "�Ыνҵ|15%"
            Range("BX1").Value = "�Ыνҵ|10%"
            Range("CC1").Value = "�g�a�ҵ|15%"
            Range("CD1").Value = "�g�a�ҵ|10%"
            Range("CG1").Value = "�P��ҵ|15%"
            Range("CH1").Value = "�P��ҵ|10%"
            '�P�_0/1
                Dim N As Long
                N = 2
                Do While Cells(N, 1).Value <> ""
                '�P�_�O�_�ҵ|
                    If Cells(N, "BK").Value <> "" Then
                        Cells(N, "BL").Value = 1
                    Else
                        Cells(N, "BL").Value = 0
                    End If
                '�P�_�Ыνҵ|
                    If Cells(N, "BU").Value <> 0 And Cells(N, "BU").Value <> "" Then
                        Cells(N, "BW").Value = 1
                    Else
                        Cells(N, "BW").Value = 0
                    End If
        
                    If Cells(N, "BV").Value <> 0 And Cells(N, "BV").Value <> "" Then
                        Cells(N, "BX").Value = 1
                    Else
                        Cells(N, "BX").Value = 0
                    End If
                '�P�_�g�a�ҵ|
                    If Cells(N, "CA").Value <> 0 And Cells(N, "CA").Value <> "" Then
                        Cells(N, "CC").Value = 1
                    Else
                        Cells(N, "CC").Value = 0
                    End If
        
                    If Cells(N, "CB").Value <> 0 And Cells(N, "CB").Value <> "" Then
                        Cells(N, "CD").Value = 1
                    Else
                        Cells(N, "CD").Value = 0
                    End If
                '�P�_�P��ҵ|
                    If Cells(N, "CE").Value <> 0 And Cells(N, "CE").Value <> "" Then
                        Cells(N, "CG").Value = 1
                    Else
                        Cells(N, "CG").Value = 0
                    End If
        
                    If Cells(N, "CF").Value <> 0 And Cells(N, "CF").Value <> "" Then
                        Cells(N, "CH").Value = 1
                    Else
                    Cells(N, "CH").Value = 0
                    End If

                N = N + 1
        
                Loop

            '�s�ɨ�����
            ActiveWorkbook.Save
            ActiveWorkbook.Close

       mFile = Dir()

    Loop
End Sub


