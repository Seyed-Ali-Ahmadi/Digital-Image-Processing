function varargout = contrast_gray(varargin)
% CONTRAST_GRAY MATLAB code for contrast_gray.fig
%      CONTRAST_GRAY, by itself, creates a new CONTRAST_GRAY or raises the existing
%      singleton*.
%
%      H = CONTRAST_GRAY returns the handle to a new CONTRAST_GRAY or the handle to
%      the existing singleton*.
%
%      CONTRAST_GRAY('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in CONTRAST_GRAY.M with the given input arguments.
%
%      CONTRAST_GRAY('Property','Value',...) creates a new CONTRAST_GRAY or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before contrast_gray_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to contrast_gray_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help contrast_gray

% Last Modified by GUIDE v2.5 04-Feb-2018 00:54:48

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @contrast_gray_OpeningFcn, ...
                   'gui_OutputFcn',  @contrast_gray_OutputFcn, ...
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


% --- Executes just before contrast_gray is made visible.
function contrast_gray_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to contrast_gray (see VARARGIN)

% Choose default command line output for contrast_gray
handles.output = hObject;
global f g
logo=imread('ZoiLogosmall.png');
axes(handles.axes3)
imshow(logo)
g=f;
axes(handles.axes1)
imshow(f)
set(handles.edit1,'string',num2str(1));
set(handles.edit2,'string',num2str(min(min(f))));
set(handles.edit3,'string',num2str(max(max(f))));

set(handles.slider1,'value',min(min(f)));
set(handles.slider2,'value',max(max(f)));

s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
axes(handles.axes2)
h=imhist(f);                        
h=255*h/max(h);                         %<== plot of function transformation
x=[0:0.01:255];                         %<== plot of function transformation    
y=[0:0.01:255];                         %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h)                                  %<== plot of function transformation
hold on                                 %<== plot of function transformation
plot(x,y,'k')                           %<== plot of function transformation
plot([min(min(f)) min(min(f))],[0,max(h)],'k','linewidth',2)
plot([max(max(f)) max(max(f))],[0,max(h)],'k','linewidth',2)

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes contrast_gray wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = contrast_gray_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g
set(handles.edit1,'string',num2str(1));
gamma=str2num(get(handles.edit1,'string'));

set(handles.slider1,'value',min(min(f)));
set(handles.slider2,'value',max(max(f)));

s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f);
h1=255*h1/max(h1);                      %<== plot of function transformation
x=[0 255];                              %<== plot of function transformation
y=[0 255];                              %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1)                                 %<== plot of function transformation
hold on                                 %<== plot of function transformation    
plot(x,y,'k')                           %<== plot of function transformation    

plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)

hold off
axes(handles.axes1)
if s1~=s2
g=imadjust(f,[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma);

imshow(g)
end



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double
global f g
clear x
gamma=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma));

s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f);                   %<== plot of function transformation
h1=255*h1/max(h1);              %<== plot of function transformation
x=0:0.01:255;                   %<== plot of function transformation
y=255*(x/255).^gamma;           %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1)                         %<== plot of function transformation
hold on                         %<== plot of function transformation
plot(x,y,'k')                   %<== plot of function transformation    

plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)

hold off
axes(handles.axes1)
if s1~=s2
g=imadjust(f,[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma);

imshow(g)
end


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
global f g
clear x
gamma=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma));

e2=str2num(get(handles.edit2,'string'));
e3=str2num(get(handles.edit3,'string'));

set(handles.slider1,'value',e2);
set(handles.slider2,'value',e3);

s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f);                       %<== plot of function transformation
h1=255*h1/max(h1);                  %<== plot of function transformation
x=0:0.01:255;                       %<== plot of function transformation    
y=255*(x/255).^gamma;               %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1)                             %<== plot of function transformation
hold on                             %<== plot of function transformation    
plot(x,y,'k')                       %<== plot of function transformation

plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)

hold off
axes(handles.axes1)
if s1~=s2
g=imadjust(f,[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma);

imshow(g)
end


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
global f g
clear x
gamma=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma));

e2=str2num(get(handles.edit2,'string'));
e3=str2num(get(handles.edit3,'string'));

set(handles.slider1,'value',e2);
set(handles.slider2,'value',e3);

s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f);                       %<== plot of function transformation
h1=255*h1/max(h1);                  %<== plot of function transformation    
x=0:0.01:255;                       %<== plot of function transformation
y=255*(x/255).^gamma;               %<== plot of function transformation        
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1)                             %<== plot of function transformation       
hold on                             %<== plot of function transformation    
plot(x,y,'k')                       %<== plot of function transformation    

plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)

hold off
axes(handles.axes1)
if s1~=s2
g=imadjust(f,[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma);

imshow(g)
end


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


% --- Executes on slider movement.
function slider1_Callback(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f g
clear x
gamma=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma));
s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f);                           %<== plot of function transformation
h1=255*h1/max(h1);                      %<== plot of function transformation
x=0:0.01:255;                           %<== plot of function transformation            
y=255*(x/255).^gamma;                   %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1)                                 %<== plot of function transformation
hold on                                 %<== plot of function transformation
plot(x,y,'k')                           %<== plot of function transformation

plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)

hold off
axes(handles.axes1)
if s1~=s2
g=imadjust(f,[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma);

imshow(g)
end


% --- Executes during object creation, after setting all properties.
function slider1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on slider movement.
function slider2_Callback(hObject, eventdata, handles)
% hObject    handle to slider2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f g
clear x
gamma=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma));
s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f);                                   %<== plot of function transformation
h1=255*h1/max(h1);                              %<== plot of function transformation
x=0:0.01:255;                                   %<== plot of function transformation
y=255*(x/255).^gamma;                           %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1)                                         %<== plot of function transformation    
hold on                                         %<== plot of function transformation
plot(x,y,'k')                                   %<== plot of function transformation

plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)

hold off
axes(handles.axes1)
if s1~=s2
g=imadjust(f,[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma);

imshow(g)
end


% --- Executes during object creation, after setting all properties.
function slider2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global g f FileName infoo

%Export image

if FileName==0 | isempty(FileName)
    FileName='Matlab Picture.PNG';
end
if isequal(infoo.Format,'GIF')
    FileName(end-2:end)='png';
end
if ~isequal(g,f)
    masir=uigetdir;
    if masir~=0
        wb=waitbar(0,'Please wait...');
        imwrite(g,[masir,'/Contrast gray ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
end
