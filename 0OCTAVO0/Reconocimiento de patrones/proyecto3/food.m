clear
clear all


[Y, data] = libsvmread('fourclass');
X = full(data);

t = templateSVM('Standardize',true,'SaveSupportVectors',true);
Mdl = fitcecoc(X,Y,'Learners',t);


L = size(Mdl.CodingMatrix,2); % Number of SVMs
sv = cell(L,1); % Preallocate for support vector indices
for j = 1:L
    SVM = Mdl.BinaryLearners{j};
    sv{j} = SVM.SupportVectors;
    sv{j} = sv{j}.*SVM.Sigma + SVM.Mu;
end

figure
gscatter(X(:,1),X(:,2),Y);
hold on
markers = {'ko','ro','bo'}; % Should be of length L
for j = 1:L
    svs = sv{j};
    plot(svs(:,1),svs(:,2),markers{j},...
        'MarkerSize',10 + (j - 1)*3);
end


