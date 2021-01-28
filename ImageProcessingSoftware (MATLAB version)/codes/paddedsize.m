function PQ =paddedsize(AB,CD,PARAM)
% functions : dftuv tofloat paddedsize lpfilter hpfilter dftfilt rectangle1
% are Prerequisite functions for D_I_P programs and Not used independently.

%this function are Prerequisite for lpfilter and hpfilter that Specifies the filter size.
%this function creat a PAD of zeros for The filter we want to build.
% inputs: AB=[A  B]; CD=[C  D];
%outputs: PQ=[P  Q];
%if the number of input arguments is one ( AB=[A B] ) ==> this function set 2*AB as the output size.  
%The number of more arguments in our Program( D_I_P ) is not required.
if nargin==1
    PQ=2*AB;
elseif nargin==2 & ~ischar(CD)
    PQ=AB + CD  -  1;
    PQ=2*ceil(PQ/2);
elseif nargin==2
    m=max(AB);
    P=2^nextpow2(2*m);
    PQ=[P, P];
else
    error('wrong number of inputs.');
end
end