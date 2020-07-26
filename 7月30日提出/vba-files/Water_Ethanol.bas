Sub Water_Ethanol()
'Antoine定数 (Ethanol)
Dim AN1 As Double
Dim BN1 As Double
Dim CN1 As Double
'Antoine定数 (Water)
Dim AN2 As Double
Dim BN2 As Double
Dim CN2 As Double

'活量係数
Dim gamma1 As Double
Dim gamma2 As Double
'Margules定数
Dim AM As Double
Dim BM As Double

'はさみうち法に用いる3つの温度
Dim TH As Double
Dim TL As Double
Dim TM As Double

'エタノール(1)および水(2)の組成
Dim x1 As Double
Dim x2 As Double

'はさみうち法の際のTLおよびTHにおける蒸気圧および全圧
Dim PL1 As Double
Dim PL2 As Double
Dim fPL As Double
Dim PH1 As Double
Dim PH2 As Double
Dim fPH As Double

'はさみうち法の際のTMにおける蒸気圧および全圧

Dim PM1 As Double
Dim PM2 As Double
Dim fPM As Double

'For文で用いる変数（整数）
Dim i As Integer
Dim j As Integer

'パラメータの入力
AN1 = Cells(5, 2).Value
BN1 = Cells(5, 3).Value
CN1 = Cells(5, 4).Value

AN2 = Cells(6, 2).Value
BN2 = Cells(6, 3).Value
CN2 = Cells(6, 4).Value

AM = Cells(5, 5).Value
BM = Cells(5, 6).Value

x1 = 0

For i = 1 To 1000
'初期温度TLおよびTH（K単位）(q1-2)
TL = Cells(5, 7).Value
TH = Cells(6, 7).Value

x2 = 1 - x1

'Margules式
gamma1 = Exp(x2 ^ 2 * (AM + 2 * (BM - AM) * x1))
gamma2 = Exp(x1 ^ 2 * (BM + 2 * (AM - BM) * x2))

For j = 1 To 1000
'TLにおける各成分蒸気圧(PL1, PL2)，および大気圧と全圧の差(fPL)(q3-5)
PL1 = Exp(AN1 + BN1 / (TL + CN1))
PL2 = Exp(AN2 + BN2 / (TL + CN2))
fPL = 0.1013 - ((PL1 * gamma1 * x1 + PL2 * gamma2 * x2) * 10 ^ (-6))
'THにおける各成分蒸気圧(PH1, PH2)，および大気圧と全圧の差(fPH)(q6-8)
PH1 = Exp(AN1 + BN1 / (TH + CN1))
PH2 = Exp(AN2 + BN2 / (TH + CN2))
fPH = 0.1013 - ((PH1 * gamma1 * x1 + PH2 * gamma2 * x2) * 10 ^ (-6))
'TMの算出 (q9)
TM = (TH - TL) * fPL / (fPL - fPH) + TL
 
'TMにおける各成分蒸気圧(PM1, PM2)，および大気圧と全圧の差(fPM) (q10-12)
PM1 = Exp(AN1 + BN1 / (TM + CN1))
PM2 = Exp(AN2 + BN2 / (TM + CN2))
fPM = 0.1013 - ((PM1 * gamma1 * x1 + PM2 * gamma2 * x2) * 10 ^ (-6))

'はさみうち法
If Abs(fPM) < 1E-06 Then
TM = TM
GoTo finish
ElseIf fPH * fPM < 0 Then
'(どちらかの点の更新q13)
TL = TM
ElseIf fPH * fPM > 0 Then
'(どちらかの点の更新q14)
TH = TM
End If

Next j

finish:
Cells(10 + i, 3) = x1
Cells(10 + i, 4) = TM
Cells(10 + i, 5) = TM - 273.15
Cells(10 + i, 6) = j


'データ出力　(q15-18)

If x1 < 1 Then
x1 = x1 + 0.05
End If

Next i


End Sub




