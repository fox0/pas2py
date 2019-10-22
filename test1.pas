var
  k, t : int64;

begin
  readln(k, t);
  t := t mod (2 * k);
  if t <= k then
    writeln(t)
  else
    writeln(2 * k - t);
end.
