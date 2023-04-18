function [resp] = WKNN(KNN, kn, a)
weigths = zeros(kn,1);
weightClass = zeros(a,1);
for i=1: kn
    if KNN(kn,4) == KNN(1,4)
        wei = 1;
    else
        wei = (KNN(kn,4)-KNN(i,4)) / ((KNN(kn,4)-KNN(1,4))+eps);
    end
    
    weigths(i) = wei;
    
    weightClass(KNN(i,3)) = weightClass(KNN(i,3))+wei;
end
classMax = find(weightClass==max(weightClass));


resp{1} = KNN;
resp{2} = classMax(1);
resp{3} = weigths;





