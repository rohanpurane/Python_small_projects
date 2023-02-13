import pywhatkit as pw

# Note that, while executing this programe Internate should be connected.

text = '''The global scope of the health benefits from the discoveries
        documented in this book is breathtaking. Their implementation
        into national health care policies will significantly reduce and
        eliminate three leading causes of mortality in the world today:
        cardiovascular disease, strokes and deaths caused by the side 
        effects of prescription drugs. This book provides the guidelines to
        reach this goal.'''

pw.text_to_handwriting(text,'text_to_handwrite.png',[0,0,138]) # Parameters are((which text wnt to convert), (in which .png file u should be store), (color code))
print('Programe Done')


