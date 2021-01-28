function varargout = threshold(varargin)
% THRESHOLD MATLAB code for threshold.fig
%      THRESHOLD, by itself, creates a new THRESHOLD or raises the existing
%      singleton*.
%
%      H = THRESHOLD returns the handle to a new THRESHOLD or the handle to
%      the existing singleton*.
%
%      THRESHOLD('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in THRESHOLD.M with the given input arguments.
%
%      THRESHOLD('Property','Value',...) creates a new THRESHOLD or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before threshold_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to threshold_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help threshold

% Last Modified by GUIDE v2.5 04-Feb-2018 04:16:43

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @threshold_OpeningFcn, ...
    'gui_OutputFcn',  @threshold_OutputFcn, ...
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


% --- Executes just before threshold is made visible.
function threshold_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to threshold (see VARARGIN)

% Choose default command line output for threshold
global f g1 RB1 RB2 RB3 g4
logo=imread('ZoiLogosmall.png');
axes(handles.axes3)
imshow(logo)
if size(f,3)==1
set(handles.radiobutton1,'enable','off')
set(handles.radiobutton2,'enable','off')
set(handles.radiobutton3,'enable','off')
end
RB1=1;
RB2=0;
RB3=0;
handles.output = hObject;


if islogical(f) %your picture can't be logical
    msgbox('your picture is logocal.','ERROR','error')
    error('your picture is logocal.')
    close threshold
end


axes(handles.axes1)
imshow(im2bw(f(:,:,1),graythresh(f(:,:,1))))
g1=im2bw(f(:,:,1),graythresh(f(:,:,1)));
g4=g1;
val=255*graythresh(f(:,:,1));
set(handles.edit1,'string',round(val));
set(handles.slider1,'value',val);


axes(handles.axes2)
hold off
hf=imhist(f(:,:,1));
imhist(f(:,:,1))
hold on
plot([val,val],[0,max(hf)],'linewidth',3)
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes threshold wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = threshold_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on slider movement.
function slider1_Callback(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g1 g2 g3 g4 RB1 RB2 RB3

%threshold
%threshold
%threshold
%threshold

hold off
val=get(handles.slider1,'value');


r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
r3=get(handles.radiobutton3,'value');


if size(f,3)==3     %for RGB image
    
    if r1==1 %Band 1
        
        RB1=1;
        RB2=0;
        RB3=0;
        set(handles.edit1,'string',round(val))
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,1),val/255));
        g1=im2bw(f(:,:,1),val/255);
        
        axes(handles.axes2)
        h1=imhist(f(:,:,1));
        imhist(f(:,:,1))
        hold on
        plot([val,val],[0,max(h1)],'linewidth',3)
        
    elseif r2==1%Band 2
        
        RB1=0;
        RB2=1;
        RB3=0;
        set(handles.edit1,'string',round(val))
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,2),val/255));
        g2=im2bw(f(:,:,2),val/255);
        axes(handles.axes2)
        
        h2=imhist(f(:,:,2));
        imhist(f(:,:,2))
        hold on
        plot([val,val],[0,max(h2)],'linewidth',3)
        
    elseif r3==1%Band 3
        
        RB1=0;
        RB2=0;
        RB3=1;
        set(handles.edit1,'string',round(val))
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,3),val/255));
        g3=im2bw(f(:,:,3),val/255);
        
        axes(handles.axes2)
        h3=imhist(f(:,:,3));
        imhist(f(:,:,3))
        hold on
        plot([val,val],[0,max(h3)],'linewidth',3)
        
    end
    
elseif size(f,3)==1
    
    set(handles.edit1,'string',round(val))
    
    axes(handles.axes1)
    imshow(im2bw(f,val/255))
    g4=im2bw(f,val/255);
    
    axes(handles.axes2)
    h4=imhist(f);
    imhist(f)
    hold on
    plot([val,val],[0,max(h4)],'linewidth',3)
    
end
% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider


% --- Executes during object creation, after setting all properties.
function slider1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g1 g2 g3 g4 RB1 RB2 RB3

%select Band 1
%select Band 1
%select Band 1
%select Band 1
%select Band 1

RB1=1;
RB2=0;
RB3=0;
hold off
if size(f,3)==3     %for RGB image
    
        gt=255*graythresh(f(:,:,1));
        set(handles.edit1,'string',round(gt))
        set(handles.slider1,'value',gt)
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,1),gt/255));
        g1=im2bw(f(:,:,1),gt/255);
        
        axes(handles.axes2)
        h6=imhist(f(:,:,1));
        imhist(f(:,:,1))
        hold on
        plot([gt,gt],[0,max(h6)],'linewidth',3)
        
elseif size(f,3)==1
    
        gt=255*graythresh(f);
        set(handles.edit1,'string',round(gt))
        set(handles.slider1,'value',gt)
        
        axes(handles.axes1)
        imshow(im2bw(f,gt/255))
        g4=im2bw(f,gt/255);
        
        axes(handles.axes2)
        h7=imhist(f);
        imhist(f)
        hold on
        plot([gt,gt],[0,max(h7)],'linewidth',3)    
        
end
% Hint: get(hObject,'Value') returns toggle state of radiobutton1


% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g1 g2 g3 g4 RB1 RB2 RB3

%select Band 2
%select Band 2
%select Band 2
%select Band 2
%select Band 2

RB1=0;
RB2=1;
RB3=0;
hold off
if size(f,3)==3     %for RGB image
        gt=255*graythresh(f(:,:,2));
        set(handles.edit1,'string',round(gt))
        set(handles.slider1,'value',gt)
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,2),gt/255));
        g2=im2bw(f(:,:,2),gt/255);
        
        axes(handles.axes2)
        h8=imhist(f(:,:,2));
        imhist(f(:,:,2))
        hold on
        plot([gt,gt],[0,max(h8)],'linewidth',3)
        
elseif size(f,3)==1
    
        gt=255*graythresh(f);
        set(handles.edit1,'string',round(gt))
        set(handles.slider1,'value',gt)
        
        axes(handles.axes1)
        imshow(im2bw(f,gt/255));
        g4=im2bw(f,gt/255);
        
        
        axes(handles.axes2)
        h9=imhist(f);
        imhist(f)
        hold on
        plot([gt,gt],[0,max(h9)],'linewidth',3)    
        
end
% Hint: get(hObject,'Value') returns toggle state of radiobutton2


% --- Executes on button press in radiobutton3.
function radiobutton3_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g1 g2 g3 g4 RB1 RB2 RB3

%select Band 3
%select Band 3
%select Band 3
%select Band 3
%select Band 3

RB1=0;
RB2=0;
RB3=1;
hold off
if size(f,3)==3     %for RGB image
    
        gt=255*graythresh(f(:,:,3));
        set(handles.edit1,'string',round(gt))
        set(handles.slider1,'value',gt)
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,3),gt/255));
        g3=im2bw(f(:,:,3),gt/255);
        
        axes(handles.axes2)
        h10=imhist(f(:,:,3));
        imhist(f(:,:,3))
        hold on
        plot([gt,gt],[0,max(h10)],'linewidth',3)
        
elseif size(f,3)==1
    
        gt=255*graythresh(f);
        set(handles.edit1,'string',round(gt))
        set(handles.slider1,'value',gt)
        
        axes(handles.axes1)
        imshow(im2bw(f,gt/255));
        g4=im2bw(f,gt/255);
        
        axes(handles.axes2)
        h11=imhist(f);
        imhist(f)
        hold on
        plot([gt,gt],[0,max(h11)],'linewidth',3)   
        
end
% Hint: get(hObject,'Value') returns toggle state of radiobutton3



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g1 g2 g3 g4 RB1 RB2 RB3

%threshold
%threshold
%threshold
%threshold
%threshold

val=str2num(get(handles.edit1,'string'));
hold off
set(handles.slider1,'value',val);

r1=get(handles.radiobutton1,'value');
r2=get(handles.radiobutton2,'value');
r3=get(handles.radiobutton3,'value');


if size(f,3)==3     %for RGB image
    
    if r1==1
        
        RB1=1;
        RB2=0;
        RB3=0;
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,1),val/255));
        g1=im2bw(f(:,:,1),val/255);
        
        axes(handles.axes2)
        h1=imhist(f(:,:,1));
        imhist(f(:,:,1))
        hold on
        plot([val,val],[0,max(h1)],'linewidth',3)
        
    elseif r2==1%Band 2
        
        RB1=0;
        RB2=1;
        RB3=0;
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,2),val/255));
        g2=im2bw(f(:,:,2),val/255);
        
        axes(handles.axes2)
        h2=imhist(f(:,:,2));
        imhist(f(:,:,2))
        hold on
        plot([val,val],[0,max(h2)],'linewidth',3)
        
    elseif r3==1%Band 3
        
        RB1=0;
        RB2=0;
        RB3=1;
        
        axes(handles.axes1)
        imshow(im2bw(f(:,:,3),val/255));
        g3=im2bw(f(:,:,3),val/255);
        
        axes(handles.axes2)
        h3=imhist(f(:,:,3));
        imhist(f(:,:,3))
        hold on
        plot([val,val],[0,max(h3)],'linewidth',3)
        
    end
    
elseif size(f,3)==1
    
    axes(handles.axes1)
    imshow(im2bw(f,val/255));
    g4=im2bw(f,val/255);
    
    axes(handles.axes2)
    h4=imhist(f);
    imhist(f)
    hold on
    plot([val,val],[0,max(h4)],'linewidth',3)
    
end
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


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f FileName g1 g2 g3 g4 RB1 RB2 RB3 infoo

%Export image
%Export image
%Export image
%Export image
%Export image

if FileName==0 | isempty(FileName)
    FileName='Matlab Picture.PNG';
end
if isequal(infoo.Format,'GIF')
    FileName(end-2:end)='png';
end
masir=uigetdir;
if masir~=0
    if size(f,3)==3
        if RB1==1 %Export Band 1
            
            
            wb=waitbar(0,'Please wait ...');
            imwrite(g1,[masir,'/Threshold Band (1) ',FileName])
            for i=1:1000
                waitbar(i/1000);
            end
            pause(0.1)
            close(wb)
            
            
        elseif RB2==1 %Export Band 2
            
            
            wb=waitbar(0,'Please wait ...');
            imwrite(g2,[masir,'/Threshold Band (2) ',FileName])
            for i=1:1000
                waitbar(i/1000);
            end
            pause(0.1)
            close(wb)
            
            
        elseif RB3==1 %Export Band 3
            
            
            wb=waitbar(0,'Please wait ...');
            imwrite(g3,[masir,'/Threshold Band (3) ',FileName])
            for i=1:1000
                waitbar(i/1000);
            end
            pause(0.1)
            close(wb)
            
            
        end
    elseif size(f,3)==1
        
        
            wb=waitbar(0,'Please wait ...');
            imwrite(g4,[masir,'/Threshold Gray ',FileName])
            for i=1:1000
                waitbar(i/1000);
            end
            pause(0.1)
            close(wb)
        
        
    end
    
end
