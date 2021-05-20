from collections import defaultdict
import tensorflow as tf
from tensorflow.python.ops import init_ops_v2

trainable_map = []
input_map = {}
g = None

def defaultCodegen(node, tree, child_codes):
    def execAll():
        if len(child_codes) == 1:
            return child_codes[0]()
        
        for code in child_codes:
            code()
            
    return execAll

def ifCodegen(node, tree, child_codes):
    def debug():
        result = child_codes[1]()*child_codes[3]() + (1-child_codes[1]())*child_codes[5]()
        return result
    return debug

def condCodegen(node, tree, child_codes):
    def debug():
        result = tf.add_n((child_codes[0](), child_codes[2]())) - child_codes[4]()
        result = tf.sigmoid(result)
        return result
    return debug

def tCodegen(node, tree, child_codes):
    def debug():
        result = tf.multiply(child_codes[0](), child_codes[4]())
        return result
    return debug

def inputCodegen(node, tree, child_codes):
    if node.data.text not in input_map:
        input_map[node.data.text] = 0
    return lambda: tf.constant(input_map[node.data.text], dtype=tf.float32)

def actCodegen(node, tree, child_codes):
    def debug():
        result = tf.add_n((child_codes[0](), child_codes[2](), child_codes[4]()))
        return result
    return debug

def varCodegen(node, tree, child_codes):
    var = tf.Variable(initial_value=tf.initializers.GlorotUniform()(shape=(1,)),  trainable=True, name=node.data.text, dtype=tf.float32)
    trainable_map.append(var)
    return lambda: var

function_lookup = defaultdict(lambda: defaultCodegen)

function_lookup.update({
    "if": ifCodegen,
    
    "cond": condCodegen,
    
    "t0": tCodegen,
    "t1": tCodegen,
    
    "input0": inputCodegen,
    "input1": inputCodegen,
    
    "var0": varCodegen,
    "var1": varCodegen,
    "var2": varCodegen,
    "var3": varCodegen,
    "var4": varCodegen,

    "act": actCodegen,
})