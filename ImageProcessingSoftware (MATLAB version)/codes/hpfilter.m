function H =hpfilter(type ,M,N,D0,n)
% functions : dftuv tofloat paddedsize lpfilter hpfilter dftfilt rectangle1
% are Prerequisite functions for D_I_P programs and Not used independently.


% creat a high pass filter
% type: 'gaussian'  or  'ideal'  or  'btw'
% M,N are filter size.
% [ M , N]=M,N in args of ([U , V]=dftuv(M,N))
if nargin==4
    n=1;
end
H=1-lpfilter(type ,M,N,D0,n);
end