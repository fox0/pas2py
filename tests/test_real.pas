{ https://github.com/Altairkin/pas2py/blob/patch-1/228 }

var
  A, B: real;

begin
  { -- Ввод данных -- }
  writeln('Введите положительные числа A и B (A > B):');
  write(' A = ');
  readln(A);
  write(' B = ');
  readln(B);
  { -- Основная программа -- }
  while A >= B do { <-- пока A ≥ B }
    A := A - B; { <== уменьшаем число A на B }
  writeln('Длина незанятой части отрезка A: ', A);
end.
