Attribute VB_Name = "Module16"
Sub �t�s���w�u�@��ܷs������ï_loop()
    Dim mFile As String
    mFile = Dir("D:\qqq\*.XLS")
    Do While mFile <> ""
       Workbooks.Open Filename:="D:\qqq\" & mFile
       
            '�ϥ�Copy��k��|�b����۰ʷӶ��ǥͦ�"����ï1"�B"����ï2"�B"����ï3"...���W�٪��s��
            '���ɨϥ�Save�K��H�ӷ�W�����x�s�A���|�������ɦW�����D
            '���������s�ͦ�������ï
            Worksheets("�ت����h").Activate
            ActiveSheet.Copy
            ActiveWorkbook.Save
            ActiveWorkbook.Close
            '�����쬡��ï
            ActiveWorkbook.Close
            
       mFile = Dir()
    Loop
End Sub
