# use qt resource to replace in the future
class styleSheets():
    AMOLED = """
QMainWindow {
	background-color:#000000;
}
QDialog {
	background-color:#000000;
}
QColorDialog {
	background-color:#000000;
}
QTextEdit {
	background-color:#000000;
	color: #a9b7c6;
}
QPlainTextEdit {
	selection-background-color:#f39c12;
	background-color:#000000;
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-width: 1px;
	color: #a9b7c6;
}
QPushButton{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding: 2px;
	background-color: #000000;
}
QPushButton::default{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #e67e22;
	border-width: 1px;
	color: #a9b7c6;
	padding: 2px;
	background-color: #000000;
}
QPushButton:hover{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #e67e22;
	border-bottom-width: 1px;
	border-bottom-radius: 6px;
	border-style: solid;
	color: #FFFFFF;
	padding-bottom: 2px;
	background-color: #000000;
}
QPushButton:pressed{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #e67e22;
	border-bottom-width: 2px;
	border-bottom-radius: 6px;
	border-style: solid;
	color: #e67e22;
	padding-bottom: 1px;
	background-color: #000000;
}
QPushButton:disabled{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 2px;
	border-bottom-radius: 6px;
	border-style: solid;
	color: #808086;
	padding-bottom: 1px;
	background-color: #000000;
}
QToolButton {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #e67e22;
	border-bottom-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding: 2px;
	background-color: #000000;
}
QToolButton:hover{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #e67e22;
	border-bottom-width: 2px;
	border-bottom-radius: 6px;
	border-style: solid;
	color: #FFFFFF;
	padding-bottom: 1px;
	background-color: #000000;
}
QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	padding: 0 8px;
	color: #a9b7c6;
	background:#000000;
	selection-background-color:#007b50;
	selection-color: #FFFFFF;
}
QLabel {
	color: #a9b7c6;
}
QLCDNumber {
	color: #e67e22;
}
QProgressBar {
	text-align: center;
	color: rgb(240, 240, 240);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	background-color:#000000;
}
QProgressBar::chunk {
	background-color: #e67e22;
	border-radius: 5px;
}
QMenu{
	background-color:#000000;
}
QMenuBar {
	background:rgb(0, 0, 0);
	color: #a9b7c6;
}
QMenuBar::item {
  	spacing: 3px; 
	padding: 1px 4px;
  	background: transparent;
}
QMenuBar::item:selected { 
  	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #e67e22;
	border-bottom-width: 1px;
	border-bottom-radius: 6px;
	border-style: solid;
	color: #FFFFFF;
	padding-bottom: 0px;
	background-color: #000000;
}
QMenu::item:selected {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: #e67e22;
	border-bottom-color: transparent;
	border-left-width: 2px;
	color: #FFFFFF;
	padding-left:15px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	background-color:#000000;
}
QMenu::item {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding-left:17px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	background-color:#000000;
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:#000000;
}
QTabWidget::pane {
		border-color: rgb(77,77,77);
		background-color:#000000;
		border-style: solid;
		border-width: 1px;
    	border-radius: 6px;
}
QTabBar::tab {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	border-style: solid;
	color: #808086;
	padding: 3px;
	margin-left:3px;
	background-color:#000000;
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #e67e22;
	border-bottom-width: 2px;
	border-style: solid;
	color: #FFFFFF;
	padding-left: 3px;
	padding-bottom: 2px;
	margin-left:3px;
	background-color:#000000;
}

QCheckBox {
	color: #a9b7c6;
	padding: 2px;
}
QCheckBox:disabled {
	color: #808086;
	padding: 2px;
}

QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: rgb(87, 97, 106);
	background-color:#000000;
}
QCheckBox::indicator:checked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #e67e22;
	color: #a9b7c6;
	background-color: #e67e22;
}
QCheckBox::indicator:unchecked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #e67e22;
	color: #a9b7c6;
	background-color: transparent;
}
QRadioButton {
	color: #a9b7c6;
	background-color:#000000;
	padding: 1px;
}
QRadioButton::indicator:checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #e67e22;
	color: #a9b7c6;
	background-color: #e67e22;
}
QRadioButton::indicator:!checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #e67e22;
	color: #a9b7c6;
	background-color: transparent;
}
QStatusBar {
	color:#027f7f;
}
QSpinBox {
	color: #a9b7c6;	
	background-color:#000000;
}
QDoubleSpinBox {
	color: #a9b7c6;	
	background-color:#000000;
}
QTimeEdit {
	color: #a9b7c6;	
	background-color:#000000;
}
QDateTimeEdit {
	color: #a9b7c6;	
	background-color:#000000;
}
QDateEdit {
	color: #a9b7c6;	
	background-color:#000000;
}
QComboBox {
	color: #a9b7c6;	
	background: #1e1d23;
}
QComboBox:editable {
	background: #1e1d23;
	color: #a9b7c6;
	selection-background-color:#000000;
}
QComboBox QAbstractItemView {
	color: #a9b7c6;	
	background: #1e1d23;
	selection-color: #FFFFFF;
	selection-background-color:#000000;
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
	color: #a9b7c6;	
	background: #1e1d23;
}
QFontComboBox {
	color: #a9b7c6;	
	background-color:#000000;
}
QToolBox {
	color: #a9b7c6;
	background-color:#000000;
}
QToolBox::tab {
	color: #a9b7c6;
	background-color:#000000;
}
QToolBox::tab:selected {
	color: #FFFFFF;
	background-color:#000000;
}
QScrollArea {
	color: #FFFFFF;
	background-color:#000000;
}
QSlider::groove:horizontal {
	height: 5px;
	background: #e67e22;
}
QSlider::groove:vertical {
	width: 5px;
	background: #e67e22;
}
QSlider::handle:horizontal {
	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
	border: 1px solid #5c5c5c;
	width: 14px;
	margin: -5px 0;
	border-radius: 7px;
}
QSlider::handle:vertical {
	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);
	border: 1px solid #5c5c5c;
	height: 14px;
	margin: 0 -5px;
	border-radius: 7px;
}
QSlider::add-page:horizontal {
    background: white;
}
QSlider::add-page:vertical {
    background: white;
}
QSlider::sub-page:horizontal {
    background: #e67e22;
}
QSlider::sub-page:vertical {
    background: #e67e22;
}
QScrollBar:horizontal {
	max-height: 20px;
	background: rgb(0,0,0);
	border: 1px transparent grey;
	margin: 0px 20px 0px 20px;
}
QScrollBar::handle:horizontal {
	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));
	border-style: solid;
	border-width: 1px;
	border-color: rgb(0,0,0);
	min-width: 25px;
}
QScrollBar::handle:horizontal:hover {
	background: rgb(230, 126, 34);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(0,0,0);
	min-width: 25px;
}
QScrollBar::add-line:horizontal {
  	border: 1px solid;
  	border-color: rgb(0,0,0);
  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));
  	width: 20px;
  	subcontrol-position: right;
  	subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:hover {
  	border: 1px solid;
  	border-color: rgb(0,0,0);
	border-radius: 8px;
  	background: rgb(230, 126, 34);
  	height: 16px;
  	width: 16px;
  	subcontrol-position: right;
  	subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:pressed {
  	border: 1px solid;
  	border-color: grey;
	border-radius: 8px;
  	background: rgb(230, 126, 34);
  	height: 16px;
  	width: 16px;
  	subcontrol-position: right;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
  	border: 1px solid;
  	border-color: rgb(0,0,0);
  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));
  	width: 20px;
  	subcontrol-position: left;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:hover {
  	border: 1px solid;
  	border-color: rgb(0,0,0);
	border-radius: 8px;
  	background: rgb(230, 126, 34);
  	height: 16px;
  	width: 16px;
  	subcontrol-position: left;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:pressed {
  	border: 1px solid;
  	border-color: grey;
	border-radius: 8px;
  	background: rgb(230, 126, 34);
  	height: 16px;
  	width: 16px;
  	subcontrol-position: left;
  	subcontrol-origin: margin;
}
QScrollBar::left-arrow:horizontal {
  	border: 1px transparent grey;
  	border-radius: 3px;
  	width: 6px;
  	height: 6px;
 	background: rgb(0,0,0);
}
QScrollBar::right-arrow:horizontal {
	border: 1px transparent grey;
	border-radius: 3px;
  	width: 6px;
  	height: 6px;
 	background: rgb(0,0,0);
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
 	background: none;
} 
QScrollBar:vertical {
	max-width: 20px;
	background: rgb(0,0,0);
	border: 1px transparent grey;
	margin: 20px 0px 20px 0px;
}
QScrollBar::add-line:vertical {
	border: 1px solid;
  	border-color: rgb(0,0,0);
  	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));
  	height: 20px;
  	subcontrol-position: bottom;
  	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover {
  	border: 1px solid;
  	border-color: rgb(0,0,0);
	border-radius: 8px;
  	background: rgb(230, 126, 34);
  	height: 16px;
  	width: 16px;
  	subcontrol-position: bottom;
  	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:pressed {
  	border: 1px solid;
  	border-color: grey;
	border-radius: 8px;
  	background: rgb(230, 126, 34);
  	height: 16px;
  	width: 16px;
  	subcontrol-position: bottom;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
  	border: 1px solid;
  	border-color: rgb(0,0,0);
	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));
  	height: 20px;
  	subcontrol-position: top;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover {
  	border: 1px solid;
  	border-color: rgb(0,0,0);
	border-radius: 8px;
  	background: rgb(230, 126, 34);
  	height: 16px;
  	width: 16px;
  	subcontrol-position: top;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:pressed {
  	border: 1px solid;
  	border-color: grey;
	border-radius: 8px;
  	background: rgb(230, 126, 34);
  	height: 16px;
  	width: 16px;
  	subcontrol-position: top;
  	subcontrol-origin: margin;
}
	QScrollBar::handle:vertical {
	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));
	border-style: solid;
	border-width: 1px;
	border-color: rgb(0,0,0);
	min-height: 25px;
}
QScrollBar::handle:vertical:hover {
	background: rgb(230, 126, 34);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(0,0,0);
	min-heigth: 25px;
}
QScrollBar::up-arrow:vertical {
	border: 1px transparent grey;
	border-radius: 3px;
  	width: 6px;
  	height: 6px;
 	background: rgb(0,0,0);
}
QScrollBar::down-arrow:vertical {
  	border: 1px transparent grey;
  	border-radius: 3px;
  	width: 6px;
  	height: 6px;
 	background: rgb(0,0,0);
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
  	background: none;
}
"""
    aqua="""
QMainWindow {
	background-color:#ececec;
}
QTextEdit {
	border-width: 1px;
	border-style: solid;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QPlainTextEdit {
	border-width: 1px;
	border-style: solid;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QToolButton {
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QToolButton:hover{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QToolButton:pressed{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(142,142,142);
}
QPushButton{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QPushButton::default{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QPushButton:hover{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QPushButton:pressed{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(142,142,142);
}
QPushButton:disabled{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: #808086;
	padding: 2px;
	background-color: rgb(142,142,142);
}
QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-style: solid;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QLabel {
	color: #000000;
}
QLCDNumber {
	color: rgb(0, 113, 255, 255);
}
QProgressBar {
	text-align: center;
	color: rgb(240, 240, 240);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(230, 230, 230);
	border-style: solid;
	background-color:rgb(207,207,207);
}
QProgressBar::chunk {
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
	border-radius: 10px;
}
QMenuBar {
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));
}
QMenuBar::item {
	color: #000000;
  	spacing: 3px;
  	padding: 1px 4px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));
}

QMenuBar::item:selected {
  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #FFFFFF;
}
QMenu::item:selected {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	border-bottom-color: transparent;
	border-left-width: 2px;
	color: #000000;
	padding-left:15px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
}
QMenu::item {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	color: #000000;
	padding-left:17px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:#000000;
}
QTabWidget::pane {
		border-color: rgb(223,223,223);
		background-color:rgb(226,226,226);
		border-style: solid;
		border-width: 2px;
    	border-radius: 6px;
}
QTabBar::tab:first {
	border-style: solid;
	border-left-width:1px;
	border-right-width:0px;
	border-top-width:1px;
	border-bottom-width:1px;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	border-top-left-radius: 4px;
	border-bottom-left-radius: 4px;
	color: #000000;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));
}
QTabBar::tab:last {
	border-style: solid;
	border-width:1px;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	border-top-right-radius: 4px;
	border-bottom-right-radius: 4px;
	color: #000000;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));
}
QTabBar::tab {
	border-style: solid;
	border-top-width:1px;
	border-bottom-width:1px;
	border-left-width:1px;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	color: #000000;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	border-style: solid;
  	border-left-width:1px;
	border-right-color: transparent;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	color: #FFFFFF;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}

QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {
  	border-style: solid;
  	border-left-width:1px;
  	border-bottom-width:1px;
  	border-top-width:1px;
	border-right-color: transparent;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	color: #FFFFFF;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}

QCheckBox {
	color: #000000;
	padding: 2px;
}
QCheckBox:disabled {
	color: #808086;
	padding: 2px;
}

QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: transparent;
}
QCheckBox::indicator:checked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #000000;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QCheckBox::indicator:unchecked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #000000;
}
QRadioButton {
	color: 000000;
	padding: 1px;
}
QRadioButton::indicator:checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #a9b7c6;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QRadioButton::indicator:!checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #a9b7c6;
	background-color: transparent;
}
QStatusBar {
	color:#027f7f;
}
QSpinBox {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QDoubleSpinBox {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QTimeEdit {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QDateTimeEdit {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QDateEdit {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}

QToolBox {
	color: #a9b7c6;
	background-color:#000000;
}
QToolBox::tab {
	color: #a9b7c6;
	background-color:#000000;
}
QToolBox::tab:selected {
	color: #FFFFFF;
	background-color:#000000;
}
QScrollArea {
	color: #FFFFFF;
	background-color:#000000;
}
QSlider::groove:horizontal {
	height: 5px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
}
QSlider::groove:vertical {
	width: 5px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
}
QSlider::handle:horizontal {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	width: 12px;
	margin: -5px 0;
	border-radius: 7px;
}
QSlider::handle:vertical {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	height: 12px;
	margin: 0 -5px;
	border-radius: 7px;
}
QSlider::add-page:horizontal {
    background: rgb(181,181,181);
}
QSlider::add-page:vertical {
    background: rgb(181,181,181);
}
QSlider::sub-page:horizontal {
    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
}
QSlider::sub-page:vertical {
    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
}
QScrollBar:horizontal {
	max-height: 20px;
	border: 1px transparent grey;
	margin: 0px 20px 0px 20px;
}
QScrollBar:vertical {
	max-width: 20px;
	border: 1px transparent grey;
	margin: 20px 0px 20px 0px;
}
QScrollBar::handle:horizontal {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	border-radius: 7px;
	min-width: 25px;
}
QScrollBar::handle:horizontal:hover {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(147, 200, 200);
	border-radius: 7px;
	min-width: 25px;
}
QScrollBar::handle:vertical {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	border-radius: 7px;
	min-height: 25px;
}
QScrollBar::handle:vertical:hover {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(147, 200, 200);
	border-radius: 7px;
	min-height: 25px;
}
QScrollBar::add-line:horizontal {
   border: 2px transparent grey;
   border-top-right-radius: 7px;
   border-bottom-right-radius: 7px;
   background: rgba(34, 142, 255, 255);
   width: 20px;
   subcontrol-position: right;
   subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:pressed {
   border: 2px transparent grey;
   border-top-right-radius: 7px;
   border-bottom-right-radius: 7px;
   background: rgb(181,181,181);
   width: 20px;
   subcontrol-position: right;
   subcontrol-origin: margin;
}
QScrollBar::add-line:vertical {
   border: 2px transparent grey;
   border-bottom-left-radius: 7px;
   border-bottom-right-radius: 7px;
   background: rgba(34, 142, 255, 255);
   height: 20px;
   subcontrol-position: bottom;
   subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:pressed {
   border: 2px transparent grey;
   border-bottom-left-radius: 7px;
   border-bottom-right-radius: 7px;
   background: rgb(181,181,181);
   height: 20px;
   subcontrol-position: bottom;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
   border: 2px transparent grey;
   border-top-left-radius: 7px;
   border-bottom-left-radius: 7px;
   background: rgba(34, 142, 255, 255);
   width: 20px;
   subcontrol-position: left;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:pressed {
   border: 2px transparent grey;
   border-top-left-radius: 7px;
   border-bottom-left-radius: 7px;
   background: rgb(181,181,181);
   width: 20px;
   subcontrol-position: left;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
   border: 2px transparent grey;
   border-top-left-radius: 7px;
   border-top-right-radius: 7px;
   background: rgba(34, 142, 255, 255);
   height: 20px;
   subcontrol-position: top;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:pressed {
   border: 2px transparent grey;
   border-top-left-radius: 7px;
   border-top-right-radius: 7px;
   background: rgb(181,181,181);
   height: 20px;
   subcontrol-position: top;
   subcontrol-origin: margin;
}
QScrollBar::left-arrow:horizontal {
   border: 1px transparent grey;
   border-top-left-radius: 3px;
   border-bottom-left-radius: 3px;
   width: 6px;
   height: 6px;
   background: white;
}
QScrollBar::right-arrow:horizontal {
   border: 1px transparent grey;
   border-top-right-radius: 3px;
   border-bottom-right-radius: 3px;
   width: 6px;
   height: 6px;
   background: white;
}
QScrollBar::up-arrow:vertical {
   border: 1px transparent grey;
   border-top-left-radius: 3px;
   border-top-right-radius: 3px;
   width: 6px;
   height: 6px;
   background: white;
}
QScrollBar::down-arrow:vertical {
   border: 1px transparent grey;
   border-bottom-left-radius: 3px;
   border-bottom-right-radius: 3px;
   width: 6px;
   height: 6px;
   background: white;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
   background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
   background: none;
}
"""
    ConsoleStyle="""
QWidget {
	background-color:rgb(0, 0, 0);
	color: rgb(240, 240, 240);
	border-color: rgb(58, 58, 58);
}

QPlainTextEdit {
	background-color:rgb(0, 0, 0);
	color: rgb(200, 200, 200);
	selection-background-color: rgb(255, 153, 0);
	selection-color: rgb(0, 0, 0);
}

QTabWidget::pane {
    	border-top: 1px solid #000000;
}

QTabBar::tab {
 	background-color:rgb(0, 0, 0);
 	border-style: outset;
	border-width: 1px;
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
  border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-top-width: 0px;
	border-style: solid;
	color: rgb(255, 153, 0);
	padding: 4px;
}

QTabBar::tab:selected, QTabBar::tab:hover {
   color: rgb(255, 255, 255);
   background-color:rgb(0, 0, 0);
   border-color:rgb(42, 42, 42);
   margin-left: 0px;
   margin-right: 0px;
   border-bottom-right-radius:4px;
   border-bottom-left-radius:4px;
}

QTabBar::tab:last:selected {
  background-color:rgb(0, 0, 0);
	border-color:rgb(42, 42, 42);
	margin-left: 0px;
  	margin-right: 0px;
	border-bottom-right-radius:4px;
	border-bottom-left-radius:4px;
}

QTabBar::tab:!selected {
   margin-bottom: 4px;
   border-bottom-right-radius:4px;
   border-bottom-left-radius:4px;
}

QPushButton{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 6px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
}

QPushButton:hover{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-bottom-color: rgb(115, 115, 115);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 6px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));
}

QPushButton:pressed{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 6px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
}

QPushButton:disabled{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(0, 0, 0);
	padding: 6px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));
}

QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	padding: 0 8px;
	color: rgb(255, 255, 255);
	background:rgb(101, 101, 101);
	selection-background-color: rgb(187, 187, 187);
	selection-color: rgb(60, 63, 65);
}

QProgressBar {
	text-align: center;
	color: rgb(255, 255, 255);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
}

QProgressBar::chunk {
	background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(0, 200, 0, 255), stop:1 rgba(30, 230, 30, 255));
	border-radius: 10px;
}

QMenuBar {
	background:rgb(0, 0, 0);
	color: rgb(255, 153, 0);
}

QMenuBar::item {
  	spacing: 3px; 
	padding: 1px 4px;
  	background: transparent;
}

QMenuBar::item:selected { 
  	background:rgb(115, 115, 115);
}

QMenu {
	border-width: 2px; 
	border-radius: 10px;
	border-color: rgb(255, 153, 0);
	border-style: outset;
}

QMenu::item {
	spacing: 3px; 
	padding: 3px 15px;
}

QMenu::item:selected {
	spacing: 3px; 
	padding: 3px 15px;
	background:rgb(115, 115, 115);
	color:rgb(255, 255, 255);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
}
"""
    ElegantDark="""
QMainWindow {
	background-color:rgb(82, 82, 82);
}
QTextEdit {
	background-color:rgb(42, 42, 42);
	color: rgb(0, 255, 0);
}
QPushButton{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
}
QPushButton:hover{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-bottom-color: rgb(115, 115, 115);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));
}
QPushButton:pressed{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
}
QPushButton:disabled{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(0, 0, 0);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));
}
QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	padding: 0 8px;
	color: rgb(255, 255, 255);
	background:rgb(100, 100, 100);
	selection-background-color: rgb(187, 187, 187);
	selection-color: rgb(60, 63, 65);
}
QLabel {
	color:rgb(255,255,255);	
}
QProgressBar {
	text-align: center;
	color: rgb(240, 240, 240);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	background-color:rgb(77,77,77);
}
QProgressBar::chunk {
	background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));
	border-radius: 5px;
}
QMenuBar {
	background:rgb(82, 82, 82);
}
QMenuBar::item {
	color:rgb(223,219,210);
	spacing: 3px;
	padding: 1px 4px;
	background: transparent;
}

QMenuBar::item:selected {
	background:rgb(115, 115, 115);
}
QMenu::item:selected {
	color:rgb(255,255,255);
	border-width:2px;
	border-style:solid;
	padding-left:18px;
	padding-right:8px;
	padding-top:2px;
	padding-bottom:3px;
	background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
}
QMenu::item {
	color:rgb(223,219,210);
	background-color:rgb(78,78,78);
	padding-left:20px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:10px;
}
QMenu{
	background-color:rgb(78,78,78);
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:rgb(247,246,246);
}
QTabWidget::pane {
		border-color: rgb(77,77,77);
		background-color:rgb(101,101,101);
		border-style: solid;
		border-width: 1px;
    	border-radius: 6px;
}
QTabBar::tab {
	padding:2px;
	color:rgb(250,250,250);
  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
	border-style: solid;
	border-width: 2px;
  	border-top-right-radius:4px;
   border-top-left-radius:4px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));
	border-bottom-color: rgb(101,101,101);
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	background-color:rgb(101,101,101);
  	margin-left: 0px;
  	margin-right: 1px;
}
QTabBar::tab:!selected {
    	margin-top: 1px;
		margin-right: 1px;
}
QCheckBox {
	color:rgb(223,219,210);
	padding: 2px;
}
QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: rgb(87, 97, 106);
	background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));
}
QCheckBox::indicator:checked {
	border-radius:4px;
	border-style:solid;
	border-width:1px;
	border-color: rgb(180,180,180);
  	background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));
}
QCheckBox::indicator:unchecked {
	border-radius:4px;
	border-style:solid;
	border-width:1px;
	border-color: rgb(87, 97, 106);
  	background-color:rgb(255,255,255);
}
QStatusBar {
	color:rgb(240,240,240);
}
"""
    ManjaroMix="""
QMainWindow {
	background-color:#151a1e;
}
QCalendar {
	background-color: #151a1e;
}
QTextEdit {
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
	background-color: #222b2e;
	color: #d3dae3;
}
QPlainTextEdit {
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
	background-color: #222b2e;
	color: #d3dae3;
}
QToolButton {
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: #d3dae3;
	padding: 2px;
	background-color: rgb(255,255,255);
}
QToolButton:hover{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QToolButton:pressed{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(142,142,142);
}
QPushButton{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #d3dae3;
	padding: 2px;
	background-color: #151a1e;
}
QPushButton::default{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #FFFFFF;
	padding: 2px;
	background-color: #151a1e;;
}
QPushButton:hover{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #d3dae3;
	padding: 2px;
	background-color: #1c1f1f;
}
QPushButton:pressed{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #d3dae3;
	padding: 2px;
	background-color: #2c2f2f;
}
QPushButton:disabled{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: #808086;
	padding: 2px;
	background-color: rgb(142,142,142);
}
QLineEdit {
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
	background-color: #222b2e;
	color: #d3dae3;
}
QLabel {
	color: #d3dae3;
}
QLCDNumber {
	color: #4d9b87;
}
QProgressBar {
	text-align: center;
	color: #d3dae3;
	border-radius: 10px;
	border-color: transparent;
	border-style: solid;
	background-color: #52595d;
}
QProgressBar::chunk {
	background-color: #214037	;
	border-radius: 10px;
}
QMenuBar {
	background-color: #151a1e;
}
QMenuBar::item {
	color: #d3dae3;
  	spacing: 3px;
  	padding: 1px 4px;
	background-color: #151a1e;
}

QMenuBar::item:selected {
  	background-color: #252a2e;
	color: #FFFFFF;
}
QMenu {
	background-color: #151a1e;
}
QMenu::item:selected {
	background-color: #252a2e;
	color: #FFFFFF;
}
QMenu::item {
	color: #d3dae3;
	background-color: #151a1e;
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:#000000;
}
QTabWidget::pane {
		border-color: #050a0e;
		background-color: #1e282c;
		border-style: solid;
		border-width: 1px;
    	border-bottom-left-radius: 4px;
		border-bottom-right-radius: 4px;
}
QTabBar::tab:first {
	border-style: solid;
	border-left-width:1px;
	border-right-width:0px;
	border-top-width:1px;
	border-bottom-width:0px;
	border-top-color: #050a0e;
	border-left-color: #050a0e;
	border-bottom-color: #050a0e;
	border-top-left-radius: 4px;
	color: #d3dae3;
	padding: 3px;
	margin-left:0px;
	background-color: #151a1e;
}
QTabBar::tab:last {
	border-style: solid;
	border-top-width:1px;
	border-left-width:1px;
	border-right-width:1px;
	border-bottom-width:0px;
	border-color: #050a0e;
	border-top-right-radius: 4px;
	color: #d3dae3;
	padding: 3px;
	margin-left:0px;
	background-color: #151a1e;
}
QTabBar::tab {
	border-style: solid;
	border-top-width:1px;
	border-bottom-width:0px;
	border-left-width:1px;
	border-top-color: #050a0e;
	border-left-color: #050a0e;
	border-bottom-color: #050a0e;
	color: #d3dae3;
	padding: 3px;
	margin-left:0px;
	background-color: #151a1e;
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	border-style: solid;
  	border-left-width:1px;
	border-bottom-width:0px;
	border-right-color: transparent;
	border-top-color: #050a0e;
	border-left-color: #050a0e;
	border-bottom-color: #050a0e;
	color: #FFFFFF;
	padding: 3px;
	margin-left:0px;
	background-color: #1e282c;
}

QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {
  	border-style: solid;
  	border-left-width:1px;
  	border-bottom-width:0px;
  	border-top-width:1px;
	border-right-color: transparent;
	border-top-color: #050a0e;
	border-left-color: #050a0e;
	border-bottom-color: #050a0e;
	color: #FFFFFF;
	padding: 3px;
	margin-left:0px;
	background-color: #1e282c;
}

QCheckBox {
	color: #d3dae3;
	padding: 2px;
}
QCheckBox:disabled {
	color: #808086;
	padding: 2px;
}

QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: transparent;
}
QCheckBox::indicator:checked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #4fa08b;
	color: #000000;
	background-color: qradialgradient(cx:0.4, cy:0.4, radius: 1.5,fx:0, fy:0, stop:0 #1e282c, stop:0.3 #1e282c, stop:0.4 #4fa08b, stop:0.5 #1e282c, stop:1 #1e282c);
}
QCheckBox::indicator:unchecked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #4fa08b;
	color: #000000;
}
QRadioButton {
	color: #d3dae3;
	padding: 1px;
}
QRadioButton::indicator:checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #4fa08b;
	color: #a9b7c6;
	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #4fa08b, stop:1 #1e282c);
}
QRadioButton::indicator:!checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #4fa08b;
	color: #a9b7c6;
	background-color: transparent;
}
QStatusBar {
	color:#027f7f;
}
QSpinBox {
	color: #d3dae3;
	background-color: #222b2e;
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
}
QDoubleSpinBox {
	color: #d3dae3;
	background-color: #222b2e;
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
}
QTimeEdit {
	color: #d3dae3;
	background-color: #222b2e;
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
}
QDateTimeEdit {
	color: #d3dae3;
	background-color: #222b2e;
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
}
QDateEdit {
	color: #d3dae3;
	background-color: #222b2e;
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
}
QFontComboBox {
	color: #d3dae3;
	background-color: #222b2e;
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
}
QComboBox {
	color: #d3dae3;
	background-color: #222b2e;
	border-width: 1px;
	border-style: solid;
	border-color: #4fa08b;
}

QDial {
	background: #16a085;
}

QToolBox {
	color: #a9b7c6;
	background-color: #222b2e;
}
QToolBox::tab {
	color: #a9b7c6;
	background-color:#222b2e;
}
QToolBox::tab:selected {
	color: #FFFFFF;
	background-color:#222b2e;
}
QScrollArea {
	color: #FFFFFF;
	background-color:#222b2e;
}
QSlider::groove:horizontal {
	height: 5px;
	background-color: #52595d;
}
QSlider::groove:vertical {
	width: 5px;
	background-color: #52595d;
}
QSlider::handle:horizontal {
	background: #1a2224;
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	width: 12px;
	margin: -5px 0;
	border-radius: 7px;
}
QSlider::handle:vertical {
	background: #1a2224;
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	height: 12px;
	margin: 0 -5px;
	border-radius: 7px;
}
QSlider::add-page:horizontal {
    background: #52595d;
}
QSlider::add-page:vertical {
    background: #52595d;
}
QSlider::sub-page:horizontal {
    background-color: #15433a;
}
QSlider::sub-page:vertical {
    background-color: #15433a;
}
QScrollBar:horizontal {
	max-height: 10px;
	border: 1px transparent grey;
	margin: 0px 20px 0px 20px;
	background: transparent;
}
QScrollBar:vertical {
	max-width: 10px;
	border: 1px transparent grey;
	margin: 20px 0px 20px 0px;
	background: transparent;
}
QScrollBar::handle:horizontal {
	background: #52595d;
	border-style: transparent;
	border-radius: 4px;
	min-width: 25px;
}
QScrollBar::handle:horizontal:hover {
	background: #58a492;
	border-style: transparent;
	border-radius: 4px;
	min-width: 25px;
}
QScrollBar::handle:vertical {
	background: #52595d;
	border-style: transparent;
	border-radius: 4px;
	min-height: 25px;
}
QScrollBar::handle:vertical:hover {
	background: #58a492;
	border-style: transparent;
	border-radius: 4px;
	min-height: 25px;
}
QScrollBar::add-line:horizontal {
   border: 2px transparent grey;
   border-top-right-radius: 4px;
   border-bottom-right-radius: 4px;
   background: #15433a;
   width: 20px;
   subcontrol-position: right;
   subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:pressed {
   border: 2px transparent grey;
   border-top-right-radius: 4px;
   border-bottom-right-radius: 4px;
   background: rgb(181,181,181);
   width: 20px;
   subcontrol-position: right;
   subcontrol-origin: margin;
}
QScrollBar::add-line:vertical {
   border: 2px transparent grey;
   border-bottom-left-radius: 4px;
   border-bottom-right-radius: 4px;
   background: #15433a;
   height: 20px;
   subcontrol-position: bottom;
   subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:pressed {
   border: 2px transparent grey;
   border-bottom-left-radius: 4px;
   border-bottom-right-radius: 4px;
   background: rgb(181,181,181);
   height: 20px;
   subcontrol-position: bottom;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
   border: 2px transparent grey;
   border-top-left-radius: 4px;
   border-bottom-left-radius: 4px;
   background: #15433a;
   width: 20px;
   subcontrol-position: left;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:pressed {
   border: 2px transparent grey;
   border-top-left-radius: 4px;
   border-bottom-left-radius: 4px;
   background: rgb(181,181,181);
   width: 20px;
   subcontrol-position: left;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
   border: 2px transparent grey;
   border-top-left-radius: 4px;
   border-top-right-radius: 4px;
   background: #15433a;
   height: 20px;
   subcontrol-position: top;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:pressed {
   border: 2px transparent grey;
   border-top-left-radius: 4px;
   border-top-right-radius: 4px;
   background: rgb(181,181,181);
   height: 20px;
   subcontrol-position: top;
   subcontrol-origin: margin;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
   background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
   background: none;
}
"""
    MaterialDark="""
QMainWindow {
	background-color:#1e1d23;
}
QDialog {
	background-color:#1e1d23;
}
QColorDialog {
	background-color:#1e1d23;
}
QTextEdit {
	background-color:#1e1d23;
	color: #a9b7c6;
}
QPlainTextEdit {
	selection-background-color:#007b50;
	background-color:#1e1d23;
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-width: 1px;
	color: #a9b7c6;
}
QPushButton{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding: 2px;
	background-color: #1e1d23;
}
QPushButton::default{
	border-style: inset;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #04b97f;
	border-width: 1px;
	color: #a9b7c6;
	padding: 2px;
	background-color: #1e1d23;
}
QToolButton {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #04b97f;
	border-bottom-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding: 2px;
	background-color: #1e1d23;
}
QToolButton:hover{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #37efba;
	border-bottom-width: 2px;
	border-style: solid;
	color: #FFFFFF;
	padding-bottom: 1px;
	background-color: #1e1d23;
}
QPushButton:hover{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #37efba;
	border-bottom-width: 1px;
	border-style: solid;
	color: #FFFFFF;
	padding-bottom: 2px;
	background-color: #1e1d23;
}
QPushButton:pressed{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #37efba;
	border-bottom-width: 2px;
	border-style: solid;
	color: #37efba;
	padding-bottom: 1px;
	background-color: #1e1d23;
}
QPushButton:disabled{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #808086;
	border-bottom-width: 2px;
	border-style: solid;
	color: #808086;
	padding-bottom: 1px;
	background-color: #1e1d23;
}
QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	padding: 0 8px;
	color: #a9b7c6;
	background:#1e1d23;
	selection-background-color:#007b50;
	selection-color: #FFFFFF;
}
QLabel {
	color: #a9b7c6;
}
QLCDNumber {
	color: #37e6b4;
}
QProgressBar {
	text-align: center;
	color: rgb(240, 240, 240);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	background-color:#1e1d23;
}
QProgressBar::chunk {
	background-color: #04b97f;
	border-radius: 5px;
}
QMenuBar {
	background-color: #1e1d23;
}
QMenuBar::item {
	color: #a9b7c6;
  	spacing: 3px;
  	padding: 1px 4px;
  	background: #1e1d23;
}

QMenuBar::item:selected {
  	background:#1e1d23;
	color: #FFFFFF;
}
QMenu::item:selected {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: #04b97f;
	border-bottom-color: transparent;
	border-left-width: 2px;
	color: #FFFFFF;
	padding-left:15px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	background-color: #1e1d23;
}
QMenu::item {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding-left:17px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	background-color: #1e1d23;
}
QMenu{
	background-color:#1e1d23;
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:#1e1d23;
}
QTabWidget::pane {
		border-color: rgb(77,77,77);
		background-color:#1e1d23;
		border-style: solid;
		border-width: 1px;
    	border-radius: 6px;
}
QTabBar::tab {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	border-style: solid;
	color: #808086;
	padding: 3px;
	margin-left:3px;
	background-color: #1e1d23;
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #04b97f;
	border-bottom-width: 2px;
	border-style: solid;
	color: #FFFFFF;
	padding-left: 3px;
	padding-bottom: 2px;
	margin-left:3px;
	background-color: #1e1d23;
}

QCheckBox {
	color: #a9b7c6;
	padding: 2px;
}
QCheckBox:disabled {
	color: #808086;
	padding: 2px;
}

QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: rgb(87, 97, 106);
	background-color:#1e1d23;
}
QCheckBox::indicator:checked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: #04b97f;
}
QCheckBox::indicator:unchecked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: transparent;
}
QRadioButton {
	color: #a9b7c6;
	background-color: #1e1d23;
	padding: 1px;
}
QRadioButton::indicator:checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: #04b97f;
}
QRadioButton::indicator:!checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: transparent;
}
QStatusBar {
	color:#027f7f;
}
QSpinBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDoubleSpinBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QTimeEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDateTimeEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDateEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QComboBox {
	color: #a9b7c6;	
	background: #1e1d23;
}
QComboBox:editable {
	background: #1e1d23;
	color: #a9b7c6;
	selection-background-color: #1e1d23;
}
QComboBox QAbstractItemView {
	color: #a9b7c6;	
	background: #1e1d23;
	selection-color: #FFFFFF;
	selection-background-color: #1e1d23;
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
	color: #a9b7c6;	
	background: #1e1d23;
}
QFontComboBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QToolBox {
	color: #a9b7c6;
	background-color: #1e1d23;
}
QToolBox::tab {
	color: #a9b7c6;
	background-color: #1e1d23;
}
QToolBox::tab:selected {
	color: #FFFFFF;
	background-color: #1e1d23;
}
QScrollArea {
	color: #FFFFFF;
	background-color: #1e1d23;
}
QSlider::groove:horizontal {
	height: 5px;
	background: #04b97f;
}
QSlider::groove:vertical {
	width: 5px;
	background: #04b97f;
}
QSlider::handle:horizontal {
	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
	border: 1px solid #5c5c5c;
	width: 14px;
	margin: -5px 0;
	border-radius: 7px;
}
QSlider::handle:vertical {
	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);
	border: 1px solid #5c5c5c;
	height: 14px;
	margin: 0 -5px;
	border-radius: 7px;
}
QSlider::add-page:horizontal {
    background: white;
}
QSlider::add-page:vertical {
    background: white;
}
QSlider::sub-page:horizontal {
    background: #04b97f;
}
QSlider::sub-page:vertical {
    background: #04b97f;
}
"""
    Ubuntu="""
QMainWindow {
	background-color:#f0f0f0;
}
QCheckBox {
	padding:2px;
}
QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	border-width:1px;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-color: rgb(255,150,60);
	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));
}
QCheckBox::indicator:checked {
	border-radius:4px;
	border-style:solid;
	border-width:1px;
	border-color: rgb(246, 134, 86);
  	background-color:rgb(246, 134, 86)
}
QCheckBox::indicator:unchecked {
	border-radius:4px;
	border-style:solid;
	border-width:1px;
	border-color:rgb(246, 134, 86);
  	background-color:rgb(255,255,255);
}
QColorDialog {
	background-color:#f0f0f0;
}
QComboBox {
	color:rgb(81,72,65);
	background: #ffffff;
}
QComboBox:editable {
	background: #ffffff;
	color: rgb(81,72,65);
	selection-color:rgb(81,72,65);
	selection-background-color: #ffffff;
}
QComboBox QAbstractItemView {
	color:rgb(81,72,65);	
	background: #ffffff;
	selection-color: #ffffff;
	selection-background-color: rgb(246, 134, 86);
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
	color:  #1e1d23;	
	background: #ffffff;
}
QDateTimeEdit {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
QDateEdit {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
QDialog {
	background-color:#f0f0f0;
}
QDoubleSpinBox {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
QFontComboBox {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
QLabel {
	color:rgb(17,17,17);
}
QLineEdit {
	background-color:rgb(255,255,255);
	selection-background-color:rgb(236,116,64);
	color:rgb(17,17,17);
}
QMenuBar {
	color:rgb(223,219,210);
	background-color:rgb(65,64,59);
}
QMenuBar::item {
	padding-top:4px;
	padding-left:4px;
	padding-right:4px;
	color:rgb(223,219,210);
	background-color:rgb(65,64,59);
}
QMenuBar::item:selected {
	color:rgb(255,255,255);
	padding-top:2px;
	padding-left:2px;
	padding-right:2px;
	border-top-width:2px;
	border-left-width:2px;
	border-right-width:2px;
	border-top-right-radius:4px;
	border-top-left-radius:4px;
	border-style:solid;
	background-color:rgb(65,64,59);
	border-top-color: rgb(47,47,44);
	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));
	border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));
}
QMenu {
	color:rgb(223,219,210);
	background-color:rgb(65,64,59);
}
QMenu::item {
	color:rgb(223,219,210);
	padding-left:20px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:10px;
}
QMenu::item:selected {
	color:rgb(255,255,255);
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));
	border-style:solid;
	border-width:3px;
	padding-left:17px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));
	border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));
	border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));
	border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));
}
QPlainTextEdit {
	border-width: 1px;
	border-style: solid;
	border-color:transparent;
	color:rgb(17,17,17);
	selection-background-color:rgb(236,116,64);
}
QProgressBar {
	text-align: center;
	color: rgb(0, 0, 0);
	border-width: 1px; 
	border-radius: 10px;
	border-style: inset;
	border-color: rgb(150,150,150);
	background-color:rgb(221,221,219);
}
QProgressBar::chunk:horizontal {
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));
	border-style: solid;
	border-radius:8px;
	border-width:1px;
	border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));
	border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));
	border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));
	border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));
}
QPushButton{
	color:rgb(17,17,17);
	border-width: 1px;
	border-radius: 6px;
	border-bottom-color: rgb(150,150,150);
	border-right-color: rgb(165,165,165);
	border-left-color: rgb(165,165,165);
	border-top-color: rgb(180,180,180);
	border-style: solid;
	padding: 4px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));
}
QPushButton:hover{
	color:rgb(17,17,17);
	border-width: 1px;
	border-radius:6px;
	border-top-color: rgb(255,150,60);
	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));
	border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));
	border-bottom-color: rgb(200,70,20);
	border-style: solid;
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));
}
QPushButton:default{
	color:rgb(17,17,17);
	border-width: 1px;
	border-radius:6px;
	border-top-color: rgb(255,150,60);
	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));
	border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));
	border-bottom-color: rgb(200,70,20);
	border-style: solid;
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));
}
QPushButton:pressed{
	color:rgb(17,17,17);
	border-width: 1px;
	border-radius: 6px;
	border-width: 1px;
	border-top-color: rgba(255,150,60,200);
	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));
	border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));
	border-bottom-color: rgba(200,70,20,200);
	border-style: solid;
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));
}
QPushButton:disabled{
	color:rgb(174,167,159);
	border-width: 1px;
	border-radius: 6px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));
}
QRadioButton {
	padding: 1px;
}
QRadioButton::indicator:checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: rgba(246, 134, 86, 255);
	color: #a9b7c6;
	background-color:rgba(246, 134, 86, 255);
}
QRadioButton::indicator:!checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: rgb(246, 134, 86);
	color: #a9b7c6;
	background-color: transparent;
}
QScrollArea {
	color: #FFFFFF;
	background-color:#f0f0f0;
}
QSlider::groove {
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
}
QSlider::groove:horizontal {
	height: 5px;
	background: rgb(246, 134, 86);
}
QSlider::groove:vertical {
	width: 5px;
	background: rgb(246, 134, 86);
}
QSlider::handle:horizontal {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	width: 12px;
	margin: -5px 0;
	border-radius: 7px;
}
QSlider::handle:vertical {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	height: 12px;
	margin: 0 -5px;
	border-radius: 7px;
}
QSlider::add-page:horizontal {
 	background: white;
}
QSlider::add-page:vertical {
	background: white;
}
QSlider::sub-page:horizontal {
	background: rgb(246, 134, 86);
}
QSlider::sub-page:vertical {
  	background: rgb(246, 134, 86);
}
QStatusBar {
	color:rgb(81,72,65);
}
QSpinBox {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
QScrollBar:horizontal {
	max-height: 20px;
	border: 1px transparent grey;
	margin: 0px 20px 0px 20px;
}
QScrollBar::handle:horizontal {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	border-radius: 7px;
	min-width: 25px;
}
QScrollBar::handle:horizontal:hover {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(255,150,60);
	border-radius: 7px;
	min-width: 25px;
}
QScrollBar::add-line:horizontal {
  	border: 1px solid;
  	border-color: rgb(207,207,207);
  	border-top-right-radius: 7px;
  	border-top-left-radius: 7px;
  	border-bottom-right-radius: 7px;
  	background: rgb(255, 255, 255);
  	width: 20px;
  	subcontrol-position: right;
  	subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:hover {
  	border: 1px solid;
  	border-top-right-radius: 7px;
  	border-top-left-radius: 7px;
  	border-bottom-right-radius: 7px;
  	border-color: rgb(255,150,60);
  	background: rgb(255, 255, 255);
  	width: 20px;
  	subcontrol-position: right;
  	subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:pressed {
  	border: 1px solid grey;
  	border-top-left-radius: 7px;
  	border-top-right-radius: 7px;
  	border-bottom-right-radius: 7px;
  	background: rgb(231,231,231);
  	width: 20px;
  	subcontrol-position: right;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
  	border: 1px solid;
  	border-color: rgb(207,207,207);
  	border-top-right-radius: 7px;
  	border-top-left-radius: 7px;
  	border-bottom-left-radius: 7px;
  	background: rgb(255, 255, 255);
  	width: 20px;
  	subcontrol-position: left;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:hover {
  	border: 1px solid;
  	border-color: rgb(255,150,60);
  	border-top-right-radius: 7px;
  	border-top-left-radius: 7px;
  	border-bottom-left-radius: 7px;
  	background: rgb(255, 255, 255);
  	width: 20px;
  	subcontrol-position: left;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:pressed {
  	border: 1px solid grey;
  	border-top-right-radius: 7px;
  	border-top-left-radius: 7px;
  	border-bottom-left-radius: 7px;
  	background: rgb(231,231,231);
  	width: 20px;
  	subcontrol-position: left;
  	subcontrol-origin: margin;
}
QScrollBar::left-arrow:horizontal {
  	border: 1px transparent grey;
  	border-top-left-radius: 3px;
  	border-bottom-left-radius: 3px;
  	width: 6px;
  	height: 6px;
  	background: rgb(230,230,230);
}
QScrollBar::right-arrow:horizontal {
	border: 1px transparent grey;
	border-top-right-radius: 3px;
	border-bottom-right-radius: 3px;
  	width: 6px;
  	height: 6px;
 	background: rgb(230,230,230);
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
 	background: none;
} 
QScrollBar:vertical {
	max-width: 20px;
	border: 1px transparent grey;
	margin: 20px 0px 20px 0px;
}
QScrollBar::add-line:vertical {
	border: 1px solid;
	border-color: rgb(207,207,207);
	border-bottom-right-radius: 7px;
	border-bottom-left-radius: 7px;
	border-top-left-radius: 7px;
	background: rgb(255, 255, 255);
  	height: 20px;
  	subcontrol-position: bottom;
  	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover {
  	border: 1px solid;
  	border-color: rgb(255,150,60);
  	border-bottom-right-radius: 7px;
  	border-bottom-left-radius: 7px;
  	border-top-left-radius: 7px;
  	background: rgb(255, 255, 255);
  	height: 20px;
  	subcontrol-position: bottom;
  	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:pressed {
  	border: 1px solid grey;
  	border-bottom-left-radius: 7px;
  	border-bottom-right-radius: 7px;
  	border-top-left-radius: 7px;
  	background: rgb(231,231,231);
  	height: 20px;
  	subcontrol-position: bottom;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
  	border: 1px solid;
  	border-color: rgb(207,207,207);
  	border-top-right-radius: 7px;
  	border-top-left-radius: 7px;
  	border-bottom-left-radius: 7px;
  	background: rgb(255, 255, 255);
  	height: 20px;
  	subcontrol-position: top;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover {
  	border: 1px solid;
  	border-color: rgb(255,150,60);
  	border-top-right-radius: 7px;
  	border-top-left-radius: 7px;
  	border-bottom-left-radius: 7px;
	background: rgb(255, 255, 255);
  	height: 20px;
  	subcontrol-position: top;
  	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:pressed {
  	border: 1px solid grey;
  	border-top-left-radius: 7px;
  	border-top-right-radius: 7px;
  	background: rgb(231,231,231);
 	height: 20px;
  	subcontrol-position: top;
  	subcontrol-origin: margin;
}
QScrollBar::handle:vertical {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	border-radius: 7px;
	min-height: 25px;
}
QScrollBar::handle:vertical:hover {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(255,150,60);
	border-radius: 7px;
	min-height: 25px;
}
QScrollBar::up-arrow:vertical {
	border: 1px transparent grey;
  	border-top-left-radius: 3px;
	border-top-right-radius: 3px;
  	width: 6px;
  	height: 6px;
  	background: rgb(230,230,230);
}
QScrollBar::down-arrow:vertical {
  	border: 1px transparent grey;
  	border-bottom-left-radius: 3px;
  	border-bottom-right-radius: 3px;
  	width: 6px;
  	height: 6px;
  	background: rgb(230,230,230);
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
  	background: none;
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:rgb(247,246,246);
}
QTabWidget::pane {
	border-color: rgb(180,180,180);
	background-color:rgb(247,246,246);
	border-style: solid;
	border-width: 1px;
  	border-radius: 6px;
}
QTabBar::tab {
	padding-left:4px;
	padding-right:4px;
	padding-bottom:2px;
	padding-top:2px;
	color:rgb(81,72,65);
  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(221,218,217,255), stop:1 rgba(240,239,238,255));
	border-style: solid;
	border-width: 1px;
  	border-top-right-radius:4px;
	border-top-left-radius:4px;
	border-top-color: rgb(180,180,180);
	border-left-color: rgb(180,180,180);
	border-right-color: rgb(180,180,180);
	border-bottom-color: transparent;
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	background-color:rgb(247,246,246);
  	margin-left: 0px;
  	margin-right: 1px;
}
QTabBar::tab:!selected {
	margin-top: 1px;
	margin-right: 1px;
}
QTextEdit {
	border-width: 1px;
	border-style: solid;
	border-color:transparent;
	color:rgb(17,17,17);
	selection-background-color:rgb(236,116,64);
}
QTimeEdit {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
QToolBox {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
QToolBox::tab {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
QToolBox::tab:selected {
	color:rgb(81,72,65);
	background-color: #ffffff;
}
"""
    @staticmethod
    def get_style(self,name):
        if name=="AMOLED":
            return self.AMOLED
        if name=="aqua":
            return self.aqua
        if name=="ConsoleStyle":
            return self.ConsoleStyle
        if name=="ElegantDark":
            return self.ElegantDark
        if name=="ManjaroMix":
            return self.ManjaroMix
        if name=="MaterialDark":
            return self.MaterialDark
        if name=="Ubuntu":
            return self.Ubuntu