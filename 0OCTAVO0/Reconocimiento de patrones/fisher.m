clear
clear all

%m= [2,2; 4,3; 5,1];
%n= [1,3; 5,5; 3,6];

m= [3,2;2,4;1,4;1,3];
n= [5,2;4,1;2,3;4,3];


[x, y] = size(m);
res = 0;
for i=1: x
    media = mean( m );
    xi = [ m(i,1); m(i,2) ];
    invXi = xi.';
    
    fprintf('([%d,%d]-[%d,%d]) * ([%d,%d]-[%d,%d]) + \n', xi(1),xi(2), media(1),media(2), invXi(1),invXi(2), media(1),media(2));
    res = res+ ( (xi-media) .* (invXi-media) ) ;
end

[x, y] = size(n);
for i=1: x
    media = mean( n );
    xi = [ n(i,1); n(i,2) ];
    invXi = xi.';
    
    fprintf('([%d,%d]-[%d,%d]) * ([%d,%d]-[%d,%d]) + \n', xi(1),xi(2), media(1),media(2), invXi(1),invXi(2), media(1),media(2));
    res = res+ ( (xi-media) .* (xi.'-media) ) ;
end

fprintf('\n');
disp(res);


