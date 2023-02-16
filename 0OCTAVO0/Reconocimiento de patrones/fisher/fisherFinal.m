clear
clear all

[n,t,r] = xlsread('data.xlsx');

[x, y] = size(n);
M = unique(n(:,y));
lases = cell(numel(M),1);
justD = n;
justD(:,y) = [];
for i=1: x
    lases{ find(M==n(i,y)) } = [ lases{find(M==n(i,y))} ; justD(i,:)];
end

[a, b] = size(lases{1});
Ow = 0;
for i=1: b
    mediax = mean( lases{i,:} );
    transM = mediax.';
    
    for j=1: a
        subX = lases{i,:};
        xi = subX(a,:);
        invXi = xi.';

        %fprintf('([%d,%d]-[%d,%d]) * ([%d,%d]-[%d,%d]) + \n', xi(1),xi(2), media(1),media(2), invXi(1),invXi(2), media(1),media(2));
        Ow = Ow+ ( (invXi-transM) *(xi-mediax) )  ;
    end
end

Media = mean(cell2mat(lases));
MediaTrans = Media.';
Ob = 0;
for i=1: b
    [N, ~] = size(lases{i});
    mediaX = mean( lases{i,:} );
    transMX = mediaX.';
    
    Ob = Ob + (N*(transMX-MediaTrans)*(mediaX-Media));
end

dif = 0;
for i=1: b
    mediaX = mean( lases{i,:} );
    dif = dif - mediaX;
end
V = (Ow.')*(dif.');

fprintf('\nEl valor de Ow es:\n');
disp(Ow);
fprintf('El valor de Ob es:\n');
disp(Ob);
fprintf('El valor de V es:\n');
disp(V);


