var
  d, c : string;
  k : integer;

begin
  Readln(d);
  k := length(d);
  c := copy(d, k - 1, 2);
  delete(d, k - 1, 2);
  if c <> '00' then
  begin
    k := length(d);
    while (k > 0) and (d[k] = '9') do
    begin
      d[k] := '0';
      k := k - 1
    end;
    if k = 0 then
      d := '1' + d
    else
      d[k] := succ(d[k])
  end;
  writeln(d)
end.
