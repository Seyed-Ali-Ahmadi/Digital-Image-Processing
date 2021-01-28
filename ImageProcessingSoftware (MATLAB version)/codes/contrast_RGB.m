function varargout = contrast_RGB(varargin)
% CONTRAST_RGB MATLAB code for contrast_RGB.fig
%      CONTRAST_RGB, by itself, creates a new CONTRAST_RGB or raises the existing
%      singleton*.
%
%      H = CONTRAST_RGB returns the handle to a new CONTRAST_RGB or the handle to
%      the existing singleton*.
%
%      CONTRAST_RGB('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in CONTRAST_RGB.M with the given input arguments.
%
%      CONTRAST_RGB('Property','Value',...) creates a new CONTRAST_RGB or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before contrast_RGB_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to contrast_RGB_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help contrast_RGB

% Last Modified by GUIDE v2.5 06-Jan-2018 16:38:03

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @contrast_RGB_OpeningFcn, ...
                   'gui_OutputFcn',  @contrast_RGB_OutputFcn, ...
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


% --- Executes just before contrast_RGB is made visible.
function contrast_RGB_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to contrast_RGB (see VARARGIN)

% Choose default command line output for contrast_RGB
handles.output = hObject;
global f g
logo=imread('ZoiLogosmall.png');
axes(handles.axes9)
imshow(logo)
g=f;
hold off
axes(handles.axes1)
imshow(f)
set(handles.edit1,'string',num2str(1));
set(handles.edit4,'string',num2str(1));
set(handles.edit7,'string',num2str(1));

set(handles.edit2,'string',num2str(min(min(f(:,:,1)))));
set(handles.edit3,'string',num2str(max(max(f(:,:,1)))));

set(handles.edit5,'string',num2str(min(min(f(:,:,2)))));
set(handles.edit6,'string',num2str(max(max(f(:,:,2)))));

set(handles.edit8,'string',num2str(min(min(f(:,:,3)))));
set(handles.edit9,'string',num2str(max(max(f(:,:,3)))));




set(handles.slider1,'value',min(min(f(:,:,1))))
set(handles.slider2,'value',max(max(f(:,:,1))))

set(handles.slider3,'value',min(min(f(:,:,2))))
set(handles.slider4,'value',max(max(f(:,:,2))))

set(handles.slider5,'value',min(min(f(:,:,3))))
set(handles.slider6,'value',max(max(f(:,:,3))))

s1=double(min(min(f(:,:,1))));
s2=double(max(max(f(:,:,1))));

s3=double(min(min(f(:,:,2))));
s4=double(max(max(f(:,:,2))));

s5=double(min(min(f(:,:,3))));
s6=double(max(max(f(:,:,3))));


axes(handles.axes2)
h1=imhist(f(:,:,1));       
h1=255*h1/max(h1);
x=[0 255];           %plot of function transformation
y=[0 255];           %plot of function transformation   
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1,'r')          %plot of function transformation   
hold on              %plot of function transformation   
plot(x,y,'k')        %plot of function transformation   
title(['{\color{red}Red}'])
plot([min(min(f(:,:,1))) min(min(f(:,:,1)))],[0 max(h1)],'k','linewidth',2)
plot([max(max(f(:,:,1))) max(max(f(:,:,1)))],[0 max(h1)],'k','linewidth',2)
                     %plot of function transformation   
                     %plot of function transformation
                     %plot of function transformation
                     
axes(handles.axes3)
h2=imhist(f(:,:,2));    %plot of function transformation
h2=255*h2/max(h2);      %plot of function transformation
x=[0 255];              %plot of function transformation
y=[0 255];              %plot of function transformation
x=min(s3,s4)+(max(s3,s4)-min(s3,s4))*(x-min(x))/(max(x)-min(x));
bar(h2,'g')             %plot of function transformation
hold on                 %plot of function transformation
plot(x,y,'k')
title(['{\color{green}Green}'])
plot([min(min(f(:,:,2))) min(min(f(:,:,2)))],[0 max(h2)],'k','linewidth',2)
plot([max(max(f(:,:,2))) max(max(f(:,:,2)))],[0 max(h2)],'k','linewidth',2)


axes(handles.axes4)     %plot of function transformation
h3=imhist(f(:,:,3));    %plot of function transformation
h3=255*h3/max(h3);      %plot of function transformation
x=[0 255];              %plot of function transformation
y=[0 255];              %plot of function transformation
x=min(s5,s6)+(max(s5,s6)-min(s5,s6))*(x-min(x))/(max(x)-min(x));
bar(h3,'b')             %plot of function transformation
hold on                 %plot of function transformation
plot(x,y,'k')           %plot of function transformation
title(['{\color{blue}Blue}'])
plot([min(min(f(:,:,3))) min(min(f(:,:,3)))],[0 max(h3)],'k','linewidth',2)
plot([max(max(f(:,:,3))) max(max(f(:,:,3)))],[0 max(h3)],'k','linewidth',2)
hold off                %plot of function transformation

axes(handles.axes6)
imshow(f(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(f(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(f(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes contrast_RGB wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = contrast_RGB_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit7_Callback(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit7 as text
%        str2double(get(hObject,'String')) returns contents of edit7 as a double
global f g

gamma3=str2num(get(handles.edit7,'string'));
set(handles.edit7,'string',num2str(gamma3));
s5=get(handles.slider5,'value');
s6=get(handles.slider6,'value');
s5=round(s5);
s6=round(s6);

set(handles.edit8,'string',num2str(s5))
set(handles.edit9,'string',num2str(s6))


axes(handles.axes4)
hold off
h3=imhist(f(:,:,3));
h3=255*h3/max(h3);      %plot of function transformation
x=0:0.01:255;           %plot of function transformation
y=255*(x/255).^gamma3;  %plot of function transformation
x=min(s5,s6)+(max(s5,s6)-min(s5,s6))*(x-min(x))/(max(x)-min(x));
bar(h3,'b')             %plot of function transformation
hold on                 %plot of function transformation
plot(x,y,'k')           %plot of function transformation    
title(['{\color{blue}Blue}'])
plot([s5 s5],[0 max(h3)],'k','linewidth',2) %plot of function transformation
plot([s6 s6],[0 max(h3)],'k','linewidth',2) %plot of function transformation
hold off                
axes(handles.axes1)
if s5~=s6
g3=imadjust(f(:,:,3),[min(s5/255,s6/255),max(s5/255,s6/255)],[0,1],gamma3);
g(:,:,3)=g3;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes during object creation, after setting all properties.
function edit7_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit8_Callback(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit8 as text
%        str2double(get(hObject,'String')) returns contents of edit8 as a double
global f g

gamma3=str2num(get(handles.edit7,'string'));
set(handles.edit7,'string',num2str(gamma3));

e8=str2num(get(handles.edit8,'string'));
e9=str2num(get(handles.edit9,'string'));

set(handles.slider5,'value',e8);
set(handles.slider6,'value',e9);

s5=get(handles.slider5,'value');
s6=get(handles.slider6,'value');
s5=round(s5);
s6=round(s6);

set(handles.edit8,'string',num2str(s5))
set(handles.edit9,'string',num2str(s6))


axes(handles.axes4)
hold off
h3=imhist(f(:,:,3));                %plot of function transformation
h3=255*h3/max(h3);                  %plot of function transformation
x=0:0.01:255;                       %plot of function transformation
y=255*(x/255).^gamma3;              %plot of function transformation
x=min(s5,s6)+(max(s5,s6)-min(s5,s6))*(x-min(x))/(max(x)-min(x)); %plot of function transformation
bar(h3,'b')                         %plot of function transformation
hold on                             %plot of function transformation    
plot(x,y,'k')                       %plot of function transformation        
title(['{\color{blue}Blue}'])       %plot of function transformation
plot([s5 s5],[0 max(h3)],'k','linewidth',2) %plot of function transformation
plot([s6 s6],[0 max(h3)],'k','linewidth',2) %plot of function transformation
hold off 
axes(handles.axes1)
if s5~=s6
g3=imadjust(f(:,:,3),[min(s5/255,s6/255),max(s5/255,s6/255)],[0,1],gamma3);
g(:,:,3)=g3;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes during object creation, after setting all properties.
function edit8_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit9_Callback(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit9 as text
%        str2double(get(hObject,'String')) returns contents of edit9 as a double
global f g

gamma3=str2num(get(handles.edit7,'string'));
set(handles.edit7,'string',num2str(gamma3));

e8=str2num(get(handles.edit8,'string'));
e9=str2num(get(handles.edit9,'string'));

set(handles.slider5,'value',e8);
set(handles.slider6,'value',e9);

s5=get(handles.slider5,'value');
s6=get(handles.slider6,'value');
s5=round(s5);
s6=round(s6);

set(handles.edit8,'string',num2str(s5))
set(handles.edit9,'string',num2str(s6))


axes(handles.axes4)
hold off
h3=imhist(f(:,:,3));
h3=255*h3/max(h3);
x=0:0.01:255;                           %plot of function transformation
y=255*(x/255).^gamma3;                  %plot of function transformation            
x=min(s5,s6)+(max(s5,s6)-min(s5,s6))*(x-min(x))/(max(x)-min(x));
bar(h3,'b')                             %plot of function transformation    
hold on                                 %plot of function transformation
plot(x,y,'k')                           %plot of function transformation
title(['{\color{blue}Blue}'])           %plot of function transformation
plot([s5 s5],[0 max(h3)],'k','linewidth',2) %plot of function transformation
plot([s6 s6],[0 max(h3)],'k','linewidth',2) %plot of function transformation 
hold off
axes(handles.axes1)
if s5~=s6
g3=imadjust(f(:,:,3),[min(s5/255,s6/255),max(s5/255,s6/255)],[0,1],gamma3);
g(:,:,3)=g3;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes during object creation, after setting all properties.
function edit9_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on slider movement.
function slider5_Callback(hObject, eventdata, handles)
% hObject    handle to slider5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f g

gamma3=str2num(get(handles.edit7,'string'));
set(handles.edit7,'string',num2str(gamma3));
s5=get(handles.slider5,'value');
s6=get(handles.slider6,'value');
s5=round(s5);
s6=round(s6);

set(handles.edit8,'string',num2str(s5))
set(handles.edit9,'string',num2str(s6))


axes(handles.axes4)
hold off
h3=imhist(f(:,:,3));                %plot of function transformation
h3=255*h3/max(h3);                  %plot of function transformation       
x=0:0.01:255;                       %plot of function transformation
y=255*(x/255).^gamma3;              %plot of function transformation    
x=min(s5,s6)+(max(s5,s6)-min(s5,s6))*(x-min(x))/(max(x)-min(x));
bar(h3,'b')                         %plot of function transformation
hold on                             %plot of function transformation    
plot(x,y,'k')
title(['{\color{blue}Blue}'])
plot([s5 s5],[0 max(h3)],'k','linewidth',2)
plot([s6 s6],[0 max(h3)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s5~=s6
g3=imadjust(f(:,:,3),[min(s5/255,s6/255),max(s5/255,s6/255)],[0,1],gamma3);
g(:,:,3)=g3;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end



% --- Executes during object creation, after setting all properties.
function slider5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on slider movement.
function slider6_Callback(hObject, eventdata, handles)
% hObject    handle to slider6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f g

gamma3=str2num(get(handles.edit7,'string'));
set(handles.edit7,'string',num2str(gamma3));
s5=get(handles.slider5,'value');
s6=get(handles.slider6,'value');
s5=round(s5);
s6=round(s6);

set(handles.edit8,'string',num2str(s5))
set(handles.edit9,'string',num2str(s6))


axes(handles.axes4)
hold off
h3=imhist(f(:,:,3));                %plot of function transformation
h3=255*h3/max(h3);                  %plot of function transformation
x=0:0.01:255;                       %plot of function transformation    
y=255*(x/255).^gamma3;              %plot of function transformation    
x=min(s5,s6)+(max(s5,s6)-min(s5,s6))*(x-min(x))/(max(x)-min(x));
bar(h3,'b')                         %plot of function transformation
hold on                             %plot of function transformation    
plot(x,y,'k')                       %plot of function transformation
title(['{\color{blue}Blue}'])       %plot of function transformation
plot([s5 s5],[0 max(h3)],'k','linewidth',2)
plot([s6 s6],[0 max(h3)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s5~=s6
g3=imadjust(f(:,:,3),[min(s5/255,s6/255),max(s5/255,s6/255)],[0,1],gamma3);
g(:,:,3)=g3;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end

% --- Executes during object creation, after setting all properties.
function slider6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double
global f g

gamma2=str2num(get(handles.edit4,'string'));
set(handles.edit4,'string',num2str(gamma2));
s3=get(handles.slider3,'value');
s4=get(handles.slider4,'value');
s3=round(s3);
s4=round(s4);

set(handles.edit5,'string',num2str(s3))
set(handles.edit6,'string',num2str(s4))


axes(handles.axes3)
hold off
h2=imhist(f(:,:,2));            %<== plot of function transformation
h2=255*h2/max(h2);              %<== plot of function transformation
x=0:0.01:255;                   %<== plot of function transformation
y=255*(x/255).^gamma2;          %<== plot of function transformation
x=min(s3,s4)+(max(s3,s4)-min(s3,s4))*(x-min(x))/(max(x)-min(x));
bar(h2,'g')                     %<== plot of function transformation
hold on                         %<== plot of function transformation
plot(x,y,'k')                   %<== plot of function transformation
title(['{\color{green}Green}']) %<== plot of function transformation
plot([s3 s3],[0 max(h2)],'k','linewidth',2)
plot([s4 s4],[0 max(h2)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s3~=s4
g2=imadjust(f(:,:,2),[min(s3/255,s4/255),max(s3/255,s4/255)],[0,1],gamma2);
g(:,:,2)=g2;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double
global f g

gamma2=str2num(get(handles.edit4,'string'));
set(handles.edit4,'string',num2str(gamma2));

e5=str2num(get(handles.edit5,'string'));
e6=str2num(get(handles.edit6,'string'));

set(handles.slider3,'value',e5);
set(handles.slider4,'value',e6);


s3=get(handles.slider3,'value');
s4=get(handles.slider4,'value');
s3=round(s3);
s4=round(s4);

set(handles.edit5,'string',num2str(s3))
set(handles.edit6,'string',num2str(s4))


axes(handles.axes3)
hold off  
h2=imhist(f(:,:,2));                %<== plot of function transformation
h2=255*h2/max(h2);                  %<== plot of function transformation
x=0:0.01:255;                       %<== plot of function transformation
y=255*(x/255).^gamma2;              %<== plot of function transformation    
x=min(s3,s4)+(max(s3,s4)-min(s3,s4))*(x-min(x))/(max(x)-min(x));
bar(h2,'g')                         %<== plot of function transformation
hold on                             %<== plot of function transformation
plot(x,y,'k')                       %<== plot of function transformation
title(['{\color{green}Green}'])     %<== plot of function transformation
plot([s3 s3],[0 max(h2)],'k','linewidth',2)
plot([s4 s4],[0 max(h2)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s3~=s4
g2=imadjust(f(:,:,2),[min(s3/255,s4/255),max(s3/255,s4/255)],[0,1],gamma2);
g(:,:,2)=g2;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end



% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit6 as text
%        str2double(get(hObject,'String')) returns contents of edit6 as a double
global f g

gamma2=str2num(get(handles.edit4,'string'));
set(handles.edit4,'string',num2str(gamma2));

e5=str2num(get(handles.edit5,'string'));
e6=str2num(get(handles.edit6,'string'));

set(handles.slider3,'value',e5);
set(handles.slider4,'value',e6);


s3=get(handles.slider3,'value');
s4=get(handles.slider4,'value');
s3=round(s3);
s4=round(s4);

set(handles.edit5,'string',num2str(s3))
set(handles.edit6,'string',num2str(s4))


axes(handles.axes3)
hold off
h2=imhist(f(:,:,2));                %<== plot of function transformation
h2=255*h2/max(h2);                  %<== plot of function transformation
x=0:0.01:255;                       %<== plot of function transformation    
y=255*(x/255).^gamma2;              %<== plot of function transformation
x=min(s3,s4)+(max(s3,s4)-min(s3,s4))*(x-min(x))/(max(x)-min(x));
bar(h2,'g')                         %<== plot of function transformation
hold on                             %<== plot of function transformation
plot(x,y,'k')                       %<== plot of function transformation
title(['{\color{green}Green}'])     %<== plot of function transformation
plot([s3 s3],[0 max(h2)],'k','linewidth',2)
plot([s4 s4],[0 max(h2)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s3~=s4
g2=imadjust(f(:,:,2),[min(s3/255,s4/255),max(s3/255,s4/255)],[0,1],gamma2);
g(:,:,2)=g2;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes during object creation, after setting all properties.
function edit6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on slider movement.
function slider3_Callback(hObject, eventdata, handles)
% hObject    handle to slider3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f g

gamma2=str2num(get(handles.edit4,'string'));
set(handles.edit4,'string',num2str(gamma2));
s3=get(handles.slider3,'value');
s4=get(handles.slider4,'value');
s3=round(s3);
s4=round(s4);

set(handles.edit5,'string',num2str(s3))
set(handles.edit6,'string',num2str(s4))


axes(handles.axes3)
hold off
h2=imhist(f(:,:,2));                %<== plot of function transformation
h2=255*h2/max(h2);                  %<== plot of function transformation
x=0:0.01:255;                       %<== plot of function transformation
y=255*(x/255).^gamma2;              %<== plot of function transformation
x=min(s3,s4)+(max(s3,s4)-min(s3,s4))*(x-min(x))/(max(x)-min(x));
bar(h2,'g')                         %<== plot of function transformation
hold on                             %<== plot of function transformation    
plot(x,y,'k')                       %<== plot of function transformation
title(['{\color{green}Green}'])     %<== plot of function transformation
plot([s3 s3],[0 max(h2)],'k','linewidth',2)
plot([s4 s4],[0 max(h2)],'k','linewidth',2)
hold off                            
axes(handles.axes1)                 
if s3~=s4
g2=imadjust(f(:,:,2),[min(s3/255,s4/255),max(s3/255,s4/255)],[0,1],gamma2);
g(:,:,2)=g2;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end

% --- Executes during object creation, after setting all properties.
function slider3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on slider movement.
function slider4_Callback(hObject, eventdata, handles)
% hObject    handle to slider4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f g

gamma2=str2num(get(handles.edit4,'string'));
set(handles.edit4,'string',num2str(gamma2));
s3=get(handles.slider3,'value');
s4=get(handles.slider4,'value');
s3=round(s3);
s4=round(s4);

set(handles.edit5,'string',num2str(s3))
set(handles.edit6,'string',num2str(s4))


axes(handles.axes3)
hold off
h2=imhist(f(:,:,2));
h2=255*h2/max(h2);              %<== plot of function transformation
x=0:0.01:255;                   %<== plot of function transformation
y=255*(x/255).^gamma2;          %<== plot of function transformation
x=min(s3,s4)+(max(s3,s4)-min(s3,s4))*(x-min(x))/(max(x)-min(x));
bar(h2,'g')                     %<== plot of function transformation
hold on                         %<== plot of function transformation
plot(x,y,'k')                   %<== plot of function transformation
title(['{\color{green}Green}']) %<== plot of function transformation
plot([s3 s3],[0 max(h2)],'k','linewidth',2)
plot([s4 s4],[0 max(h2)],'k','linewidth',2)
hold off                        
axes(handles.axes1)
if s3~=s4
g2=imadjust(f(:,:,2),[min(s3/255,s4/255),max(s3/255,s4/255)],[0,1],gamma2);
g(:,:,2)=g2;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end

% --- Executes during object creation, after setting all properties.
function slider4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double
global f g

gamma1=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma1));
s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f(:,:,1));            %<== plot of function transformation
h1=255*h1/max(h1);              %<== plot of function transformation
x=0:0.01:255;                   %<== plot of function transformation
y=255*(x/255).^gamma1;          %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1,'r')                     %<== plot of function transformation
hold on                         %<== plot of function transformation
plot(x,y,'k')                   %<== plot of function transformation    
title(['{\color{red}Red}'])
plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s1~=s2
g1=imadjust(f(:,:,1),[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma1);
g(:,:,1)=g1;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


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



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double
global f g

gamma1=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma1));

e2=str2num(get(handles.edit2,'string'));
e3=str2num(get(handles.edit3,'string'));

set(handles.slider1,'value',e2);
set(handles.slider2,'value',e3);

s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f(:,:,1));
h1=255*h1/max(h1);                  %<== plot of function transformation
x=0:0.01:255;                       %<== plot of function transformation
y=255*(x/255).^gamma1;              %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1,'r')                         %<== plot of function transformation
hold on                             %<== plot of function transformation
plot(x,y,'k')                       %<== plot of function transformation
title(['{\color{red}Red}'])         %<== plot of function transformation
plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s1~=s2
g1=imadjust(f(:,:,1),[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma1);
g(:,:,1)=g1;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double
global f g

gamma1=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma1));

e2=str2num(get(handles.edit2,'string'));
e3=str2num(get(handles.edit3,'string'));

set(handles.slider1,'value',e2);
set(handles.slider2,'value',e3);

s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f(:,:,1));            %<== plot of function transformation
h1=255*h1/max(h1);              %<== plot of function transformation
x=0:0.01:255;                   %<== plot of function transformation
y=255*(x/255).^gamma1;          %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1,'r')                     %<== plot of function transformation
hold on                         %<== plot of function transformation
plot(x,y,'k')                   %<== plot of function transformation
title(['{\color{red}Red}'])
plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s1~=s2
g1=imadjust(f(:,:,1),[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma1);
g(:,:,1)=g1;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on slider movement.
function slider1_Callback(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f g

gamma1=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma1));
s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)         
hold off
h1=imhist(f(:,:,1));                %<== plot of function transformation
h1=255*h1/max(h1);                  %<== plot of function transformation
x=0:0.01:255;                       %<== plot of function transformation
y=255*(x/255).^gamma1;              %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1,'r')                         %<== plot of function transformation
hold on                             %<== plot of function transformation
plot(x,y,'k')                       %<== plot of function transformation    
title(['{\color{red}Red}'])         %<== plot of function transformation
plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s1~=s2
g1=imadjust(f(:,:,1),[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma1);
g(:,:,1)=g1;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes during object creation, after setting all properties.
function slider1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on slider movement.
function slider2_Callback(hObject, eventdata, handles)
% hObject    handle to slider2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global f g

gamma1=str2num(get(handles.edit1,'string'));
set(handles.edit1,'string',num2str(gamma1));
s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f(:,:,1));                %<== plot of function transformation
h1=255*h1/max(h1);                  %<== plot of function transformation    
x=0:0.01:255;                       %<== plot of function transformation    
y=255*(x/255).^gamma1;              %<== plot of function transformation
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1,'r')                         %<== plot of function transformation
hold on                             %<== plot of function transformation
plot(x,y,'k')                       %<== plot of function transformation
title(['{\color{red}Red}'])         %<== plot of function transformation
plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s1~=s2
g1=imadjust(f(:,:,1),[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma1);
g(:,:,1)=g1;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end



% --- Executes during object creation, after setting all properties.
function slider2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g

set(handles.edit1,'string',num2str(1));
gamma1=str2num(get(handles.edit1,'string'));

set(handles.slider1,'value',min(min(f(:,:,1))));
set(handles.slider2,'value',max(max(f(:,:,1))));

s1=get(handles.slider1,'value');
s2=get(handles.slider2,'value');
s1=round(s1);
s2=round(s2);

set(handles.edit2,'string',num2str(s1))
set(handles.edit3,'string',num2str(s2))

axes(handles.axes2)
hold off
h1=imhist(f(:,:,1));            %<== plot of function transformation
h1=255*h1/max(h1);              %<== plot of function transformation
x=0:0.01:255;                   %<== plot of function transformation
y=255*(x/255).^gamma1;          %<== plot of function transformation    
x=min(s1,s2)+(max(s1,s2)-min(s1,s2))*(x-min(x))/(max(x)-min(x));
bar(h1,'r')                     %<== plot of function transformation
hold on                         %<== plot of function transformation    
plot(x,y,'k')
title(['{\color{red}Red}'])
plot([s1 s1],[0 max(h1)],'k','linewidth',2)
plot([s2 s2],[0 max(h1)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s1~=s2
g1=imadjust(f(:,:,1),[min(s1/255,s2/255),max(s1/255,s2/255)],[0,1],gamma1);
g(:,:,1)=g1;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g

set(handles.edit4,'string',num2str(1));
gamma2=str2num(get(handles.edit4,'string'));

set(handles.slider3,'value',min(min(f(:,:,2))));
set(handles.slider4,'value',max(max(f(:,:,2))));


s3=get(handles.slider3,'value');
s4=get(handles.slider4,'value');
s3=round(s3);
s4=round(s4);

set(handles.edit5,'string',num2str(s3))
set(handles.edit6,'string',num2str(s4))


axes(handles.axes3)
hold off
h2=imhist(f(:,:,2));            %<== plot of function transformation
h2=255*h2/max(h2);              %<== plot of function transformation
x=[0:0.01:255];                 %<== plot of function transformation
y=[0:0.01:255];                 %<== plot of function transformation
x=min(s3,s4)+(max(s3,s4)-min(s3,s4))*(x-min(x))/(max(x)-min(x));
bar(h2,'g')                     %<== plot of function transformation
hold on                         %<== plot of function transformation
plot(x,y,'k')                   %<== plot of function transformation
title(['{\color{green}Green}']) %<== plot of function transformation
plot([s3 s3],[0 max(h2)],'k','linewidth',2)
plot([s4 s4],[0 max(h2)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s3~=s4
g2=imadjust(f(:,:,2),[min(s3/255,s4/255),max(s3/255,s4/255)],[0,1],gamma2);
g(:,:,2)=g2;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end




% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global f g

set(handles.edit7,'string',num2str(1));
gamma3=str2num(get(handles.edit7,'string'));

set(handles.slider5,'value',min(min(f(:,:,3))));
set(handles.slider6,'value',max(max(f(:,:,3))));


s5=get(handles.slider5,'value');
s6=get(handles.slider6,'value');
s5=round(s5);
s6=round(s6);

set(handles.edit8,'string',num2str(s5))
set(handles.edit9,'string',num2str(s6))


axes(handles.axes4)
hold off
h3=imhist(f(:,:,3));            %<== plot of function transformation
h3=255*h3/max(h3);              %<== plot of function transformation            
x=[0:0.01:255];                 %<== plot of function transformation    
y=[0:0.01:255];                 %<== plot of function transformation
x=min(s5,s6)+(max(s5,s6)-min(s5,s6))*(x-min(x))/(max(x)-min(x));
bar(h3,'b')                     %<== plot of function transformation     
hold on                         %<== plot of function transformation
plot(x,y,'k')                   %<== plot of function transformation
title(['{\color{blue}Blue}'])   %<== plot of function transformation
plot([s5 s5],[0 max(h3)],'k','linewidth',2)
plot([s6 s6],[0 max(h3)],'k','linewidth',2)
hold off
axes(handles.axes1)
if s5~=s6
g3=imadjust(f(:,:,3),[min(s5/255,s6/255),max(s5/255,s6/255)],[0,1],gamma3);
g(:,:,3)=g3;
imshow(g)

axes(handles.axes6)
imshow(g(:,:,1))
title(['{\color{red}\fontsize{8}Red}'])
axes(handles.axes7)
imshow(g(:,:,2))
title(['{\color{green}\fontsize{8}Green}'])
axes(handles.axes8)
imshow(g(:,:,3))
title(['{\color{blue}\fontsize{8}Blue}'])

end


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global g f FileName infoo

% Export image

if FileName==0 | isempty(FileName)
    FileName='Matlab Picture.PNG';
end
if isequal(infoo.Format,'GIF')
    FileName(end-2:end)='png';
end
if ~isequal(g,f)
    masir=uigetdir;
    if masir~=0
        wb=waitbar(0,'Please wait...');
        imwrite(g,[masir,'/Contrast ',FileName])
        
        
        for i=1:1000
            waitbar(i/1000);
        end
        pause(0.1)
        close(wb)
    end
end
