var i, n, k, k1, kdel: LongInt;
begin
 write ('n, k (через пробел) = ');
 readln (n, k);
 k1:=0;
 kdel:=-1;
 for i:=1 to n do
 begin
 if n mod i = 0 then inc(k1);
 if (n mod i = 0) and (k1 = k) then kdel:=i;
 end;
 writeln (kdel);
end.
