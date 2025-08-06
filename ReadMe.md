# GroceryVis 
This was my senior capstone project during my undergraduate studies in computer science. We have created a system to help the user track their personal ingredients, their quantities, and what meals they could prepare from them. The main objective of our system was to be able to consistently keep track of the ingredients one purchases. The other goal of our system is to be able to recommend the user recipes from food they have in their kitchen. Alas, reducing unnecessary waste. The live-maintained inventory is personalized for each user as only their items and no one else’s, are recognized from the camera and object detection model. This is the AI and machine learning portion of the project done by Fernando Estrada.

<img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/0c3e0173-5226-46a6-a067-d41ce26454a2" />

# YoloV5 Model 
YOLOv5 is a popular object detection algorithm. With a good reputation in the AI
 vision community and relatively easy-to-follow documentation, it works as a CNN processing images
 should: breaking down a picture into a grid, and withing the grid measuring probabilities for classes
 detected using convolution. However, it works perfectly with Python computer vision libraries to draw bounding boxes around objects humans can recognize, attaching labels, probabilities, and
 maintaining counts of each item. ”YOLO” stands for ”You only look once”, and describes the one
time propagation the algorithm runs when classifying items. This is convenient in production-type
 projects. Developed by the Ultralytics research team, it currently stands at version 7.0.

<img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/842f6de6-399c-4b9f-8510-d712d721a403" />
 We ran multiple experiments when Training our YoloV5 Model and out of all the experiments, our
 last version performed the best. When training our YoloV5 model we decided that having seven
 different items the model can detect will be more then enough to prove the concept of our project.
 The seven items picked were an Apple, a Milk Jug, Egg Carton, Packaged Ramen, Peanut Butter,
 a Loaf of Bread, and I plastic Container. When it came to collecting data on the container we took
 pictures of the container with cereal in it at different levels. This will be important for our second
 model. Each item had over 600 images and up to 900 images of the item with the appropriate
 bounding box labeled to create our dataset. When collecting data we made sure to take pictures
 of almost every permutation of multiple items being in the picture simultaneously and at multiple
 angles. This was done to help the model generalize well in a real-world setting. In total, we collected
 over 2500 images and with data augmentation, we had a total of 5600 images. We trained the model
 for 100 epochs and ran validation set testing and at the end of the training, we ran it through a
 test set to ensure no overfitting occurred. Once the model was done training we ran our model live
 using a webcam to see how well it generalizes and found that the model performed very well.

#  Capacity Model (Convolutional Neural Network)
 When training our Capacity Model we decided to go with a Convolutional Neural Network since we
 are working with images. Out of the seven items our YoloV5 model can detect we decided to focus
 on the plastic container to prove detecting the capacity of an item is possible. We used the same
 data our YoloV5 model used but only focused on the pictures that had the plastic container in them.
 Since the data had the container at different levels we used the YoloV5 model to output pictures
 of the container but not the entire picture, a cropped picture using the bounding box to crop out
 the container. With this, we were able to make a dataset that comprised of cropped pictures of the
 plastic container at different levels of capacity. Since each bounding box can be different sizes for
 our capacity model we resize each picture to 300 by 420 and since the container is see-through we
 decided to keep the color in the pictures. The model itself is made up of multiple Convolutional
 layers with a Max Pooling layer following after and the second last layer was a flattened layer that
 leads to a dense layer with two outputs. All activation functions were relu but the last one was a
 softmax. We trained the model for 45 epochs and ran validation set testing and at the end of the
 training, we ran it through a test set to ensure no overfitting occurred. The model predicts when
 the container is low or high on it capacity. We use this output to send the user notifications and
 to send an email reminder when there container is low.
<img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/6a34af00-7c26-4488-a0ea-bfe3d10e0675" />

#  Examples from our Datasets

<img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/4c00d997-f71e-437a-a07d-42dd8a150b70" />
<img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/ca84d924-14b4-4677-b4fb-cad76e9e47cb" />

#  How to run 
    -CapstoneAI.zip: 
	This folder lists the necessary files and code concerning the ai portion for this project. It contain the files used
	to create the dataset,train the models,and live run each model. It also contains the models so can run them without
	training.
	-Prerequisites To Run the models:
		1. Pip install any packages to run the python files.
		2. For the yolo model pip install -r requirements.txt 

	- Prerequisites To train the models:
		1. YoloV5 Custom Dataset 
			This should be downloadable within our code.
		- Prerequisites To train the models:
		2. Capacity Dataset
			The Pictures and txt files are located in the CapacityDataset folder.

#  Summary
For my capstone project, I was in charge of the AI/ML side of the project. Our project would use computer vision to capture common grocery items and keep a live and up-to-date list of those items. These items range from a gallon of milk to fruit, bread, and a container of cereal. The AI/ML portion of the project used models like YoloV5 to capture and make a bounding box for each item. I made a custom dataset with each item used in the project and had to label them. For the container of cereal, since it was clear, I made another model using neural networks (used python tools pytorch, tensorflow, keras) that would use the image within the bounding box to detect if you were high, low, or out of cereal. This would then connect to our frontend interface where a user could check there pantry/groceries. This project aimed to reduce food waste by giving the user a live and up-to-date feed of what's in their pantry. This was mainly a proof-of-concept project, and at the end, we held a live demo of everything working.
 
