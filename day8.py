with open('adventofcode/day8_input.txt', 'r') as f:    
    input_data = f.read().strip()
# input_data = [int(x) for x in input_data]    
tall = 6
wide = 25
layers = [input_data[i:i+(tall*wide)] for i in range(0,len(input_data), tall*wide)]

l = layers[0]
for layer in layers:
    if layer.count('0') < l.count('0'):
        l = layer


image = [' '] * (tall * wide)
layers = [layers[-i-1] for i in range(0, len(layers))]
for layer in layers:
    for i in range(0, len(layer)):
        if layer[i] == '0':
            image[i] = ' '
        if layer[i] == '1':
            image[i] = 'x'
        if layer[i] == '2':
            pass
image_rows = [image[i:i+wide] for i in range(0,len(image), wide)]
for r in image_rows:
    print(' '.join(r))