function [resp] = FUZZYKNN(n, kn, P, m)

[x, y] = size(n);
M = unique(n(:,y));
lases = cell(numel(M),1);
justD = n;
justD(:,y) = [];
for i=1: x
    lases{ find(M==n(i,y)) } = [ lases{find(M==n(i,y))} ; justD(i,:)];
end

[a, b] = size(lases);
dist = zeros(x,5);
for i=1: x
      dist(i,1) = n(i,1,1);
      dist(i,2) = n(i,2,1);
      dist(i,3) = n(i,3,1);
      
      dist(i,4) = sqrt( power(n(i,1,1)-P(1),2) + power(n(i,2,1)-P(2),2) );
      dist(i,5) = i;
end
sortedDists = sortrows(dist,4);
KNN = sortedDists(1:kn,:);

equi = zeros(1, a);
denominadorF = 0;
for i=1:a
    denominadorF = denominadorF + ( 1 / ( power(KNN(i,4), 2/m-1) ) );
    equi(KNN(i,3)) = equi(KNN(i,3)) + ( 1 / ( power(KNN(i,4), 2/m-1) ) );
end

for i=1:a
    equi(i) = equi(i) / denominadorF;
end

resp{1} = KNN;
resp{2} = find(equi == max(equi));
resp{3} = equi;





