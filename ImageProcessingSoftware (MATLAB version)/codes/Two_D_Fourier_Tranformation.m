function varargout = Two_D_Fourier_Tranformation(varargin)
% TWO_D_FOURIER_TRANFORMATION MATLAB code for Two_D_Fourier_Tranformation.fig
%      TWO_D_FOURIER_TRANFORMATION, by itself, creates a new TWO_D_FOURIER_TRANFORMATION or raises the existing
%      singleton*.
%
%      H = TWO_D_FOURIER_TRANFORMATION returns the handle to a new TWO_D_FOURIER_TRANFORMATION or the handle to
%      the existing singleton*.
%
%      TWO_D_FOURIER_TRANFORMATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in TWO_D_FOURIER_TRANFORMATION.M with the given input arguments.
%
%      TWO_D_FOURIER_TRANFORMATION('Property','Value',...) creates a new TWO_D_FOURIER_TRANFORMATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Two_D_Fourier_Tranformation_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Two_D_Fourier_Tranformation_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Two_D_Fourier_Tranformation

% Last Modified by GUIDE v2.5 11-Jan-2018 01:00:10

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @Two_D_Fourier_Tranformation_OpeningFcn, ...
    'gui_OutputFcn',  @Two_D_Fourier_Tranformation_OutputFcn, ...
    'gui_LayoutFcn',  [] , ...
    'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Two_D_Fourier_Tranformation is made visible.
function Two_D_Fourier_Tranformation_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Two_D_Fourier_Tranformation (see VARARGIN)

% Choose default command line output for Two_D_Fourier_Tranformation
handles.output = hObject;
global f g Fshow
set(handles.text8,'Visible','off')
logo=imread('ZoiLogosmall.png');
axes(handles.axes3)
imshow(logo)
set(handles.edit2,'enable','off')
set(handles.edit3,'enable','off')
set(handles.text3,'enable','off')
set(handles.text4,'enable','off')
f1=f;
g=zeros(size(f));

if size(f,3)==3  %for RGB image
    f1=rgb2gray(f);
end

set(handles.edit1,'string',num2str(100))
F=fft2(f1);
Fshow=100*mat2gray(abs(fftshift(F)));

axes(handles.axes1)
imshow(Fshow)

axes(handles.axes2)
imshow(f)
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Two_D_Fourier_Tranformation wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Two_D_Fourier_Tranformation_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
clear g 
global f g H Fshow

% select type of filter
% select type of filter
% select type of filter
% select type of filter
% select type of filter

f1=f;

if size(f,3)==3  %for RGB image
    f1=rgb2gray(f);
end

gg=get(handles.popupmenu1,'value');
ggg=get(handles.popupmenu2,'value');
[m,n]=size(f1);
F=fft2(f1);
LS=str2num(get(handles.edit1,'string'));
Fshow=LS*mat2gray(abs(fftshift(F)));

if gg==2 %Custom-Stop-Masks
    
    set(handles.text8,'Visible','on')
    set(handles.popupmenu1,'enable','off')
    set(handles.popupmenu2,'enable','off')
    set(handles.pushbutton1,'enable','off')
    set(handles.pushbutton2,'enable','off')
    set(handles.pushbutton3,'enable','off')
    set(handles.pushbutton4,'enable','off')
    set(handles.pushbutton5,'enable','off')
    set(handles.pushbutton6,'enable','off')
    set(handles.edit1,'enable','off')
    set(handles.edit2,'enable','off')
    set(handles.edit3,'enable','off')
    set(handles.text2,'enable','off')
    set(handles.text3,'enable','off')
    set(handles.text4,'enable','off')
    
    F=fft2(f1);
    Fshow=LS*mat2gray(abs(fftshift(F)));
    BW2=zeros(size(f1));
    axes(handles.axes2)
    imshow(~BW2)
    m=size(f1,1)/2;
    n=size(f1,2)/2;
    
    while 1
        
        axes(handles.axes1)
        [x, y, BW, xi, yi] = roipoly(Fshow);
        
        if isempty(BW) %press enter
            set(handles.popupmenu1,'enable','on')
            set(handles.pushbutton1,'enable','on')
            set(handles.pushbutton2,'enable','on')
            set(handles.pushbutton3,'enable','on')
            set(handles.pushbutton4,'enable','on')
            set(handles.pushbutton5,'enable','on')
            set(handles.pushbutton6,'enable','on')
            set(handles.edit1,'enable','on')
            set(handles.text2,'enable','on')
            set(handles.text8,'Visible','off')
            break
        end
        
        [r,c]=find(BW==1);
        r1=2*m-r;
        c1=2*n-c;
        t=sub2ind(size(f1),r1,c1);
        BW(t)=1;
        BW2=BW2+BW;
        Fshow=Fshow.*~BW2;
        axes(handles.axes2)
        imshow(~BW2)
        
    end
    
    BW2=~BW2;
    g=ifft2(ifftshift(BW2).*F);
    
elseif gg==3 %Custom-Pass-Masks
    
    set(handles.text8,'Visible','on')
    set(handles.popupmenu1,'enable','off')
    set(handles.popupmenu2,'enable','off')
    set(handles.pushbutton1,'enable','off')
    set(handles.pushbutton2,'enable','off')
    set(handles.pushbutton3,'enable','off')
    set(handles.pushbutton4,'enable','off')
    set(handles.pushbutton5,'enable','off')
    set(handles.pushbutton6,'enable','off')
    set(handles.edit1,'enable','off')
    set(handles.edit2,'enable','off')
    set(handles.edit3,'enable','off')
    set(handles.text2,'enable','off')
    set(handles.text3,'enable','off')
    set(handles.text4,'enable','off')
    
    F=fft2(f1);
    Fshow=LS*mat2gray(abs(fftshift(F)));
    BW2=zeros(size(f1));
    axes(handles.axes2)
    imshow(BW2)
    m=size(f1,1)/2;
    n=size(f1,2)/2;
    
    while 1
        axes(handles.axes1)
        [x, y, BW, xi, yi] = roipoly(Fshow);
        
        if isempty(BW) %press enter
            set(handles.popupmenu1,'enable','on')
            set(handles.pushbutton1,'enable','on')
            set(handles.pushbutton2,'enable','on')
            set(handles.pushbutton3,'enable','on')
            set(handles.pushbutton4,'enable','on')
            set(handles.pushbutton5,'enable','on')
            set(handles.pushbutton6,'enable','on')
            set(handles.edit1,'enable','on')
            set(handles.text2,'enable','on')
            set(handles.text8,'Visible','off')
            break
        end
        
        [r,c]=find(BW==1);
        r1=2*m-r;
        c1=2*n-c;
        t=sub2ind(size(f1),r1,c1);
        BW(t)=1;
        BW2=BW2+BW;
        BWshow=bwmorph(BW2,'remove');
        Fshow=Fshow+BWshow;
        axes(handles.axes2)
        imshow(BW2)
        
    end
    g=ifft2(ifftshift(BW2).*F);
    
elseif gg==4 %Low-Pass-Filter
    
    set(handles.text8,'Visible','off')
    set(handles.popupmenu2,'enable','on')
    
    if ggg==2 %ideal
        
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','off')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','off')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',' ');
        
        p=paddedsize(size(f1));
        H=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        axes(handles.axes1)
        imshow(Fshow+h)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==3 %Gaussian
        
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','off')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','off')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',' ');
        
        p=paddedsize(size(f1));
        H=lpfilter('gaussian',p(1),p(2),0.1*min(m,n));
        t=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==4 %BTW
        
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','on')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','on')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',num2str(1));
        
        p=paddedsize(size(f1));
        H=lpfilter('btw',p(1),p(2),0.1*min(m,n));
        t=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    end
    
elseif gg==5 %High-Pass-Filter
    
    set(handles.text8,'Visible','off')
    set(handles.popupmenu2,'enable','on')
    
    if ggg==2 %ideal
        
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','off')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','off')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',' ');
        p=paddedsize(size(f1));
        H=hpfilter('ideal',p(1),p(2),0.1*min(m,n));
        h=fftshift(H);
        h=bwmorph(~h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+h)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==3 %Gaussian
        
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','off')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','off')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',' ');
        
        p=paddedsize(size(f1));
        H=hpfilter('gaussian',p(1),p(2),0.1*min(m,n));
        t=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==4 %BTW
        
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','on')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','on')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',num2str(1));
        p=paddedsize(size(f1));
        H=hpfilter('btw',p(1),p(2),0.1*min(m,n));
        t=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    end
    
end

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1


% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in popupmenu2.
function popupmenu2_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g H Fshow
set(handles.text8,'Visible','off')
f1=f;
if size(f,3)==3
    f1=rgb2gray(f);
end
ggg=get(handles.popupmenu2,'value');
gg=get(handles.popupmenu1,'value');
[m,n]=size(f1);
F=fft2(f1);
LS=str2num(get(handles.edit1,'string'));
Fshow=LS*mat2gray(abs(fftshift(F)));

if gg==4 %Low-Pass-Filter
    
    if ggg==2 %ideal
        
        set(handles.text8,'Visible','off')
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','off')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','off')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',' ');
        
        
        p=paddedsize(size(f1));
        H=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+h)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==3 %Gaussian
        
        set(handles.text8,'Visible','off')
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','off')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','off')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',' ');
        
        
        p=paddedsize(size(f1));
        H=lpfilter('gaussian',p(1),p(2),0.1*min(m,n));
        t=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==4 %BTW
        
        set(handles.text8,'Visible','off')
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','on')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','on')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',num2str(1));
        
        
        p=paddedsize(size(f1));
        H=lpfilter('btw',p(1),p(2),0.1*min(m,n));
        t=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    end
    
elseif gg==5 %High-Pass-Filter
    
    
    if ggg==2 %ideal
        
        
        set(handles.text8,'Visible','off')
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','off')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','off')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',' ');
        
        
        p=paddedsize(size(f1));
        H=hpfilter('ideal',p(1),p(2),0.1*min(m,n));
        h=fftshift(H);
        h=bwmorph(~h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+h)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
        
    elseif ggg==3 %Gaussian
        
        set(handles.text8,'Visible','off')
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','off')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','off')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',' ');
        
        p=paddedsize(size(f1));
        H=hpfilter('gaussian',p(1),p(2),0.1*min(m,n));
        t=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==4 %BTW
        
        set(handles.text8,'Visible','off')
        set(handles.edit2,'enable','on')
        set(handles.edit3,'enable','on')
        set(handles.text3,'enable','on')
        set(handles.text4,'enable','on')
        set(handles.edit2,'string',num2str(0.1*min(m,n)));
        set(handles.edit3,'string',num2str(1));
        
        p=paddedsize(size(f1));
        H=hpfilter('btw',p(1),p(2),0.1*min(m,n));
        t=lpfilter('ideal',p(1),p(2),0.1*min(m,n));
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
    end
end
% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu2 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu2


% --- Executes during object creation, after setting all properties.
function popupmenu2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g Fshow

%linear scal
%linear scal
%linear scal
%linear scal
%linear scal

f1=f;

if size(f,3)==3 %for RGB image
    f1=rgb2gray(f);
end

LS=str2num(get(handles.edit1,'string'));
F=fft2(f1);
Fshow=LS*mat2gray(abs(fftshift(F)));

axes(handles.axes1)
imshow(Fshow)


% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g

% filtering
% filtering
% filtering
% filtering

f1=f;
if size(f,3)==3 %for RGB image
    f1=rgb2gray(f);
end

figure
subplot(121)
imshow(f1)
subplot(122)
imshow(abs(g),[])



% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName g Fshow infoo 

%Read image
%Read image
%Read image
%Read image

set(handles.edit1,'string',num2str(100));
set(handles.edit2,'string',' ');
set(handles.edit3,'string',' ');
set(handles.popupmenu1,'value',1);
set(handles.popupmenu2,'value',1);
set(handles.text8,'Visible','off')
set(handles.edit2,'enable','off')
set(handles.edit3,'enable','off')
set(handles.text3,'enable','off')
set(handles.text4,'enable','off')
warning('off')

FileName=0;
[FileName,PathName]=uigetfile('*.*');
if FileName~=0
    f=imread([PathName,FileName]);
    infoo=imfinfo([PathName,FileName]);
    f1=f;
    
    if size(f,3)==3 %for RGB image
        f1=rgb2gray(f);
    end
    
    g=zeros(size(f1));
    set(handles.edit1,'string',num2str(100))
    F=fft2(f1);
    Fshow=100*mat2gray(abs(fftshift(F)));
    axes(handles.axes1)
    imshow(Fshow)
    axes(handles.axes2)
    imshow(f)
    
end






function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global f g H Fshow
f1=f;

if size(f,3)==3 %for RGB image
    f1=rgb2gray(f);
end

ggg=get(handles.popupmenu2,'value');
gg=get(handles.popupmenu1,'value');
[m,n]=size(f1);
F=fft2(f1);
LS=str2num(get(handles.edit1,'string'));
Fshow=LS*mat2gray(abs(fftshift(F)));

if gg==4 %Low-Pass-Filter
    
    if ggg==2 %ideal
        
        D0=str2num(get(handles.edit2,'string'));
        set(handles.edit3,'string',' ');
        p=paddedsize(size(f1));
        H=lpfilter('ideal',p(1),p(2),D0);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        
        axes(handles.axes1)
        imshow(Fshow+h)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==3 %Gaussian
        
        D0=str2num(get(handles.edit2,'string'));
        set(handles.edit3,'string',' ');
        p=paddedsize(size(f1));
        H=lpfilter('gaussian',p(1),p(2),D0);
        t=lpfilter('ideal',p(1),p(2),D0);
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==4 %BTW
        
        D0=str2num(get(handles.edit2,'string'));
        n1=str2num(get(handles.edit3,'string'));
        p=paddedsize(size(f1));
        H=lpfilter('btw',p(1),p(2),D0,n1);
        t=lpfilter('ideal',p(1),p(2),D0);
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    end
    
elseif gg==5 %High-Pass-Filter
    
    if ggg==2 %ideal
        
        D0=str2num(get(handles.edit2,'string'));
        set(handles.edit3,'string',' ');
        p=paddedsize(size(f1));
        H=hpfilter('ideal',p(1),p(2),D0);
        h=fftshift(H);
        h=bwmorph(~h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+h)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==3 %Gaussian
        
        D0=str2num(get(handles.edit2,'string'));
        set(handles.edit3,'string',' ');
        p=paddedsize(size(f1));
        H=hpfilter('gaussian',p(1),p(2),D0);
        t=lpfilter('ideal',p(1),p(2),D0);
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==4 %BTW
        
        D0=str2num(get(handles.edit2,'string'));
        n1=str2num(get(handles.edit3,'string'));
        p=paddedsize(size(f1));
        H=hpfilter('btw',p(1),p(2),D0,n1);
        t=lpfilter('ideal',p(1),p(2),D0);
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    end
    
end

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g H Fshow
f1=f;

if size(f,3)==3 %for RGB image
    f1=rgb2gray(f);
end

ggg=get(handles.popupmenu2,'value');
gg=get(handles.popupmenu1,'value');
[m,n]=size(f1);
F=fft2(f1);
LS=str2num(get(handles.edit1,'string'));
Fshow=LS*mat2gray(abs(fftshift(F)));

if gg==4 %Low-Pass-Filter
    
    if ggg==2 %ideal
        
        D0=str2num(get(handles.edit2,'string'));
        p=paddedsize(size(f1));
        H=lpfilter('ideal',p(1),p(2),D0);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+h)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==3 %Gaussian
        
        D0=str2num(get(handles.edit2,'string'));
        p=paddedsize(size(f1));
        H=lpfilter('gaussian',p(1),p(2),D0);
        t=lpfilter('ideal',p(1),p(2),D0);
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==4 %BTW
        
        D0=str2num(get(handles.edit2,'string'));
        n1=str2num(get(handles.edit3,'string'));
        p=paddedsize(size(f1));
        H=lpfilter('btw',p(1),p(2),D0,n1);
        t=lpfilter('ideal',p(1),p(2),D0);
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    end
    
elseif gg==5 %High-Pass-Filter
    
    if ggg==2 %ideal
        
        D0=str2num(get(handles.edit2,'string'));
        p=paddedsize(size(f1));
        H=hpfilter('ideal',p(1),p(2),D0);
        h=fftshift(H);
        h=bwmorph(~h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+h)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==3 %Gaussian
        
        D0=str2num(get(handles.edit2,'string'));
        p=paddedsize(size(f1));
        H=hpfilter('gaussian',p(1),p(2),D0);
        t=lpfilter('ideal',p(1),p(2),D0);
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    elseif ggg==4 %BTW
        
        D0=str2num(get(handles.edit2,'string'));
        n1=str2num(get(handles.edit3,'string'));
        p=paddedsize(size(f1));
        H=hpfilter('btw',p(1),p(2),D0,n1);
        t=lpfilter('ideal',p(1),p(2),D0);
        t=fftshift(t);
        t=bwmorph(t,'remove');
        t=t((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        h=fftshift(H);
        h=bwmorph(h,'remove');
        h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
        g=dftfilt(f1,H,'fltpoint');
        
        axes(handles.axes1)
        imshow(Fshow+t)
        axes(handles.axes2)
        Hshow=fftshift(H);
        imshow(Hshow((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2))
        
    end
    
end
% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g H

%show space domain of filter
%show space domain of filter
%show space domain of filter
%show space domain of filter
%show space domain of filter

f1=f;
if size(f,3)==3 %for RGB image
    f1=rgb2gray(f);
end

v=get(handles.popupmenu1,'value');

if v==4 | v==5 % low pass orhigh pass filter
    
p=paddedsize(size(f1));
[m,n]=size(f1);
h=ifft2(H);
h=fftshift(h);
h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
h=h(1:3:end,1:3 :end);

axes(handles.axes2)
mesh(h)
end

% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g H

%show frequency domain of filter
%show frequency domain of filter
%show frequency domain of filter
%show frequency domain of filter
%show frequency domain of filter

f1=f;
if size(f,3)==3
    f1=rgb2gray(f);
end

v=get(handles.popupmenu1,'value');

if v==4 | v==5 % low pass orhigh pass filter
    p=paddedsize(size(f1));
    [m,n]=size(f1);
    
    
    axes(handles.axes2)
    h=fftshift(H);
    h=h((p(1)-m)/2:p(1)-1-(p(1)-m)/2  ,  (p(2)-n)/2:p(2)-1-(p(2)-n)/2);
    imshow(h)
end


% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global g Fshow FileName infoo

%Export image
%Export image
%Export image
%Export image
%Export image

if FileName==0 | isempty(FileName)  
    FileName='Matlab Picture.PNG';
end

if isequal(infoo.Format,'GIF')
    FileName(end-2:end)='png';
end

absg=mat2gray(abs(g));
masir=uigetdir;
zer=zeros(size(g));

if masir~=0
    if ~isequal(g,zer)
        wb=waitbar(0,'Please wait ...');
        imwrite(absg,[masir,'/Filtered Fourier ',FileName])
        
        imwrite(Fshow,[masir,'/Fourier Spectrom ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
        
    elseif isequal(g,zer)
        wb=waitbar(0,'Please wait ...');
        imwrite(Fshow,[masir,'/Fourier Spectrom ',FileName])    
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
            end
    end


% --- Executes on button press in pushbutton6.
function pushbutton6_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global Fshow

%3D plot
%3D plot
%3D plot
%3D plot
%3D plot

figure
mesh(log(1+Fshow)),view([173,22])
