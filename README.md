This Application is used to classtify Dogs or Cats Images. It is using Tensorflow (InceptionV3) and build on Flask Framework.
To train AI, I used the data at link: [Traning Dataset](https://github.com/thanhson1085/Hello-AI/tree/master/dataset/training_set)

### Document
See link [How to build a simple AI](https://sonnguyen.ws/first-ai-application/)

If you want to custom the AI, you just need to add/modify the training dataset, or change the training model.
### Train your AI
```
bash train.sh
```
After traning the AI, we have the trained model file at: [Trained Model](https://github.com/thanhson1085/Hello-AI/tree/master/output)
### Run AI as a Service
We are using Flask Framework to public AI as a Service via Web Interface.
```
python app.py
```

Access site: http://localhost:3000
![cat or dog AI](https://sonnguyen.ws/wp-content/uploads/2017/03/Capture.jpg)

### Demo
[https://thanhson1085-hello-ai.herokuapp.com/](https://thanhson1085-hello-ai.herokuapp.com/)

## Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/thanhson1085/Hello-AI.git)
