clear
clear all

[n,t,r] = xlsread('data.xlsx');
umbral=4;

%[n,t,r] = xlsread('data02.xlsx');
%umbral=2;

aux = t.';
nWords = 8;
mat = strcat('a':'n','ñ','o':'x');
transTbl = strings(nWords,25);

iN = 1;
jN = 0;
for i=1 : numel(aux)
    jN= jN+1;
    transTbl(iN,jN) = aux{i};
    
    if mod(i,25)==0
        iN= iN+1;
        jN= 0;
    end
end

incidencias = zeros(1,25);
for i=1: nWords
    for j=1: 25
        if find(transTbl(i:i,1:25) == mat(j))
            incidencias(j) = incidencias(j)+1;
        end
    end
end


newTransTbls = [ ];
for i=1: nWords
    strAx = '';
    for j=1: 25
        if mat(j)==transTbl(i,j) && incidencias(j)>umbral
            strAx = addOrderElement(mat, incidencias, strAx, j);
        end
    end
    newTransTbls = [newTransTbls strcat(strAx, "")];
end

justPoint = [ ];
points = [ ];
nodes = [ ];
nodesCh = [ ];

newTransTbls = newTransTbls.';

x = 1;
y = 1;
newNodes = 0;
for i=1:nWords
    B = convertStringsToChars( newTransTbls(i) );
    y=0;
    
    for j=1:numel(B)-1
        nP = strcat(B(j),",",B(j+1));
        nC = strcat(num2str(x),",",num2str(y));
        nCnext = strcat(num2str(x),",",num2str(y));
        
        if numel(justPoint) == 0
            justPoint = [ justPoint strcat("",nP) ];
            points = [ points strcat("",nP)  ];
            
            nodes = [ strcat("",B(j)) ];
            nodes = [ nodes strcat("",B(j+1)) ];
            nodesCh = [ strcat(num2str(x),",",num2str(y)) ];
            nodesCh = [ nodesCh strcat(num2str(x),",",num2str(y-1)) ];
        else
            if i==1
                justPoint = [ justPoint strcat("",nP) ];
                points = [ points strcat("",nP) ];
                nodes = [ nodes strcat("",B(j+1))];
                nodesCh = [ nodesCh strcat(num2str(x),",",num2str(y-1)) ];
            else
                if numel( find( justPoint==nP ) ) == 0 
                    newNodes = newNodes+1;
                    axCh = '';
                    for a=1:newNodes
                        axCh = strcat(axCh, "'");
                    end
                    
                    points = [ points strcat(B(j),",",B(j),axCh) ];
                    nodes = [ nodes strcat("",B(j),axCh)];
                    nodesCh = [ nodesCh strcat(num2str(x),",",num2str(y)) ];
                    
                    for k=j: numel(B)-1
                       nP = strcat(B(k),",",B(k+1));
                       nC = strcat(num2str(x),",",num2str(y));
        
                       justPoint = [ justPoint strcat("",nP) ];
                       points = [ points strcat(B(k),axCh,",",B(k+1),axCh) ];
                       nodes = [ nodes strcat("",B(k+1),axCh)];
                       nodesCh = [ nodesCh strcat(num2str(x-1),",",num2str(y)) ];
                       x = x-1;
                   end
                   j=k;
                end
            end
        end
        y = y-1;
    end
end

G = zeros(numel(nodes), numel(nodes));
V = zeros(2, numel(nodes));
for i=1: numel(nodes)
    for j=1: numel(nodes)
        vertic = strcat(nodes(i),",",nodes(j));
        if find( points==vertic ) ~= 0
            G(i,j) = 1;
        end
    end
    [dot ,y] = split(nodesCh(i), ",");
    V(1,i) = str2double(dot(1));
    V(2,i) = str2double(dot(2));
end

V = V.';
figure(100);
plot( V(:,1), V(:,2), 'ok','MarkerSize',10 );
hold on

for i=1: size(G,1)
    for j=1: size(G,1)
        if G(i,j)==1
            [dot01 ,~] = split( nodesCh(find( nodes==nodes(i) )), ",");
            [dot02 ,~] = split( nodesCh(find( nodes==nodes(j) )), ",");
            arisA = [str2double(dot01(1)) str2double(dot01(2))];
            arisB = [str2double(dot02(1))  str2double(dot02(2))];
            
            Y = [ arisA(1:2); arisB(1:2) ];
            
            plot( Y(:,1), Y(:,2) ,'-r' );
            hold on
        end
    end
end

plot( [1,1], [1,1], 'ok','MarkerSize',15 );
plot( [1,1], [0,1] ,'-r' );
hold on




