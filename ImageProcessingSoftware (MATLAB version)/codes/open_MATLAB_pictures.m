function varargout = open_MATLAB_pictures(varargin)
% OPEN_MATLAB_PICTURES MATLAB code for open_MATLAB_pictures.fig
%      OPEN_MATLAB_PICTURES, by itself, creates a new OPEN_MATLAB_PICTURES or raises the existing
%      singleton*.
%
%      H = OPEN_MATLAB_PICTURES returns the handle to a new OPEN_MATLAB_PICTURES or the handle to
%      the existing singleton*.
%
%      OPEN_MATLAB_PICTURES('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in OPEN_MATLAB_PICTURES.M with the given input arguments.
%
%      OPEN_MATLAB_PICTURES('Property','Value',...) creates a new OPEN_MATLAB_PICTURES or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before open_MATLAB_pictures_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to open_MATLAB_pictures_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help open_MATLAB_pictures

% Last Modified by GUIDE v2.5 03-Dec-2017 20:54:55

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @open_MATLAB_pictures_OpeningFcn, ...
    'gui_OutputFcn',  @open_MATLAB_pictures_OutputFcn, ...
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


% --- Executes just before open_MATLAB_pictures is made visible.
function open_MATLAB_pictures_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to open_MATLAB_pictures (see VARARGIN)
logo=imread('ZoiLogosmall.png');
axes(handles.axes1)
imshow(logo)
% Choose default command line output for open_MATLAB_pictures
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes open_MATLAB_pictures wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = open_MATLAB_pictures_OutputFcn(hObject, eventdata, handles)
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
global fn f infoo
fn=get(handles.edit1,'string');
if ~isempty(fn)
    f=imread(fn);
    infoo=imfinfo(fn);
    close open_MATLAB_pictures
    figure
    imshow(f)
end



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double
pushbutton1_Callback(hObject, eventdata, handles)


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


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1
global f fn infoo
val=get(hObject,'value');
if val==2
    fn=1;
    f=imread('cameraman.tif');
    infoo=imfinfo('cameraman.tif');
    close open_MATLAB_pictures
    figure
    imshow(f)
elseif val==3
    fn=1;
    f=imread('peppers.png');
    infoo=imfinfo('peppers.png');
    close open_MATLAB_pictures
    figure
    imshow(f)
elseif val==4
    fn=1;
    f=imread('tire.tif');
    infoo=imfinfo('tire.tif');
    close open_MATLAB_pictures
    figure
    imshow(f)
elseif val==5
    fn=1;
    f=imread('circuit.tif');
    infoo=imfinfo('circuit.tif');
    close open_MATLAB_pictures
    figure
    imshow(f)
elseif val==6
    fn=1;
    f=imread('westconcordaerial.png');
    infoo=imfinfo('westconcordaerial.png');
    close open_MATLAB_pictures
    figure
    imshow(f)
elseif val==7
    fn=1;
    f=imread('westconcordorthophoto.png');
    infoo=imfinfo('westconcordorthophoto.png');
    close open_MATLAB_pictures
    figure
    imshow(f)
elseif val==8
    fn=1;
    f=imread('moon.tif');
    infoo=imfinfo('moon.tif');
    close open_MATLAB_pictures
    figure
    imshow(f)
elseif val==9
    fn=1;
    f=imread('coins.png');
    infoo=imfinfo('coins.png');
    close open_MATLAB_pictures
    figure
    imshow(f)
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
