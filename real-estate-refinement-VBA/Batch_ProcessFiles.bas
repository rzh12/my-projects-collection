Attribute VB_Name = "Module10"
Sub Procedure()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.XLS")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
            Sheets("¥DÀÉ").Select
            '·s¼W7Äæ¨Ã³]©wÄæ¦W
            Columns("BL:BL").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
            Columns("BW:BX").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
            Columns("CC:CD").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
            Columns("CG:CH").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
            Range("BL1").Value = "¬O§_½Òµ|"
            Range("BW1").Value = "©Ð«Î½Òµ|15%"
            Range("BX1").Value = "©Ð«Î½Òµ|10%"
            Range("CC1").Value = "¤g¦a½Òµ|15%"
            Range("CD1").Value = "¤g¦a½Òµ|10%"
            Range("CG1").Value = "¾P°â½Òµ|15%"
            Range("CH1").Value = "¾P°â½Òµ|10%"
            '§PÂ_0/1
                Dim N As Long
                N = 2
                Do While Cells(N, 1).Value <> ""
                '§PÂ_¬O§_½Òµ|
                    If Cells(N, "BK").Value <> "" Then
                        Cells(N, "BL").Value = 1
                    Else
                        Cells(N, "BL").Value = 0
                    End If
                '§PÂ_©Ð«Î½Òµ|
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
                '§PÂ_¤g¦a½Òµ|
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
                '§PÂ_¾P°â½Òµ|
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

            '¦sÀÉ¨ÃÃö³¬
            ActiveWorkbook.Save
            ActiveWorkbook.Close

       mFile = Dir()

    Loop
End Sub


