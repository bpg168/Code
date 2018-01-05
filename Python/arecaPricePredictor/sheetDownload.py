import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from lxml import html

class Render(QWebPage):
	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self._loadFinished)
		self.mainFrame().load(url)
		self.app.exec_()

	def _loadFinished(self, result):
		self.frame = self.mainFrame()
		self.app.quit()

url = 'http://pycoders.com/archive'
r = Render(url)
result = r. frame.toHtml()
formatted_result = str(result.toAscii())
tree = html.fromstring(formatted_result)
archive_links = tree.xpath('//div[@class = "campaign"]/a/@href')
print(archive_links)