Sub DecodeBase64()
 For Each cell In Selection
 cell.Value = Base64DecodeString(cell.Value)
 Next
End Sub
Sub EncodeBase64()
 For Each cell In Selection
 cell.Value = Base64EncodeString(cell.Value)
 Next
End Sub