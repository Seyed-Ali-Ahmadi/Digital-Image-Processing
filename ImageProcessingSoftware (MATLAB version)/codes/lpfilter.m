function H = lpfilter(type,M,N,D0,n)
% functions : dftuv tofloat paddedsize lpfilter hpfilter dftfilt rectangle1
% are Prerequisite functions for D_I_P programs and Not used independently.


% creat a low pass filter
%type: 'gaussian'  or  'ideal'  or  'btw'
% M,N are filter size.
%[ M , N]=M,N in args of ([U , V]=dftuv(M,N))
[U,V]=dftuv(M,N);
D=hypot(U,V);
switch type
    case 'ideal'
        H=single(D<=D0);
    case 'btw'
        if nargin==4
            n=1;
        end
        H=1./(1+(D./D0).^(2*n));
    case 'gaussian'
        H=exp(-(D.^2)./(2*(D0^2)));
    otherwise
        error('Unknown filter type.')
end
end