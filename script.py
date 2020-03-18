import face_recognition as fr 
import numpy as np
import cv2
import os
import glob
import pickle


path = './image'
folders = [f for f in glob.glob(path + '**/*', recursive=True)]

known_encoding = []
known_name = []

def get_encoding():
	for f in folders:
		names = f.split('/')[2]

		for images in glob.glob(f + '**/*.jpg'):

			image_file = fr.load_image_file(images)
			location = fr.face_locations(image_file)
			face_encoding = fr.face_encodings(image_file, known_face_locations = location)[0]

			print('[INFO] Processing in images')

			known_encoding.append(face_encoding)
			known_name.append(names)

def dump_pickle():
	try: 
		data = {'nama' : known_name, 'encoding' : known_encoding }
		file = open('encoding.pickle', 'wb')
		file.write(pickle.dumps(data))
		file.close()
		print('[INFO] processing done !')

	except Exception as e:
		error_message = 'message: ' + str(e)

		print('[ERROR] {}'.format(error_message))

def main():
	get_encoding()
	dump_pickle()

if __name__ == '__main__':
	main()