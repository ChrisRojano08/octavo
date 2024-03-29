clear
clear all

shapesP = ['.','o','x','+','*','s','d','v','^','<','>','p','h'];
nVec = 10;
aN=0;
bN=5;
P = [aN + (bN+bN)*rand(1),aN + (bN+bN)*rand(1)];
n = zeros(nVec,4);
for i=1:nVec
   rX = aN + (bN+bN)*rand(1);
   rY = aN + (bN+bN)*rand(1);
   n(i,1) = rX;
   n(i,2) = rY;
end


for i=1: nVec
    subX = n(i,:);
    f = subX(1)+subX(2)-10;
    subX(4) = f;
    
    if f>0
        subX(3) = 1;
    end
    n(i,:) = subX;
end

blues = n(n(:,3) == 1,:);
greens = n(n(:,3) == 0,:);

scatter( blues(:,1), blues(:,2), [], 'blue', 'filled');
hold on
scatter( greens(:,1), greens(:,2), [], 'green', 'filled');
hold on








function [colorC] = getColors(x)
    rng(x);
    % Generar tres números aleatorios distintos entre 0 y 1
    numeros_aleatorios = rand(1, 3);
    indice_permutacion = randperm(3);
    colorC = numeros_aleatorios(indice_permutacion);
end

