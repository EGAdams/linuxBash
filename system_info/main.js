const { app, BrowserWindow, dialog, ipcMain, Tray, Menu } = require( 'electron' );
const fs = require( 'fs' );
const os_util = require( 'node-os-utils' );
const os = require( "os" );
const child_process = require( "child_process" );

let mainWindow;
let isQuiting;
let tray;


function createWindow() {
    mainWindow = new BrowserWindow({ width: 550, height: 700 });
    mainWindow.loadFile( 'index.html' );
 
    // create system tray
    // let appIcon = new Tray( "./icon.png" );
    let contextMenu = Menu.buildFromTemplate( [ {
            label: 'Show App',
            click: function () {
                mainWindow.show()
            }
        },

        {
            label: 'Open Program Files',
            click: function () {
         child_process.exec( 'start "" "C:\\Program Files"' )
            }
        },

        {
            label: 'Open Temp Folder',
            click: function () {
         child_process.exec( 'start ' + os.tmpdir() );
            }
        },

        {
            label: 'Open NotePad',
            click: function () {
         child_process.spawn( 'C:\\windows\\notepad.exe' )
            }
        },

        {
            label: 'Quit',
            click: function () {
                app.isQuiting = true;
                app.quit()
            }
        }
    ] );
    // appIcon.setContextMenu(contextMenu);

    mainWindow.on( 'close', function ( event ) {
        if ( !app.isQuiting ) {
            event.preventDefault();
            mainWindow.hide();
        }
        return false;
    } );

    mainWindow.on( 'minimize', function ( event ) {
        event.preventDefault();
        mainWindow.hide()
    } );

    mainWindow.on( 'show', function () {
        // appIcon.setHighlightMode('always')
    } );

}
app.on( 'ready', createWindow );

// Open Select file dialog
ipcMain.on( 'select-file', () => {
    const path = ( dialog.showOpenDialog( {
        properties: [ 'openFile', 'openDirectory', 'multiSelections' ]
    } ) );
    fs.readdir( path[ 0 ], ( _err, files ) => {
        files.forEach( file => {
            console.log( path[ 0 ] + '\\' + file );
        } )
    } )
} );

// Get CPU Usage
ipcMain.on( 'get-cpu', () => {
    setInterval( getcpuusage, 100 )
} );

function getcpuusage() {
    let cpu = os_util.cpu;
    cpu.usage().then( info => {
            mainWindow.webContents.send( 'cpu', info )
            // send uptime to front end
            mainWindow.webContents.send( 'uptime', os.uptime() );
        } )
}

// open notepad
// ipcMain.on('open-notepad', (event, arg) => {
// child_process.spawn('C:\\windows\\notepad.exe')
// });

ipcMain.on( 'home-spa',                        () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\rol\\rol_map"' )});
ipcMain.on( 'typescript-source',               () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\march\\3_week\\pkief_debug_article"' )});
ipcMain.on( 'vite-electron-typescript-source', () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\march\\4th_week\\wed\\vite-vue-electron\\src\\typescript_source"' )});
ipcMain.on( 'open-this-folder',                () => { child_process.exec( 'start "" "C:\\Users\\EG\\march\\week_3\\linuxBash\\system_info"' )});
ipcMain.on( 'log-vuer-plugin',                 () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\april\\2nd_week\\log-vuer"' )});
ipcMain.on( 'log-object-processor',            () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\april\\1st_week\\log_object_processor_new_build\\log-object-processor"' )});
ipcMain.on( 'log-object-processor-test',       () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\april\\2nd_week\\friday\\log-viewer-test"' )});
ipcMain.on( 'open-vue-sequence',               () => { child_process.exec( 'start "" "C:\\Users\\EG\\vue-sequence-diagram"' )});
ipcMain.on( 'sourced-log-viewer',              () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\june\\4th_week\\egadams_log_viewer"' )});
ipcMain.on( 'original-monitor',                () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\july\\1st_week\\vite-vue-electron"' )});
ipcMain.on( 'monitor-led',                     () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\july\\1st_week\\monitor-led"' )});
ipcMain.on( 'bank-interrogation',              () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\june\\3rd_week\\jasmine_selenium"' )});
ipcMain.on( 'wordpress-project',               () => { child_process.exec( 'start "" "C:\\xampp-joomla\\htdocs\\wordpress\\wp-content\\plugins\\MCBA-Wordpress"' )});
ipcMain.on( 'test-folder',                     () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\june\\4th_week\\test_folder"' )});
ipcMain.on( 'tennis-cpp',                      () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\june\\2nd_week\\tennis_cpp"' )});
ipcMain.on( 'library-transfer',                () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\june\\2nd_week\\libraries"' )});
ipcMain.on( 'tennis-view',                     () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\april\\5th_week\\electron-quick-start"' )});
ipcMain.on( 'vanilla-web',                     () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\july\\3rd_week\\vanilla_web_component"' )});
ipcMain.on( 'vue-node-chat-app',               () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\july\\4th_week\\vue-node-chatapp\\parsingTools"' )});
ipcMain.on( 'local-php-api',                   () => { child_process.exec( 'start "" "C:\\Users\\EG\\local-php-api"' )});
ipcMain.on( 'monitored-object-js',             () => { child_process.exec( 'start "" "C:\\Users\\EG\\Desktop\\2022\\august\\3rd_week\\monitored-object-js"' )});
