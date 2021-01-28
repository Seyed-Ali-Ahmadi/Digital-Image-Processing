function varargout = bands_gray(varargin)
% BANDS_GRAY MATLAB code for bands_gray.fig
%      BANDS_GRAY, by itself, creates a new BANDS_GRAY or raises the existing
%      singleton*.
%
%      H = BANDS_GRAY returns the handle to a new BANDS_GRAY or the handle to
%      the existing singleton*.
%
%      BANDS_GRAY('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in BANDS_GRAY.M with the given input arguments.
%
%      BANDS_GRAY('Property','Value',...) creates a new BANDS_GRAY or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before bands_gray_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to bands_gray_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help bands_gray

% Last Modified by GUIDE v2.5 14-Nov-2017 22:07:44

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @bands_gray_OpeningFcn, ...
                   'gui_OutputFcn',  @bands_gray_OutputFcn, ...
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


% --- Executes just before bands_gray is made visible.
function bands_gray_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to bands_gray (see VARARGIN)
logo=imread('ZoiLogosmall.png');
axes(handles.axes3)
imshow(logo)
% Choose default command line output for bands_gray
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes bands_gray wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = bands_gray_OutputFcn(hObject, eventdata, handles) 
global f
axes(handles.axes1)
imshow(f)

axes(handles.axes2)
imhist(f)
guidata(handles.axes1);
guidata(handles.axes2);

% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
