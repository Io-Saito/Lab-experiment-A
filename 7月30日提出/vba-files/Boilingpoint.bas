Attribute VB_Name = "BoilingPoint"
Sub bp()

'Antoine�萔
Dim AN As Double
Dim BN As Double
Dim CN As Double
'���x
Dim T As Double
'Newton�@
Dim fP As Double
Dim dfP As Double
'�J��Ԃ���
Dim i As Integer

AN = Cells(5, 1).Value
BN = Cells(5, 2).Value
CN = Cells(5, 3).Value
T = Cells(5, 4).Value

For i = 1 To 1000
'Newton�@�Ŏg����2��(q1,q2)
fP = 0.1013 - Exp(AN + BN / (T + CN)) * 10 ^ (-6)
dfP = BN / (T + CN) ^ 2 * Exp(AN + BN / (T + CN)) * 10 ^ (-6)
Cells(10,10)="Hello.world"


'Newton�@�Ŏg����������Ȃ�(q3-q7)
If Abs(fP / dfP) < 10 ^ (-6) Then
GoTo finish

Else
T = T - fP / dfP
End If
Next i
finish:

Cells(9, 3) = T
Cells(9, 4) = T - 273.15
Cells(9, 5) = i

End Sub


