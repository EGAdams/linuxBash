const { app, BrowserWindow, dialog, ipcMain, Tray, Menu} = require('electron');
const fs = require('fs');
const os_util = require('node-os-utils');
const os = require("os");
const child_process = require("child_process");

let mainWindow;
let isQuiting;
let tray;


function createWindow() {
    mainWindow = new BrowserWindow({
        width: 550,
        height: 700,
        // maxWidth:1000,
        // icon:"icon.png",

    });
    mainWindow.loadFile('index.html');
    // mainWindow.maximize();

    // create system tray
    // var appIcon = new Tray( "./icon.png" );
    var contextMenu = Menu.buildFromTemplate([
        {
            label: 'Show App', click: function () {
                mainWindow.show()
            }
        },

        {
            label: 'Open Program Files', click: function () {
                child_process.exec('start "" "C:\\Program Files"')
            }
        },

        {
            label: 'Open Temp Folder', click: function () {
                child_process.exec('start ' + os.tmpdir());
            }
        },

        {
            label: 'Open NotePad', click: function () {
                child_process.spawn('C:\\windows\\notepad.exe')
            }
        },

        {
            label: 'Quit', click: function () {
                app.isQuiting = true;
                app.quit()
            }
        }
    ]);
    // appIcon.setContextMenu(contextMenu);

    mainWindow.on('close', function (event) {
        if(!app.isQuiting){
            event.preventDefault();
            mainWindow.hide();
        }
        return false;
    });

    mainWindow.on('minimize', function (event) {
        event.preventDefault();
        mainWindow.hide()
    });

    mainWindow.on('show', function () {
        // appIcon.setHighlightMode('always')
    });

}
app.on('ready', createWindow);

// Open Select file dialog
ipcMain.on('select-file', (event, arg) => {
    const path = (dialog.showOpenDialog({ properties: ['openFile', 'openDirectory', 'multiSelections'] }));
    fs.readdir(path[0], (err, files) =>{
        files.forEach(file =>{
            console.log(path[0]+ '\\' + file);
        })
    })
});

// Get CPU Usage
ipcMain.on('get-cpu', (event, arg) => {
    setInterval(getcpuusage, 100)
});

function getcpuusage() {
    var cpu = os_util.cpu;
    cpu.usage()
        .then(info => {
            mainWindow.webContents.send('cpu', info)
            // send uptime to front end
            mainWindow.webContents.send('uptime', os.uptime());
        })
}

// open notepad
// ipcMain.on('open-notepad', (event, arg) => {
//     child_process.spawn('C:\\windows\\notepad.exe')
// });



// open folder
ipcMain.on('home-spa', (event, arg) => {
    child_process.exec('start "" "C:\\Users\\EG\\Desktop\\2022\\rol\\rol_map"')
});

// open folder
ipcMain.on('typescript-source', (event, arg) => {
    child_process.exec('start "" "C:\\Users\\EG\\Desktop\\2022\\march\\3_week\\pkief_debug_article"')
});

ipcMain.on('open-this-folder', (event, arg) => {
    child_process.exec('start "" "C:\\Users\\EG\\march\\week_3\\linuxBash\\system_info"')
});

ipcMain.on('log-vuer-plugin', (event, arg) => {
    child_process.exec('start "" "C:\\Users\\EG\\Desktop\\2022\\april\\2nd_week\\friday\\vue3-plugin"')
});

ipcMain.on('log-object-processor', (event, arg) => {
    child_process.exec('start "" "C:\\Users\\EG\\Desktop\\2022\\april\\1st_week\\log_object_processor_new_build\\log-object-processor"')
});

ipcMain.on('log-object-processor-test', (event, arg) => {
    child_process.exec('start "" "C:\\Users\\EG\\Desktop\\2022\\april\\2nd_week\\friday\\log-viewer-test"')
});

ipcMain.on('open-vue-sequence', (event, arg) => {
    child_process.exec('start "" "C:\\Users\\EG\\vue-sequence-diagram"')
});
