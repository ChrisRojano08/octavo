clear
clear all

shapesP = ['.','o','x','+','*','s','d','v','^','<','>','p','h'];
nVec = 7000;
aN=0;
bN=2.5;
P = [aN + (bN+bN)*rand(1),aN + (bN+bN)*rand(1)];
m = zeros(nVec,4);
for i=1:nVec
   rX = aN + (bN+bN)*rand(1);
   rY = aN + (bN+bN)*rand(1);
   m(i,1) = rX;
   m(i,2) = rY;
end

% Perceptron
for i=1: nVec
    subX = m(i,:);
    f1 = getActivation((subX(1).^2) + (subX(2).^2) + (-6*subX(1)) + (-4*subX(2)) +12);
    
    subX(4) = f1;
    
    %azul
    if f1==0
        subX(3) = 1;
    end
    
    m(i,:) = subX;
end

blues = m(m(:,3) == 1,:);
grays = m(m(:,3) == 0,:);

figure(200);
scatter( blues(:,1), blues(:,2), [], [0 0.4470 0.7410], 'filled');
hold on
scatter( grays(:,1), grays(:,2), [], [0.4660 0.4660 0.4660], 'filled');
hold on
scatter( 3, 2, [], [0 0 0], 'filled');
hold on

function [val] = getActivation(x)
    if x>0
       val=1; 
    else
       val=0; 
    end
end


