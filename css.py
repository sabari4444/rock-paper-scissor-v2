"""
QLabel#scoreBoard {
    font-family: 'k2d Light';
    font-size: 16px;
    background-color: lightblue;
    border-radius: 15px;
}

QPushButton::hover {
    background: #fff;
    }
QPushButton#start::hover {
    background-color : #fff;
}

"""

btn= """
background-image : url(Resoures/{path});
background-repeat: no-repeat;
background-position: center;
border-radius: 10px;
padding: 4px;
"""

backgroundCSS = """
    background: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 1,
        stop: 0 #FFAE8B,
        stop: 1 #DF5A72 );
"""
playAreaCSS = """
    background-color: skyblue;
    border-radius: 20px;
"""

scoreBannerCSS = """
    background-color: #D9D9D9;
    border-radius: 10px;
"""

choicePlayAreaCSS = """
    background-color : #FFF;
    border-radius: 20px;

"""
nameTagCSS = """
    font-family: 'k2d Light';
    font-size: 14px;
    border-radius : 10px;
    background-color: pink;
"""

choiceDefault = """
    background-image : url(Resoures/{path});
    background-repeat: no-repeat;
    background-position: center;
    border-radius: 10px;
    padding: 4px;
"""