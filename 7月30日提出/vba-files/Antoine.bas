Attribute VB_Name = "VaporPressure"
Sub antoineEq()

'Antoine定数
Dim AN As Double
Dim BN As Double
Dim CN As Double
'蒸気圧
Dim P0 As Double
'温度
Dim T As Double
'臨界温度
Dim Tc As Double
'繰り返し数
Dim i As Integer

AN = Cells(5, 1).Value
BN = Cells(5, 2).Value
CN = Cells(5, 3).Value
Tc = Cells(5, 4).Value
T = Cells(5, 5).Value

For i = 1 To 1000

'Antoine式 (q1)
P0 = Exp(AN + BN / (T + CN))

'温度T出力 (q2)
Cells(i + 8, 3) = T
'蒸気圧P0出力 (q3)
Cells(i + 8, 4) = P0 * 10 ^ (-6)


If Abs(Tc - T) < 20 Then
GoTo finish
Else
'温度の更新(q4)

T = T + 5
End If

Next i
finish:

End Sub
