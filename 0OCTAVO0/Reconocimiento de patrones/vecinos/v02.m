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
Ow = 0;

figure(100);
for i=1: a
    subX = lases{i,:};
    plot( subX(:,1), subX(:,2), shapesP(i+shMod));
    hold on
end

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
claseP = mode(KNN(:, (3) ) );
plot( P(1), P(2), shapesP(claseP+shMod) );

weigths = zeros(kn,1);
weightClass = zeros(a,1);
for i=1: kn
    wei = (KNN(kn,4)-KNN(i,4)) / (KNN(kn,4)-KNN(1,4)) ;
    weigths(i) = wei;
    
    weightClass(KNN(i,3)) = weightClass(KNN(i,3))+wei;
end
classMax = find(weightClass==max(weightClass));

fprintf('\nLos vecinos màs cercanos fueron\n');
fprintf('\nId | Coordenadas | Clase | Distancia | Peso');
for i=1:  kn
    fprintf('\n%d  | (%.2f,%.2f) | \t %d   |\t %.4f  | %.4f',KNN(i,5),KNN(i,1),KNN(i,2),KNN(i,3),KNN(i,4),weigths(i));
end
%disp(KNN);
fprintf('\n\nLa suma de los pesos fueron');
for i=1:a
   fprintf('\n%d -> %g',i,weightClass(i)); 
end
fprintf('\n\nPor lo tanto el punto (%g,%g) pertenece a la clase %d\n',P(1),P(2),classMax);
%fprintf('El menor fue para x(%g,%g) con %g de distancia en la clase %d\n',dist(idX,1),dist(idX,2),dist(idX,4),dist(idX,3));







