import QtQuick
import QtQuick.Controls.Basic
import QtWebEngine

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    title: "Ereader"

    WebEngineView {
        anchors.fill: parent
        url: "file:///C:/Users/USER/Documents/GitHub/EReader/EReader/iframe.html"

    }

    /*WebEngineView {
        anchors.fill: parent
        url: ""
    }*/


}
