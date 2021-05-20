from collections import defaultdict
import tensorflow as tf
from tensorflow.python.ops import init_ops_v2

trainable_map = {}
input_map = {}
g = None

def defaultCodegen(node, tree, child_codes):
    def execAll():
        if len(child_codes) == 1:
            return child_codes[0]()
        
        for code in child_codes:
            code()

    return execAll

# def ECodegen(node, tree, child_codes):
#     return child_codes[0]

def ifCodegen(node, tree, child_codes):
    def debug():
        result = child_codes[1]()*child_codes[3]() + (1-child_codes[1]())*child_codes[5]()
        return result
    
    return debug

# def BCodegen(node, tree, child_codes):
    # return child_codes[0]

def condCodegen(node, tree, child_codes):
    def debug():
        result = tf.add_n((child_codes[0](), child_codes[2](), child_codes[4](), child_codes[6]())) - child_codes[8]()
        # result = tf.maximum(result, 0)
        # result = tf.where(result > 0, tf.minimum(result+1, 1), tf.maximum(result, 0))
        # result = tf.minimum(result+1, 1)
        # sources = [item[1] for item in trainable_map.items()]
        result = tf.sigmoid(result)
        # print(g.gradient(result, sources))
        return result
    return debug

# def ORCodegen(node, tree, child_codes):
#     return lambda: tf.clip_by_value(child_codes[0]() + child_codes[2](), 0, 1)

# def ANDCodegen(node, tree, child_codes):
#     def debug():
#         result = tf.sigmoid((child_codes[0]() + child_codes[2]() - 1.5)*3)
#         # print(result, child_codes[0](), child_codes[2]())
#         # sources = [item[1] for item in trainable_map.items()]
#         # print(g.gradient(result, sources))
#         return result
#     return debug

def tCodegen(node, tree, child_codes):
    def debug():
        result =tf.multiply(child_codes[0](), child_codes[4]())
        # print("*"*10, result, child_codes[0](), child_codes[4]())

        return result
    
    return debug

def inputCodegen(node, tree, child_codes):
    if node.data.text in input_map:
        input = input_map[node.data.text]
    else:
        input = 0
        input_map[node.data.text] = input
    return lambda: tf.constant(input_map[node.data.text], dtype=tf.float32)

def constCodegen(node, tree, child_codes):
    return lambda: tf.constant(float(node.data.text), dtype=tf.float32)

def varCodegen(node, tree, child_codes):
    if node.data.text in trainable_map:
        var = trainable_map[node.data.text]
    else:
        var = tf.Variable(initial_value=tf.initializers.GlorotUniform()(shape=(1,)),  trainable=True, name=node.data.text, dtype=tf.float32)
        trainable_map[node.data.text] = var
    return lambda: var


function_lookup = defaultdict(lambda: defaultCodegen)

function_lookup.update({
    # "E": ECodegen,
    "if": ifCodegen,
    # "B": BCodegen,
    # "OR": ORCodegen,
    # "AND": ANDCodegen,
    "cond": condCodegen,
    "t0": tCodegen,
    "t1": tCodegen,
    "t2": tCodegen,
    "t3": tCodegen,
    "input1": inputCodegen,
    "input2": inputCodegen,
    "input3": inputCodegen,
    "input4": inputCodegen,
    "var1": varCodegen,
    "var2": varCodegen,
    "var3": varCodegen,
    "var4": varCodegen,
    "var5": varCodegen,
    "left": constCodegen,
    "right": constCodegen,
})