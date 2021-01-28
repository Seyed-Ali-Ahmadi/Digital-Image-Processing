function varargout = brightness(varargin)
% BRIGHTNESS MATLAB code for brightness.fig
%      BRIGHTNESS, by itself, creates a new BRIGHTNESS or raises the existing
%      singleton*.
%
%      H = BRIGHTNESS returns the handle to a new BRIGHTNESS or the handle to
%      the existing singleton*.
%
%      BRIGHTNESS('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in BRIGHTNESS.M with the given input arguments.
%
%      BRIGHTNESS('Property','Value',...) creates a new BRIGHTNESS or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before brightness_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to brightness_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help brightness

% Last Modified by GUIDE v2.5 04-Feb-2018 04:20:32

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @brightness_OpeningFcn, ...
    'gui_OutputFcn',  @brightness_OutputFcn, ...
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


% --- Executes just before brightness is made visible.
function brightness_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to brightness (see VARARGIN)

% Choose default command line output for brightness
handles.output = hObject;

% Update handles structure
global f g val1 val2 val3
logo=imread('ZoiLogosmall.png');
axes(handles.axes4)
imshow(logo)
if size(f,3)==1
    set(handles.radiobutton1,'enable','off')
    set(handles.radiobutton2,'enable','off')
    set(handles.radiobutton3,'enable','off')
end
val3=0;val2=0;val1=0;
guidata(hObject, handles);
axes(handles.axes1)
imshow(f)
g=f;
val=get(handles.slider1,'value');
set(handles.edit1,'string',round(val));
axes(handles.axes2)
imhist(f(:,:,1))
% UIWAIT makes brightness wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = brightness_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton1
global f val1 g
axes(handles.axes2);
imhist(g)
set(handles.slider1,'value',val1);
val1=get(handles.slider1,'value');
if size(f,3)==1
    g=imadd(f,get(handles.slider1,'value'));
    axes(handles.axes2);
    imhist(g)
elseif size(f,3)==3
    set(handles.slider1,'value',val1);
    set(handles.edit1,'string',round(val1));
    g(:,:,1)=imadd(f(:,:,1),val1);
    axes(handles.axes2);
    imhist(g(:,:,1))
end


% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton2
global f val2 g
axes(handles.axes2);
imhist(g)
set(handles.slider1,'value',val2);
val2=get(handles.slider1,'value');
if size(f,3)==1
    g=imadd(f,get(handles.slider1,'value'));
    axes(handles.axes2);
    imhist(g)
elseif size(f,3)==3
    set(handles.slider1,'value',val2);
    set(handles.edit1,'string',round(val2));
    g(:,:,2)=imadd(f(:,:,2),val2);
    axes(handles.axes2);
    imhist(g(:,:,2))
end

% --- Executes on button press in radiobutton3.
function radiobutton3_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton3
global f val3 g
axes(handles.axes2);
imhist(g)
set(handles.slider1,'value',val3);
val3=get(handles.slider1,'value');
if size(f,3)==1
    g=imadd(f,get(handles.slider1,'value'));
    axes(handles.axes2);
    imhist(g)
elseif size(f,3)==3
    set(handles.slider1,'value',val3);
    set(handles.edit1,'string',round(val3));
    g(:,:,3)=imadd(f(:,:,3),val3);
    axes(handles.axes2);
    imhist(g(:,:,3))
end

% --- Executes on slider movement.
function slider1_Callback(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f val1 val2 val3 g
axes(handles.axes1)
imshow(g)
r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
r3=get(handles.radiobutton3,'value');
if r1==1
    
    val1=get(handles.slider1,'value');
    set(handles.edit1,'string',round(val1));
    if size(f,3)==1
        g=imadd(f,get(handles.slider1,'value'));
        axes(handles.axes2);
        imhist(g)
        axes(handles.axes1)
        imshow(g)
    elseif size(f,3)==3
        g(:,:,1)=imadd(f(:,:,1),val1);
        axes(handles.axes2);
        imhist(g(:,:,1))
        axes(handles.axes1);
        imshow(g)
    end
elseif r2==1
    
    val2=get(handles.slider1,'value');
    set(handles.edit1,'string',round(val2));
    if size(f,3)==1
        g=imadd(f,get(handles.slider1,'value'));
        axes(handles.axes2);
        imhist(g)
        axes(handles.axes1);
        imshow(g)
    elseif size(f,3)==3
        g(:,:,2)=imadd(f(:,:,2),val2);
        axes(handles.axes2);
        imhist(g(:,:,2))
        axes(handles.axes1);
        imshow(g)
    end
elseif r3==1
    
    val3=get(handles.slider1,'value');
    set(handles.edit1,'string',round(val3));
    if size(f,3)==1
        g=imadd(f,get(handles.slider1,'value'));
        axes(handles.axes2);
        imhist(g)
        axes(handles.axes1);
        imshow(g)
    elseif size(f,3)==3
        g(:,:,3)=imadd(f(:,:,3),val3);
        axes(handles.axes2);
        imhist(g(:,:,3))
        axes(handles.axes1);
        imshow(g)
    end
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



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g val1 val2 val3
r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
r3=get(handles.radiobutton3,'value');
if r1==1
    val1=str2num(get(handles.edit1,'string'));
    set(handles.slider1,'value',round(val1));
    
    if size(f,3)==1
        g=imadd(f,get(handles.slider1,'value'));
        axes(handles.axes2);
        imhist(g)
        axes(handles.axes1);
        imshow(g)
    elseif size(f,3)==3
        g(:,:,1)=imadd(f(:,:,1),val1);
        axes(handles.axes2);
        imhist(g(:,:,1))
        axes(handles.axes1);
        imshow(g)
    end
elseif r2==1
    
    val2=str2num(get(handles.edit1,'string'));
    set(handles.slider1,'value',round(val2));
    if size(f,3)==1
        g=imadd(f,get(handles.slider1,'value'));
        axes(handles.axes2);
        imhist(g)
        axes(handles.axes1);
        imshow(g)
    elseif size(f,3)==3
        g(:,:,2)=imadd(f(:,:,2),val2);
        axes(handles.axes2);
        imhist(g(:,:,2))
        axes(handles.axes1);
        imshow(g)
    end
elseif r3==1
   
    val3=str2num(get(handles.edit1,'string'));
     set(handles.slider1,'value',round(val3));
    if size(f,3)==1
        g=imadd(f,get(handles.slider1,'value'));
        axes(handles.axes2);
        imhist(g)
        axes(handles.axes1);
        imshow(g)
    elseif size(f,3)==3
        g(:,:,3)=imadd(f(:,:,3),val2);
        axes(handles.axes2);
        imhist(g(:,:,3))
        axes(handles.axes1);
        imshow(g)
    end
end
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

%%
%help : zamani k tasvir rangi nabashad dar har yek az radio buttom ha
%taghirat mishavad ijad kard vali taghirat ruye aks yeksan ast dar har
%kodam az anha


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g FileName infoo
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
        imwrite(g,[masir,'/Brightness ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
    
end


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g val1 val2 val3
val3=0;val2=0;val1=0;
axes(handles.axes1)
imshow(f)
g=f;
set(handles.slider1,'value',0);
set(handles.edit1,'string',num2str(0))
set(handles.radiobutton1,'value',1)
axes(handles.axes2)
imhist(f(:,:,1))
