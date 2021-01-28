function varargout = inverse_histogram(varargin)
% INVERSE_HISTOGRAM MATLAB code for inverse_histogram.fig
%      INVERSE_HISTOGRAM, by itself, creates a new INVERSE_HISTOGRAM or raises the existing
%      singleton*.
%
%      H = INVERSE_HISTOGRAM returns the handle to a new INVERSE_HISTOGRAM or the handle to
%      the existing singleton*.
%
%      INVERSE_HISTOGRAM('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in INVERSE_HISTOGRAM.M with the given input arguments.
%
%      INVERSE_HISTOGRAM('Property','Value',...) creates a new INVERSE_HISTOGRAM or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before inverse_histogram_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to inverse_histogram_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help inverse_histogram

% Last Modified by GUIDE v2.5 04-Feb-2018 02:42:38

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @inverse_histogram_OpeningFcn, ...
    'gui_OutputFcn',  @inverse_histogram_OutputFcn, ...
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


% --- Executes just before inverse_histogram is made visible.
function inverse_histogram_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to inverse_histogram (see VARARGIN)

% Choose default command line output for inverse_histogram
handles.output = hObject;

% Update handles structure
global f g
logo=imread('ZoiLogosmall.png');
axes(handles.axes3)
imshow(logo)
if size(f,3)==1
    set(handles.radiobutton3,'enable','off')
    set(handles.radiobutton4,'enable','off')
    set(handles.radiobutton5,'enable','off')
end
g=imcomplement(f);
set(handles.radiobutton1,'value',1)
guidata(hObject, handles);
axes(handles.axes1)
imshow(f(:,:,1))
axes(handles.axes2)
imhist(f(:,:,1))
% UIWAIT makes inverse_histogram wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = inverse_histogram_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in radiobutton4.
function radiobutton4_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g
g=imcomplement(f);
r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
if r1==1
    if size(f,3)==1
        axes(handles.axes1);
        imshow(f)        
        axes(handles.axes2);
        imhist(f)
    elseif size(f,3)==3
        axes(handles.axes1);
        imshow(f(:,:,2))
        axes(handles.axes2);
        imhist(f(:,:,2))
    end
elseif r2==1
    if size(g,3)==1
        axes(handles.axes1);
        imshow(g)
        axes(handles.axes2);
        imhist(g)
    elseif size(g,3)==3
        axes(handles.axes1);
        imshow(g(:,:,2))
        axes(handles.axes2);
        imhist(g(:,:,2))
    end
end

% Hint: get(hObject,'Value') returns toggle state of radiobutton4


% --- Executes on button press in radiobutton3.
function radiobutton3_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g
g=imcomplement(f);
r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
if r1==1
    if size(f,3)==1
        axes(handles.axes1);
        imshow(f)        
        axes(handles.axes2);
        imhist(f)
    elseif size(f,3)==3
        axes(handles.axes1);
        imshow(f(:,:,1))
        axes(handles.axes2);
        imhist(f(:,:,1))
    end
elseif r2==1
    if size(g,3)==1
        axes(handles.axes1);
        imshow(g)
        axes(handles.axes2);
        imhist(g)
    elseif size(g,3)==3
        axes(handles.axes1);
        imshow(g(:,:,1))
        axes(handles.axes2);
        imhist(g(:,:,1))
    end
end
% Hint: get(hObject,'Value') returns toggle state of radiobutton3


% --- Executes on button press in radiobutton5.
function radiobutton5_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g
g=imcomplement(f);
r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
if r1==1
    if size(f,3)==1
        axes(handles.axes1);
        imshow(f)
        axes(handles.axes2);
        imhist(f)
    elseif size(f,3)==3
        axes(handles.axes1);
        imshow(f(:,:,3))
        axes(handles.axes2);
        imhist(f(:,:,3))
    end
elseif r2==1
    if size(g,3)==1
        axes(handles.axes1);
        imshow(g)
        axes(handles.axes2);
        imhist(g)
    elseif size(g,3)==3
        axes(handles.axes1);
        imshow(g(:,:,3))
        axes(handles.axes2);
        imhist(g(:,:,3))
    end
end
% Hint: get(hObject,'Value') returns toggle state of radiobutton5


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g
g=imcomplement(f);
r3=get(handles.radiobutton3,'value');
r4=get(handles.radiobutton4,'value');
r5=get(handles.radiobutton5,'value');
if r3==1
    if size(f,3)==1
        axes(handles.axes1);
        imshow(f)
        axes(handles.axes2);
        imhist(f)
    elseif size(f,3)==3
        axes(handles.axes1);
        imshow(f(:,:,1))
        axes(handles.axes2);
        imhist(f(:,:,1))
    end
elseif r4==1
    if size(f,3)==1
        axes(handles.axes1);
        imshow(f)
        axes(handles.axes2);
        imhist(f)
    elseif size(f,3)==3
        axes(handles.axes1);
        imshow(f(:,:,2))
        axes(handles.axes2);
        imhist(f(:,:,2))
    end
elseif r5==1
    if size(f,3)==1
        axes(handles.axes1);
        imshow(f)
        axes(handles.axes2);
        imhist(f)
    elseif size(f,3)==3
        axes(handles.axes1);
        imshow(f(:,:,3))
        axes(handles.axes2);
        imhist(f(:,:,3))
    end
end
% Hint: get(hObject,'Value') returns toggle state of radiobutton1


% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton2
global f g
g=imcomplement(f);
r3=get(handles.radiobutton3,'value');
r4=get(handles.radiobutton4,'value');
r5=get(handles.radiobutton5,'value');
if r3==1
    if size(g,3)==1
        axes(handles.axes1);
        imshow(g)
        axes(handles.axes2);
        imhist(g)
    elseif size(g,3)==3
        axes(handles.axes1);
        imshow(g(:,:,1))
        axes(handles.axes2);
        imhist(g(:,:,1))
    end
elseif r4==1
    if size(g,3)==1
        axes(handles.axes1);
        imshow(g)
        axes(handles.axes2);
        imhist(g)
    elseif size(g,3)==3
        axes(handles.axes1);
        imshow(g(:,:,2))
        axes(handles.axes2);
        imhist(g(:,:,2))
    end
elseif r5==1
    if size(g,3)==1
        axes(handles.axes1);
        imshow(g)
        axes(handles.axes2);
        imhist(g)
    elseif size(g,3)==3
        axes(handles.axes1);
        imshow(g(:,:,3))
        axes(handles.axes2);
        imhist(g(:,:,3))
    end
end


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
    imwrite(g,[masir,'/Inverse Histogram ',FileName])
    
    
    for i=1:1000
        waitbar(i/1000);
    end
    pause(0.1)
    close(wb)
end
