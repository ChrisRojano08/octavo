function [resp] = FUZZYKNN(KNN, kn, a, m)
equi = zeros(1, a);
denominadorF = 0;
for i=1:kn
    denominadorF = denominadorF + ( 1 / ( power(KNN(i,4), 2/m-1) ) +eps);
    equi(KNN(i,3)) = equi(KNN(i,3)) + ( 1 / ( power(KNN(i,4), 2/m-1) ) +eps);
end

for i=1:a
    equi(i) = equi(i) / denominadorF;
end

classFin = find(equi == max(equi));
resp{1} = KNN;
resp{2} = classFin(1);
resp{3} = equi;





