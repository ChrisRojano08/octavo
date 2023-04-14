function [resp] = WKNN(n, kn, P)

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
claseP = mode(KNN(:, (3) ) );

weigths = zeros(kn,1);
weightClass = zeros(a,1);
for i=1: kn
    wei = (KNN(kn,4)-KNN(i,4)) / (KNN(kn,4)-KNN(1,4)) ;
    weigths(i) = wei;
    
    weightClass(KNN(i,3)) = weightClass(KNN(i,3))+wei;
end
classMax = find(weightClass==max(weightClass));


resp{1} = KNN;
resp{2} = classMax;
resp{3} = weigths;





