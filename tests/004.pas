var
  A, B, L, P, Circle : Integer;
Begin
  WriteLn('Введите длину: ');
  ReadLn(A);
  WriteLn('Введите шириру: ');
  ReadLn(B);
  WriteLn('Введите дистанцию: ');
  ReadLn(L);
  P := (A + B) * 2;
  Circle := L div P;
  L := L - P * Circle;
  If (L <= B) then
    WriteLn('LEFT');
  If ((L > B) and (L <= (A + B))) then
    WriteLn('BOTTOM');
  If ((L > (A + B)) and (L <= (A + 2 * B))) then
    WriteLn('RIGHT');
  If ((L > A + 2 * B) and (L <= P)) then
    WriteLn('TOP');
End.
