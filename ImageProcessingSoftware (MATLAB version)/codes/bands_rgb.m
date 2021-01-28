function varargout = bands_rgb(varargin)
% BANDS_RGB MATLAB code for bands_rgb.fig
%      BANDS_RGB, by itself, creates a new BANDS_RGB or raises the existing
%      singleton*.
%
%      H = BANDS_RGB returns the handle to a new BANDS_RGB or the handle to
%      the existing singleton*.
%
%      BANDS_RGB('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in BANDS_RGB.M with the given input arguments.
%
%      BANDS_RGB('Property','Value',...) creates a new BANDS_RGB or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before bands_rgb_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to bands_rgb_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help bands_rgb

% Last Modified by GUIDE v2.5 14-Nov-2017 21:35:41

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @bands_rgb_OpeningFcn, ...
                   'gui_OutputFcn',  @bands_rgb_OutputFcn, ...
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


% --- Executes just before bands_rgb is made visible.
function bands_rgb_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to bands_rgb (see VARARGIN)
logo=imread('ZoiLogosmall.png');
axes(handles.axes7)
imshow(logo)
% Choose default command line output for bands_rgb
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes bands_rgb wait for user response (see UIRESUME)
% uiwait(handles.figure1);

% --- Outputs from this function are returned to the command line.
function varargout = bands_rgb_OutputFcn(hObject, eventdata, handles)
global f 
% [FileName,PathName]=uigetfile('*.*');
% if FileName~=0
% f=imread([PathName,FileName]);
axes(handles.axes1)
imshow(f(:,:,1))
title('\color{red}Red')
axes(handles.axes2)
imshow(f(:,:,2))
title('\color{green}Green')
axes(handles.axes3)
imshow(f(:,:,3))
title('\color{blue}Blue')


axes(handles.axes4)
h1=imhist(f(:,:,1));
bar(h1,'r')

axes(handles.axes5)
h2=imhist(f(:,:,2));
bar(h2,'g')

axes(handles.axes6)
h3=imhist(f(:,:,3));
bar(h3,'b')

% end
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
