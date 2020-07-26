Attribute VB_Name = "SaturatedDensity"
Sub PR()

'Antoine�萔
Dim AN As Double
Dim BN As Double
Dim CN As Double

'���x
Dim T As Double
'���C��������
Dim P0 As Double

'���q��[g/mol]�C�ՊE���x[K]�C�ՊE����[MPa]�C�ՊE����[Pa]�C�ΐS���q[-]
Dim Mw As Double
Dim Tc As Double
Dim MPc As Double
Dim Pc As Double
Dim w As Double

'�C�̒萔
Const R As Double = 8.314

'Peng-Robison��ԕ������e��p�����[�^
Dim Tr As Double
Dim AA As Double
Dim BB As Double
Dim aT As Double
Dim bT As Double
Dim aTc As Double
Dim bTc As Double
Dim m As Double
Dim alpha As Double

'�C����f(Z)�Af'(Z)�AZ
Dim fZv As Double
Dim dfZv As Double
Dim Zv As Double

'�C���̃����̐�[m3/mol]�Ɩ��x[g/cm3]
Dim Vv As Double
Dim rhov As Double

'�t����f(Z)�Af'(Z)�AZ
Dim fZl As Double
Dim dfZl As Double
Dim Zl As Double

'�t���̃����̐�[m3/mol]�Ɩ��x[g/cm3]
Dim Vl As Double
Dim rhol As Double

'For���ŗp����ϐ�
Dim i As Integer
Dim j As Integer
Dim k As Integer


'�p�����[�^�̓���
AN = Cells(5, 2).Value
BN = Cells(5, 3).Value
CN = Cells(5, 4).Value
Mw = Cells(5, 5).Value
Tc = Cells(5, 6).Value
MPc = Cells(5, 7).Value
Pc = MPc * 10 ^ 6
w = Cells(5, 8).Value
T = Cells(5, 9).Value


'5K刻みfor roop'
For i = 1 To 1000

'Antoine'
P0 = Exp(AN + BN / (T + CN))
    
'Peng-Robinson'
'Tr "Tr" [-]
Tr=T/Tc
'm "m"
m=0.37464 + 1.54226*w - 0.26992 * w ^ 2
'alpha "��"
alpha = (1 + m * (1- Tr ^ 0.5)) ^ 2
'aTc "a(Tc)"
aTc= 0.45724 * R ^ 2 *Tc ^ 2 / Pc
'bTc "b(Tc)"
bTc = 0.0778 * R * Tc /Pc
'aT "a"
aT=alpha * aTc
'bT "b"
bT=bTc
'AA "A"
AA = aT * P0 / (R ^2 * T ^2)
'BB "B"
BB = bT * P0 / (R * T)


'�t����Z
Zl = 0.0001

'�t���̖��x�v�Z�ENewton�@(q11�`19)
fZl=Zl ^ 3 -(1-BB)* Zl ^ 2 + (AA - 3*BB ^ 2　-2*BB)* Zl - (AA*BB-BB^2-BB^3)
dfZl= 3* Zl ^ 2 -2*(1-BB)*Zl + (AA -3*B^2-2*B)

If Abs(fZl / dfZl) < 10 ^ (-6) Then
GoTo finishl
Else 
Zl = Zl - fZl/dfZl
End If

finishl:
Vl = Zl * R * T / P0
rhol = Mw * 10 ^ -6 / Vl
Cells(8 + i, 5) = rhol


'�C����Z
Zv = 1000

'液相の密度計算Newton法(q20�`28)

fZv=Zv ^ 3 -(1-BB)* Zv ^ 2 + (AA - 3*BB ^ 2　-2*BB)* Zv - (AA*BB-BB^2-BB^3)
dfZv= 3* Zv ^ 2 -2*(1-BB)*Zv + (AA -3*B^2-2*B)

If Abs(fZv / dfZv) < 10 ^ (-6) Then
GoTo finishv
Else 
Zv = Zv - fZv/dfZv
End If


finishv:
Vv = Zv * R * T / P0
rhov = Mw * 10 ^ -6 / Vv
Cells(8 + i, 6) = rhov


Cells(8 + i, 3) = T
Cells(8 + i, 4) = P0 * 10 ^ (-6)


'�ՊE���xTc�Ƃ̍���20���ɂȂ�����v�Z����߂�
'���x��5��������B(q29�`33)
If abs(T-Tc)<20 Then 
GoTo finish
Else 
T = T +5
End If

Next i
finish:

End Sub
