# Free-Style-Transfer

Welcome to my Neural-Style-Transfer repository. Over the past couple of week(ends), I have built a free Neural Style Transfer web-application that runs entirely on Google Cloud. My goal was to achieve this, while predominately using Cloud services and Open-Source technologies to make it tangible and accessible for everyone. In detail, to build and run the web-application, I leverage (a) Google App Engine, (b) Google Cloud Storage, and (c) TensorFlow-Hub.

Tl;Dr: Machine Learning does not have to be a black-box. Applications that use ML generally consist of different building blocks. My motivation to write this article and publish the repository is entirely focused on educational purposes. Further, I want to introduce a simple guide on how to deploy ML applications in the Cloud and make them accessible to the wider public. Therefore, I am going to outline how to become a ML artist, respectively, how to do this:

A) The Basics
THE IDEA - I wanted to build a Web-App that runs entirely on Google Cloud and allows users to perform Neural Style Transfer for free on their desktop and mobile devices. In this regard, I rebuild the NST functionality of the Google Art & Culture App in Google Cloud while adding new features & functionalities, such as adding 'custom styles'. I particularly pursued this project idea, as I wanted to understand how Neural Style Transfer works under the hood and the model predictions are cool to visualize. It turns out, the style of an image can be described by the means and correlations across the different feature maps. However, for the purpose of this article, I will mostly focus on the tools that I used to build the application.

THE BACKGROUND - Neural Style Transfer (NST) refers to a class of software algorithms that manipulate digital images, or videos, in order to adopt the appearance or visual style of another image. NST algorithms are characterized by their use of deep neural networks for the sake of image transformation. Common uses for NST are the creation of artificial artwork from photographs, for example by transferring the appearance of famous paintings to user-supplied images or photographs. 

THE RESEARCH - I want to highlight the seminal work of Gatys et al. (2016) who demonstrated the power of Convolutional Neural Networks (CNNs) in creating artistic imagery. Their work has inspired a lot of machine learning researchers. As of 2020, we have numerous pretrained models, such as from TensorFlow & PyTorch for NST.

Today we find multiple applications that leverage NST to produce machine learning art based on the early work from Gatys et al. (2016). However, besides some online applications that charge money for usage, most of the ML models available never got deployed. With this article, I want to highlight that the deployment process of ML models has never been easier as of 2020. In the next section, I am going to guide you through a step-by-step guide on how to build and deploy ML models entirely on Google Cloud.

B) Let's build the application.
THE THINGS WE NEED - Building on what we have learned from building the Disney Classification model, I planned to follow a similar exercise leveraging Google Cloud technologies together with a micro web framework for Python. The plan for the free Style Transfer App was the following:

Step: Build a web interface that allows users to upload their images and styles.
Step: Set up a Python environment to run the Neural Style Transfer Model.
Step: Set up Storage for hosting the style images.
Step: Overcome the Challenges & Connect everything together.
Step: Get a domain and make the Application available for free.

Web interface - The Essentials:
In order to build the web interface for the application, I used the grid system from bootstrap4 to allow a responsive web page. As the foundation was set up, I started building the upload functionality that allows users to upload an image or photograph to the site. From here on, I will refer to the uploaded image as "content image" in addition to the "style image" which is the complementary image used for the style transfer. The uploaded image can be encoded to base64 in order to send it to the python server on Google App Engine, which we will set up in the next section. In this regard, I built a function that converts both "jpg & png" image files to base64 using JavaScript magic. After converting the file to base64, I used a post request method from jQuery to send the data to the Python server. The Python server will respond with the prediction of the style transfer model.

Besides, building the functionality for the 'content image', I built a style picker for the 'style images' that allow the users to select their preferred image style. My approach was twofold: First, I built a custom image carousel using pure CSS with my personal choice of nice paintings and graffiti styles. In this regard, special shout-out to EvEnglert for providing me some of her work.

This being said, I do not claim any copyright on the provided styles used in the web application. Second, besides the provided style selection, I built a custom style upload function for users that allows them to upload their own 'style images' to make the app more flexible. For example, this is a feature that is not available in the Google Cloud & Culture application.

Lastly, I needed to build the transfer function that triggers the post request and handles the response on client side while providing a nice visualization of the model output that the user can directly download and share with friends and family. Furthermore, I can easily admit that I am terrible with web design, however, I tried my best to make the web interface feel pretty and intuitive to use.

The Python Server and Google Cloud Storage - The Essentials:
Remember that I want the application entirely to run on Cloud Services. Hence, I opted for a microframework (Flask) that is supported by Google App Engine and allows me to use a custom Python runtime. For being state-of-the-art, I picked Python 3.8 which is compatible with TensorFlow 2.3.0 and TensorFlow-Hub 0.9.0.

On the server side, I introduced the Flask endpoint for the (a) web interface and the (b) transfer function which we have set up via jQuery in the section before. So in case an user uploads an image, selects a pre-provided style and triggers the post request on the web interface, the base64 data will be received by the transfer endpoint on the server side. Here the decoded base64 data will be encoded and resized to a tensor that fits our NST model. In parallel, a file request will be initiated to download the select style image. In preparation for that, I set up a Google Cloud Storage bucket where all provided 'style images' are hosted.

Using this approach, the python application can directly download the style files form GCP without the need to transfer them from the frontend. Similarly, in case the user chooses to upload a 'custom style', the received base64 string will be encoded and resized in the identical manner as the 'content image'. Both the 'content image' and the 'style image' (respectively 'custom style image') are fed into the NST model from TensorFlow. After both inputs have been provided to the model, we can predict the New Image. In other words, we can start producing our own ARTWORK.

Last thing to do was to get a cool domain name. Luckily, I found the .icu domains are quite popular and cheap at the moment. Further, I wanted to make sure that everyone can use the application for free - therefore, I bough Free-Style-Transfer.icu

I think it sounds alright ;)

Some Challenges
After building the functionality outlined above, I came across some challenges that took me quite some time and effort to solve:

Users most likely will use their phones in order to provide photos and images that have been captured in different orientations (eg. landscape, portrait). When encoding image information to base64 the exif metadata gets lost. Thus, the orientation gets messed up when receiving the model prediction back on the web-interface. In this regard, I needed to write a function to save the exif orientation and client side and apply this orientation back to the model prediction.
In order to run TensorFlow 2.x on Google App Engine - I needed to configure a larger instance class than provided by default when opting for a Python 3.8 runtime with a 'standard' environment. Furthermore, it was quite a struggle to figure that TensorFlow-Hub 0.9.0 seems to have compatibility problems with Python 3.7 on Google App Engine.
Instances on Google App Engine seem to shut-down by default after 60 minutes. This is per-se not a problem, however, spinning up a new instance does take some time. In detail, a cold-start of an instance does take up to 30 seconds, which surely causes a bad user experience. A solution for this challenge was preventing at least one instance from shutting down by running a cron-job on an empty function on the server side.
All in all this was a very project as a ML model with visual output is generally cool and more fun to use. For those of you who are more interested in code work - check out the repository on Github or follow my ML-Blog www.epicML.net.
