import tensorflow as tf
import sys
import os 
# change this as you see fit
# Loads label file, strips off carriage return

class CatOrDog():
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.label_lines = [line.rstrip() for line 
                           in tf.gfile.GFile(os.path.join(self.dir_path, "output/retrained_labels.txt"))]
        self.create_graph()
        self.sess = tf.Session()

    def create_graph(self):
        with tf.gfile.FastGFile(os.path.join(self.dir_path, "output/retrained_graph.pb"), 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

    def run(self, image_path):
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = self.sess.graph.get_tensor_by_name('final_result:0')
        
        predictions = self.sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
        print('Result for %s' % (image_path))
        ret = ''
        for node_id in top_k:
            human_string = self.label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, score))
            if (score > 0.5):
                ret += human_string

        return ret


