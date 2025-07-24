@echo off
echo Checking for input.txt file...

IF EXIST input.txt (
    echo Input data present.
) ELSE (
    echo input.txt not found. Exiting.
    pause
    exit /b
)

echo Running the Python program...
python main.py input.txt

echo.
echo Program execution completed.
echo Output has been saved in output.txt
echo.
pause
