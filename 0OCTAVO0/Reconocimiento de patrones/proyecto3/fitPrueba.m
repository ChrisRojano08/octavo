clear
clear all


%[Y, data] = libsvmread('svmguide1');
[Y, data] = libsvmread('fourclass');
X = full(data);
svmModel = fitcsvm(X,Y);


predictions = predict(svmModel, X);

figure;
gscatter(X(:,1), X(:,2), Y, 'rb', 'o+');
hold on;

sv = svmModel.SupportVectors;
plot(sv(:,1), sv(:,2), 'ko', 'MarkerSize', 10);

x1 = linspace(min(X(:,1))-1, max(X(:,1))+1, 100);
x2 = linspace(min(X(:,2))-1, max(X(:,2))+1, 100);
[X1, X2] = meshgrid(x1, x2);
XGrid = [X1(:), X2(:)];

xlabel('X1');
ylabel('X2');
title('Clasificación con Máquinas de Soporte Vectorial');
legend('Clase 1', 'Clase -1', 'Vectores de Soporte');


