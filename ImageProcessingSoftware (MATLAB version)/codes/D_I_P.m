function varargout = D_I_P(varargin)
warning('off')
% D_I_P MATLAB code for D_I_P.fig
%      D_I_P, by itself, creates a new D_I_P or raises the existing
%      singleton*.
%
%      H = D_I_P returns the handle to a new D_I_P or the handle to
%      the existing singleton*.
%
%      D_I_P('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in D_I_P.M with the given input arguments.
%
%      D_I_P('Property','Value',...) creates a new D_I_P or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before D_I_P_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to D_I_P_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help D_I_P

% Last Modified by GUIDE v2.5 06-Feb-2018 01:39:22

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @D_I_P_OpeningFcn, ...
    'gui_OutputFcn',  @D_I_P_OutputFcn, ...
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

% --- Executes just before D_I_P is made visible.
function D_I_P_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to D_I_P (see VARARGIN)

% Choose default command line output for D_I_P
handles.output = hObject;
whitebg('white')
logo=imread('logo.png');
tarh=imread('ZoiLogo.png');
axes(handles.axes2)
imshow(logo)
axes(handles.axes1)
imshow(tarh)
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes D_I_P wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = D_I_P_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --------------------------------------------------------------------
function Read_Callback(hObject, eventdata, handles)
% hObject    handle to Read (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function show_Callback(hObject, eventdata, handles)
% hObject    handle to show (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% --------------------------------------------------------------------
function Info_Callback(hObject, eventdata, handles)

% hObject    handle to Info (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn infoo
if FileName~=0
    infoo=imfinfo([PathName,FileName]);
    info(infoo)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
%     infoo=imfinfo(fn);
    info(infoo)
end
% --------------------------------------------------------------------
function sh_band_Callback(hObject, eventdata, handles)
% hObject    handle to sh_band (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn
if FileName~=0
    if size(f,3)==3
        bands_rgb(f)
    else
        bands_gray(f)
    end
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end




if ~isempty(fn)
    if size(f,3)==3
        bands_rgb(f)
    else
        bands_gray(f)
    end
end


% --------------------------------------------------------------------
function IMTOOL_Callback(hObject, eventdata, handles)
% hObject    handle to IMTOOL (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function rgbtool_Callback(hObject, eventdata, handles)
% hObject    handle to rgbtool (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function graytool_Callback(hObject, eventdata, handles)
% hObject    handle to graytool (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f FileName fn
if FileName~=0
    if size(f,3)==3
        msgbox('your picture is RGB.','Error','error')
        error('your picture is RGB.')
    else
        imtool(f)
    end
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end




if ~isempty(fn)
    if size(f,3)==3
        msgbox('your picture is RGB.','Error','error')
        error('your picture is RGB.')
    else
        imtool(f)
    end
end



% --------------------------------------------------------------------
function Band1tool_Callback(hObject, eventdata, handles)
% hObject    handle to Band1tool (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f FileName fn
if FileName~=0
    if size(f,3)==1
        msgbox('your picture is Single band.','Error','error')
        error('your picture is Single band.')
    else
        imtool(f(:,:,1))
    end
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end




if ~isempty(fn)
    if size(f,3)==1
        msgbox('your picture is Single band.','Error','error')
        error('your picture is Single band.')
    else
        imtool(f(:,:,1))
    end
end

% --------------------------------------------------------------------
function Band2tool_Callback(hObject, eventdata, handles)
% hObject    handle to Band2tool (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f FileName fn
if FileName~=0
    if size(f,3)==1
        msgbox('your picture is Single band.','Error','error')
        error('your picture is Single band.')
    else
        imtool(f(:,:,2))
    end
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end




if ~isempty(fn)
    if size(f,3)==1
        msgbox('your picture is Single band.','Error','error')
        error('your picture is Single band.')
    else
        imtool(f(:,:,2))
    end
end

% --------------------------------------------------------------------
function Band3tool_Callback(hObject, eventdata, handles)
% hObject    handle to Band3tool (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f FileName fn
if FileName~=0
    if size(f,3)==1
        msgbox('your picture is Single band.','Error','error')
        error('your picture is Single band.')
    else
        imtool(f(:,:,3))
    end
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end




if ~isempty(fn)
    if size(f,3)==1
        msgbox('your picture is Single band.','Error','error')
        error('please open a picture first.')
    else
        imtool(f(:,:,3))
    end
end

% --------------------------------------------------------------------
function read_gallery_Callback(hObject, eventdata, handles)
% hObject    handle to read_gallery (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
clear all
global f PathName FileName infoo
warning('off')
FileName=0;
[FileName,PathName]=uigetfile('*.*');
if FileName~=0
    f=imread([PathName,FileName]);
    infoo=imfinfo([PathName,FileName]);
    figure
    imshow(f)
end




% --------------------------------------------------------------------
function read_matpic_Callback(hObject, eventdata, handles)
% hObject    handle to read_matpic (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
clear all
global f fn FileName infoo
FileName=0;
open_MATLAB_pictures


% --------------------------------------------------------------------
function Resolutions_Callback(hObject, eventdata, handles)
% hObject    handle to Resolutions (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function im_resize_Callback(hObject, eventdata, handles)
% hObject    handle to im_resize (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    image_resize(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    image_resize(f)
end


% --------------------------------------------------------------------
function radiometric_Callback(hObject, eventdata, handles)
% hObject    handle to radiometric (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    radiometric_resolution(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    radiometric_resolution(f)
end


% --------------------------------------------------------------------
function image_histogram_Callback(hObject, eventdata, handles)
% hObject    handle to image_histogram (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function brightness_manipulation_Callback(hObject, eventdata, handles)
% hObject    handle to brightness_manipulation (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    brightness(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    brightness(f)
end


% --------------------------------------------------------------------
function Threshold_Callback(hObject, eventdata, handles)
% hObject    handle to Threshold (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    threshold(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
     threshold(f)
end


% --------------------------------------------------------------------
function Inverse_Histogram_Callback(hObject, eventdata, handles)
% hObject    handle to Inverse_Histogram (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    inverse_histogram(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
     inverse_histogram(f)
end


% --------------------------------------------------------------------
function Close_Callback(hObject, eventdata, handles)
% hObject    handle to Close (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
clear all
close all
clc


% --------------------------------------------------------------------
function contrast_manipulation_Callback(hObject, eventdata, handles)
% hObject    handle to contrast_manipulation (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



% --------------------------------------------------------------------
function ContrastRGB_Callback(hObject, eventdata, handles)
% hObject    handle to ContrastRGB (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f FileName fn
if FileName~=0
    if size(f,3)==1
        msgbox('your picture is Single band.','Error','error')
        error('your picture is Single band.')
    else
        contrast_RGB(f)
    end
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end




if ~isempty(fn)
    if size(f,3)==1
        msgbox('your picture is Single band.','Error','error')
        error('your picture is Single band.')
    else
        contrast_RGB(f)
    end
end


% --------------------------------------------------------------------
function Contrastgray_Callback(hObject, eventdata, handles)
% hObject    handle to Contrastgray (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f FileName fn
if FileName~=0
    if size(f,3)==3
        msgbox('your picture is RGB.','Error','error')
        error('your picture is RGB.')
    else
        contrast_gray(f)
    end
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end




if ~isempty(fn)
    if size(f,3)==3
        msgbox('your picture is RGB.','Error','error')
        error('your picture is RGB.')
    else
        contrast_gray(f)
    end
end


% --------------------------------------------------------------------
function gray_level_transformation_Callback(hObject, eventdata, handles)
% hObject    handle to gray_level_transformation (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    function_transformation(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    function_transformation(f)
end


% --------------------------------------------------------------------
function histogram_equalization_Callback(hObject, eventdata, handles)
% hObject    handle to histogram_equalization (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    histogram_equalization(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    histogram_equalization(f)
end


% --------------------------------------------------------------------
function spatial_filtering_Callback(hObject, eventdata, handles)
% hObject    handle to spatial_filtering (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function smooth_noise_Callback(hObject, eventdata, handles)
% hObject    handle to smooth_noise (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    Noise_and_smoothing(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    Noise_and_smoothing(f)
end


% --------------------------------------------------------------------
function Frequency_domain_Callback(hObject, eventdata, handles)
% hObject    handle to Frequency_domain (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function TwoD_Fourier_Transforms_Callback(hObject, eventdata, handles)
% hObject    handle to TwoD_Fourier_Transforms (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    Two_D_Fourier_Tranformation(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    Two_D_Fourier_Tranformation(f)
end


% --------------------------------------------------------------------
function Sharpening_Filter_Callback(hObject, eventdata, handles)
% hObject    handle to Sharpening_Filter (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    sharpening_filters(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    sharpening_filters(f)
end


% --------------------------------------------------------------------
function oneD_Fourier_Transformation_Callback(hObject, eventdata, handles)
% hObject    handle to oneD_Fourier_Transformation (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
one_D_fourier_transformation


% --------------------------------------------------------------------
function Morphological_Callback(hObject, eventdata, handles)
% hObject    handle to Morphological (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function Morphological_Operations_Callback(hObject, eventdata, handles)
% hObject    handle to Morphological_Operations (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    Morphological_operations(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    Morphological_operations(f)
end

% --------------------------------------------------------------------
function region_filling_Callback(hObject, eventdata, handles)
% hObject    handle to region_filling (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f PathName FileName fn 
if FileName~=0
    Region_Filling(f)
elseif isempty(fn) | (FileName==0 & isempty(fn))
    msgbox('please open a picture first.','Error','error')
    error('please open a picture first.')
end


if ~isempty(fn)
    Region_Filling(f)
end
 


% --------------------------------------------------------------------
function About_US_Callback(hObject, eventdata, handles)
% hObject    handle to About_US (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
About
