import cv2
import time
import face_recognition
import sys
import os
import requests



def reconhecimento():

    hierarquia = []

    aba = "Sem Cadastrado"
      
    video_capture = cv2.VideoCapture(0)
    known_face_encodings = []
    known_face_names = []
    hierarquias = []
    for file in os.listdir('./'):
        if file.endswith('.jpg'):
            pessoa_image = face_recognition.load_image_file(file)
            pessoa_face_encoding = face_recognition.face_encodings(pessoa_image)[0]
            known_face_encodings.append(pessoa_face_encoding)
            data = file.split('.')[0].split('_')
            known_face_names.append(data[0])
            if len(data) == 2:
                hierarquias.append(data[1])
            else:
                hierarquias.append('')

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
    # Grab a single frame of video
        ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
        if process_this_frame:
            #name = aba
        # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = aba
                

            # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    hierarquia = hierarquias[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame


    # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
        
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

        
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, (name + ' ' + hierarquia), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            #acrescentar uma comparação tipo & para evitar que pesseoas 
            #sem cadastro herdem o nível de acesso de outras pessoas

            #print(name, hierarquia)
            print(name, hierarquia)

            if ('a' in hierarquia) & (name != aba):
                print('pode abrir porta a')
                #requests.request("GET", "http://192.168.43.67:8888/gpio5on" , data='', headers={'TWFuc3VyOk1hbnN1cjAx': ''} )
                #requests.request("GET", "http://192.168.43.67:8888/gpio5off" , data='', headers={'TWFuc3VyOk1hbnN1cjAx': ''} )
            
            if ('b' in hierarquia) & (name != aba):
                print('pode abrir porta b')
                #requests.request("GET", "http://192.168.43.67:8888/gpio2on" , data='', headers={'TWFuc3VyOk1hbnN1cjAx': ''} )
                #requests.request("GET", "http://192.168.43.67:8888/gpio2off" , data='', headers={'TWFuc3VyOk1hbnN1cjAx': ''} )
                
            if ('c' in hierarquia) & (name != aba):
                print('pode abrir porta c')
                #requests.request("GET", "http://192.168.43.67:8888/gpio4on" , data='', headers={'TWFuc3VyOk1hbnN1cjAx': ''} )
                #requests.request("GET", "http://192.168.43.67:8888/gpio4off" , data='', headers={'TWFuc3VyOk1hbnN1cjAx': ''} )
                
        cv2.imshow('Video', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break