function varargout = histogram_equalization(varargin)
% HISTOGRAM_EQUALIZATION MATLAB code for histogram_equalization.fig
%      HISTOGRAM_EQUALIZATION, by itself, creates a new HISTOGRAM_EQUALIZATION or raises the existing
%      singleton*.
%
%      H = HISTOGRAM_EQUALIZATION returns the handle to a new HISTOGRAM_EQUALIZATION or the handle to
%      the existing singleton*.
%
%      HISTOGRAM_EQUALIZATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in HISTOGRAM_EQUALIZATION.M with the given input arguments.
%
%      HISTOGRAM_EQUALIZATION('Property','Value',...) creates a new HISTOGRAM_EQUALIZATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before histogram_equalization_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to histogram_equalization_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help histogram_equalization

% Last Modified by GUIDE v2.5 04-Feb-2018 01:37:55

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @histogram_equalization_OpeningFcn, ...
                   'gui_OutputFcn',  @histogram_equalization_OutputFcn, ...
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


% --- Executes just before histogram_equalization is made visible.
function histogram_equalization_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to histogram_equalization (see VARARGIN)

% Choose default command line output for histogram_equalization
handles.output = hObject;
global f g
% Update handles structure
logo=imread('ZoiLogosmall.png');
axes(handles.axes10)
imshow(logo)
guidata(hObject, handles);
axes(handles.axes1)
imshow(f)
title('Original Picture')
axes(handles.axes3)
imhist(f)
hold on
h=imhist(f);
h1=cumsum(h);
h1=max(h)*h1/max(h1);
plot(h1)
axis([0 255 0 (1.1)*max((h1))])
hold off
title('Original Histogram')
g=histeq(f);
axes(handles.axes2)
imshow(g)
title('Picture after Histogram Equlization')
axes(handles.axes4)
imhist(g)
hold on
h2=imhist(g);
h3=cumsum(h2);
h3=max(h2)*h3/max(h3);
plot(h3)
axis([0 255 0 (1.1)*max((h3))])
hold off
title('Histogram Equalization')
axis([0 255 0 (1.1)*max(imhist(g))])
set(handles.edit1,'string',num2str(64))
% UIWAIT makes histogram_equalization wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = histogram_equalization_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double

global f g
n=get(handles.edit1,'string');
g=histeq(f,str2num(n));
axes(handles.axes2)
imshow(g)
title('Picture after Histogram Equlization')
axes(handles.axes4)
imhist(g)
title('Histogram Equalization')
axis([0 255 0 (1.1)*max(imhist(g))])
hold on
h4=imhist(g);
h5=cumsum(h4);
h5=max(h4)*h5/max(h5);
plot(h5)
axis([0 255 0 (1.1)*max((h5))])
hold off


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


% --- Executes during object creation, after setting all properties.
function axes1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes1


% --- Executes during object creation, after setting all properties.
function axes2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes2


% --- Executes during object creation, after setting all properties.
function axes3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes3


% --- Executes during object creation, after setting all properties.
function axes4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes4


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
masir=uigetdir;
if masir~=0
    wb=waitbar(0,'Please wait ...');
    imwrite(g,[masir,'/Histogram Equalization ',FileName])
    
    
    for i=1:1000
        waitbar(i/1000);
    end
    pause(0.1)
    close(wb)
end
