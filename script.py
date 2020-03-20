import face_recognition as fr 
import cv2
import os
import glob
import pickle


path = './image'
folders = [f for f in glob.glob(path + '**/*', recursive=True)]

known_encoding = []
known_name = []

def get_encoding():
	print('[INFO] Processing in images')
	
	for f in folders:
		names = f.split('/')[2]

		for images in glob.glob(f + '**/*.jpg'):

			images_file = cv2.imread(images)
			rgb = cv2.cvtColor(images_file, cv2.COLOR_BGR2RGB)

			location = fr.face_locations(rgb)
			face_encoding = fr.face_encodings(rgb, known_face_locations = location)

			for encoding in face_encoding:
				known_encoding.append(encoding)
				known_name.append(names)

def dump_pickle():
	try: 
		data = {'encoding':known_encoding, 'nama':known_name}
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