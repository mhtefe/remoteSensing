@echo off
SET OSGEO4W_ROOT=C:\OSGeo4W64
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat

#echo off
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass-6.4.3\lib
path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\plugins\platforms
path %PATH%;C:\OSGeo4W64\apps\Qt5\bin
path %PATH%;C:\OSGeo4W64\apps\Python37\Scripts
path %PATH%;C:\OSGeo4W64\apps\qgis\python
path %PATH%;C:\OSGeo4W64\apps\Python37\lib\site-packages

set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python
set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins\platforms
set QT_QPA_PLATFORM_PLUGIN_PATH=C:\OSGeo4W64\apps\Qt5\plugins
#set QT_DEBUG_PLUGINS=1
set QGIS_PREFIX=%OSGEO4W_ROOT%\apps\qgis

set PATH=C:\Program Files\Git\bin;%PATH%

cmd.exe
