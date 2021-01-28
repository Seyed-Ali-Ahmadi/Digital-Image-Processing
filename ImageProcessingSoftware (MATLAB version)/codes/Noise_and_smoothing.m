function varargout = Noise_and_smoothing(varargin)
% NOISE_AND_SMOOTHING MATLAB code for Noise_and_smoothing.fig
%      NOISE_AND_SMOOTHING, by itself, creates a new NOISE_AND_SMOOTHING or raises the existing
%      singleton*.
%
%      H = NOISE_AND_SMOOTHING returns the handle to a new NOISE_AND_SMOOTHING or the handle to
%      the existing singleton*.
%
%      NOISE_AND_SMOOTHING('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in NOISE_AND_SMOOTHING.M with the given input arguments.
%
%      NOISE_AND_SMOOTHING('Property','Value',...) creates a new NOISE_AND_SMOOTHING or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Noise_and_smoothing_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Noise_and_smoothing_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Noise_and_smoothing

% Last Modified by GUIDE v2.5 02-Feb-2018 21:54:15

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @Noise_and_smoothing_OpeningFcn, ...
    'gui_OutputFcn',  @Noise_and_smoothing_OutputFcn, ...
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


% --- Executes just before Noise_and_smoothing is made visible.
function Noise_and_smoothing_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Noise_and_smoothing (see VARARGIN)
global f g z
logo=imread('ZoiLogosmall.png');
axes(handles.axes3)
imshow(logo)
set(handles.edit1,'enable','off')
set(handles.edit2,'enable','off')
set(handles.edit3,'enable','off')
set(handles.edit4,'enable','off')
set(handles.edit5,'enable','off')
set(handles.edit6,'enable','off')
g=f;
z=f;
axes(handles.axes1)
imshow(f)
title('orginal picture')
axes(handles.axes2)
imshow(f)
title('Filtered or Noised picture')
% Choose default command line output for Noise_and_smoothing
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Noise_and_smoothing wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Noise_and_smoothing_OutputFcn(hObject, eventdata, handles)
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
global f
v=get(hObject,'value');
if v==2 %average filter
    set(handles.edit1,'enable','on')
    set(handles.edit2,'enable','on')
    set(handles.edit3,'enable','off')
    set(handles.edit1,'string',num2str(3))
    set(handles.edit2,'string',num2str(3))
    set(handles.edit3,'string',' ')
elseif v==3 %gaussian filter
    set(handles.edit1,'enable','on')
    set(handles.edit2,'enable','on')
    set(handles.edit3,'enable','on')
    set(handles.edit1,'string',num2str(3))
    set(handles.edit2,'string',num2str(3))
    set(handles.edit3,'string',num2str(0.5))
elseif v==4 %median filter
    set(handles.edit1,'enable','on')
    set(handles.edit2,'enable','on')
    set(handles.edit3,'enable','off')
    set(handles.edit1,'string',num2str(3))
    set(handles.edit2,'string',num2str(3))
    set(handles.edit3,'string',' ')
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


% --- Executes on button press in checkbox1.
function checkbox1_Callback(hObject, eventdata, handles)
% hObject    handle to checkbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox1



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


% --- Executes on selection change in popupmenu2.
function popupmenu3_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f
v1=get(hObject,'value');
if v1==2 %gaussian Noise
    set(handles.edit4,'enable','on')
    set(handles.edit5,'enable','on')
    set(handles.edit6,'enable','off')
    set(handles.edit4,'string',num2str(0))
    set(handles.edit5,'string',num2str(0.01))
    set(handles.edit6,'string',' ')
elseif v1==3 %salt & pepper Noise
    set(handles.edit4,'enable','off')
    set(handles.edit5,'enable','off')
    set(handles.edit6,'enable','on')
    set(handles.edit4,'string',' ')
    set(handles.edit5,'string',' ')
    set(handles.edit6,'string',num2str(0.05))
end
% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu2 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu2


% --- Executes during object creation, after setting all properties.
function popupmenu3_CreateFcn(hObject, eventdata, handles)
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
global f g z

% Filtering
% Filtering
% Filtering
% Filtering
% Filtering

ch=get(handles.checkbox1,'value');
if ch==0 %perform on original image
    
    g=f;
    v=get(handles.popupmenu1,'value');
    v2=get(handles.popupmenu2,'value');
    if v==2 %average filter
        
        e1=str2num(get(handles.edit1,'string'));
        e2=str2num(get(handles.edit2,'string'));
        set(handles.edit3,'string',' ')
        h=fspecial('average',[e1,e2]);
        
        if v2==2 %replicate adge 
            
            z=imfilter(f,h,'replicate');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==3 %symmetric adge 
            
            z=imfilter(f,h,'symmetric');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==4 %circular adge 
            
            z=imfilter(f,h,'circular');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==1 %pad edge 
            
            z=imfilter(f,h);
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        end
    elseif v==3 %gaussian filter
        
        e1=str2num(get(handles.edit1,'string'));
        e2=str2num(get(handles.edit2,'string'));
        e3=str2num(get(handles.edit3,'string'));
        h=fspecial('gaussian',[e1,e2],e3);
        
        if v2==2 %replicate edge
            
            z=imfilter(f,h,'replicate');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==3 %symmetric edge
            
            z=imfilter(f,h,'symmetric');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==4 %circular edge
            
            z=imfilter(f,h,'circular');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==1 %pad edge
            
            z=imfilter(f,h);
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        end
    elseif v==4 %median filter
        
        e1=str2num(get(handles.edit1,'string')); %size(filter,1)
        e2=str2num(get(handles.edit2,'string')); %size(filter,2)
        set(handles.edit3,'string',' ')
        
        
        % if the size of filter be even it convert to odd
        if rem(e1,2)==0 %even size
            e1=e1+1; % if the size of filter be even it convert to odd
        end
        % if the size of filter be even it convert to odd
        if rem(e2,2)==0 %even size
            e2=e2+1; % if the size of filter be even it convert to odd
        end
        
        z=medfilt3(f,[e1,e2,3]);
        axes(handles.axes1)
        imshow(f)
        title('orginal picture')
        axes(handles.axes2)
        imshow(z)
        title('Filtered or Noised picture')
    end
    
elseif ch==1 %Perform on Noisy image 
    
    v=get(handles.popupmenu1,'value'); %size(filter)
    v2=get(handles.popupmenu2,'value');
    
    if v==2 %average filter
        
        e1=str2num(get(handles.edit1,'string'));
        e2=str2num(get(handles.edit2,'string'));
        
        set(handles.edit3,'string',' ')
        h=fspecial('average',[e1,e2]);
        
        if v2==2 %replicate edge
            
            z=imfilter(g,h,'replicate');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==3 %symmetric edge
            
            z=imfilter(g,h,'symmetric');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==4 %circular edge
            
            z=imfilter(g,h,'circular');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==1 %pad edge
            
            z=imfilter(g,h);
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        end
    elseif v==3 %gaussian filter
        
        e1=str2num(get(handles.edit1,'string'));
        e2=str2num(get(handles.edit2,'string'));
        e3=str2num(get(handles.edit3,'string'));
        h=fspecial('gaussian',[e1,e2],e3);
        
        if v2==2 %replicate edge
            
            z=imfilter(g,h,'replicate');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==3 %symmetric edge
            
            z=imfilter(g,h,'symmetric');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==4 %circular edge
            
            z=imfilter(g,h,'circular');
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        elseif v2==1 %pad edge
            
            z=imfilter(g,h);
            axes(handles.axes1)
            imshow(f)
            title('orginal picture')
            axes(handles.axes2)
            imshow(z)
            title('Filtered or Noised picture')
            
        end
    elseif v==4 %median filter
        
        e1=str2num(get(handles.edit1,'string'));
        e2=str2num(get(handles.edit2,'string'));
        set(handles.edit3,'string',' ')
        % if the size of filter be even it convert to odd
        if rem(e1,2)==0 %even size
            e1=e1+1;% if the size of filter be even it convert to odd
        end
        % if the size of filter be even it convert to odd
        if rem(e2,2)==0 %even size
            e2=e2+1;% if the size of filter be even it convert to odd
        end
        
        z=medfilt3(g,[e1,e2,3]);
        axes(handles.axes1)
        imshow(f)
        title('orginal picture')
        axes(handles.axes2)
        imshow(z)
        title('Filtered or Noised picture')
        
    end
    
end


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g NOISE z

%ADD Noise
%ADD Noise
%ADD Noise
%ADD Noise
%ADD Noise

z=f;
p=get(handles.popupmenu3,'value');
if p==2 %gaussian Noise
    
    e1=str2num(get(handles.edit4,'string'));
    e2=str2num(get(handles.edit5,'string'));
    set(handles.edit6,'string',' ')
    
    g=imnoise(f,'gaussian',e1,e2);
    NOISE=g;
    axes(handles.axes1)
    imshow(f)
    title('orginal picture')
    axes(handles.axes2)
    imshow(g)
    title('Filtered or Noised picture')
    
elseif p==3 %salt & pepper Noise
    
    e1=str2num(get(handles.edit6,'string'));
    set(handles.edit4,'string',' ')
    set(handles.edit5,'string',' ')
    
    g=imnoise(f,'salt & pepper',e1);
    NOISE=g;
    axes(handles.axes1)
    imshow(f)
    title('orginal picture')
    axes(handles.axes2)
    imshow(g)
    title('Filtered or Noised picture')
    
end




% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g z NOISE

% profile
% profile
% profile
% profile
% profile
% profile

clear x y
if size(f,3)==3
    f1=rgb2gray(f);
elseif size(f,3)==1
    f1=f;
end

v1=get(handles.radiobutton1,'value');
v2=get(handles.radiobutton2,'value');
figure('name','ginput')
imshow(f)
title('\fontsize{10}\color{red}if you Do Not need select any Row or Culomn press (ENTER) and close it.')

[x,y]=ginput(1);
close Figure ginput
if ~isempty(x)
    
    x=round(x);
    y=round(y);
    figure
    if v1==1  %Row profile
        
        
        if z==f & g==f % NO Noise  NO Filter
            subplot(311)
            plot(f1(y,:))
            title('Orginal image')
            
            subplot(312) %empty
            title('Blur image')
            
            subplot(313) %empty
            title('Noisy image')
            
            
        elseif isequal(z,f) & ~isequal(g,f) % just Noise
            
            subplot(311)
            plot(f1(y,:))
            title('Orginal image')
            
            subplot(312) %empty
            title('Blur image')
            
            subplot(313)
            plot(g(y,:))
            title('Noisy image')
            
            
            
        elseif ~isequal(z,f) & isequal(g,f) % just filter
            
            subplot(311)
            plot(f1(y,:))
            title('Orginal image')
            
            subplot(312)
            plot(z(y,:))
            title('Blur image')
            
            subplot(313) %empty
            title('Noisy image')
            
            
            
        elseif ~isequal(z,f) & ~isequal(g,f) % Noise & Filter
            
            subplot(311)
            plot(f1(y,:))
            title('Orginal image')
            
            subplot(312)
            plot(z(y,:))
            title('Blur image')
            
            subplot(313)
            plot(g(y,:))
            title('Noisy image')
            
        end
        
    elseif v2==1 %Culomn profile
        
        if z==f & g==f % NO Noise  NO Filter
            subplot(311)
            plot(f1(:,x))
            title('Orginal image')
            
            subplot(312) %empty
            title('Blur image')
             
            subplot(313) %empty
            title('Noisy image')
            
            
        elseif isequal(z,f) & ~isequal(g,f) % just Noise
            
            subplot(311)
            plot(f1(:,x))
            title('Orginal image')
            
            subplot(312) %empty
            title('Blur image')
            
            subplot(313)
            plot(g(:,x))
            title('Noisy image')
            
            
            
        elseif ~isequal(z,f) & isequal(g,f) % just filter
            
            subplot(311)
            plot(f1(:,x))
            title('Orginal image')
            
            subplot(312)
            plot(z(:,x))
            title('Blur image')
            
            subplot(313) %empty
            title('Noisy image') 
            
            
            
        elseif ~isequal(z,f) & ~isequal(g,f) % Noise & Filter
            
            subplot(311)
            plot(f1(:,x))
            title('Orginal image')
            
            subplot(312)
            plot(z(:,x))
            title('Blur image')
            
            subplot(313)
            plot(g(:,x))
            title('Noisy image')
            
        end
        
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


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g z

%3D plot
%3D plot
%3D plot
%3D plot
%3D plot

if size(f,3)==3
    f1=rgb2gray(f);
    z1=rgb2gray(z);
    g1=rgb2gray(g);
elseif size(f,3)==1
    f1=f;
    z1=z;
    g1=g;
end
figure('name','roipoly')
imshow(f)
title('\color{red}select 2 corners of rectangle.')
for i=1:2                                                                %<== | window selecting
    [x(i),y(i)]=ginput(1); %select 2 corner of rectangle                 %<== | window selecting
    x=round(x); y=round(y);                                              %<== | window selecting
    hold on                                                              %<== | window selecting
    plot(x(i),y(i),'ob','markerfacecolor','blue'),title('\color{red}select 2 corners of rectangle.')
end                                                                      %<== | window selecting
minx=min(x); %Window range                                               %<== | window selecting           
maxx=max(x); %Window range                                               %<== | window selecting  
miny=min(y); %Window range                                               %<== | window selecting       
maxy=max(y); %Window range                                               %<== | window selecting           
                                                                         %<== | window selecting
X=[minx maxx maxx minx minx]; %Window range                              %<== | window selecting           
Y=[maxy maxy miny miny maxy]; %Window range                              %<== | window selecting   
                                                                         %<== | window selecting   
plot(X,Y,'-.w','linewidth',3)                                            %<== | window selecting   
pause(1)                                                                 %<== | window selecting
close Figure roipoly                                                     %<== | window selecting
f1=f1(miny:maxy,minx:maxx); %Window range                                %<== | window selecting           
z1=z1(miny:maxy,minx:maxx); %Window range                                %<== | window selecting
g1=g1(miny:maxy,minx:maxx); %Window range                                %<== | window selecting           
                                                                            
                                                                           
if z==f & g==f % NO Noise  NO Filter                                        
                                                                            
    figure
    mesh(f1)
    title('Orginal image')
    
elseif isequal(z,f) & ~isequal(g,f) % just Noise
    
    figure
    mesh(f1)
    title('Orginal image')
    
    figure
    mesh(g1)
    title('Noisy image')
    
elseif ~isequal(z,f) & isequal(g,f) % just filter
    
    figure
    mesh(f1)
    title('Orginal image')
    
    figure
    mesh(z1)
    title('Blur image')
    
    
    
elseif ~isequal(z,f) & ~isequal(g,f) % Noise & Filter
    
    figure
    mesh(f1)
    title('Orginal image')
    
    figure
    mesh(z1)
    title('Blur image')
    
    figure
    mesh(g1)
    title('Noisy image')
    
end


% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g z FileName infoo

%Export Image
%Export Image
%Export Image
%Export Image
%Export Image

if FileName==0 | isempty(FileName)
    FileName='Matlab Picture.PNG';
end
if isequal(infoo.Format,'GIF')
    FileName(end-2:end)='png';
end
if z==f & g==f % NO Noise  NO Filter
    return
elseif isequal(z,f) & ~isequal(g,f) % just Noise
    masir=uigetdir;
    if masir~=0 
        wb=waitbar(0,'Please wait...');
        imwrite(g,[masir,'/Noisy ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
elseif ~isequal(z,f) & isequal(g,f) % just filter
    masir=uigetdir;
    if masir~=0
        wb=waitbar(0,'Please wait...');
        imwrite(z,[masir,'/Blur ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
elseif ~isequal(z,f) & ~isequal(g,f) % Noise & Filter
    masir=uigetdir;
    if masir~=0
        wb=waitbar(0,'Please wait...');
        imwrite(g,[masir,'/Noisy ',FileName])
        
        imwrite(z,[masir,'/Blur ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
end


% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f z mask g

% Custom filter
% Custom filter
% Custom filter
% Custom filter
% Custom filter

ch=get(handles.checkbox1,'value');
mask=[];
mask=str2num(get(handles.edit8,'string'));
if ~isempty(mask)
    if ch==0 %Perform on Original image
        sam=sum(mask(:));
        if sam~=0
            mask=mask/sam;
        end
        z=imfilter(f,mask);
        axes(handles.axes1)
        imshow(f)
        title('orginal picture')
        axes(handles.axes2)
        imshow(z)
        title('Filtered or Noised picture')
    elseif ch==1 %Perform on Noisy image
        sam=sum(mask(:));
        if sam~=0
            mask=mask/sam;
        end
        z=imfilter(g,mask);
        axes(handles.axes1)
        imshow(f)
        title('orginal picture')
        axes(handles.axes2)
        imshow(z)
        title('Filtered or Noised picture')
    end
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
