from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image1 = face_recognition.load_image_file("images/vivaan3.jpg")
encoding1 = face_recognition.face_encodings(image1, model = "cnn")[0]


image2 = face_recognition.load_image_file("images/aryan13.jpg")
encoding2 = face_recognition.face_encodings(image1, model = "cnn")[0]

known_face_encodings = [
    encoding1,
    encoding2
]
known_face_names = [
    "Vivaan",
    "Aryan"
]


#face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()