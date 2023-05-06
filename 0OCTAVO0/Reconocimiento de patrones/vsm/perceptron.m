clear
clear all

shapesP = ['.','o','x','+','*','s','d','v','^','<','>','p','h'];
nVec = 3000;
aN=0;
bN=1;
P = [aN + (bN+bN)*rand(1),aN + (bN+bN)*rand(1)];
n = zeros(nVec,6);
for i=1:nVec
   rX = aN + (bN+bN)*rand(1);
   rY = aN + (bN+bN)*rand(1);
   n(i,1) = rX;
   n(i,2) = rY;
end

for i=1: nVec
    subX = n(i,:);
    f1 = subX(1)-subX(2)-0.3;
    f2 = subX(2)-0.8;
    f3 = -subX(1)-subX(2)+1;
    
    subX(4) = f1;
    subX(5) = f2;
    subX(6) = f3;
    
    %azul
    if f1>0 && f2<0 && f3<0
        subX(3) = 2;
    end
    
    %rojo
    if f1<0 && f2<0 && f3>0
        subX(3) = 1;
    end
    
    %verde
    if f1<0 && f2>0 && f3<0
        subX(3) = 3;
    end
    
    
    
    n(i,:) = subX;
end

reds = n(n(:,3) == 1,:);
blues = n(n(:,3) == 2,:);
greens = n(n(:,3) == 3,:);
% grays = n(n(:,3) == 0,:);

scatter( blues(:,1), blues(:,2), [], 'blue', 'filled');
hold on
scatter( greens(:,1), greens(:,2), [], 'green', 'filled');
hold on
scatter( reds(:,1), reds(:,2), [], 'red', 'filled');
hold on
% 
% scatter( grays(:,1), grays(:,2), [], 'yellow', 'filled');
% hold on







function [colorC] = getColors(x)
    rng(x);
    % Generar tres números aleatorios distintos entre 0 y 1
    numeros_aleatorios = rand(1, 3);
    indice_permutacion = randperm(3);
    colorC = numeros_aleatorios(indice_permutacion);
end

