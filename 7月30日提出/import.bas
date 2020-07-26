Const MyName As String = "Hashigodaka"
Const MyDir As String = "P:\tabiclient"
Private Sub ImportComponents()
    DeleteComponents
    For Each name In GetComponentNames()
        ThisWorkbook.VBProject.VBComponents.Import name
    Next name
End Sub
Private Sub DeleteComponents()
    Dim comp As Variant
    For Each comp In ThisWorkbook.VBProject.VBComponents
        If (comp.Type = 1 Or comp.Type = 2) And (Not comp.name = MyName) Then
            ThisWorkbook.VBProject.VBComponents.Remove comp
        End If
    Next comp
End Sub
Private Sub ExportComponents()
    Dim comp As Variant
    For Each comp In ThisWorkbook.VBProject.VBComponents
        Dim ext As String: ext = IIf(comp.Type = 1, "bas", IIf(comp.Type = 2, "cls", ""))
        If ext <> "" Then
            comp.Export MyDir & "\" & comp.name & ".vb." & ext
        End If
    Next comp
End Sub
Private Function GetComponentNames() As Collection
    Set GetComponentNames = New Collection
    On Error GoTo Err
    Dim buf As String, fileNo As Integer: fileNo = FreeFile
    Open MyDir & "\cmps.txt" For Input As #fileNo
    Line Input #fileNo, buf
    Close #fileNo
    Dim name
    For Each name In Split(buf, vbLf)
        Dim path As String: path = MyDir & "\" & name
        If name <> "" And Dir(path) <> "" Then
            GetComponentNames.Add path
        End If
    Next name
Err:

End Function