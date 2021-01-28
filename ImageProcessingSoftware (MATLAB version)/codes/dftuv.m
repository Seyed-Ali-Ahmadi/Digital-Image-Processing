function [U,V] =dftuv(m,n)
% functions : dftuv tofloat paddedsize lpfilter hpfilter dftfilt rectangle1
% are Prerequisite functions for D_I_P programs and Not used independently.
%%% this function is a Prerequisite for lpfilter and hpfilter 
% this function creat a meshgrid at a distance of 0 to m-1 and 0 to n-1
% m , n are filter size
%Example:
%                      [U,V]=dftuv(5,3)
%                       U =
%                             5×3 single matrix
%
%                             0     0     0
%                             1     1     1
%                             2     2     2
%                            -2    -2    -2
%                            -1    -1    -1
%
%                        V =
% 
%                          5×3 single matrix
% 
%                             0     1    -1
%                             0     1    -1
%                             0     1    -1
%                             0     1    -1
%                             0     1    -1

u=single(0:(m-1));
v=single(0:(n-1));
idx=find(u>m/2);
u(idx)=u(idx)-m;
idy=find(v>n/2);
v(idy)=v(idy)-n;
[V,U]=meshgrid(v,u);
end