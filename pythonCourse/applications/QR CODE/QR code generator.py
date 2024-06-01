
import qrcode


the_page = ""

gen = qrcode.make(the_page) 
gen.save('QR3.png')
