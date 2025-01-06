import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Dialogs
import QtWebEngine


ApplicationWindow {
    visible: true
    width: 400
    height: 400
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
        anchors.fill: parent
        url: "file:///C:/Users/USER/Documents/GitHub/EReader/EReader/iframe.html"

    }

    FileDialog {
        id: openDialog
        nameFilters: ["*.epub"]
        currentFolder: "file:///C:/"
        onAccepted: users_epub_file = selectedFile
    }

}
