function varargout = sharpening_filters(varargin)
% SHARPENING_FILTERS MATLAB code for sharpening_filters.fig
%      SHARPENING_FILTERS, by itself, creates a new SHARPENING_FILTERS or raises the existing
%      singleton*.
%
%      H = SHARPENING_FILTERS returns the handle to a new SHARPENING_FILTERS or the handle to
%      the existing singleton*.
%
%      SHARPENING_FILTERS('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SHARPENING_FILTERS.M with the given input arguments.
%
%      SHARPENING_FILTERS('Property','Value',...) creates a new SHARPENING_FILTERS or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before sharpening_filters_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to sharpening_filters_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help sharpening_filters

% Last Modified by GUIDE v2.5 06-Jan-2018 15:53:57

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @sharpening_filters_OpeningFcn, ...
    'gui_OutputFcn',  @sharpening_filters_OutputFcn, ...
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


% --- Executes just before sharpening_filters is made visible.
function sharpening_filters_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to sharpening_filters (see VARARGIN)

% Choose default command line output for sharpening_filters
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);
global f g
logo=imread('ZoiLogosmall.png');
axes(handles.axes3)
imshow(logo)
set(handles.edit1,'enable','off')
set(handles.edit2,'enable','off')
set(handles.edit3,'enable','off')
set(handles.edit7,'enable','off')
set(handles.text2,'enable','off')
set(handles.text3,'enable','off')
set(handles.text4,'enable','off')
set(handles.text8,'enable','off')
axes(handles.axes1)
imshow(f)
g=f;
title('Original Picture')
axes(handles.axes2)
imshow(f)
title('Oiginal Picture')

% UIWAIT makes sharpening_filters wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = sharpening_filters_OutputFcn(hObject, eventdata, handles)
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

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1

global f g

v1=get(hObject,'value');

if v1 ~= 4
    set(handles.edit1,'enable','off')
    set(handles.edit2,'enable','off')
    set(handles.edit3,'enable','off')
    set(handles.edit7,'enable','off')
    set(handles.text2,'enable','off')
    set(handles.text3,'enable','off')
    set(handles.text4,'enable','off')
    set(handles.text8,'enable','off')
    set(handles.edit1,'string',' ');
    set(handles.edit2,'string',' ');
    set(handles.edit3,'string',' ');
    set(handles.edit7,'string',' ');
end

if v1 == 4
    set(handles.edit1,'enable','on')
    set(handles.edit2,'enable','on')
    set(handles.edit3,'enable','on')
    set(handles.edit7,'enable','on')
    set(handles.text2,'enable','on')
    set(handles.text3,'enable','on')
    set(handles.text4,'enable','on')
    set(handles.text8,'enable','on')
    set(handles.edit1,'string',num2str(3));
    set(handles.edit2,'string',num2str(3));
    set(handles.edit3,'string',num2str(5));
    set(handles.edit7,'string',num2str(1));
end


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


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global f g vpb1 vpb2
vpb1=1;
vpb2=0;

val1=get(handles.popupmenu1,'value');
val2=get(handles.popupmenu3,'value');

if val1 == 2
    
    h=[0,  -1,   0;
        -1,   5,  -1;
        0,  -1,  0;];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
    elseif val2==3
        g=imfilter(f,h,'symmetric');
    elseif val2==4
        g=imfilter(f,h,'circular');
    else
        g=imfilter(f,h);
    end
    
elseif val1==3
    
    h=[-1,  -1,  -1;
        -1,   9,  -1;
        -1,  -1,  -1;];
    
    if val2==2
        g=imfilter(f,h,'replicate');
    elseif val2==3
        g=imfilter(f,h,'symmetric');
    elseif val2==4
        g=imfilter(f,h,'circular');
    else
        g = imfilter(f,h);
    end
    
elseif val1==4
    
    k=str2num(get(handles.edit7,'string'));
    sigma=str2num(get(handles.edit3,'string'));
    hsize1=str2num(get(handles.edit1,'string'));
    hsize2=str2num(get(handles.edit2,'string'));
    h=fspecial('gaussian',[hsize1 hsize2],sigma);
    
    if val2==2
        g = imfilter(f,h,'replicate');
        g = f-g;
        g = f+k*g;
        
    elseif val2==3
        g = imfilter(f,h,'symmetric');
        g = f-g;
        g = f+k*g;
        
    elseif val2==4
        g = imfilter(f,h,'circular');
        g = f-g;
        g = f+k*g;
    else
        g = imfilter(f,h);
        g = f-g;
        g = f+k*g;
    end
    
elseif val1 == 5
    h = fspecial('sobel');
    
    if val2==2
        I1 = imfilter(f,h,'replicate');
        I2 = imfilter(f,h','replicate');
        g = f-(abs(I1)+abs(I2));
        
    elseif val2 == 3
        I1 = imfilter(f,h,'symmetric');
        I1 = imfilter(f,h','symmetric');
        g = f-(abs(I1)+abs(I2));
        
    elseif val2 == 4
        I1 = imfilter(f,h,'circular');
        I2 = imfilter(f,h','circular');
        g = f-(abs(I1)+abs(I2));
    else
        I1 = imfilter(f,h);
        I2 = imfilter(f,h);
        g = f-(abs(I1)+abs(I2));
    end
    
elseif val1 == 6
    
    h = fspecial('prewitt');
    
    if val2 == 2
        I1 = imfilter(f,h,'replicate');
        I2 = imfilter(f,h','replicate');
        g = f-(abs(I1)+abs(I2));
        
    elseif val2 == 3
        I1 = imfilter(f,h,'symmetric');
        I1 = imfilter(f,h','symmetric');
        g = f-(abs(I1)+abs(I2));
        
    elseif val2 == 4
        I1 = imfilter(f,h,'circular');
        I2 = imfilter(f,h','circular');
        g = f-(abs(I1)+abs(I2));
    else
        I1 = imfilter(f,h);
        I2 = imfilter(f,h);
        g = f-(abs(I1)+abs(I2));
    end
    
elseif val1 == 7
    
    h1 = [-1 0;
        0 1];
    
    h2=[0 -1;
        1  0];
    
    if val2 == 2
        I1 = imfilter(f,h1,'replicate');
        I2 = imfilter(f,h2,'replicate');
        g = f-(abs(I1)+abs(I2));
        
    elseif val2 == 3
        I1 = imfilter(f,h1,'symmetric');
        I1 = imfilter(f,h2,'symmetric');
        g = f-(abs(I1)+abs(I2));
        
    elseif val2 == 4
        I1 = imfilter(f,h1,'circular');
        I2 = imfilter(f,h2,'circular');
        g = f-(abs(I1)+abs(I2));
    else
        I1 = imfilter(f,h1);
        I2 = imfilter(f,h2);
        g = f-(abs(I1)+abs(I2));
    end
end

axes(handles.axes2)
imshow(g);
title('Sharped Image')

% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global f g vpb1 vpb2

vpb1=0;
vpb2=1;

val1=get(handles.popupmenu2,'value');
val2=get(handles.popupmenu4,'value');

if val1 == 2
    
    h=[0 1 0;
        1 -4 1;
        0 1 0;];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
        
    elseif val2==3
        g=imfilter(f,h,'symmetric');
        
    elseif val2==4
        g=imfilter(f,h,'circular');
    else
        g=imfilter(f,h);
    end
    
elseif val1 == 3
    
    h=[1  1  1;
        1 -8  1;
        1  1  1;];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
        
    elseif val2==3
        g=imfilter(f,h,'symmetric');
        
    elseif val2==4
        g=imfilter(f,h,'circular');
    else
        g=imfilter(f,h);
    end
    
elseif val1 == 4
    
    h=[-1 0;
        0 1;];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
        
    elseif val2==3
        g=imfilter(f,h,'symmetric');
        
    elseif val2==4
        g=imfilter(f,h,'circular');
    else
        g=imfilter(f,h);
    end
    
elseif val1 == 5
    
    h=[0 -1;
        1  0;];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
        
    elseif val2 == 3
        g=imfilter(f,h,'symmetric');
        
    elseif val2 == 4
        g = imfilter(f,h,'circular');
    else
        g = imfilter(f,h);
    end
    
elseif val1 == 6
    
    h1=[-1 0;
        0 1;];
    
    h2=[0 -1;
        1  0;];
    
    if val2 == 2
        I1 = imfilter(f,h1,'replicate');
        I2 = imfilter(f,h2,'replicate');
        g=abs(I1)+abs(I2);
        
    elseif val2 == 3
        I1 = imfilter(f,h1,'symmetric');
        I2 = imfilter(f,h2,'symmetric');
        g=abs(I1)+abs(I2);
        
    elseif val2 == 4
        I1 = imfilter(f,h1,'circular');
        I2 = imfilter(f,h2,'circular');
        g=abs(I1)+abs(I2);
    else
        I1 = imfilter(f,h1);
        I2 = imfilter(f,h2);
        g=abs(I1)+abs(I2);
    end
    
elseif val1 == 7
    
    h=[1  1  1;
        0  0  0;
        -1 -1 -1];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
        
    elseif val2 == 3
        g=imfilter(f,h,'symmetric');
        
    elseif val2 == 4
        g = imfilter(f,h,'circular');
    else
        g = imfilter(f,h);
    end
    
elseif val1 == 8
    
    h=[-1 0 1;
        -1 0 1;
        -1 0 1;];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
        
    elseif val2 == 3
        g=imfilter(f,h,'symmetric');
        
    elseif val2 == 4
        g = imfilter(f,h,'circular');
    else
        g = imfilter(f,h);
    end
    
elseif val1 == 9
    
    h1=[1  1  1;
        0  0  0;
        -1 -1 -1];
    
    h2=[-1 0 1;
        -1 0 1;
        -1 0 1;];
    
    if val2 == 2
        I1 = imfilter(f,h1,'replicate');
        I2 = imfilter(f,h2,'replicate');
        g=abs(I1)+abs(I2);
        
    elseif val2 == 3
        I1 = imfilter(f,h1,'symmetric');
        I2 = imfilter(f,h2,'symmetric');
        g=abs(I1)+abs(I2);
        
    elseif val2 == 4
        I1 = imfilter(f,h1,'circular');
        I2 = imfilter(f,h2,'circular');
        g=abs(I1)+abs(I2);
    else
        I1 = imfilter(f,h1);
        I2 = imfilter(f,h2);
        g=abs(I1)+abs(I2);
    end
    
elseif val1 == 10
    
    h=[-1 -2 -1;
        0 0 0;
        1 2 1;];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
        
    elseif val2 == 3
        g=imfilter(f,h,'symmetric');
        
    elseif val2 == 4
        g = imfilter(f,h,'circular');
    else
        g = imfilter(f,h);
    end
    
elseif val1 == 11
    
    h=[-1 0 1;
        -2 0 2;
        -1 0 1;];
    
    if val2 == 2
        g=imfilter(f,h,'replicate');
        
    elseif val2 == 3
        g=imfilter(f,h,'symmetric');
        
    elseif val2 == 4
        g = imfilter(f,h,'circular');
    else
        g = imfilter(f,h);
    end
    
elseif val1 == 12
    
    h1=[-1 -2 -1;
        0   0  0;
        1   2  1;];
    
    h2=[-1 0 1;
        -2 0 2;
        -1 0 1;];
    
    if val2 == 2
        I1 = imfilter(f,h1,'replicate');
        I2 = imfilter(f,h2,'replicate');
        g=abs(I1)+abs(I2);
        
    elseif val2 == 3
        I1 = imfilter(f,h1,'symmetric');
        I2 = imfilter(f,h2,'symmetric');
        g=abs(I1)+abs(I2);
        
    elseif val2 == 4
        I1 = imfilter(f,h1,'circular');
        I2 = imfilter(f,h2,'circular');
        g=abs(I1)+abs(I2);
    else
        I1 = imfilter(f,h1);
        I2 = imfilter(f,h2);
        g=abs(I1)+abs(I2);
    end
end

axes(handles.axes2)
imshow(g,[])
title('Detected Image')



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

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



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

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



function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

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



function edit8_Callback(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit8 as text
%        str2double(get(hObject,'String')) returns contents of edit8 as a double


% --- Executes during object creation, after setting all properties.
function edit8_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in popupmenu4.
function popupmenu4_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu4 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu4


% --- Executes during object creation, after setting all properties.
function popupmenu4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
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



function edit7_Callback(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit7 as text
%        str2double(get(hObject,'String')) returns contents of edit7 as a double


% --- Executes during object creation, after setting all properties.
function edit7_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in popupmenu3.
function popupmenu3_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu3 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu3


% --- Executes during object creation, after setting all properties.
function popupmenu3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global f g
v1=get(handles.radiobutton1,'value');
v2=get(handles.radiobutton2,'value');
if v1 == 1
    figure
    imshow(f)
    [x,y]=ginput(1);
    subplot(2,1,1)
    plot(f(round(y),:))
    title('Original')
    subplot(2,1,2)
    plot(g(round(y),:))
    title('Filtered')
elseif v2 == 1
    figure
    imshow(f)
    [x,y]=ginput(1);
    subplot(2,1,1)
    plot(f(:,round(x)))
    title('Original')
    subplot(2,1,2)
    plot(g(:,round(x)))
    title('Filtered')
end


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g

figure('name','roipoly')
imshow(f)
title('\color{red}select 2 corners of rectangle.')
for i=1:2
    [x(i),y(i)]=ginput(1);
    x=round(x); y=round(y);
    hold on
    plot(x(i),y(i),'ob','markerfacecolor','blue'),title('\color{red}select 2 corners of rectangle.')
end
minx=min(x);
maxx=max(x);
miny=min(y);
maxy=max(y);
X=[minx maxx maxx minx minx];
Y=[maxy maxy miny miny maxy];
plot(X,Y,'-.w','linewidth',3)
pause(1)
close Figure roipoly
f1=f(miny:maxy,minx:maxx,:);
if g == f
    figure
    if size(f,3)==3
        mesh(rgb2gray(f1))
        title('Original')
    elseif size(f,3)==1
        mesh(f1)
        title('Original')
    end
else
    figure
    if size(f,3)==3
        mesh(rgb2gray(f1))
        title('Original')
        figure
        g1=g(miny:maxy,minx:maxx,:);
        mesh(rgb2gray(g1))
        title('Filtered')
    elseif size(f,3)==1
        mesh(f1)
        title('Original')
        figure
        g1=g(miny:maxy,minx:maxx,:);
        mesh(g1)
        title('Filtered')
    end
end
% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton1



% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton2


% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global g f vpb1 vpb2 FileName infoo
if FileName==0 | isempty(FileName)
    FileName='Matlab Picture.PNG';
end
if isequal(infoo.Format,'GIF')
    FileName(end-2:end)='png';
end
if ~isequal(g,f)
    if vpb2==1
        masir=uigetdir;
        if masir~=0
            wb=waitbar(0,'Please wait...');
            imwrite(g,[masir,'/Edge ',FileName])
            
            
            for i=1:1000
                waitbar(i/1000);
            end
            pause(0.1)
            close(wb)
        end
    elseif vpb1==1
        masir=uigetdir;
        if masir~=0
            wb=waitbar(0,'Please wait...');
            imwrite(g,[masir,'/Sharp ',FileName])
            
            
            for i=1:1000
                waitbar(i/1000);
            end
            pause(0.1)
            close(wb)
        end
    end
end
