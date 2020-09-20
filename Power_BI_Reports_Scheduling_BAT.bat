@echo off:

start:

title File Creator with extension as per user

echo Enter the details(Name) of a text file :...

set /file_name =        Enter the details(Name) of the file :...
set /file_extension =    Enter the extension of the file:...


echo.>%file_name%.%file_extension%




pause

