import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Dialogs
import QtWebEngine


ApplicationWindow {
    visible: true
    width: 920
    height: 600
    title: "Ereader"

    property string users_epub_file

    menuBar: MenuBar {
        Menu {
            title: "&File " + users_epub_file

            Action {
                text: "Open"
                onTriggered: openDialog.open()
            }
        }
    }

    WebEngineView {
        id: webEngine
        anchors.fill: parent
        url: "file:///C:/Users/USER/Documents/GitHub/EReader/EReader/reader_files/reader.html"

    }

    FileDialog {
        id: openDialog
        nameFilters: ["*.epub"]
        currentFolder: "file:///C:/"
        onAccepted: users_epub_file = selectedFile
    }

}
