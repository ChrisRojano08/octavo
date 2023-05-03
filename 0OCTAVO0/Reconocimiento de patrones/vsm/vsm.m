clear
clear all

nVec = 3000;
aN=0;
bN=5;
P = [aN + (bN+bN)*rand(1),aN + (bN+bN)*rand(1)];
n = zeros(nVec,3);
for i=1:nVec
   rX = aN + (bN+bN)*rand(1);
   rY = aN + (bN+bN)*rand(1);
   n(i,1) = rX;
   n(i,2) = rY;
end


for i=1: nVec
    subX = n(i,:);
    f = subX(1)+subX(2)-10;
    
    if f>0
        subX(3) = 1;
        n(i,:) = subX;
    end
end

blues = n(n(:,3) == 1,:);
greens = n(n(:,3) == 0,:);

scatter( blues(:,1), blues(:,2), [], 'blue', 'filled');
hold on
scatter( greens(:,1), greens(:,2), [], 'green', 'filled');
hold on




