function varargout = function_transformation(varargin)
% FUNCTION_TRANSFORMATION MATLAB code for function_transformation.fig
%      FUNCTION_TRANSFORMATION, by itself, creates a new FUNCTION_TRANSFORMATION or raises the existing
%      singleton*.
%
%      H = FUNCTION_TRANSFORMATION returns the handle to a new FUNCTION_TRANSFORMATION or the handle to
%      the existing singleton*.
%
%      FUNCTION_TRANSFORMATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in FUNCTION_TRANSFORMATION.M with the given input arguments.
%
%      FUNCTION_TRANSFORMATION('Property','Value',...) creates a new FUNCTION_TRANSFORMATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before function_transformation_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to function_transformation_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help function_transformation

% Last Modified by GUIDE v2.5 04-Feb-2018 01:35:06

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @function_transformation_OpeningFcn, ...
                   'gui_OutputFcn',  @function_transformation_OutputFcn, ...
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


% --- Executes just before function_transformation is made visible.
function function_transformation_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to function_transformation (see VARARGIN)

% Choose default command line output for function_transformation
handles.output = hObject;
global f g
logo=imread('ZoiLogosmall.png');
axes(handles.axes6)
imshow(logo)
f1=f; 
if size(f,3)==3  %for RGB images
    f1=rgb2gray(f);
end
g=f1;
set(handles.edit1,'string',num2str(1));

axes(handles.axes1)
imshow(f1)
title('\fontsize{15}{\color{blue}Input Image}')


axes(handles.axes3)

x=[0 1];y=[0 1];                %<== plot of function transformation
plot(x,y)                       %<== plot of function transformation
xlabel('\fontsize{10}{\color{red}Input graylevel}')
ylabel('\fontsize{10}{\color{red}Output graylevel}')
title('\fontsize{15}{\color{blue}Function of Transformation}')
set(gca,'xtick',0:0.1:1)
set(gca,'ytick',0:0.1:1)
grid on

axes(handles.axes2)
imshow(f1)
title('\fontsize{15}{\color{blue}Output Image}')
axes(handles.axes5)
imhist(f1)
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes function_transformation wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = function_transformation_OutputFcn(hObject, eventdata, handles) 
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
f1=f;
if size(f,3)==3 %for RGB images
    f1=rgb2gray(f);
end
gamma=str2num(get(handles.edit1,'string'));

axes(handles.axes1)
imshow(f1)
title('\fontsize{15}{\color{blue}Input Image}')


axes(handles.axes3)
x=0:0.01:1;
y=x.^gamma;             %<== plot of function transformation

plot(x,y)               %<== plot of function transformation
xlabel('\fontsize{10}{\color{red}Input graylevel}')
ylabel('\fontsize{10}{\color{red}Output graylevel}')
set(gca,'xtick',0:0.1:1)
set(gca,'ytick',0:0.1:1)
title('\fontsize{15}{\color{blue}Function of Transformation}')
grid on


axes(handles.axes2)
g=imadjust(f1,[0 1],[0 1],gamma);
imshow(g)
title('\fontsize{15}{\color{blue}Output Image}')
axes(handles.axes5)
imhist(g)

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
f1=f;
if size(f,3)==3
    f1=rgb2gray(f);
end
if ~isequal(g,f1)
    
    masir=uigetdir;
    if masir~=0
        wb=waitbar(0,'Please wait...');
        imwrite(g,[masir,'/transformation ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
    
end
