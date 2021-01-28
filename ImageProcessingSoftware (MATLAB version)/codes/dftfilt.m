function g =dftfilt(f,H,classout)
% functions : dftuv tofloat paddedsize lpfilter hpfilter dftfilt rectangle1
% are Prerequisite functions for D_I_P programs and Not used independently.

% this function do filtering in frequency domain.
% f is input image 
% H is Filter produced by lpfilter or hpfilter. 
[f,revertclass]=tofloat(f);
F=fft2(f,size(H,1),size(H,2));
g=ifft2(H.*F);
g=g(1:size(f,1),1:size(f,2));
if nargin==2 || strcmp(classout,'original')
    g=revertclass(g);
elseif strcmp(classout,'fltpoint')
    return
else
    error('Undefined class for the output image.')
end
end