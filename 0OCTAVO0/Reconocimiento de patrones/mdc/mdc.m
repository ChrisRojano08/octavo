clear
clear all

shapesP = ['.','o','x','+','*','s','d','v','^','<','>','p','h'];
P = [3,2];
%P = [4.2,1.8];
%P = [2,2.1];
%P = [1,4];
%P = [2.5,2.5];
kn = 5;

shMod = 9;
[n,t,r] = xlsread('data.xlsx');
[x, y] = size(n);
M = unique(n(:,y));
lases = cell(numel(M),1);
justD = n;
justD(:,y) = [];
for i=1: x
    lases{ find(M==n(i,y)) } = [ lases{find(M==n(i,y))} ; justD(i,:)];
end

[a, b] = size(lases);

nS = zeros(1,a);
sumP = zeros(a,3);
for i=1:x
    sumP(n(i,3),1) = sumP(n(i,3),1)+n(i,1);
    sumP(n(i,3),2) = sumP(n(i,3),2)+n(i,2);
    sumP(i,3) = i;
    
    nS(n(i,3)) = nS(n(i,3))+1;
end

for i=1:a
   sumP(i,1) = sumP(i,1)/nS(i);
   sumP(i,2) = sumP(i,2)/nS(i); 
end

figure(100);
for i=1: a
    plot( sumP(i,1), sumP(i,2), shapesP(i+shMod));
    hold on
end

dist = zeros(a,4);
for i=1: a
      dist(i,1) = sumP(i,1,1);
      dist(i,2) = sumP(i,2,1);
      dist(i,3) = sumP(i,3,1);
      
      dist(i,4) = sqrt( power(sumP(i,1,1)-P(1),2) + power(sumP(i,2,1)-P(2),2) );
end

sortedDists = sortrows(dist,4);
nearest = sortedDists(1,:);
fprintf('\n\nEl más cercano fue (%g,%g)\n',nearest(1),nearest(2));
fprintf('\n\nPor lo tanto el punto (%g,%g) pertenece a la clase %d\n',P(1),P(2),nearest(3));
plot( P(1), P(2), shapesP(nearest(3)+shMod), 'MarkerSize',7, 'LineWidth',1.5);




