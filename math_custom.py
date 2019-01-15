import random as rnd

var1, var2 = rnd.randrange(100), rnd.randrange(100)

def easy():
	return render_template('./easy.html', titre="Mathematical examples EASY", task=""++var1++"+"++var2, solution="solution")

def medium():
	return render_template('./medium.html', titre="Mathematical examples MEDIUM", task=""++var1++"-"++var2, solution="solution")

def hard():
	return render_template('./hard.html', titre="Mathematical examples HARD", task=""++var1++"*"++var2, solution="solution")

