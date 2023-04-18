clear
tic;
%  Formas para la grafica
%shapesP = ['.','o','x','+','*','s','d','v','^','<','>','p','h'];

% Leyendo datos
dataA = fopen('urbanGB.txt','r');
labelsA = fopen('urbanGB.labels.txt','r');
dataAx = fscanf(dataA,'%f,%f', [2, Inf]);
dataAx = dataAx';
labels = fscanf(labelsA,'%d');

data = [dataAx labels];

% Calculando clases
[~,n] = size(data);
M = unique(data(:,n));
[nClass,~] = size(M);

[m,~] = size(data);
rescue = 0.4;
idx = randperm(m);
data   = data(idx(1:round(rescue*m)),:); 
[m,~] = size(data);

%Generando puntos para entrenamiento y validación
pTrain = 0.30;
pVal = 0.15;
idx = randperm(m);
TrainingPoints   = data(idx(1:round(pTrain*m)),:); 
ValidationPoints = data(idx(round((pTrain)*m)+1:(round((pTrain)*m)+1) + (round(pVal*m))),:);

%Generando conjunto sin los punto de entranamiento y validación
trainingM = data;
trainingM( idx(1:round(pTrain*m)),:) = [];

validationM = data;
validationM( idx(round((pTrain)*m)+1:(round((pTrain)*m)+1) + (round(pVal*m))),:) = [];


%%% Entranamiento %%%
[a,~] = size(TrainingPoints);
maxKn = 33;
mu = 2;
pointsTR = round(a);
[b,~] = size(trainingM);

fprintf('\nEntrenando...\n');
success = zeros(3, round(maxKn/2)-1);
for i=1:pointsTR
    
    P = TrainingPoints(i,:);
    sortedDists = getSortedDist(b,P,trainingM);
    
    k=1;
    
    for j=3:2:maxKn
        knn = sortedDists(1:j,:);
        
        resp = KNN(knn);
        if resp{2}==P(3)
            success(1,k) = success(1,k)+1;
        end
        
        resp = WKNN(knn, j, nClass);
        if resp{2}==P(3)
            success(2,k) = success(2,k)+1;
        end
        
        resp = FUZZYKNN(knn, j, nClass, mu);
        if resp{2}==P(3)
            success(3,k) = success(3,k)+1;
        end
        
        k = k+1;
    end
    
end

percentFail = 100-((success/pointsTR)*100);


l = 1;
minFail = ones(3,1)*100;
kOpti = zeros(3,1);
for i=3:2:maxKn
   fprintf('\nPara k=%d se tuvo un %.2f %% de falla para k-NN', i, percentFail(1,l));
   if percentFail(1,l) < minFail(1)
       minFail(1) = percentFail(1,l);
       kOpti(1) = i;
   end
   
   fprintf(', un %.2f %% de falla para MK-NN', percentFail(2,l));
   if percentFail(2,l) < minFail(2)
       minFail(2) = percentFail(2,l);
       kOpti(2) = i;
   end
   
   fprintf(', un %.2f %% de falla para Fuzzy NN', percentFail(3,l));
   if percentFail(3,l) < minFail(3)
       minFail(3) = percentFail(3,l);
       kOpti(3) = i;
   end
   
   l = l+1;
end
fprintf('\n');

fprintf('\n');
toc;
tic;

%%% Validacion %%%
pointsTR = round(a);
[b,~] = size(validationM);

fprintf('\nValidando...\n');
successV = zeros(3,1);
[poin, ~] = size(ValidationPoints);
pointsVL = round(poin);
finalKNN = zeros(pointsVL,3);
finalWKNN = zeros(pointsVL,3);
finalFuzzy = zeros(pointsVL,3);

for i=1:pointsVL
    P = ValidationPoints(i,:);
    sortedDists = getSortedDist(b,P,validationM);
    
    knn = sortedDists(1:kOpti(1),:);
    resp = KNN(knn);
    if resp{2}==P(3)
        successV(1) = successV(1)+1;
    end
    P(3) = resp{2};
    finalKNN(i,:) = P;
    
    knn = sortedDists(1:kOpti(2),:);
    resp = WKNN(knn, kOpti(2), nClass);
    if resp{2}==P(3)
        successV(2) = successV(2)+1;
    end
    P(3) = resp{2};
    finalWKNN(i,:) = P;
    
    knn = sortedDists(1:kOpti(3),:);
    resp = FUZZYKNN(knn, kOpti(3), nClass, mu);
    if resp{2}==P(3)
        successV(3) = successV(3)+1;
    end
    P(3) = resp{2};
    finalFuzzy(i,:) = P;
end

percentSuccess = (successV/pointsVL)*100;
fprintf('\nSe tuvo un %.2f %% de exito para k-NN', percentSuccess(1));
fprintf('\nSe tuvo un %.2f %% de exito para Wk-NN', percentSuccess(2));
fprintf('\nSe tuvo un %.2f %% de exito para Fuzzy NN', percentSuccess(3));

fprintf('\n');
toc;

fprintf('\nGraficando...\n');
[aa,~] = size(validationM);
colorsS = zeros(aa,3);

figure(100);
for i=1: round(aa)
    colorsS(i,:) = getColors(validationM(i,3));
end
scatter( validationM(:,1), validationM(:,2), [],colorsS);
hold on

colorsKNN = zeros(pointsVL,3);
colorsWKNN = zeros(pointsVL,3);
colorsFKNN = zeros(pointsVL,3);
for i=1: pointsVL
    colorsKNN(i,:) = getColors(finalKNN(i,3));
    colorsWKNN(i,:) = getColors(finalWKNN(i,3));
    colorsFKNN(i,:) = getColors(finalFuzzy(i,3));
end

scatter( finalKNN(:,1), finalKNN(:,2), [], colorsKNN, 'filled');
hold on
scatter( finalWKNN(:,1), finalWKNN(:,2), [], colorsWKNN, 'filled');
hold on
scatter( finalFuzzy(:,1), finalFuzzy(:,2), [], colorsFKNN, 'filled');
hold on

tic;
% MDC
[a, ~] = size(M);
nNeig = a;
nSamples = aa;
nPoints = pointsVL;

mdcFull = MDC(nNeig, validationM, nSamples, ValidationPoints, nPoints, kOpti, mu);
percentageExit = mdcFull{9};
sumP = mdcFull{1};
colorsMDC = mdcFull{2};

pointsKNN = mdcFull{3};
colorsMDCKNN = mdcFull{4};

pointsWKNN = mdcFull{5};
colorsMDCWK = mdcFull{6};

pointsFuzzy = mdcFull{7};
colorsMDCFuzzy = mdcFull{8};

figure(200);
scatter( sumP(:,1), sumP(:,2), [], colorsMDC);
hold on
scatter( pointsKNN(:,1), pointsKNN(:,2), [], colorsMDCKNN, 'filled');
hold on
scatter( pointsWKNN(:,1), pointsWKNN(:,2), [], colorsMDCWK, 'filled');
hold on
scatter( pointsFuzzy(:,1), pointsFuzzy(:,2), [], colorsMDCFuzzy, 'filled');
hold on
fprintf('\nPara MDC se tuvo un exito del %f %% con %d vecindarios en KNN', percentageExit(1), nNeig);
fprintf('\nPara MDC se tuvo un exito del %f %% con %d vecindarios en WKNN', percentageExit(2), nNeig);
fprintf('\nPara MDC se tuvo un exito del %f %% con %d vecindarios en Fuzzy KNN\n', percentageExit(3), nNeig);
toc;

tic;
mdcFull = MDC(20, validationM, nSamples, ValidationPoints, nPoints, kOpti, mu);
percentageExit = mdcFull{9};
sumP = mdcFull{1};
colorsMDC = mdcFull{2};

pointsKNN = mdcFull{3};
colorsMDCKNN = mdcFull{4};

pointsWKNN = mdcFull{5};
colorsMDCWK = mdcFull{6};

pointsFuzzy = mdcFull{7};
colorsMDCFuzzy = mdcFull{8};

figure(300);
scatter( sumP(:,1), sumP(:,2), [], colorsMDC);
hold on
scatter( pointsKNN(:,1), pointsKNN(:,2), [], colorsMDCKNN, 'filled');
hold on
scatter( pointsWKNN(:,1), pointsWKNN(:,2), [], colorsMDCWK, 'filled');
hold on
scatter( pointsFuzzy(:,1), pointsFuzzy(:,2), [], colorsMDCFuzzy, 'filled');
hold on
fprintf('\nPara MDC se tuvo un exito del %f %% con %d vecindarios en KNN', percentageExit(1), 20);
fprintf('\nPara MDC se tuvo un exito del %f %% con %d vecindarios en WKNN', percentageExit(2), 20);
fprintf('\nPara MDC se tuvo un exito del %f %% con %d vecindarios en Fuzzy KNN\n', percentageExit(3), 20);
toc;

fprintf('\n');


function [colorC] = getColors(x)
    rng(x);
    % Generar tres números aleatorios distintos entre 0 y 1
    numeros_aleatorios = rand(1, 3);
    indice_permutacion = randperm(3);
    colorC = numeros_aleatorios(indice_permutacion);
end

function [sortedDists] = getSortedDist(b,P,points)
    % Calcular distancias
    dist = zeros(b,5);
    for iP=1: b
      dist(iP,1) = points(iP,1,1);
      dist(iP,2) = points(iP,2,1);
      dist(iP,3) = points(iP,3,1);
      
      dist(iP,4) = sqrt( power(points(iP,1,1)-P(1),2) + power(points(iP,2,1)-P(2),2) );
      dist(iP,5) = iP;
    end
    
    % Ordenar distancias
    sortedDists = sortrows(dist,4);
end


function [resp] = MDC(nNeig, M, nSamples, Points, nPoints, kOpti, mu)
    nS = zeros(1,nNeig);
    sumP = zeros(nNeig,3);
    colorsMDC = zeros(nNeig,3);
    for i=1:nSamples
        positionNew = mod(M(i,3)-1,nNeig)+1;
        sumP(positionNew,1) = sumP(positionNew,1)+M(i,1);
        sumP(positionNew,2) = sumP(positionNew,2)+M(i,2);
        sumP(positionNew,3) = positionNew;
        
        nS(positionNew) = nS(positionNew)+1;
    end

    for i=1:nNeig
       sumP(i,1) = sumP(i,1)/nS(i);
       sumP(i,2) = sumP(i,2)/nS(i);
       
       colorsMDC(i,:) = getColors(sumP(i,3));
    end

    mdcPointsKN = zeros(nPoints,3);
    mdcPointsWK = zeros(nPoints,3);
    mdcPointsFuzzy = zeros(nPoints,3);
    successV = zeros(3,1);
    for i=1: nPoints
        P = Points(i,:);
        sortedDists = getSortedDist(nNeig,P,sumP);
        newClass = mod(P(3)-1,nNeig)+1;
        
        knn = sortedDists(1:kOpti(1),:);
        resp = KNN(knn);
        if mod(resp{2}-1,nNeig)+1==newClass
            successV(1) = successV(1)+1;
        end
        P(3) = mod(resp{2}-1,nNeig)+1;
        mdcPointsKN(i,:) = P;
    
        knn = sortedDists(1:kOpti(2),:);
        resp = WKNN(knn, kOpti(2), nNeig);
        if mod(resp{2}-1,nNeig)+1==newClass
            successV(2) = successV(2)+1;
        end
        P(3) = mod(resp{2}-1,nNeig)+1;
        mdcPointsWK(i,:) = P;
    
        knn = sortedDists(1:kOpti(3),:);
        resp = FUZZYKNN(knn, kOpti(3), nNeig, mu);
        if mod(resp{2}-1,nNeig)+1==newClass
            successV(3) = successV(3)+1;
        end
        P(3) = mod(resp{2}-1,nNeig)+1;
        mdcPointsFuzzy(i,:) = P;
    end

    colorsMDCPointsKNN = zeros(nPoints,3);
    colorsMDCPointsWKNN = zeros(nPoints,3);
    colorsMDCPointsFuzzy = zeros(nPoints,3);
    for i=1: nPoints
        colorsMDCPointsKNN(i,:) = getColors(mdcPointsKN(i,3));
        colorsMDCPointsWKNN(i,:) = getColors(mdcPointsWK(i,3));
        colorsMDCPointsFuzzy(i,:) = getColors(mdcPointsFuzzy(i,3));
    end
    
    resp{1} = sumP;
    resp{2} = colorsMDC;
    
    resp{3} = mdcPointsKN;
    resp{4} = colorsMDCPointsKNN;

    resp{5} = mdcPointsWK;
    resp{6} = colorsMDCPointsWKNN;
    
    resp{7} = mdcPointsFuzzy;
    resp{8} = colorsMDCPointsFuzzy;

    resp{9} = ((successV/nPoints)*100);
end













