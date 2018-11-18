import tensorflow as tf

def weight(algos,format="raw"):
    for algo in list(algos):
        if algo.isdigit():
            print("weight for the number %s time of training is" % algo)
            tvs = output(algo) #list of objects
            for v in tvs:
                print(v)
        else:
            raise ValueError("Algorithm name is not found.")

def output(algo):
    tf.reset_default_graph()
    saver = tf.train.import_meta_graph('/home/liuqun/lr_portfolio/train_package/'+algo+'/netfile.meta')
    with tf.Session() as sess:
        saver.restore(sess, '/home/liuqun/lr_portfolio/train_package/'+algo+'/netfile')
        tvs = [v for v in tf.global_variables()]
        for v in tvs:
            print(v.name)
            print(sess.run(v))
    return tvs
