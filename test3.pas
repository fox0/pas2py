var
  a, b, n, k : integer;

begin
  Readln(n);
  k := 0;
  a := 0;
  while (k = 0) and (a <= n div 3) do
  begin
    b := 0;
    while (k = 0) and (b <= n div 5) do
    begin
      if 3 * a + 5 * b = n then
      begin
        writeln(a, ' ', b);
        k := k + 1;
      end;
      b := b + 1
    end;
    a := a + 1
  end;
  if k = 0 then
    writeln('IMPOSSIBLE');
end.
