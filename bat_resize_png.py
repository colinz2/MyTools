#pip install pillow

from PIL import Image
import os 


def my_print(x):
	print(x)
	
def resize_png2(name, ratio):
	print(name + '.png', ratio)

def resize_png(name, ratio):
	im = Image.open(name + '.png')
	w, h = im.size
	print('Original image size: %sx%s' % (w, h))
	im.thumbnail((w//ratio, h//ratio))
	print('Resize image to: %sx%s' % (w//ratio, h//ratio))
	im.save(name + '_s.png', 'png')
	return name + '_s.png';
	

	
def main(dir, ratio):
	resize_dir = os.path.join(dir, 'resize_png')
	os.mkdir(resize_dir)
	for x in os.listdir(dir):
		if os.path.isfile(x) and os.path.splitext(x)[1] == '.png':
			file_name = os.path.splitext(x)[0]
			if len(file_name) == 3:
				resze_name = resize_png(os.path.join(dir, file_name), ratio)
				os.rename(resze_name, os.path.join(resize_dir, os.path.split(resze_name)[1]))
				
if __name__=='__main__':	
	main('.', 4.7)
	
