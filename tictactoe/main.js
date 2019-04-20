const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu} = electron;

let mainWindow;

app.on('ready', function(){
    mainWindow = new BrowserWindow({});
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'gui.html'),
        protocol: 'file',
        slashes: true
    }));

    //build menu from template
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    //Insert menu
    Menu.setApplicationMenu(mainMenu);
});

//create menu template
const mainMenuTemplate = [
    {
        label: 'file',
        submenu: [
            {
                label: 'quit',
                accelerator: process.platform == 'darwin' ? 'command+Q' : 'ctrl+Q',
                click(){
                    app.quit();
                }
            }
        ]
    }
];

/*
//emitted when the window is closed
mainWindow.on('closed', function(){
    //karena window disimpan dalam bentuk array jika app support multiwindow
    //ini digunakan untuk menghapus coresponding element
    mainWindow = null;
})
*/