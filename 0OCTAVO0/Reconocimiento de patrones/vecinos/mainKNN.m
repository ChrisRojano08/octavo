clear
clear all

shapesP = ['.','o','x','+','*','s','d','v','^','<','>','p','h'];
%P = [3,2];
%P = [4.2,1.8];
%P = [2,2.1];
P = [1,4];
%P = [2.5,2.5];
kn = 5;
m = 2;

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
figure(100);
for i=1: a
    subX = lases{i,:};
    plot( subX(:,1), subX(:,2), shapesP(i+shMod));
    hold on
end


res01 = UKNN(n, P);
res02 = KNN(n, kn, P);
res03 = WKNN(n, kn, P);
res04 = FUZZYKNN(n, kn, P, m);

fprintf('\nPara 1-NN la clase es -> %d', res01{2});
plot( P(1), P(2), shapesP(res01{2}+shMod), 'MarkerSize',7, 'LineWidth',1.5);

fprintf('\nPara K-NN la clase es -> %d', res02{2});
plot( P(1), P(2), shapesP(res02{2}+shMod), 'MarkerSize',7, 'LineWidth',1.5);

fprintf('\nPara MK-NN la clase es -> %d', res03{2});
plot( P(1), P(2), shapesP(res03{2}+shMod), 'MarkerSize',7, 'LineWidth',1.5);

fprintf('\nPara Fuzzy-NN la clase es -> %d\n', res04{2});
plot( P(1), P(2), shapesP(res04{2}+shMod), 'MarkerSize',7, 'LineWidth',1.5);

