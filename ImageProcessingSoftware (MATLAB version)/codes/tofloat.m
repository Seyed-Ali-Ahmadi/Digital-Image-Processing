function [out revertclass] =tofloat(in)
% functions : dftuv tofloat paddedsize lpfilter hpfilter dftfilt rectangle1
% are Prerequisite functions for D_I_P programs and Not used independently.
% the input is an image of class uint8 uint16 logical double single.
% out is an image of double or single class that is in range [0 1].
% revertclass is a handle to return the out image to calss of in image.
identity=@(x)x;
tosingle=@im2single;
table={'uint8' , tosingle , @im2uint8
    'uint16',tosingle,@im2uint16
    'int16',tosingle,@im2int16
    'logical',tosingle,@logical
    'double',identity,identity
    'single',identity,identity};
classindex=find(strcmp(class(in),table(:,1)));
if isempty(classindex)
    error('Unsupported input image class.');
end
out=table{classindex,2}(in);
revertclass=table{classindex,3};
end