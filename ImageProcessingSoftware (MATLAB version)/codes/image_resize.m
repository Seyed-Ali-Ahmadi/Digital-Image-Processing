function varargout = image_resize(varargin)
% IMAGE_RESIZE MATLAB code for image_resize.fig
%      IMAGE_RESIZE, by itself, creates a new IMAGE_RESIZE or raises the existing
%      singleton*.
%
%      H = IMAGE_RESIZE returns the handle to a new IMAGE_RESIZE or the handle to
%      the existing singleton*.
%
%      IMAGE_RESIZE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in IMAGE_RESIZE.M with the given input arguments.
%
%      IMAGE_RESIZE('Property','Value',...) creates a new IMAGE_RESIZE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before image_resize_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to image_resize_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help image_resize

% Last Modified by GUIDE v2.5 04-Feb-2018 01:41:52

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @image_resize_OpeningFcn, ...
    'gui_OutputFcn',  @image_resize_OutputFcn, ...
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


% --- Executes just before image_resize is made visible.
function image_resize_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to image_resize (see VARARGIN)
logo=imread('ZoiLogosmall.png');
axes(handles.axes2)
imshow(logo)
% Choose default command line output for image_resize
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes image_resize wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = image_resize_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f h
axes(handles.axes1)
imshow(f)
h=f;
% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1


global f h


val=get(hObject,'value');   % M=1/(2^(val-1))
val=1/(2^(val-1));          % M=1/(2^(val-1))
                            % M=1/(2^(val-1))
%If you set (M) as the size, this means that the size of the image will be (1/M), OR it means that  the PixelSize will be (M) times bigger.  

if size(f,3)==1
    g=imresize(f,val);
    h=imresize(g,size(f));
end
if size(f,3)==3 %for RGB images
g1=imresize(f(:,:,1),val);          %g=f  But
g2=imresize(f(:,:,2),val);          %size(g)= M percent * size(f)
g3=imresize(f(:,:,3),val);          %size(g) < size(f)


h1=imresize(g1,[size(f,1),size(f,2)]); % size(h)=size(f) But pixelsize(h) > pixelsize(f) and h is blur
h2=imresize(g2,[size(f,1),size(f,2)]);
h3=imresize(g3,[size(f,1),size(f,2)]);
h=cat(3,h1,h2,h3);
end
axes(handles.axes1)
imshow(h)





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
global f h FileName infoo

%Export image

if FileName==0 | isempty(FileName)
    FileName='Matlab Picture.PNG';
end
if isequal(infoo.Format,'GIF')
    FileName(end-2:end)='png';
end
if ~isequal(h,f)
    masir=uigetdir;
    if masir~=0
        wb=waitbar(0,'Please wait ...');
        imwrite(h,[masir,'/Image Resize ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
end
