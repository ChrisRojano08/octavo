function [strAx] = addOrderElement(mat, incidencias, strAx, j)

if numel(strAx) == 0
    strAx = mat(j);
elseif numel(strAx) == 1
    if incidencias(find(mat==mat(j))) >= incidencias(find(mat==strAx)) && j < find(mat==strAx)
        strAx = strcat(mat(j),strAx);
    else
        strAx = strcat(strAx,mat(j));
    end
else
    if incidencias(j) >= incidencias(find(mat==strAx(1))) && j < find(mat==strAx(1))
        strAx = strcat(mat(j),strAx);
    elseif incidencias(j) <= incidencias(find(mat==strAx(numel(strAx)))) && j > find(mat==strAx(numel(strAx)))
        strAx = strcat(strAx,mat(j));
    else
        inserted=0;
        for k=2: numel(strAx)
            if incidencias(j) == incidencias(find(mat==strAx(k))) && j < find(mat==strAx(k))
                strAx = strcat(strAx(1:k), mat(j), strAx(k+1:numel(strAx)));
                inserted=1;
                break
            else
                if incidencias(j) > incidencias(find(mat==strAx(k))) 
                    strAx = strcat(strAx(1:k-1), mat(j), strAx(k:numel(strAx)));
                    inserted=1;
                    break
                end
            end
        end
        if inserted==0
            strAx = strcat(strAx,mat(j));
        end
    end
end










