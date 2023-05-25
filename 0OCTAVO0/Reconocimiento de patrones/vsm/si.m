x1 = -10:0.1:10;

axis equal

x2 = x1 - x1;
plot(x1, x2);
hold on

x2 = x1 - 2;
plot(x1, x2);
hold on

x2 = -x1 + 1;
plot(x1, x2);
hold on

