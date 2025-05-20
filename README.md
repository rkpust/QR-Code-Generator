# QR Code Generator
<div align="center">
  <img height="500" width="400" src="https://github.com/rkpust/QR-Code-Generator/blob/master/QR%20Code%20Generator%20UI%201.jpg"/>
  <img height="500" width="400" src="https://github.com/rkpust/QR-Code-Generator/blob/master/QR%20Code%20Generator%20UI%202.jpg"/>
</div>

## How To Use QR Code Generator
### Method 1
- You can download it directly from [this repository](https://github.com/rkpust/QR-Code-Generator/).
- You need to find the file 'QR Code Generator.exe' and then click on it.
- Find the download icon. Then click here.
- Finally 'QR Code Generator.exe' will be downloaded.
- After downloading, you need to double-click on the app.
- You may get a warning from Microsoft Defender SmartScreen for the first time; click on 'More info'.
- Then you will see the 'Run anyway' button, now click here.
- !!! Boom !!! the app is running.
- Thanks for using it.

### Method 2
- You can download this repository directly from [here](https://github.com/rkpust/QR-Code-Generator/). Find the green button, Code > Download ZIP. Otherwise, follow the command:
```
git clone https://github.com/rkpust/QR-Code-Generator.git
```

- Create a virtual environment and activate it. Python 3.11.5 is recommended.
```
python -m venv venv_name
venv_name\Scripts\activate
```

- Install the required packages with the following command.
```
pip install -r requirements.txt
```

- Run the following command to build your target app.
```
pyinstaller --onefile --noconsole --icon="RezaulKarim.ico" --add-data "RezaulKarim.ico;." "QR Code Generator.py"
```
- **!!! Boom !!!** Wait for a while; you will see two folders named 'build' and 'dist'. You will find your targeted app in the 'dist' folder.
- After building, you need to double-click on the app.
- You may get a warning from 'Microsoft Defender SmartScreen' for the first time; click on 'More info'.
- Then you will see the 'Run Anyway' button; now click here.
- **!!! Congratulations !!!** The app has been successfully run.
- Thanks for using it.
  