clc
clear all
 
C=[0 0 0 0 0 -1 0;
   0 0 0 0 0 0 0;
   0 0 0 0 0 0 0;
   0 0 0 0 0 0 0;
   0 0 0 0 0 0 0;
   0 0 0 0 0 0 0;
   0 0 0 0 0 0 0];
%C=randi(3,10)-2;
n=size(C,1);
p(:,1)=cos(2.1*pi*((0:(n-1))/n));
p(:,2)=sin(1.9*pi*((0:(n-1))/n));
 
 
for i=1:n
    plot(p(i,1),p(i,2),'ok','MarkerSize',20),hold on
    axis equal
    xlim([-1.2 1.2]);ylim([-1.2 1.2]);
    for j=1:n
 
        if abs(C(i,j))==1
            pm=p(i,:)/16+p(j,:)*15/16;
            ps=[p(j,2)-p(i,2),p(i,1)-p(j,1)];
            pk=pm+ps/72;pk2=pm+ps/36;
            xq=[p(i,1) pk(1) pk2(1) p(j,1) pk(1)];
            vq2 = [p(i,2) pk(2) pk2(2) p(j,2) pk(2)];
            if C(i,j)==-1
                fill(xq,vq2,'b','edgecolor','b')
            else
                fill(xq,vq2,'r','edgecolor','r')
            end
 
        end
 
    end
end