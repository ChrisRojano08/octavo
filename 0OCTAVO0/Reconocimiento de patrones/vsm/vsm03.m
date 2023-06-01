clear
clear all

shapesP = ['.','o','x','+','*','s','d','v','^','<','>','p','h'];
nVec = 3;
aN=-3;
bN=3;
P = [aN + (bN+bN)*rand(1),aN + (bN+bN)*rand(1)];
m = zeros(nVec,6);

m(1,1) = 1;
m(1,2) = 0;

m(2,1) = 1;
m(2,2) = 1.5;

m(3,1) = 3;
m(3,2) = 2.5;

% Perceptron
for i=1: nVec
    subX = m(i,:);
%     f1 = getActivation((-1*  subX(1)) + (1* subX(2)) -0);
%     f2 = getActivation((0*  subX(1)) + (1*  subX(2)) -2);
%     f3 = getActivation((-0* subX(1)) + (-1* subX(2)) +1);
    
    f1 = subX(2)-subX(1);
    f2 = subX(2)-2;
    f3 = -subX(2)+1;
    
    subX(4) = f1;
    subX(5) = f2;
    subX(6) = f3;
    
    %azul
    if f1==0 && f2==1 && f3==0
        subX(3) = 1;
    end
    
    %rojo
    if f1==0 && f2==1 && f3==0
        subX(3) = 2;
    end
    
    %verde
    if f1==0 && f2==0 && f3==1
        subX(3) = 3;
    end
    
    m(i,:) = subX;
end

reds = m(m(:,3) == 1,:);
blues = m(m(:,3) == 2,:);
greens = m(m(:,3) == 3,:);
grays = m(m(:,3) == 0,:);

figure(200);
scatter( reds(:,1), reds(:,2), [], [0.8500 0.3250 0.0980], 'filled');
hold on
scatter( blues(:,1), blues(:,2), [], [0 0.4470 0.7410], 'filled');
hold on
scatter( greens(:,1), greens(:,2), [], [0.4660 0.6740 0.1880], 'filled');
hold on
scatter( grays(:,1), grays(:,2), [], [0.4660 0.4660 0.4660], 'filled');
hold on


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



function [val] = getActivation(x)
    if x>0
       val=1; 
    else
       val=0; 
    end
end

