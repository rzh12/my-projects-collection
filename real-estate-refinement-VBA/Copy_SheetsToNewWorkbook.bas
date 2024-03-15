Attribute VB_Name = "Module16"
Sub 另存指定工作表至新的活頁簿_loop()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.XLS")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
       
            '使用Copy方法後會在此刻自動照順序生成"活頁簿1"、"活頁簿2"、"活頁簿3"...之名稱的新檔
            '此時使用Save便能以該當名直接儲存，不會有重複檔名的問題
            '之後關閉新生成的活頁簿
            Worksheets("建物分層").Activate
            ActiveSheet.Copy
            ActiveWorkbook.Save
            ActiveWorkbook.Close
            '關閉原活頁簿
            ActiveWorkbook.Close
            
       mFile = Dir()
    Loop
End Sub
