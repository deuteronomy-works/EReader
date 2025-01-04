import QtQuick
import QtQuick.Controls.Basic
//import QtWebEngine

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    title: "Ereader"

    /*WebEngineView {
        anchors.fill: parent
        url: "file:///C:/Users/USER/Documents/GitHub/EReader/EReader/index.xhtml"

    }*/

    TreeView {
        width: 200
        height: 200
        model: ListModel {
            ListElement {
                name: "l"
                children: [ListElement{name: "ll"}]
            }
            ListElement {
                name: "l2"
            }
        }

        delegate: TreeViewDelegate {} /*Rectangle {
            width: 200
            height: 20
            color: "gold"

            Text {
                text:index
            }

        }*/
    }


}
