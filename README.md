# Free-Style-Transfer
### Neutral Style Transfer Application that runs on Google Cloud App Engine using Flask.

Please checkout the blog post on [EpicML!](https://epicml.net)

### [>>> Blog article]( https://epicml.net/_articles/2020/style_transfer/neural_style_transfer.php "Free Style Transfer Explained!")


![Image of Style Transfer](https://epicml.net/_articles/2020/style_transfer/images/heading.jpg)

In detail, in this project I have explored Neural-Style-Transfer. In particular, I have built a free Neural Style Transfer web-application that runs entirely on Google Cloud. The idea is to use predominately Cloud services and Open-Source technologies to make the app tangible and accessible for everyone. In detail, to build and run the web-application, I used:
- [x] Google App Engine
- [x] Google Cloud Storage
- [x] TensorFlow Hub
- [x] Flask

__Tl;dr__: Machine Learning does not have to be a black-box. Applications that use ML generally consist of different building blocks. My motivation to build the application and write the blog post mentioned above is entirely focused on educational purposes. Further, I want to introduce a simple guide on how to deploy ML applications in the Cloud and make them accessible to the wider public. In this blog post, I am only going to outline the steps on how to deploy the machine learning model and web application. I uploaded the entire code in this github repo. 

the repo does hold the following:
- [x] app.yaml (to specify the python runtime)
- [x] cron.yaml (to avoid shutting down of the Google app engine)
- [x] main.py (the python application with the ml model)
- [x] requiremenrs.txt (to specify the dependencies)
- [x] A static folder (including the web interface and the images / favicons used

Example pic:

![Example pic:](https://epicml.net/_articles/2020/style_transfer/images/example_transfer.png)
