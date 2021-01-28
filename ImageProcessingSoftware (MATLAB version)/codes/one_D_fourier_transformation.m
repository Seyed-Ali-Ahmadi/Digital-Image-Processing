function varargout = one_D_fourier_transformation(varargin)
% ONE_D_FOURIER_TRANSFORMATION MATLAB code for one_D_fourier_transformation.fig
%      ONE_D_FOURIER_TRANSFORMATION, by itself, creates a new ONE_D_FOURIER_TRANSFORMATION or raises the existing
%      singleton*.
%
%      H = ONE_D_FOURIER_TRANSFORMATION returns the handle to a new ONE_D_FOURIER_TRANSFORMATION or the handle to
%      the existing singleton*.
%
%      ONE_D_FOURIER_TRANSFORMATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ONE_D_FOURIER_TRANSFORMATION.M with the given input arguments.
%
%      ONE_D_FOURIER_TRANSFORMATION('Property','Value',...) creates a new ONE_D_FOURIER_TRANSFORMATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before one_D_fourier_transformation_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to one_D_fourier_transformation_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help one_D_fourier_transformation

% Last Modified by GUIDE v2.5 01-Jan-2018 22:41:49

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @one_D_fourier_transformation_OpeningFcn, ...
    'gui_OutputFcn',  @one_D_fourier_transformation_OutputFcn, ...
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


% --- Executes just before one_D_fourier_transformation is made visible.
function one_D_fourier_transformation_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to one_D_fourier_transformation (see VARARGIN)
logo=imread('ZoiLogosmall.png');
axes(handles.axes3)
imshow(logo)
axes(handles.axes1)
whitebg('black')
x1=0:0.001:0.5-0.001;
x2=0.5;
x3=0.5+0.001:0.001:1;
y1=zeros(1,length(x1));
y2=0.08;
y3=zeros(1,length(x3));
x=[x1 x2 x3];
y=[y1 y2 y3];
plot(x,y,'g'),axis([0 1 0 .1]),set(gca,'xtick',0:0.05:1)
title('\color{red}Spatial Domain')
axes(handles.axes2)
whitebg('black')
g=fft(y);
g1=abs(fftshift(g));
plot(x,g1)
title('\color{red}Frequency Domain')
set(handles.edit1,'string',num2str(1));
set(handles.edit3,'string',num2str(1));
set(handles.edit2,'string',num2str(0.5));
set(handles.edit4,'string',num2str(0.5));
set(handles.edit5,'string',num2str(0.05));
% Choose default command line output for one_D_fourier_transformation
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes one_D_fourier_transformation wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = one_D_fourier_transformation_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
v=round(str2num(get(hObject,'string')));
set(handles.edit3,'string',num2str(round(v)));
D=[];
if v==1
    set(handles.edit1,'string',' ');
    set(handles.edit2,'string',' ');
    set(handles.edit4,'string',num2str(0.5));
end
set(handles.edit1,'string',' ');
set(handles.edit2,'string',' ');
v5=str2num(get(handles.edit5,'string'));
d=1/(v+1);

set(handles.edit4,'string',num2str(d));
D=0:d:1;
X=[];
Y=[];
x=[];
y=[];
x(1,:) = D(1):0.001:d-v5/2;
y(1,:) = zeros(1,length(x(1,:)));
X=[X,x];
Y=[Y,y];
for i=2:length(D)-1
    x=[];
    y=[];
    x(1,:)=D(i)-v5/2:0.001:D(i)+v5/2;
    y(1,:)=0.08*ones(1,length(x(1,:)));
    X=[X,x];
    Y=[Y,y];
    x=[];
    y=[];
    x(1,:) = D(i)+v5/2:0.001:D(i)+v5/2+d-v5;
    y(1,:) = zeros(1,length(x(1,:)));
    X=[X,x];
    Y=[Y,y];
end
x=[];
y=[];
x(1,:) = X(end):0.001:D(i) + d;
y(1,:) = zeros(1,length(x(1,:)));
X=[X,x];
Y=[Y,y];
axes(handles.axes1)
plot(X,Y,'g'),axis([0 1 0 .1]),set(gca,'xtick',0:0.05:1)
title('\color{red}Spatial Domain')


axes(handles.axes2)
g=fft(Y);
g1=abs(fftshift(g));
plot(X,g1)
title('\color{red}Frequency Domain')
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



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
v=round(str2num(get(handles.edit3,'string')));
set(handles.edit3,'string',num2str(round(v)));
v4=str2num(get(hObject,'string'));
D=[];
if v==1
    set(handles.edit1,'string',' ');
    set(handles.edit2,'string',' ');
end
set(handles.edit1,'string',' ');
set(handles.edit2,'string',' ');
v5=str2num(get(handles.edit5,'string'));

d=1/(v+1);
D=0:d:1;
n=d/v4;
n=n-1;
zarib=(0.5-D(2:end-1))./(d/v4);
D(2:end-1)=D(2:end-1)+zarib*n;
dd=d;
if v>1
dd=D(3)-D(2);
end
X=[];
Y=[];
x=[];
y=[];
x(1,:) = D(1):0.001:D(2)-v5/2;
y(1,:) = zeros(1,length(x(1,:)));
X=[X,x];
Y=[Y,y];
for i=2:length(D)-1
    x=[];
    y=[];
    x(1,:)=D(i)-v5/2:0.001:D(i)+v5/2;
    y(1,:)=0.08*ones(1,length(x(1,:)));
    X=[X,x];
    Y=[Y,y];
    x=[];
    y=[];
    x(1,:) = D(i)+v5/2:0.001:D(i)+v5/2+dd-v5;
    y(1,:) = zeros(1,length(x(1,:)));
    X=[X,x];
    Y=[Y,y];
end
x=[];
y=[];
x(1,:) = X(end):0.001:1;
y(1,:) = zeros(1,length(x(1,:)));
X=[X,x];
Y=[Y,y];
axes(handles.axes1)
plot(X,Y,'g'),axis([0 1 0 .1]),set(gca,'xtick',0:0.05:1)
title('\color{red}Spatial Domain')


axes(handles.axes2)
g=fft(Y);
g1=abs(fftshift(g));
plot(X,g1)
title('\color{red}Frequency Domain')
% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


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
v=round(str2num(get(handles.edit3,'string')));
set(handles.edit3,'string',num2str(round(v)));
v4=str2num(get(handles.edit4,'string'));
D=[];
if v==1
    set(handles.edit1,'string',' ');
    set(handles.edit2,'string',' ');
end
set(handles.edit1,'string',' ');
set(handles.edit2,'string',' ');
v5=str2num(get(handles.edit5,'string'));

d=1/(v+1);

D=0:d:1;
n=d/v4;
n=n-1;
zarib=(0.5-D(2:end-1))./(d/v4);
D(2:end-1)=D(2:end-1)+zarib*n;
dd=d;
if v>1
dd=D(3)-D(2);
end
X=[];
Y=[];
x=[];
y=[];
x(1,:) = D(1):0.001:D(2)-v5/2;
y(1,:) = zeros(1,length(x(1,:)));
X=[X,x];
Y=[Y,y];
for i=2:length(D)-1
    x=[];
    y=[];
    x(1,:)=D(i)-v5/2:0.001:D(i)+v5/2;
    y(1,:)=0.08*ones(1,length(x(1,:)));
    X=[X,x];
    Y=[Y,y];
    x=[];
    y=[];
    x(1,:) = D(i)+v5/2:0.001:D(i)+v5/2+dd-v5;
    y(1,:) = zeros(1,length(x(1,:)));
    X=[X,x];
    Y=[Y,y];
end
x=[];
y=[];
x(1,:) = X(end):0.001:1;
y(1,:) = zeros(1,length(x(1,:)));
X=[X,x];
Y=[Y,y];
axes(handles.axes1)
plot(X,Y,'g'),axis([0 1 0 .1]),set(gca,'xtick',0:0.05:1)
title('\color{red}Spatial Domain')


axes(handles.axes2)
g=fft(Y);
g1=abs(fftshift(g));
plot(X,g1)
title('\color{red}Frequency Domain')

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double


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



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
v=round(str2num(get(hObject,'string')));
D=[];
if v==1
    set(handles.edit2,'string',num2str(0.5));
    set(handles.edit3,'string',num2str(1));
    set(handles.edit4,'string',num2str(0.5));
    set(handles.edit5,'string',num2str(0.05));
end
set(handles.edit3,'string',num2str(1));
set(handles.edit4,'string',num2str(0.5));
set(handles.edit5,'string',num2str(0.05));
set(handles.edit1,'string',num2str(round(v)));
d=1/(v+1);
set(handles.edit2,'string',num2str(d));
D=0:d:1;
X=[];
Y=[];
for i=1:length(D)-1
    x(1,:)=D(i)+0.001:0.001:D(i+1)-0.001;
    y(1,:)=zeros(1,length(x(1,:)));
    if i==1
        X=[X,x];
        Y=[Y,zeros(1,length(x))];
    elseif i>1
        X=[X,D(i),x];
        Y=[Y,0.08,zeros(1,length(x))];
    end
    
end
axes(handles.axes1)
plot(X,Y,'g'),axis([0 1 0 .1]),set(gca,'xtick',0:0.05:1)
title('\color{red}Spatial Domain')


axes(handles.axes2)
g=fft(Y);
g1=abs(fftshift(g));
plot(X,g1)
title('\color{red}Frequency Domain')
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



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
v=round(str2num(get(handles.edit1,'string')));
D=[];
if v==1
    set(handles.edit2,'string',num2str(0.5));
set(handles.edit3,'string',num2str(1));
set(handles.edit4,'string',num2str(0.5));
set(handles.edit5,'string',num2str(0.05));
end
set(handles.edit3,'string',num2str(1));
set(handles.edit4,'string',num2str(0.5));
set(handles.edit5,'string',num2str(0.05));
set(handles.edit1,'string',num2str(round(v)));
v2=str2num(get(handles.edit2,'string'));
d=1/(v+1);
D=0:d:1;
n=d/v2;
n=n-1;
zarib=(0.5-D(2:end-1))./(d/v2);
D(2:end-1)=D(2:end-1)+zarib*n;
X=[];
Y=[];
for i=1:length(D)-1
    x(1,:)=D(i)+0.001:0.001:D(i+1)-0.001;
    y(1,:)=zeros(1,length(x(1,:)));
    if i==1
        X=[X,x];
        Y=[Y,zeros(1,length(x))];
    elseif i>1
        X=[X,D(i),x];
        Y=[Y,0.08,zeros(1,length(x))];
    end
    clear x y
end
axes(handles.axes1)
plot(X,Y,'g'),axis([0 1 0 .1]),set(gca,'xtick',0:0.05:1)
title('\color{red}Spatial Domain')


axes(handles.axes2)
g=fft(Y);
g1=abs(fftshift(g));
plot(X,g1)
title('\color{red}Frequency Domain')
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
