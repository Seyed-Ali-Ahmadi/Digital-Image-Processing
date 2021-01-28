function varargout = radiometric_resolution(varargin)
% RADIOMETRIC_RESOLUTION MATLAB code for radiometric_resolution.fig
%      RADIOMETRIC_RESOLUTION, by itself, creates a new RADIOMETRIC_RESOLUTION or raises the existing
%      singleton*.
%
%      H = RADIOMETRIC_RESOLUTION returns the handle to a new RADIOMETRIC_RESOLUTION or the handle to
%      the existing singleton*.
%
%      RADIOMETRIC_RESOLUTION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in RADIOMETRIC_RESOLUTION.M with the given input arguments.
%
%      RADIOMETRIC_RESOLUTION('Property','Value',...) creates a new RADIOMETRIC_RESOLUTION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before radiometric_resolution_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to radiometric_resolution_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help radiometric_resolution

% Last Modified by GUIDE v2.5 04-Feb-2018 04:10:31

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @radiometric_resolution_OpeningFcn, ...
                   'gui_OutputFcn',  @radiometric_resolution_OutputFcn, ...
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


% --- Executes just before radiometric_resolution is made visible.
function radiometric_resolution_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to radiometric_resolution (see VARARGIN)

% Choose default command line output for radiometric_resolution
handles.output = hObject;
global f g
logo=imread('ZoiLogosmall.png');
axes(handles.axes2)
imshow(logo)
g=f;
axes(handles.axes1)
imshow(f)
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes radiometric_resolution wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = radiometric_resolution_OutputFcn(hObject, eventdata, handles) 
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
val=get(hObject,'value');
val=9-val;
if val==8
    g=f;
    axes(handles.axes1)
    imshow(f)
else                           %Example: val=6(Bit)
    g=mat2gray(f);             %step_1 (transfer) f from uint8[0 255] to double[0 1]
    g=uint8((2^val-1)*g);      %step_2 (transfer) g from double[0 1]  to uint8[0 63]
    g=im2uint8(mat2gray(g));   %step_3 (Stretch)  g from uint8[0 63]  to uint8[0 255] ===> its mean that graylevel of [0 63] stretching to graylevel [0 255]
    axes(handles.axes1)                                                                   %and the number of graylevels from 256 Decrease to 64
    imshow(g)                                                                             %Binsize = (2^8) / (2^6)=4  (Quantization)
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


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g FileName infoo

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
        wb=waitbar(0,'Please wait ...');
        imwrite(g,[masir,'/Radiometric Resolution ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
end
