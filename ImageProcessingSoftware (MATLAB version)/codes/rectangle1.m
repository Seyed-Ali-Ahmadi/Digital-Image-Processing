function f=rectangle(len,width,angle)
% functions : dftuv tofloat paddedsize lpfilter hpfilter dftfilt rectangle1
% are Prerequisite functions for D_I_P programs and Not used independently.
% this function creat a binary rectangle of LENGTH len and WIDTH width and
% ORIENTATION angle in center of image.

if width>len
    error('THE LENGTH OF RECTANGLE MUST BIGER THAN Width.')
end
f=zeros(400);
miny=200-len/2;
maxy=200+len/2;
minx=200-width/2;
maxx=200+width/2;
f(minx:maxx,miny:maxy)=1;
g=imrotate(f,angle);
g=imresize(g,size(f));
s=strel('square',3);
g=imclose(g,s);
f=g;
end

