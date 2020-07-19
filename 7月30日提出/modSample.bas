Attribute VB_Name = "modSample"

Option Explicit


Sub dispOS()
  Dim nameOS As String 
  nameOS = Application.OperatingSystem

  If nameOS Like "Windows *" Then
    ' Windows (32-bit) NT 6.01
    MsgBox "you have Windows OS. [" & nameOS & "]"
 
  ElseIf nameOS Like "Macintosh *" Then
    ' Macintosh (Intel) 10.8
    MsgBox "This is Mac OS X. hello apple [" & nameOS & "]"

  End If
End Sub


Sub dispVersion()
  MsgBox Application.Version
End Sub

