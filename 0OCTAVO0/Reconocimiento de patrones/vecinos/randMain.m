clear
clear all

shapesP = ['.','o','x','+','*','s','d','v','^','<','>','p','h'];
kn = 5;
m = 2;

shMod = 6;
aN=0;
bN=3;

P = zeros(10,2);
for i=1:10
    P(i,1) = aN + (bN+bN)*rand(1);
    P(i,2) = aN + (bN+bN)*rand(1);
end
[n,t,r] = xlsread('data.xlsx');

[x, y] = size(n);
M = unique(n(:,y));
lases = cell(numel(M),1);
justD = n;
justD(:,y) = [];
for i=1: x
    lases{ find(M==n(i,y)) } = [ lases{find(M==n(i,y))} ; justD(i,:)];
end

% [a, b] = size(lases);
% figure(100);
% for i=1: a
%     subX = lases{i,:};
%     plot( subX(:,1), subX(:,2), shapesP(i+shMod));
%     hold on
% end

Ps = zeros(10,6);
for i=1:10
    res01 = UKNN(n, kn, P(i,:));
    res02 = KNN(n, kn, P(i,:));
    res03 = WKNN(n, kn, P(i,:));
    res04 = FUZZYKNN(n, kn, P(i,:), m);
    
    Ps(i,1) = P(i,1);
    Ps(i,2) = P(i,2);
    
    Ps(i,3) = res01{2};
    Ps(i,4) = res02{2};
    Ps(i,5) = res03{2};
    Ps(i,6) = res04{2};
end

% fprintf('\nPara 1-NN la clase es -> %d', res01{2});
% plot( P(1), P(2), shapesP(res01{2}+shMod), 'MarkerSize',7, 'LineWidth',1.5);
% 
% fprintf('\nPara K-NN la clase es -> %d', res02{2});
% plot( P(1), P(2), shapesP(res02{2}+shMod), 'MarkerSize',7, 'LineWidth',1.5);
% 
% fprintf('\nPara MK-NN la clase es -> %d', res03{2});
% plot( P(1), P(2), shapesP(res03{2}+shMod), 'MarkerSize',7, 'LineWidth',1.5);
% 
% fprintf('\nPara Fuzzy-NN la clase es -> %d\n', res04{2});
% plot( P(1), P(2), shapesP(res04{2}+shMod), 'MarkerSize',7, 'LineWidth',1.5);
