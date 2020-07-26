Attribute VB_Name = "VaporPressure"
Sub antoineEq()

'Antoine�萔
Dim AN As Double
Dim BN As Double
Dim CN As Double
'���C��
Dim P0 As Double
'���x
Dim T As Double
'�ՊE���x
Dim Tc As Double
'�J��Ԃ���
Dim i As Integer

AN = Cells(5, 1).Value
BN = Cells(5, 2).Value
CN = Cells(5, 3).Value
Tc = Cells(5, 4).Value
T = Cells(5, 5).Value

For i = 1 To 1000

'Antoine�� (q1)
P0 = Exp(AN + BN / (T + CN))

'���xT�o�� (q2)
Cells(i + 8, 3) = T
'���C��P0�o�� (q3)
Cells(i + 8, 4) = P0 * 10 ^ (-6)


If Abs(Tc - T) < 20 Then
GoTo finish
Else
'���x�̍X�V(q4)

T = T + 5
End If

Next i
finish:

End Sub
