function varargout = Region_Filling(varargin)
% REGION_FILLING MATLAB code for Region_Filling.fig
%      REGION_FILLING, by itself, creates a new REGION_FILLING or raises the existing
%      singleton*.
%
%      H = REGION_FILLING returns the handle to a new REGION_FILLING or the handle to
%      the existing singleton*.
%
%      REGION_FILLING('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in REGION_FILLING.M with the given input arguments.
%
%      REGION_FILLING('Property','Value',...) creates a new REGION_FILLING or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Region_Filling_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Region_Filling_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Region_Filling

% Last Modified by GUIDE v2.5 02-Feb-2018 19:23:51

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @Region_Filling_OpeningFcn, ...
    'gui_OutputFcn',  @Region_Filling_OutputFcn, ...
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


% --- Executes just before Region_Filling is made visible.
function Region_Filling_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Region_Filling (see VARARGIN)

% Choose default command line output for Region_Filling
handles.output = hObject;
global f g rb1 rb2 kh pm
logo=imread('ZoiLogosmall.png');
axes(handles.axes2)
imshow(logo)
pm=[];
set(handles.radiobutton1,'value',1)
set(handles.edit1,'enable','off')
set(handles.edit2,'enable','off')
set(handles.edit3,'enable','off')
set(handles.edit4,'enable','off')
set(handles.edit5,'enable','off')

set(handles.text2,'enable','off')
set(handles.text3,'enable','off')
set(handles.text4,'enable','off')
set(handles.text5,'enable','off')
set(handles.text6,'enable','off')

rb1=1;
rb2=0;
set(handles.slider1,'enable','off')
set(handles.edit6,'enable','off')
f1=f;

if size(f,3)==3    %for RGB image
    
    f1=rgb2gray(f);
    set(handles.slider1,'enable','on')
    set(handles.edit6,'enable','on')
    set(handles.slider1,'value',graythresh(f)*255)
    set(handles.edit6,'string',num2str(graythresh(f)*255))
    f1=im2bw(f,graythresh(f));
    
elseif size(f,3)==1 & ~islogical(f)
    
    set(handles.slider1,'enable','on')
    set(handles.edit6,'enable','on')
    f1=im2bw(f,graythresh(f));
    set(handles.slider1,'value',graythresh(f)*255)
    set(handles.edit6,'string',num2str(graythresh(f)*255))
    
end

kh=f1;
g=logical(zeros(size(f1)));
axes(handles.axes1)
imshow(f1)
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Region_Filling wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Region_Filling_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton2.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName g rb1 rb2 kh infoo pm

%Read image
%Read image
%Read image
%Read image
%Read image

pm=[];
set(handles.radiobutton1,'value',1);
set(handles.radiobutton2,'value',0);
rb1=1;
rb2=0;
warning('off')
FileName=0;
[FileName,PathName]=uigetfile('*.*');
if FileName~=0
    f=imread([PathName,FileName]);
    infoo=imfinfo([PathName,FileName]);
    f1=f;
    set(handles.slider1,'enable','off')
    set(handles.edit6,'enable','off')
    
    if size(f,3)==3    %for RGB image
        
        set(handles.slider1,'enable','on')
        set(handles.edit6,'enable','on')
        f1=rgb2gray(f);
        set(handles.slider1,'value',graythresh(f)*255)
        set(handles.edit6,'string',num2str(graythresh(f)*255))
        f1=im2bw(f,graythresh(f));
        
    elseif size(f,3)==1 & ~islogical(f)
        
        set(handles.slider1,'enable','on')
        set(handles.edit6,'enable','on')
        f1=im2bw(f,graythresh(f));
        set(handles.slider1,'value',graythresh(f)*255)
        set(handles.edit6,'string',num2str(graythresh(f)*255))
        
    end
    
    kh=f1;
    g=logical(zeros(size(f1)));
    axes(handles.axes1)
    imshow(f1)
end

% --- Executes on selection change in popupmenu2.
function popupmenu2_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global kh g
g=logical(zeros(size(kh)));
v=get(hObject,'value');
if v==2  %Square
    
    set(handles.edit1,'enable','on')
    set(handles.text2,'enable','on')
    
    set(handles.edit2,'enable','off')
    set(handles.edit3,'enable','off')
    set(handles.edit4,'enable','off')
    set(handles.edit5,'enable','off')
    
    set(handles.text3,'enable','off')
    set(handles.text4,'enable','off')
    set(handles.text5,'enable','off')
    set(handles.text6,'enable','off')
    
    set(handles.edit1,'string',num2str(3));
    set(handles.edit2,'string',' ');
    set(handles.edit3,'string',' ');
    set(handles.edit4,'string',' ');
    set(handles.edit5,'string',' ');
    
elseif v==3 %Disk
    
    set(handles.edit1,'enable','on')
    set(handles.text2,'enable','on')
    
    set(handles.edit2,'enable','off')
    set(handles.edit3,'enable','off')
    set(handles.edit4,'enable','off')
    set(handles.edit5,'enable','off')
    
    set(handles.text3,'enable','off')
    set(handles.text4,'enable','off')
    set(handles.text5,'enable','off')
    set(handles.text6,'enable','off')
    
    set(handles.edit1,'string',num2str(1));
    set(handles.edit2,'string',' ');
    set(handles.edit3,'string',' ');
    set(handles.edit4,'string',' ');
    set(handles.edit5,'string',' ');
    
elseif v==4 %Line
    
    set(handles.edit1,'enable','off')
    set(handles.text2,'enable','off')
    
    set(handles.edit2,'enable','on')
    set(handles.edit3,'enable','on')
    set(handles.edit4,'enable','off')
    set(handles.edit5,'enable','off')
    
    set(handles.text3,'enable','on')
    set(handles.text4,'enable','off')
    set(handles.text5,'enable','on')
    set(handles.text6,'enable','off')
    
    set(handles.edit1,'string',' ');
    set(handles.edit2,'string',num2str(5));
    set(handles.edit3,'string',num2str(0));
    set(handles.edit4,'string',' ');
    set(handles.edit5,'string',' ');
    
elseif v==5 %Rectangle
    
    set(handles.edit1,'enable','off')
    set(handles.text2,'enable','off')
    
    set(handles.edit2,'enable','off')
    set(handles.edit3,'enable','off')
    set(handles.edit4,'enable','on')
    set(handles.edit5,'enable','on')
    
    set(handles.text3,'enable','off')
    set(handles.text4,'enable','on')
    set(handles.text5,'enable','off')
    set(handles.text6,'enable','on')
    
    set(handles.edit1,'string',' ');
    set(handles.edit2,'string',' ');
    set(handles.edit3,'string',' ');
    set(handles.edit4,'string',num2str(5));
    set(handles.edit5,'string',num2str(2));
    
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

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double
global kh g
g=logical(zeros(size(kh)));


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



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double
global kh g
g=logical(zeros(size(kh)));

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

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double
global kh g
g=logical(zeros(size(kh)));


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



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double
global kh g
g=logical(zeros(size(kh)));

% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double
global kh g
g=logical(zeros(size(kh)));


% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g rb1 rb2 kh pm

%region filling
%region filling
%region filling
%region filling
%region filling

r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
s=get(handles.slider1,'value');
s=round(s);
set(handles.edit6,'string',num2str(s))
p2=get(handles.popupmenu2,'value');
if p2==1  %No operator selected
    mgb=msgbox('Please select a Structure Element first.','Warning','Warn');
elseif p2~=1  %An operator has been selected
    if r1==1 %orginal image
        
        
        f1=f;
        if size(f,3)==3    %for RGB image
            f1=rgb2gray(f);
            f1=im2bw(f,s/255);
        elseif size(f,3)==1 & ~islogical(f)
            f1=im2bw(f,s/255);
        end
        
        
    elseif r2==1 %inverse image
        
        
        nf=imcomplement(f);
        if size(f,3)==3    %for RGB image
            nf=rgb2gray(imcomplement(f));
            nf=im2bw(imcomplement(f),s/255);
        elseif size(f,3)==1 & ~islogical(f)
            nf=im2bw(imcomplement(f),s/255);
        end
        
        
    end
    
    
    if ~isempty(pm) %Press Enter
        f1=pm;
        nf=pm;
    end
    
    if p2==2 %Square
        
        e1=round(str2num(get(handles.edit1,'string')));
        set(handles.edit1,'string',num2str(e1))
        s=strel('square',e1);
        
    elseif p2==3 %Disk
        
        e1=round(str2num(get(handles.edit1,'string')));
        set(handles.edit1,'string',num2str(e1))
        s=strel('disk',e1);
        
    elseif p2==4 %Line
        
        e2=round(str2num(get(handles.edit2,'string')));
        set(handles.edit2,'string',num2str(e2))
        e3=round(str2num(get(handles.edit3,'string')));
        set(handles.edit3,'string',num2str(e3))
        s=strel('line',e2,e3);
        
    elseif p2==5 %Rectangle
        
        e4=round(str2num(get(handles.edit4,'string')));
        set(handles.edit4,'string',num2str(e4))
        e5=round(str2num(get(handles.edit5,'string')));
        set(handles.edit5,'string',num2str(e5))
        s=strel('rectangle',[e4,e5]);
        
    end
    
    %start region filling
    %start region filling
    %start region filling
    %start region filling
    %start region filling
    
    if r2==1 %inverse image
        
        kh=nf;
        rb1=0;
        rb2=1;
        while 1
            
            [x,y]=ginput(1);
            if isempty(x) %Press Enter
                break
            end
            
            
            g(round(y),round(x))=1;
            imshow(g);
            
            while 1
                g1=g;
                g=imdilate(g,s) & ~nf;   
                axes(handles.axes1)     %start region filling
                imshow(g+nf)
                pause(0.001)
                if g==g1 
                    break
                end
            end
            
        end
        
        
        kh=g+nf;
        pm=kh;
        
    elseif r1==1 %orginal image
        
        kh=f1;
        rb1=1;
        rb2=0;
        
        while 1
            
            
            [x,y]=ginput(1);
            if isempty(x)
                break
            end
            
            
            g(round(y),round(x))=1;
            imshow(g);
            
            while 1
                g1=g;
                g=imdilate(g,s) & ~f1;
                axes(handles.axes1)     %start region filling
                imshow(g+f1)
                pause(0.001)
                if g==g1
                    break
                end
            end
            
        end
        
        kh=g+f1;
        pm=kh;
        
    end
end

% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g rb1 rb2 kh pm

%Reset ALL
%Reset ALL
%Reset ALL
%Reset ALL
%Reset ALL

pm=[];
set(handles.edit1,'enable','off')
set(handles.edit2,'enable','off')
set(handles.edit3,'enable','off')
set(handles.edit4,'enable','off')
set(handles.edit5,'enable','off')

set(handles.text2,'enable','off')
set(handles.text3,'enable','off')
set(handles.text4,'enable','off')
set(handles.text5,'enable','off')
set(handles.text6,'enable','off')



f1=f;
if size(f,3)==3    %for RGB image
    
    f1=rgb2gray(f);
    set(handles.slider1,'value',graythresh(f)*255)
    set(handles.edit6,'string',num2str(graythresh(f)*255))
    f1=im2bw(f,graythresh(f));
    
elseif size(f,3)==1 & ~islogical(f)
    
    f1=im2bw(f,graythresh(f));
    set(handles.slider1,'value',graythresh(f)*255)
    set(handles.edit6,'string',num2str(graythresh(f)*255))
    
end
kh=f1;


g=logical(zeros(size(f1)));
axes(handles.axes1)
imshow(f1)
set(handles.edit1,'string',' ')
set(handles.edit2,'string',' ')
set(handles.edit3,'string',' ')
set(handles.edit4,'string',' ')
set(handles.edit5,'string',' ')
set(handles.popupmenu2,'value',1)
set(handles.radiobutton1,'value',1)
set(handles.radiobutton2,'value',0)
rb1=1;
rb2=0;


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g rb1 rb2 kh pm 

%original image
%original image
%original image
%original image
%original image
%original image

pm=[];
rb1=1;
rb2=0;
f1=f;

if size(f,3)==3   %for RGB image
    
    f1=rgb2gray(f);
    set(handles.slider1,'value',graythresh(f)*255)
    set(handles.edit6,'string',num2str(graythresh(f)*255))
    f1=im2bw(f,graythresh(f));
    
elseif size(f,3)==1 & ~islogical(f)
    
    f1=im2bw(f,graythresh(f));
    set(handles.slider1,'value',graythresh(f)*255)
    set(handles.edit6,'string',num2str(graythresh(f)*255))
    
end


kh=f1;
g=logical(zeros(size(f1)));
axes(handles.axes1)
imshow(f1)
% Hint: get(hObject,'Value') returns toggle state of radiobutton1


% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g rb1 rb2 kh pm

%original image
%original image
%original image
%original image
%original image
%original image

pm=[];
rb1=0;
rb2=1;
f1=f;


if size(f,3)==3   %for RGB image
    
    f1=rgb2gray(f);
    set(handles.slider1,'value',graythresh(imcomplement(f))*255)
    set(handles.edit6,'string',num2str(graythresh(imcomplement(f))*255))
    f1=im2bw(f,graythresh(f));
    
elseif size(f,3)==1 & ~islogical(f)
    
    f1=im2bw(f,graythresh(f));
    set(handles.slider1,'value',graythresh(imcomplement(f))*255)
    set(handles.edit6,'string',num2str(graythresh(imcomplement(f))*255))
    
end
kh=f1;

f1=~f1;
g=logical(zeros(size(f1)));
axes(handles.axes1)
imshow(f1)
% Hint: get(hObject,'Value') returns toggle state of radiobutton2


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g kh FileName rb1 rb2 infoo

%Export image
%Export image
%Export image
%Export image
%Export image

s=get(handles.slider1,'value');
s=round(s);
if FileName==0 | isempty(FileName)
    FileName='Matlab Picture.PNG';
end
if isequal(infoo.Format,'GIF')
    FileName(end-2:end)='png';
end
f1=f;


if size(f,3)==3   %for RGB image
    f1=rgb2gray(f);
    f1=im2bw(f,s/255);
elseif size(f,3)==1 & ~islogical(f)
    f1=im2bw(f,s/255);
end


if ~isequal(kh,f1)
    masir=uigetdir;
    if masir~=0
        wb=waitbar(0,'Please wait ...');
        imwrite(kh,[masir,'/Region Filling ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
end


% --- Executes on slider movement.
function slider1_Callback(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g pm

%threshold
%threshold
%threshold
%threshold
%threshold

pm=[];
r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
s=get(handles.slider1,'value');
s=round(s);
set(handles.edit6,'string',num2str(s))

if r1==1 %original image
    
    
    f1=f;
    if size(f,3)==3   %for RGB image
        f1=rgb2gray(f);
        f1=im2bw(f,s/255);
    elseif size(f,3)==1 & ~islogical(f)
        f1=im2bw(f,s/255);
    end 
    g=f1;
    axes(handles.axes1)
    imshow(f1)
    
    
elseif r2==1 %inverse image
    
    
    f1=imcomplement(f);
    if size(f,3)==3   %for RGB image
        f1=rgb2gray(imcomplement(f));
        f1=im2bw(imcomplement(f),s/255);
    elseif size(f,3)==1 & ~islogical(f)
        f1=im2bw(imcomplement(f),s/255);
    end 
    g=f1;
    axes(handles.axes1)
    imshow(f1)
    
    
end
g=logical(zeros(size(f1)));
% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider


% --- Executes during object creation, after setting all properties.
function slider1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end



function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g pm

%threshold
%threshold
%threshold
%threshold
%threshold

pm=[];
r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
s=str2num(get(handles.edit6,'string'));
set(handles.slider1,'value',s)

if r1==1 %original image
    
    
    f1=f;
    if size(f,3)==3   %for RGB image
        f1=rgb2gray(f);
        f1=im2bw(f,s/255);
    elseif size(f,3)==1 & ~islogical(f)
        f1=im2bw(f,s/255);
    end
    g=f1;
    axes(handles.axes1)
    imshow(f1)
    
    
elseif r2==1 %inverse image
    
    
    f1=imcomplement(f);
    if size(f,3)==3   %for RGB image
        f1=rgb2gray(imcomplement(f));
        f1=im2bw(imcomplement(f),s/255);
    elseif size(f,3)==1 & ~islogical(f)
        f1=im2bw(imcomplement(f),s/255);
    end
    g=f1;
    axes(handles.axes1)
    imshow(f1)

    
end
% Hints: get(hObject,'String') returns contents of edit6 as text
%        str2double(get(hObject,'String')) returns contents of edit6 as a double


% --- Executes during object creation, after setting all properties.
function edit6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
