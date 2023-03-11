var
  a, b, c, n, x, y, z, d : int64;

begin
  Readln(a, b, c, n);
  d := (a + b + c + n) div 4;
  if (a > 2 * d) or (b > d) or (c > d) then
    writeln(0)
  else
  begin
    writeln(2 * d - a);
    writeln(d - b);
    writeln(d - c)
  end;
end.
