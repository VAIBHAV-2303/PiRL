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
        result = child_codes[0]()
        return result
    return debug

def retCodegen(node, tree, child_codes):
    def debug():
        result = tf.concat((
            child_codes[0](),
            child_codes[2](),
            child_codes[4](),
            child_codes[6]()
        ), axis = -1)

        return result
    
    return debug

def oCodegen(node, tree, child_codes):
    def debug():
        result = tf.multiply(child_codes[0](), child_codes[2]())\
                +tf.multiply(child_codes[4](), child_codes[6]())\
                +tf.multiply(child_codes[8](), child_codes[10]())\
                +tf.multiply(child_codes[12](), child_codes[14]())\
                +child_codes[16]()

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
    var = tf.Variable(initial_value=tf.initializers.GlorotUniform()(shape=(1,)),  trainable=True, name=node.data.text, dtype=tf.float32)
    trainable_map.append(var)
    return lambda: var


function_lookup = defaultdict(lambda: defaultCodegen)

function_lookup.update({
    "if1": ifCodegen,
    "if2": ifCodegen,
    "ret": retCodegen,
    "cond1": condCodegen,
    "cond2": condCodegen,

    "o1" : oCodegen,
    "o2" : oCodegen,
    "o3" : oCodegen,
    "o4" : oCodegen,

    "var0": varCodegen,
    "var1": varCodegen,
    "var2": varCodegen,
    "var3": varCodegen,
    "var4": varCodegen,
    "var5": varCodegen,
    "var6": varCodegen,
    "var7": varCodegen,
    "var8": varCodegen,
    "var9": varCodegen,
    "var10": varCodegen,
    "var11": varCodegen,
    "var12": varCodegen,
    "var13": varCodegen,
    "var14": varCodegen,
    "var15": varCodegen,
    "var16": varCodegen,
    "var17": varCodegen,
    "var18": varCodegen,
    "var19": varCodegen,

    "input0": inputCodegen,
    "input1": inputCodegen,
    "input2": inputCodegen,
    "input3": inputCodegen,
    "input4": inputCodegen,
    "input5": inputCodegen,
    "input6": inputCodegen,
    "input7": inputCodegen,
    "input8": inputCodegen,
    "input9": inputCodegen,
    "input10": inputCodegen,
    "input11": inputCodegen,
    "input12": inputCodegen,
    "input13": inputCodegen,

    "const1": constCodegen
})